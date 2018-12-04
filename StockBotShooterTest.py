import bs4 as bs
import requests
from iexfinance import Stock
import time

start_time = time.time()

def save_company_names():# gets all the tickers
    tickers = []
    append = tickers.append
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    #print(table.fi)
    e = {}
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text;
        #tickers.append(ticker);
        append(ticker)
    #print(tickers)
    return(tickers)

class Get_Stocks:
    def __init__(self, **kwargs):
        self.stock_list = kwargs

    def opening(num):# finds relevant information from the quote
    tickers = save_company_names()
    num = int(num)
    a = 0
    info = []
    append = info.append
    for i in tickers:
        if a < num:
            i = str(i)
            tick = i.replace("-", ".")
            firm = Stock('%s' % tick)
            quote = firm.get_quote()
            company = quote['companyName']
            openn = quote['open']
            lp = quote['latestPrice']
            close = quote['close']
            pricing = {'name': company, 'open': openn,'close': lp}
            #info.append(pricing)
            append(pricing)
            #return()
        a += 1
    #print(info) 
