from django.contrib import admin

from model.sell import Sell
from model.log import Log

@admin.register(Sell, Log)
class  StockSellAdmin(admin.ModelAdmin):
    pass