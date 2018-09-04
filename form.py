from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Email

 
class ContactForm(Form):
  name = TextField("Name",  [InputRequired("Required Field")])
  venmo = TextField("Venmo")
  method = SelectField(u"Preferred Payment Method", choices=[('ven','venmo'),('check','check')])
  description = TextField("Brief Description", [InputRequired("Required Field")])
  date = DateField("Date of Transaction",[InputRequired("Required Field")], format='%m-%d-%y')
  address = TextAreaField("Address if Check")
  upload = FileField('Receipt', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
  submit = SubmitField("Send")