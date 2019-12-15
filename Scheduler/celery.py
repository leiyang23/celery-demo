from celery import Celery
from celery.schedules import crontab
from Scheduler.settings import redis_conf


app = Celery("Scheduler",
             broker=f"redis://{redis_conf['host']}:{redis_conf['port']}/1",
             backend=f"redis://{redis_conf['host']}:{redis_conf['port']}/2",
             include=['Scheduler.weather_predict.tasks', 'Scheduler.alarm.tasks'])

app.conf.beat_schedule = {
    "weather": {
        'task': "Scheduler.weather_predict.tasks.weather",
        'schedule': crontab(minute=0, hour="20,"),
        'args': ()
    }
}

app.conf.enable_utc = False
app.conf.timezone = "Asia/Shanghai"

if __name__ == '__main__':
    app.start()
