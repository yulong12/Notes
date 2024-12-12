# conda创建虚拟环境
```
conda create --name dify_deve python=3.10
conda activate dify_deve
conda deactivate
conda env list
```
# pgadmin4
pgadmin4是postgress的dashboard
```
docker pull dpage/pgadmin4
docker run -d -p 5433:80 --name pgadmin4 -e PGADMIN_DEFAULT_EMAIL=test@123.com -e PGADMIN_DEFAULT_PASSWORD=123456 dpage/pgadmin4
```
打开浏览器访问：
```
http://localhost:5433/
```
# postgress
- 进入postgress：`psql`
- 创建数据库：`CREATE DATABASE dbname;`
- 查看已经存在的数据库'：`\l `
- 进入数据库：`\c + 数据库名`
- 查看当前数据库下有哪些表：`\d`

- 删除数据库： `DROP DATABASE dbname;`

- 

flask run --host 0.0.0.0 --port=5001 --debug

celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail,ops_trace --loglevel INFO

npm run start


# ollama

https://www.53ai.com/news/LargeLanguageModel/2024081317230.html

- 启动ollama
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart always ollama/ollama
```
- http://host.docker.internal:11434
- http://localhost:11434

# Xinference(mac平台)
- 安装
```pip install "xinference[mlx]"```
- 启动
```xinference-local --host 0.0.0.0 --port 9997```
- 进入
    - http://127.0.0.1:9997/ui 
    - http://127.0.0.1:9997/docs 
