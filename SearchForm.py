from wtforms import Form, StringField, validators

class SearchForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    company = StringField('Company', [validators.DataRequired(), validators.Length(min=1, max=25)])


