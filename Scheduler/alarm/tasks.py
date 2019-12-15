import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from Scheduler.celery import app
from Scheduler.logger_conf import logger


@app.task(ignore_result=True,)
def email_alarm(receivers: "接受者邮箱 list", con: str):
    sender = 'leiyang_ace@163.com'

    html = f"<h1>{con}</h1>"
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = formataddr(("leon", sender))
    msg['To'] = formataddr((None, '; '.join(receivers)))
    msg['Subject'] = Header('提醒', 'utf-8').encode()

    try:
        server = smtplib.SMTP_SSL("smtp.163.com", 465, timeout=30)  # SMTP协议默认端口是25，SMTP_SSL使用 465，
        # server.set_debuglevel(1)
        server.login(sender, "1005931665sqm")
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        logger.error(f"邮件发送失败：{e}")
