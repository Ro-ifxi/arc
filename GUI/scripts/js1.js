function search() {
    var searchInput = document.getElementById("input1").value;
    var apiUrl = 'http://127.0.0.1:8080/name/' + searchInput;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('网络错误');
            }
            return response.json(); // 解析JSON数据
        })
        .then(data => {
            displayResult(data);
        })
        .catch(error => {
            displayError(error);
        });
}

function displayResult(data) {
    var resultDiv = document.getElementById("result");
    // 在这里可以访问解析后的JSON数据，根据需要处理数据
    resultDiv.innerHTML = "结果：" + JSON.stringify(data);
}

function displayError(error) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "发生错误：" + error.message;
}
