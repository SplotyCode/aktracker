from django.shortcuts import render
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot

import yfinance as yf
import ast

from aktracker.models import Stock
from aktracker.models import StockCloseHistory
from aktracker.models import StockIndex

def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'), 
            title=request.POST['imgtitle'], 
        )
        #new_img.title=request.GET['imgtitle']
        new_img.save()

    return render(request, 'uploadimg.html')

def uploadArt(request):
    if request.method == 'POST':
        new_art = ART(
            content=request.POST['content'], 
            title=request.POST['arttitle'], 
        )
        new_art.save()

    return render(request, 'articleupload.html')

def uploadMus(request):
    if(request.method=='POST'):
        new_mus = MUS(
            title = request.POST['mustitle'],
            mus = request.FILES.get('mus'),
            )
        new_mus.save()
    return render(request, 'musicupload.html')

def uploadVideo(request):
    if(request.method=='POST'):
        new_video = VIDEO(
            title = request.POST['videotitle'],
            vid = request.FILES.get('video'),
            )
        new_video.save()
    return render(request, 'videoupload.html')

def home(request):
    stocks = StockIndex.objects.all()
    content = {
    'stocks':stocks
    }
    return render(request, 'stocks.html', content)

#indexes = ["AAPL", "ABNB", "ADBE", "ADI", "ADP", "ADSK", "AEP", "ALGN", "AMAT", "AMD", "AMGN", "AMZN", "ANSS", "ASML", "ATVI", "AVGO", "AZN", "BIDU", "BIIB", "BKNG", "CDNS", "CEG", "CHTR", "CMCSA", "COST", "CPRT", "CRWD", "CSCO", "CSX", "CTAS", "CTSH", "DDOG", "DLTR", "DOCU", "DXCM", "EA", "EBAY", "EXC", "FAST", "FISV", "FTNT", "GILD", "GOOG", "GOOGL", "HON", "IDXX", "ILMN", "INTC", "INTU", "ISRG", "JD", "KDP", "KHC", "KLAC", "LCID", "LRCX", "LULU", "MAR", "MCHP", "MDLZ", "MELI", "META", "MNST", "MRNA", "MRVL", "MSFT", "MTCH", "MU", "NFLX", "NTES", "NVDA", "NXPI", "ODFL", "OKTA", "ORLY", "PANW", "PAYX", "PCAR", "PDD", "PEP", "PYPL", "QCOM", "REGN", "ROST", "SBUX", "SGEN", "SIRI", "SNPS", "SPLK", "SWKS", "TEAM", "TMUS", "TSLA", "TXN", "VRSK", "VRSN", "VRTX", "WBA", "WDAY", "XEL", "ZM", "ZS"]
#for index in indexes:
#   data = yf.download(index,'2022-01-01','2022-06-23')
#   for index2, row in data.iterrows():
#     StockCloseHistory.objects.create(stock=index, day=index2, close=row["Close"])
#     #print(index + " " + row["Close"]
#   print("finished for " + index)
#  Stock.objects.create(name=index, info=yf.Ticker(index).info)

def stock(request, stockName):
    stock = Stock.objects.filter(name=stockName).first()
    queryset = StockCloseHistory.objects.filter(stock=stockName)
    print("query set is ",queryset)
    data_source = ModelDataSource(queryset,
                              fields=['day', 'close'])
    chart = flot.LineChart(data_source)
    print("chart is ",chart)
    content = {
    'chart':chart,
    'stock': stock,
    'longName': ast.literal_eval(stock.info)["longName"]
    }
    return render(request, 'stock.html', content)
