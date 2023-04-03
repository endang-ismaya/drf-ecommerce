from django.contrib import admin
from _apps.product import models


admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.Category)
