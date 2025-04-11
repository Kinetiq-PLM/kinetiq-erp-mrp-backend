from django.contrib import admin
from .models import *

admin.site.register(BillOfMaterials)
admin.site.register(NonProjectOrderPricing)
admin.site.register(ProductMats)
admin.site.register(LaborCost)

# Register your models here.
