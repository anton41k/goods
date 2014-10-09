from django import template
from expense.models import *
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect, HttpResponse
register=template.Library()

@register.filter
def count_goods(value):
	return sum([goods.amount for goods in Goods.objects.all() if value == goods.brand.brand])

@register.filter
def count_goods_spacies(value):
	return sum([spacies.amount for spacies in value.spaciess.all()])

@register.filter
def sum_expense_goods(value, arg):
	return sum([x.__dict__[arg[1]] for x in value.expense.all() if x.__dict__[arg[1]] and x.date.month == arg[0]])

@register.filter
def sum_expense_day1(value, arg):
	return [x for x in Expense.objects.all() if str(x.date.day) == value and x.goods.brand.brand  == arg]
@register.filter
def sum_expense_day2(value, arg):
	return sum([ x.__dict__[arg[1]] for x in value if x.__dict__[arg[1]] and x.date.month == arg[0]])

@register.filter
def sum_expense(value,arg):
	return sum([ x.__dict__[arg[1]] for y in Goods.objects.all() if y.brand.brand==value for x in Expense.objects.all() if x.goods == y and x.__dict__[arg[1]] and x.date.month == arg[0]])


@register.filter
def list_date(value,arg):
	list_date = [datetime.datetime.strftime((x.date),'%d') for x in value.expense.all() if x.__dict__[arg[1]] and x.date.month == arg[0]]
	for day in list_date:
		if day[0]=='0':
			list_date[list_date.index(day)]=day[1]
	return list_date
	
@register.filter
def brand_goods(value):
	return [(x.brand).replace(' ','') for x in Goods.objects.all() if x.spacies == value]

@register.filter
def count_goods_all(value):
	return sum([goods.amount for goods in Goods.objects.all()])

@register.filter
def sum_expense_day_all(value,arg):
	return sum([x.__dict__[arg[1]] for x in Expense.objects.all() if x.__dict__[arg[1]] and str(x.date.day) == value and x.date.month == arg[0]])

@register.filter
def sum_expense_all(value,arg):
	return sum([ x.__dict__[arg[1]] for y in Goods.objects.all() for x in Expense.objects.all() if x.goods == y and x.__dict__[arg[1]] and x.date.month == arg[0]])

