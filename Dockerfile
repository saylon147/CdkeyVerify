# 使用官方 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码（受 .dockerignore 规则影响）
COPY . .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 的默认端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "app.py"]
