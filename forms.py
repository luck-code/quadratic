from wtforms import Form, StringField


class CoefficientForm(Form):
    a = StringField('A')
    b = StringField('B')
    c = StringField('C')
