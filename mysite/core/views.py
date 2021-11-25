from django.views.generic import TemplateView
from django.http import JsonResponse
from model.log import Log_crud
from model.sell import Sell_crud
from stock.module import *

from django.template.response import TemplateResponse
log_crud = Log_crud()
sell_crud = Sell_crud()

# views
class Home(TemplateView):
    template_name = 'home.html'


def sell_view(request, template_name="sell.html"):
    args = {}
    logs = log_crud.read()
    sells = sell_crud.read()

    stocks= []
    for name, stop in sells:
        stocks.append((name, CheckPrice(name).live()))
        # stocks.append((name, stop))

    args['stocks'] = stocks
    args['logs'] = logs[:10]

    return TemplateResponse(request, template_name, args)


class Api(): 
    def test(request):  
        print("\n\n*************************************test*************************************")
        
        log_crud = Log_crud()
        # log_crud.create( str(datetime.now()), "this is log test")
        # logs = log_crud.read()
        # print(logs)
        log_crud.delete()

        stocks = Sell_crud().read()
        for name, x in stocks:
            print(name,x)



        dataJson= {
            "test": "test"
        }

        return JsonResponse(dataJson)
