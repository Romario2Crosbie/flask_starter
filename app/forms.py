from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('apartment', 'Apartment'), ('house', 'House')], validators=[DataRequired()])
    num_bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    num_bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

   