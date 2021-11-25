from django.db import models

class Sell(models.Model):
    name = models.CharField(max_length=255)
    stop_sell_percentage = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'model_stocksell'
 

class Sell_crud:
    # def __init__(self):
    #     print("Sell_crud")
    
    def read(self):
        # print("read")
        all_entries = Sell.objects.all()
        names = all_entries.values_list('name', flat=True)
        stop_sell_percentages = all_entries.values_list('stop_sell_percentage', flat=True)

        all_records = tuple(zip(names, stop_sell_percentages))
        return all_records