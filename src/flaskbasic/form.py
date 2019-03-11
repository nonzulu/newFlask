# Referencing the modules
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length 

# form validation so that the input will not input empty data

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    physics = IntegerField('Physics',validators=[DataRequired()])

    maths = IntegerField('Maths', validators=[DataRequired()])

    chemistry = IntegerField('Chemistry', validators=[DataRequired()])

    submit = SubmitField('Submit')


# IntegerField('Telephone', [validators.NumberRange(min=0, max=10)])