from django.contrib import admin

from .models import Order, OrderDetails



class OrderDetailsInlines(admin.TabularInline):
    model = OrderDetails
    # classes = ['collapse']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','date_time','user','status']
    search_fields = ['id']
    list_filter = ['status']
    inlines = [OrderDetailsInlines]
admin.site.register(Order,OrderAdmin)
