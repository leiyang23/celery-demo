dev = True

if dev:
    redis_conf = {
        "host": "127.0.0.1",
        "port": 6379,
    }
    mongodb_conf = {
        "host": "127.0.0.1",
        "port": 27017,
    }
    mysql_conf = {
        "host": "127.0.0.1",
        "port": 3306,
        "username": "root",
        "password": "leon123",
        "database": "butler"

    }
else:
    redis_conf = {
        "host": "47.111.175.222",
        "port": 6379,
    }
