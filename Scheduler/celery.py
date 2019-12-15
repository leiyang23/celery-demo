from celery import Celery

app = Celery("Scheduler", broker="redis://127.0.0.1:6379/1", backend="redis://127.0.0.1:6379/2",
             include=['Scheduler.weather_predict.tasks','Scheduler.alarm.tasks'])

app.conf.beat_schedule = {
    "add-per-30s": {
        'task': "Scheduler.weather_predict.tasks.weather",
        'schedule': 30,
        'args': ()
    }
}

app.conf.enable_utc = False
app.conf.timezone = "Asia/Shanghai"

if __name__ == '__main__':
    app.start()
