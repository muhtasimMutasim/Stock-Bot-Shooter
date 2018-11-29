import time
import os
import subprocess
import urllib
import requests as r
from StockBackEnd import opening as op
from StockBackEnd import returnRate as rr
from StockBackEnd import pc_data as pd
from StockBackEnd import sbeTime as t
start_time = time.time()

#this function gives the option of request posting to the url
def smRequestPost(mess):
    response = r.get("https://api.groupme.com/v3/bots/post")
    groupMeID = str('')#insert Group Me ID
    p_params = { 'bot_id' : groupMeID, 'text': str(mess)}
    message = r.post("https://api.groupme.com/v3/bots/post", params = p_params)
    if (response.status_code == 200):
        return(message)
    else:
        time.sleep(1)
        return(message)
    
#this function gives the option of subprocessing or execution through the terminal
def smSubProcces(mess):
    groupMeID = str('') #insert Group Me ID
    m = urllib.parse.quote_plus(mess, safe='_.-~')
    command = 'curl -X POST \"https://api.groupme.com/v3/bots/post?bot_id='+ groupMeID +'&text=' + m + '\"'
    return(subprocess.run(command))

if __name__ == '__main__':
    # outputs the groupme messages
    #x = rr(pd(op(499)))
    a = 1
    #the for loop is able to use both requests post and subprocess curl post. Do not recommend using both at the same time!!
    # SubProccesing is recommend for posting fast messages to the bot.
    # request posts are a bit slower.
    for i in rr(pd(op(100))):
        #smRequestPost(i)
        smSubProcces(i)
        print(a, i)
        a += 1
    print("\n")
    ## prints out both of the execution times of the code
    t1 = t(); t2 = '---StockBackEnd2 took: {0} seconds --- # of Companies: {1}'.format((time.time() - start_time), (a-1))
    print(t1); print(t2);
    ## sends the execution time to the groupme bots
    #smRequestPost(t1);smRequestPost(t2);  ##uncomment when using posts
    time.sleep(3)
    #smSubProcces(t1); smSubProcces(t2);## uncomment when using subproccess
