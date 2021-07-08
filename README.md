# jupyter-webhook


### Redash

1. 数据查询+可视化
2. 报警
3. 开源：python + rq + redis + postgresql
4. 支持：常见数据库，presto，es，clickhouse，prometheus，dgraph, **url request , shell script**



### JSON

1. 建Json数据源后，分组，这个url 可以请求 redash share API 
2. V9 需要开启不检查内网 API，V9之前是不支持内网查询的，V9 docker 也不是最新的代码的话，也不支持



## 警报

1. https://redash.io/help/user-guide/alerts/custom-alert-notifications ： 自定义报警内容

2. https://github.com/lishulongVI/redash-alert，支持飞书，钉钉，企业微信通知

   

### QA

1. 创建的query 非admin 账户其他人无法 编辑： 在settings 中生效`Enable experimental multiple owners support`
2. Json 不允许使用 内网地址访问：设置环境变量`REDASH_ENFORCE_PRIVATE_IP_BLOCK=false`





### 调度（Jupyter，Python，Sql）

1. Json 实现 + **redash refresh schedule**

   ```
   url : "http://dags.xxxx.com/m1/label_insight/"
   auth: ['xxxx','xxxxx']
   ```

2. Jupyter：https://github.com/lishulongVI/jupyter-webhook

   ```
   # 计算ks
   url : "http://dags.xxxx.com/m1/label_insight?env=/opt/conda3/bin/jupyter&sh=nbconvert --execute --to notebook --inplace /home/xxxx/tasks_schedule/xxxx.ipynb"
   
   auth: ['xxxxx','xxxxx']
   ```

3. Sql + **redash refresh schedule**

   ```
   ## 创建表结构
   CREATE TABLE  NEW_TABLE  AS
   (
       SELECT * FROM TABLE
   )
    WITH NO DATA
   
   # 插入数据
   insert into risk_mongo_1.dags.convert_new_r_incash 
   
   (
       SELECT * FROM TABLE
   )
   ```

   

