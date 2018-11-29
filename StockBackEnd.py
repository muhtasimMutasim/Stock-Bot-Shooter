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
        append(ticker)
    #print(tickers)
    return(tickers)

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
            #high = quote['high']
            #low = quote['low']
            #ot = quote['openTime']
            #ct = quote['closeTime']
            pricing = {'name': company, 'open': openn,'close': lp}
            append(pricing)
            #return()
        a += 1
    #print(info)
    return(info)

def increase(start, end):# function to find the rate of change
    inc = end - start
    inc = inc/start
    inc = round((inc*100), 3)
    return(inc)

def precent_change_output(x): #same as the function below it but this outputs just rate of change
    #x = opening()
    percentChange = []
    append = percentChange.append
    for x in x:
        rate_change = increase(x['open'], x['close'])
        pCOutput = x['name'] + ' precent change: % ' + str(rate_change)
        append(pCOutput)
    #print(percentChange)
    return(percentChange)

def pc_data(x):# finds the return rate of the company
    #x = opening()
    percent_change_data = []
    append = percent_change_data.append
    for x in x:
        rate_change = increase(x['open'], x['close'])
        pCDict = {'name': x['name'], '%': rate_change}
        append(pCDict)
        #print(pCDict)
    #print(percent_change_data)
    return(percent_change_data)

def returnRate(in_data):#checks the return rate of every 
    gb_list = []# input and spits out a stock 
    good = int(3)# statement.
    bad = int(-3)
    append = gb_list.append
    numFirms = 0
    for i in in_data:
        #print(i['%'])
        num = i['%']
        if ((num < good and num > 0) or (num > bad and num < 0)):
            continue
        elif i['%']  > good:
            good_return = "{0} made a positive return of: % {1}".format(i['name'], i['%'])
            append(good_return)
            numFirms += 1
        elif i['%'] < bad:
            bad_return = "{0} made a negative return of: % {1}".format(i['name'], i['%'])
            append(bad_return)
            numFirms += 1
    return(gb_list)
    #print(gb_list)
    #print(numFirms)
        
##### this function if executed tests the file and times the execution of the file #####
#if __name__ == '__main__':
    #returnRate(pc_data(opening(499)))
#    returnRate(pc_data(opening(130)))
#    print("--- %s seconds ---" % (time.time() - start_time))
    
