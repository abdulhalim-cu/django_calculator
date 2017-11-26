from django.contrib import admin
from .models import MediaType, CustomerType, SquareFeetRange


class MediaTypeAdmin(admin.ModelAdmin):
    fields = ['media_type']
    
class CustomerTypeAdmin(admin.ModelAdmin):
	fields = ['customer_type']

class SquareFeetRangeAdmin(admin.ModelAdmin):
	list_display = ('media', 'customer', 'square_feet', 'cost_per_sqft')


# admin.site.register(MediaTypes)
# admin.site.register(CustomerType)
admin.site.register(MediaType, MediaTypeAdmin)
admin.site.register(CustomerType, CustomerTypeAdmin)
admin.site.register(SquareFeetRange, SquareFeetRangeAdmin)
