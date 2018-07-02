from django.contrib import admin
from .models import U8S,Invoices


# Register your models here.
class U8SAdmin(admin.ModelAdmin):
    search_fields = ('supplier','material_name', 'order_code')
    list_display = ('id','add_date','supplier','up_code','order_code','stock_code', 'material_name','model')
    list_filter = ('add_date','supplier',)
    ordering = ('id',)


# Register your models here.
class InvoicesAdmin(admin.ModelAdmin):
    search_fields = ('supplier','material_name', 'order_code')
    list_display = ('id','add_date','supplier','material_name','order_code','model')
    list_filter = ('add_date','supplier',)
    ordering = ('id',)

admin.site.register(U8S, U8SAdmin)
admin.site.register(Invoices, InvoicesAdmin)

