from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    # recaptcha = RecaptchaField('A sample recaptcha field')
    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  app.config['SECRET_KEY'] = 'devkey'

  @app.route('/', methods=('GET', 'POST'))
  def index():
      form = ExampleForm()
      form.validate_on_submit()  # to get error messages to the browser
      flash('critical message', 'critical')
      flash('error message', 'error')
      flash('warning message', 'warning')
      flash('info message', 'info')
      flash('debug message', 'debug')
      flash('different message', 'different')
      flash('uncategorized message')
      return render_template('index.html', form=form)

  return app

# create an app instance
app = create_app()

app.run(debug=True)
