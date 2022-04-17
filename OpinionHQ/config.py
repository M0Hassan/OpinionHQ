import os

# use environmental variables to set the mail settings
# and the secret_key as well as the database uri 

class Config:
    SECRET_KEY = 'be28ab14b07ce763b986a6937d5ca400'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'flaskblog327@gmail.com'
    MAIL_PASSWORD = 'project@blog1'



