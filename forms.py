from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
      title = StringField ('Tytuł')
      description = TextAreaField ('Opis')
      done = BooleanField ('Czy zapłacone?')
      submit = SubmitField ('Potwierdź')