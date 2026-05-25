from django.contrib import admin
from ecommerceapp.models import Contact,Product,Category,Orders,OrderUpdate

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(OrderUpdate)