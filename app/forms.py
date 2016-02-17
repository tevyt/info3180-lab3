from flask.ext.wtf import Form
from wtforms import TextField , TextAreaField

class EmailForm(Form):
    name = TextField('name')
    email= TextField('email')
    subject = TextField('subject')
    message = TextAreaField('message')
