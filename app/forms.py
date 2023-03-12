from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DecimalField, FileField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from flask_wtf.file import FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired(), NumberRange(min=0, max=10)])
    bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired(), NumberRange(min=0, max=10)])
    location = StringField('Location', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired(), NumberRange(min=0, max=100000)])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_photo(self, field):
        if not field.data or field.data.filename == '':
            raise ValidationError('Please select a photo.')