from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PumpConfigForm(FlaskForm):
  pump_on_time = IntegerField('On Time (minutes)', validators=[DataRequired()])
  pump_off_time = IntegerField('Off Time (minutes)', validators=[DataRequired()])
  submit = SubmitField('Update')
