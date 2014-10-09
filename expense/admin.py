from expense.models import *
from django.contrib import admin

class SpaciesAdmin(admin.ModelAdmin):
	list_display=('spacies',)
class BrandAdmin(admin.ModelAdmin):
	list_display=('brand',)

class GoodsAdmin(admin.ModelAdmin):
	list_display=('spacies','brand','sort','capacity','amount')
class ExpenseAdmin(admin.ModelAdmin):
	list_display=('goods','expense','retrieve','coming','date')

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Spacies, SpaciesAdmin)
admin.site.register(Brand, BrandAdmin)

