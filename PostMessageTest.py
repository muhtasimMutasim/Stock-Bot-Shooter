###This document is for testing and implementing Ideas###
import time, subprocess, urllib
import requests as r
from StockBackEnd import opening as op
from StockBackEnd import pc_data as pd
from StockBackEnd import sbeTime as t

start_time = time.time()
response = r.get("https://api.groupme.com/v3/bots/post")
bot_id = ''
response2 = r.get("https://api.groupme.com/v3/bots/post?bot_id=") #

#if __name__ == '__main__':
#    print(response.status_code)
#    print(response2.status_code)

def smRequestPost(mess):
    #response = r.get("https://api.groupme.com/v3/bots/post")
    groupMeID = str('28e7f399ce22e87fc6670df7b7')#insert Group Me ID
    #p_params2 = { 'bot_id' : groupMeID, 'text': str(mess)}
    idGm = { 'bot_id' : groupMeID} #, 'text': str(mess)}
    dataa = {'text': mess}
    #message2 = r.post("https://api.groupme.com/v3/bots/post", params = p_params)
    message = r.post("https://api.groupme.com/v3/bots/post", params = idGm, data = dataa)
    if (response2.status_code == 200):
        return(message)
    else:
        time.sleep(.5)
        if (response2.status_code == 200):
            return(message)

def smSubProcces(mess):
    groupMeID = str('28e7f399ce22e87fc6670df7b7')#insert Group Me ID
    m = urllib.parse.quote_plus(mess, safe='_.-~')
    command = 'curl -X POST \"https://api.groupme.com/v3/bots/post?bot_id='+ groupMeID +'&text=' + m + '\"'
    if (response.status_code == 500):
        return(subprocess.run(command))
    else:
        time.sleep(.5)
        return(subprocess.run(command))
        

##if __name__ == '__main__':
##    #for i in reList(opening()):# outputs the groupme messages
##    #x = rr(pd(op(499)))
##    for i in rr(pd(op(100))):
##        print(i['return'])
##    


def returnRate(in_data):#checks the return rate of every 
    gb_list = []# input and spits out a stock 
    good = int(3)# statement.
    bad = int(-3)
    append = gb_list.append
    numFirms = 0
    for i in in_data:
        num = i['%']
        if ((num < good and num > 0) or (num > bad and num < 0)):
            continue
        elif i['%']  > good:
            good_return = "{0} made a positive return of: % {1}".format(i['name'], i['%'])
            g_dict = {'return': good_return}
            append(g_dict)
            numFirms += 1
            #return(g_dict)
        elif i['%'] < bad:
            bad_return = "{0} made a negative return of: % {1}".format(i['name'], i['%'])
            b_dict = {'return': bad_return}
            append(b_dict)
            numFirms += 1
    return(gb_list)

def everything():
    a = 1
    for i in returnRate(pd(op(500))):
        i = i['return']
        i = "{0} {1}".format(a, i)
        smRequestPost(i)
        #time.sleep(.5)
        #smSubProcces(i)
        print(i)
        a += 1
    print("\n")
    t1 = t(); t2 = '---StockBackEnd2 took: {0} seconds --- # of Companies: {1}'.format((time.time() - start_time), (a-1))
    print(t1); print(t2);
    #smRequestPost(t1);
    
    smRequestPost(t2);
    time.sleep(3)
    #smSubProcces(t1); smSubProcces(t2);
    
