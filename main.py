
import os, copy

import smtplib # SMTP 라이브러리

from string import Template  # string 템플릿 모듈

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.image import MIMEImage


class EmailHTMLContent:
    """ e메일에 담길 컨텐츠"""

    def __init__(self, str_subject, template, template_params):

        assert isinstance(template, Template)

        assert isinstance(template_params, dict)

        self.msg = MIMEMultipart()


        # 이메일 제목 설정

        self.msg['Subject'] = str_subject

        str_msg = template.safe_substitute(**template_params) #

        mime_msg = MIMEText(str_msg, 'html')

        self.msg.attach(mime_msg)

    def get_message(self, str_from_email_addr, str_to_email_addrs):
        # 발신자, 수신자 리스트를 사용하여 보낼 메세지를 만든다.

        mm = copy.deepcopy(self.msg)

        mm['From'] = str_from_email_addr

        mm['To'] = ",".join(str_to_email_addrs)

        return mm



class EmailSender:
    """ 이메일 발송자"""

    def __init__(self, str_host, num_port=25):
        """호스트와 포트번호로 SMTP로 연결한다"""

        self.str_host = str_host
        self.num_port = num_port
        self.ss = smtplib.SMTP(host = str_host, port = num_port)

        # SMTP 인증이 필요하면 아래 주석을 해제한다.

        # self.ss.starttls()
        # self.ss.login('계정명', '비번') # 메일 서버에 연결한 계정과 비밀번호

    def send_message(self, emailContent, str_from_email_addr, str_to_email_addrs):
        """이메일을 발송함 """
        cc = emailContent.get_message(str_from_email_addr, str_to_email_addrs)
        self.ss.send_message(cc, from_addr = str_from_email_addr, to_addrs=str_to_email_addrs)
        del cc


str_host = 'postfix.test.com'
num_port = 25 # SMTP Port


str_subject = 'hello'

template = Template("""<html>
                            <head></head>
                            <body>
                                Hi ${NAME}.<br>
                                This is a test message.
                            </body>
                        </html>""")


template_params = {'NAME': 'Son'}
emailSender = EmailSender(str_host, num_port)


emailHTMLContent = EmailHTMLContent(str_subject, template, template_params)

str_from_email_addr = 'god@test.com'
str_to_email_addrs = ['angel@tests.com', 'devil@test.com']

emailSender.send_message(emailHTMLContent, str_from_email_addr, str_to_email_addrs)






