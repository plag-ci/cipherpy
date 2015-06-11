from flask_wtf import Form
from wtforms import TextField, SelectField,TextAreaField
from wtforms.validators import DataRequired

class CipherForm(Form):
	text = TextAreaField('form-control', validators=[DataRequired()])
	key1 = TextField('form-control', validators=[DataRequired()])
	key2 = TextField('form-control')
	algorithm = SelectField('form-control', choices=[(0,'Ceasar'),(1,'Affine'),(6,'Additive'),(7,'Multiplicative'),(5,'Substitution'),(2,'Playfair'),(3,'Vigenere'),(4,'Autokey'),(8,'Hill')])
	switch = SelectField('form-control', choices=[(1,'encipher'),(0,'decipher')])

		#0 : ceasar, # key
		#1 : affine, # key1 key2
		#2 : playfair, # key (string)
		#3 : vigenere, # key (string)
		#4 : autokey, #key (string)
		#5 : substitution, #key (string)
		#6 : additive, #key (string)
		#7 : multiplicative, #key (string)