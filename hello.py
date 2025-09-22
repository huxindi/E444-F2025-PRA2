from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)  

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    greeting = "Hello Stranger! Welcome to PRA2 Docker!"
    email_info = None

    if form.validate_on_submit():
        name = (form.name.data or "").strip()
        email = (form.email.data or "").strip()
        if "utoronto" in email.lower():
            first_name = name.split()[0] if name else "Stranger"
            greeting = f"Hello {first_name}, Welcome to PRA2 Docker!"
            email_info = f"Your UofT email is {email}."
        else:
            greeting = f"Hello {name}! Welcome to PRA2 Docker!" if name else "Hello Stranger! Welcome to PRA2 Docker!"
            email_info = f"Please use your UofT email"
            flash("Looks like you have changed your name!")
            flash("Looks like you have changed your name!")
        form = NameForm(formdata=None)

    return render_template(
        "index.html",
        form=form,
        greeting=greeting,
        email_info=email_info,
    )

@app.route("/user/<name>")
def user(name):
    form = NameForm()
    greeting = f"Hello {name}! Welcome to PRA2 Docker!"
    return render_template(
        "index.html",
        form=form,
        greeting=greeting,
        email_info=None,
    )

if __name__ == "__main__":
    app.run(debug=True)
