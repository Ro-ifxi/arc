# arc

# 项目部署流程

## 1.创建虚拟环境

    python -m venv venv

## 2.安装依赖

    pip install -r requirements.txt

## 注意：若出现api服务器启动失败，请注意是否切换到正确的目录下。

### 若错误码为10013：使用netstat -ano|findstr 8000查询占用端口的程序，使用taskkill /pid 进程id /F杀死进程

### 使用uvicorn WebGUI:app --host 0.0.0.0 --port 8080 --reload进行高度自定义启动