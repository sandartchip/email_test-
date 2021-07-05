# -*- coding:utf-8 -*-

import smtplib

from email.mime.text import MIMEText


smtp = smtplib.SMTP('smtp.gmail.com', 587) # 지메일 포트 -> 587 

smtp.ehlo()

smtp.starttls()

smtp.login('linayachika@outlook.com', 'cho@2013')

msg = MIMEText('본문 테스트')

msg['Subject'] = '테스트'

msg['To'] = 'kim@naver.com'

smtp.sendmail('linayachika@outlook.com', 'linayachika2@gmail.com', msg.as_string())

smtp.quit() 
