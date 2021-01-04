from datetime import datetime
from email.mime.text import MIMEText
from smtplib import SMTP
import os

# 需在环境变量配置qq SMTP服务账号密码
username = os.getenv("email_name")
password = os.getenv("email_pwd")

# 自动发送邮件
def auto_send_email(to_address, subject, content, from_address, if_add_time=True):
    """
    :param to_address:
    :param subject:
    :param content:
    :param from_address:
    :return:
    使用foxmail发送邮件的程序
    """
    try:
        if if_add_time:
            msg = MIMEText(datetime.now().strftime("%m-%d %H:%M:%S") + '\n\n' + content)
        else:
            msg = MIMEText(content)
        msg["Subject"] = subject + ' ' + datetime.now().strftime("%m-%d %H:%M:%S")
        msg["From"] = from_address
        msg["To"] = to_address


        server = SMTP('smtp.qq.com', port=587)
        server.starttls()
        username = os.getenv("email_name")
        password = os.getenv("email_pwd")
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()

        print('邮件发送成功')
    except Exception as err:
        print('邮件发送失败', err)