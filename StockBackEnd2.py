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
    for i in rr(pd(op(100))):
        #smRequestPost(i)
        smSubProcces(i)
        print(a, i)
        a += 1
    t() # this function and the statement below measures and prints the execution time for both files
    print("---StockBackEnd2 took: %s seconds --- # of Companies: %s" % ((time.time() - start_time), (a-1)))
