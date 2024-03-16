function search() {
    var searchInput = document.getElementById("input1").value;
    var apiUrl = 'https://api.example.com/search?query=' + searchInput;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('网络错误');
            }
            return response.json();
        })
        .then(data => {
            displayResult(data);
        })
        .catch(error => {
            displayError(error);
        });
}

function displayError(error) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "发生错误：" + error.message;
}
