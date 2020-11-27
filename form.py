from models import Post
from flask_wtf import FlaskForm, Form
from wtforms import TextField, IntegerField, DateField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = TextField("Post Title", validators=[DataRequired()])
    date = DateField("Date (MM/DD/YYYY)", format='%m/%d/%Y', validators=[
        DataRequired()])
    time_spent = IntegerField("time Spent (Hours)", validators=[
        DataRequired()])
    learned = TextField("What was learned", validators=[DataRequired()])
    resources = TextField("Resources to remember", validators=[DataRequired()])