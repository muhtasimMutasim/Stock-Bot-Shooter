import iexfinance
import bs4 as bs
import requests
import pickle
from iexfinance import Stock
import pprint

def save_company_names():# gets all the tickers
    tickers = []
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    #print(table.fi)
    e = {}
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text;
        tickers.append(ticker);
    #print(tickers)
    return(tickers)

def opening(num):# finds relevant information from the quote
    tickers = save_company_names()
    num = int(num)
    a = 0
    info = []
    for i in tickers:
        if a <= num:
            i = str(i)
            tick = i.replace("-", ".")
            firm = Stock('%s' % tick)
            quote = firm.get_quote()
            company = quote['companyName']
            openn = quote['open']
            lp = quote['latestPrice']
            close = quote['close']
            #high = quote['high']
            #low = quote['low']
            #ot = quote['openTime']
            #ct = quote['closeTime']
            pricing = {'name': company, 'open': openn,'close': lp}
            info.append(pricing)
            #return()
        a += 1
    #print(info)
    return(info)

def increase(start, end):# simple function to find the rate of change
    inc = end - start
    inc = inc/start
    inc = round((inc*100), 3)
    return(inc)

def precent_change_output(x): #same as the function below it
    #x = opening()
    percentChange = []
    for x in x:
        rate_change = increase(x['open'], x['close'])
        pCOutput = x['name'] + ' precent change: % ' + str(rate_change)
        percentChange.append(pCOutput)
    #print(percentChange)
    return(percentChange)

def pc_data(x):# finds the return rate of the company
    #x = opening()
    percent_change_data = []
    for x in x:
        rate_change = increase(x['open'], x['close'])
        pCDict = {'name': x['name'], '%': rate_change}
        percent_change_data.append(pCDict)
        #print(pCDict)
    #print(percent_change_data)
    return(percent_change_data)

def returnRate(in_data):#checks the return rate of every 
    gb_list = []# input and spits out a stock 
    good = int(2)# statement.
    bad = int(-1)
    for i in in_data:
        #print(i['%'])
        if i['%']  > good:
            good_return = i['name'] + " made a positive return of: % " + str(i['%'])
            #print(good_return)
            gb_list.append(good_return)
        elif i['%'] < bad:
            bad_return = i['name'] + " made a negative return of: % " + str(i['%'])
            #print(bad_return)
            gb_list.append(bad_return)
        else:
            pass
    return(gb_list)
    #print(gb_list)
        

#if __name__ == '__main__':
    #returnRate(pc_data(opening(230)))
    #print(x)
    #pc_data(opening())
#    save_company_names()
#    opening()
