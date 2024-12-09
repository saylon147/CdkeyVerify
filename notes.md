# 1. 运行使用
1. 初始化数据库，现在项目代码里面改为启动app如果发现没有数据库文件，会重新初始化数据库
   ```
   python db_setup.py
   ```
2. 启动 Flask 应用
   ```
   python app.py
   ```
3. cmd下运行
   1. 生成 CDKey
   ```
   curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d "{\"count\": 5}"
   ```
   2. 获取未使用的 CDKey
   ```
   curl -X GET http://127.0.0.1:5000/unused
   ```
   3. 验证 CDKey
   ```
   curl -X POST http://127.0.0.1:5000/validate -H "Content-Type: application/json" -d "{\"cdkey\": \"106GSUNT\"}"
   ```
4. 完整LOG
   ```
   C:\Users\9you>curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d "{\"count\": 5}"
   {
     "generated_cdkeys": [
       "KSXCB9U7",
       "SS9V8CFJ",
       "GY7V31RD",
       "106GSUNT",
       "KKUH72SJ"
     ],
     "status": "success"
   }
   
   C:\Users\9you>curl -X GET http://127.0.0.1:5000/unused
   {
     "status": "success",
     "unused_cdkeys": [
       "KSXCB9U7",
       "SS9V8CFJ",
       "GY7V31RD",
       "106GSUNT",
       "KKUH72SJ"
     ]
   }
   
   C:\Users\9you>curl -X POST http://127.0.0.1:5000/validate -H "Content-Type: application/json" -d "{\"cdkey\": \"106GSUNT\"}"
   {
     "message": "CDKey is valid and marked as used",
     "status": "success"
   }
   
   C:\Users\9you>curl -X GET http://127.0.0.1:5000/unused
   {
     "status": "success",
     "unused_cdkeys": [
       "KSXCB9U7",
       "SS9V8CFJ",
       "GY7V31RD",
       "KKUH72SJ"
     ]
   }
   ```
   
# 2. docker打包发布
   1. 创建 Dockerfile
      - 具体内容参考项目文件
   2. 创建 .dockerignore （可选）
      - 具体内容参考项目文件
   3. 构建 Docker 镜像
      ```
      docker build -t cdkey-verify-app .
      ```
      - 拉取官方镜像文件如果失败，需要设置 DockerDesktop 的设置，Docker Engine 添加设置后重启 DockerDesktop。
      ```
      "registry-mirrors": [
         "https://docker.m.daocloud.io"
      ]
      ```
   4. 运行容器
      ```
      docker run -d -p 5000:5000 --name cdkey-verify-app cdkey-verify-app
      ```
   5. 导入发布包镜像
      ```
      docker save -o cdkey-verify-app.tar cdkey-verify-app:latest
      ```
   


   
# 3. 数据库重建步骤
1. 删除旧表（如果存在）
    ```
    DROP TABLE IF EXISTS cdkeys;
    ```
2. 创建新表 使用设计的表结构
    ```
    CREATE TABLE cdkeys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT UNIQUE NOT NULL,
        is_used INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    ```
3. 验证表结构
    ```
    PRAGMA table_info(cdkeys);
    ```
4. 完整LOG
```
C:\Users\9you\Desktop\CdkeyVerify> sqlite3 .\cdkeys.db
SQLite version 3.47.2 2024-12-07 20:39:59
Enter ".help" for usage hints.
sqlite> DROP TABLE IF EXISTS cdkeys;
sqlite> CREATE TABLE cdkeys (
(x1...>     id INTEGER PRIMARY KEY AUTOINCREMENT,
(x1...>     key TEXT UNIQUE NOT NULL,
(x1...>     is_used INTEGER DEFAULT 0,
(x1...>     created_at TEXT DEFAULT CURRENT_TIMESTAMP
(x1...> );
sqlite> PRAGMA table_info(cdkeys);
0|id|INTEGER|0||1
1|key|TEXT|1||0
2|is_used|INTEGER|0|0|0
3|created_at|TEXT|0|CURRENT_TIMESTAMP|0
sqlite> .exit
```