import pandas as pd
from stock.module import *
from model.sell import *
from model.log import *

class TraderSellStock:
    def __init__(self):
        print("TraderSellStock")
        self.log_crud = Log_crud()
        self.sell_crud = Sell_crud()

    def log(self, time, log):
        print(log)
        self.log_crud.create(time, log)
        self.log_crud.delete()

    def updateStock(self):
        stocks =  self.sell_crud.read()
        return stocks

    def process(self):
        timenow = getTimeNow()
        print("\n" + timenow)
        stocks = self.updateStock()
        for name, stop_sell_percentage in stocks:
            is_stock_have_share, share_hold = stock_have_share(name)
            log1=  "sell " + name + " stopPercentage:" + str(stop_sell_percentage) + " share:" + str(share_hold)

            if is_stock_have_share:
                res = stockSelltrailingStop(name, share_hold, stop_sell_percentage)
                log1 += " " +str(res)

            self.log(timenow, log1)
