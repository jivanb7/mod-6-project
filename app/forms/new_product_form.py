from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, IntegerField, URLField
from wtforms.validators import DataRequired, NumberRange, URL, Optional, Length

class NewProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    category = StringField('Category', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    image_url1 = URLField('Image URL 1', validators=[DataRequired(), URL()])
    image_url2 = URLField('Image URL 2', validators=[Optional(), URL()])
    image_url3 = URLField('Image URL 3', validators=[Optional(), URL()])
    image_url4 = URLField('Image URL 4', validators=[Optional(), URL()])
    image_url5 = URLField('Image URL 5', validators=[Optional(), URL()])

