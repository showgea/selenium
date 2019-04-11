import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import readcfg

# 设置连接信息


# # 163 账号密码
# smtpserver = "smtp.163.com"
# port = 994
# sender = "tangguobing2011@163.com"
# psw = "tangguobing000"
# reciever = "tangguobing2011@163.com"

# qq账号授权码
# server = "smtp.qq.com"
# port = 465
# sender = "844125553@qq.com"
# psw = "egiolppqixjsbfjg"
# reciever = "844125553@qq.com"

server = readcfg.server
port = readcfg.port
sender = readcfg.sender
psw = readcfg.psw
reciever = readcfg.reciever

# 加正文
f = open(r'E:\PaaS\result\report-2019-03-29.html', encoding='utf-8')
att_body = f.read()
f.close()

# 添加写信模板
msg = MIMEText(att_body, "html", "utf-8")
msg["From"] = sender
msg["To"] = reciever
msg["Subject"] = "自动化测试报告。"

# 加附件
att = MIMEText(att_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment; filename='report.html'"
msg.attach(att)

# 加正文
# body = MIMEText(att_body, "html", "utf-8")
# msg.attach(body)


# 写信流程 授权码登录
smtp = smtplib.SMTP_SSL(server, port)
smtp.login(sender, psw)
smtp.sendmail(sender, reciever, msg.as_string())
smtp.quit()

# 账号密码登录
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver, port)
# smtp.login(sender, psw)
# smtp.sendmail(sender, reciever, msg.as_string())
# smtp.quit()
