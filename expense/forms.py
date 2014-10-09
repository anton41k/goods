# -*- coding: utf-8 -*-
from django.forms import ModelForm
from expense.models import *
from django import forms
from django.contrib import auth

class ExpenseForm(ModelForm):
	class Meta:
		model=Expense
	
class Month(forms.Form):
	m = ((u'--Месяц--',(
				('1',u'Январь'),
				('2',u'Февраль'),
				('3',u'Март'),
				('4',u'Апрель'),
				('5',u'Май'),
				('6',u'Июнь'),
				('7',u'Июль'),
				('8',u'Август'),
				('9',u'Сентябрь'),
				('10',u'Октябрь'),
				('11',u'Ноябрь'),
				('12',u'Декабрь'),
			)
		),)
	month = forms.ChoiceField(choices = m,widget = forms.Select(attrs = {'size':'1'}))

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())
