# -*- coding: utf-8 -*-
from app import my_app
from flask import render_template
from app import forms
from app.forms import EventSearch
from app.bm25 import timkiem
import re
#@@@@@
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')
#@
@my_app.route('/search', methods=['GET', 'POST'])
def search():
	posts = []
	form = EventSearch()
	if form.validate_on_submit():
		event = form.event_name.data
		posts = timkiem(event)
	return render_template('search.html', title='ahihi', form=form, posts = posts)
