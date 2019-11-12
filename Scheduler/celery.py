from celery import Celery

app = Celery("Scheduler", broker="redis://47.111.175.222:6379/1", backend="redis://47.111.175.222:6379/1",include=['Scheduler.tasks'])

app.conf.beat_schedule = {
    "add-per-30s":{
        'task': "Scheduler.tasks.add",
        'schedule':30,
        'args':(12,13)
    }
}

app.conf.timezone = "Asia/Shanghai"


if __name__ == '__main__':
    app.start()
