import time, os, subprocess, urllib;
import requests as r
from StockBackEnd import opening as op
from StockBackEnd import returnRate as rr
from StockBackEnd import pc_data as pd
from StockBackEnd import sbeTime as t

start_time = time.time()

#this function gives the option of request posting to the url
def smRequestPost(mess):
    groupMeID = str('')#insert Group Me ID
    p_params = { 'bot_id' : groupMeID, 'text': str(mess)}
    message = r.post("https://api.groupme.com/v3/bots/post", params = p_params)
    return(message)
        
#this function gives the option of subprocessing or execution through the terminal
def smSubProcces(mess):
    groupMeID = str('') #insert Group Me ID
    m = urllib.parse.quote_plus(mess, safe='_.-~')
    command = 'curl -X POST \"https://api.groupme.com/v3/bots/post?bot_id='+ groupMeID +'&text=' + m + '\"'
    return(subprocess.run(command))

'''#the for loop is able to use both requests post and subprocess curl post. Do not recommend using both at the same time!!
    # SubProccesing is recommend for posting fast messages to the bot but not all messages post.
    # request posts are a bit slower but all the messages post.
  '''

if __name__ == '__main__':
    # outputs the groupme messages
    #x = rr(pd(op(499)))
    a = 1
        for i in rr(pd(op(100))):
        # prints out a number making it easier to check for companies that did not show
        #up in the messenger
        i = "{0} {1}".format(a, i)
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
