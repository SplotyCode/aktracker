from django.contrib import admin

from aktracker.models import Stock
from aktracker.models import StockCloseHistory
from aktracker.models import StockIndex

admin.site.register(Stock)
admin.site.register(StockCloseHistory)
admin.site.register(StockIndex)