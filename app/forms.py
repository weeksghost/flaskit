from wtforms import Form, TextField, validators

class AjaxForm(Form):
    name = TextField('Name', [validators.Length(min=4, max=25)])
