from Scheduler.celery import app
from Scheduler.weather_predict.base import tomorrow_weather
from Scheduler.alarm.tasks import email_alarm

from Scheduler.weather_predict.setting import SAFE_WEATHER
from Scheduler.logger_conf import logger

from Scheduler.weather_predict.setting import USERS


@app.task
def weather():
    for user in USERS:
        weather, temp_change = tomorrow_weather(user['address'])
        logger.debug(weather, temp_change)
        if weather not in SAFE_WEATHER or abs(temp_change) >= 5:
            email_alarm.apply_async(([user['email']], weather+ "\n温差：" + str(temp_change)))
