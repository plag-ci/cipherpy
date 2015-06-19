import os
from werkzeug import secure_filename
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, render_template, request, redirect, url_for,make_response
from forms import *
from utils.monos import *
from utils.poly import *

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt'])
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/download-file', methods = [ 'GET', 'POST' ])
def download_file():
	response = make_response(request.form['the_file'].strip())
	response.headers["Content-Disposition"] = "attachment; filename=cipher.txt"
	return response

@app.route('/', methods = ['GET', 'POST'])
def home():
	options = {
		0 : ceasar, # key
		1 : affine, # key1 key2
		2 : playfair, # key (string)
		3 : vigenere, # key (string)
		4 : autokey, #key (string)
		5 : substitution, #key (string)
		6 : additive, #key (string)
		7 : multiplicative, #key (string)
		8 : hill,
	}

	form = CipherForm(csrf_enabled=True)
	#Form Submit
	if form.is_submitted():
		text = ''
		if request.files['file']:
			text = Cipher().remove_punctuation(request.files['file'].read())
			# for line in request.files['file'].readlines():
			# 	text += line
		else:		
			text = form.text.data

		key1 = form.key1.data
		key2 = form.key2.data
		choice = int(form.algorithm.data)
		switch = int(form.switch.data) # 0 decipher, 1 encipher
		l_txt = options[choice](key1,key2,text,switch)
	else:
		print 'oh shit'
	return render_template('form-cipher.html', **locals())

# POLY
def playfair(k1,k2,t,s): # Mono cikiyor !
	c = Playfair(k1)
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def autokey(k1,k2,t,s):
	c = Autokey(k1)
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def vigenere(k1,k2,t,s):
	c = Vigenere(k1)
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

# MONO
def substitution(k1,k2,t,s):
	c = Substitution(k1)
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def ceasar(k1,k2,t,s):
	c = Caesar(int(k1))
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def additive(k1,k2,t,s):
	c = Additive(int(k1))
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def multiplicative(k1,k2,t,s):
	c = Multiplicative(int(k1))
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def affine(k1,k2,t,s):
	if k2 == '': k2 = 0
	c = Affine(int(k1),int(k2))
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct

def hill(k1,k2,t,s):
	c = Hill([[11, 3], [8, 7]])
	if s: ct = c.encipher(t)
	else: ct = c.decipher(t)
	return ct	

app.wsgi_app = ProxyFix(app.wsgi_app)