from django.contrib import admin
from .models import Category,SubCategory,Product1,Cart,Customer,OrderPlaced

class orderadmin(admin.ModelAdmin) :
    list_display=('user','customer','product','quantity','date_ordered','status')
    list_editable=('status',)
    list_filter=('date_ordered',)

class productfilter(admin.ModelAdmin):
    list_display=('name','cat_id','img','price')
    list_editable=('price','img')
    search_fields=('name',)

# Register your models here.
admin.site.register(Product1,productfilter)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(OrderPlaced,orderadmin)