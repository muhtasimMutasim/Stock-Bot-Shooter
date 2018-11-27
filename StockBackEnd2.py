import os
import urllib
from StockBackEnd import opening as op
from StockBackEnd import returnRate as rr
from StockBackEnd import pc_data as pd


def sendMessage(mess):
    groupMeID = str('')#insert Group Me ID
    m = urllib.parse.quote(mess, safe='_.-~')
    command = 'curl -X POST \"https://api.groupme.com/v3/bots/post?bot_id='+ groupMeID +'&text=' + m + '\"'
    return(os.system(command))

if __name__ == '__main__':
    #for i in reList(opening()):# outputs the groupme messages
    for i in rr(pd(op(230))):
        sendMessage(i)
        print(i)
