# -*- coding:utf-8 -*-

import smtplib # 파이썬은 자체적으로 SMTP 모듈을 지원한다.

from email.mime.text import MIMEText


smtp = smtplib.SMTP('smtp.gmail.com', 587) # 지메일 포트 -> 587 

smtp.ehlo() # say Hello 

smtp.starttls() # TLS  보안 시작 

smtp.login('cnkegnome@gmail.com', '8804822!!')  # 로그인 인증

# 보낼 메세지 설정 

msg = MIMEText('JOB ID : 본문 테스트')

msg['Subject'] = '제목 테스트'

msg['To'] = 'sandartchippp@naver.com'


smtp.sendmail('cnkegnome@gmail.com', msg['To'] , msg.as_string())

#smtp.sendmail(   sender,   receiver , 메세지 내용 )

smtp.quit() 

