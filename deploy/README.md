### 生产环境部署

#### 主要流程
1. 配置 python 环境，并安装 celery。
2. 找到 celery 的 bin 命令。如果 通过 `pip`安装的话一般在python的安装包路径下的`bin`目录下。  
3. 将 celery 的 [github仓库](https://github.com/celery/celery)下的 `extra/generic-init.d/` 的 celeryd 和 celerybeat 两个 shell 脚本复制到项目中，
直接修改 这两个脚本中 引用配置文件的路径 就能使用自定义的配置了。    
celeryd.sh 的引用代码在 66 行。celerybeat.sh 的引用代码在 91-104 行。**实质上是调用 `_config_sanity` 这个函数从文件中读取
配置并验证。**     
本项目中 直接将 celeryd 和 celerybeat 这两个命令的配置放到一个文件中了。    
4. 脚本的使用方式不变 `sh celeryd.sh {start|stop|restart|status}`。

> 官方是将 脚本文件放置到 `/etc/init.d/` 目录下，配置文件放在`/etc/default/`下，脚本中直接读取这个目录下的同名配置文件，
>这样可以实现开机自启动，这是比较通用的做法。但这也导致了项目文件分散，不好管理。具体使用何种方式，看需求了。

#### 配置文件的写法
通用的以`CELERY_`作为前缀。    
celeryd 的配置以`CELERYD_`作为前缀，可用配置[文档](http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#available-options)   
celerybeat 的配置以`CELERYBEAT`作为前缀，可用配置[文档](http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#generic-initd-celerybeat-options)   


