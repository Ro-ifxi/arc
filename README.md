# arc

# 项目部署流程

## 1.创建虚拟环境

    python -m venv venv

## 2.安装依赖

    pip install -r requirements.txt

## 注意：若出现api服务器启动失败，请注意是否切换到正确的目录下。

### 若错误码为10013：
    
    netstat -ano|findstr 8000  # 查询占用端口的程序
    taskkill /pid 进程id /F # 杀死进程

### 自定义启动api服务器

    uvicorn WebGUI:app --host 0.0.0.0 --port 8080 --reload  

## 3.运行：双击GUI目录下的index.html文件
