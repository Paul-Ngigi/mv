from flask_wtf import FlaskForm
from wtforms import EmailField ,IntegerField,SubmitField

class OrderForm(FlaskForm):
    email = EmailField('Email address')
    tickets = IntegerField('No of Tickets')
    submit = SubmitField('order')