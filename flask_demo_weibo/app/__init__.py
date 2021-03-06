#encoding:utf-8
'''
Created on 

@author: pan
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir,ADMINS,MAIL_PASSWORD,MAIL_PORT,MAIL_SERVER,MAIL_USERNAME

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models

#在非debug模式下开启邮件功能
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = (MAIL_USERNAME,MAIL_PASSWORD)
    mail_handler=SMTPHandler((MAIL_SERVER,MAIL_PORT),'no_reply@'+MAIL_SERVER,ADMINS,'microblog failure',credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    
#在非debug模式下开启日志记录功能
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler=RotatingFileHandler('tmp/microblog.log','a',1*1024*2014,10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

#初始化Mial实例，这个对象为我们连接到SMTP服务器并且发送邮件
from flask_mail import Mail
mail=Mail(app)
