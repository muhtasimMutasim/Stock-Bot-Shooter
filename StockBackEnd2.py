import os
import urllib
from StockBackend import opening as op
from StockBackend import returnRate as rr
from StockBackend import pc_data as pd


def sendMessage(mess):
    groupMeID = ''#insert Group Me ID
    m = urllib.parse.quote(mess, safe='_.-~')
    command = 'curl -X POST \"https://api.groupme.com/v3/bots/post?bot_id=%s&text=' + m + '\"' % groupMeID
    return(os.system(command))

if __name__ == '__main__':
    #for i in reList(opening()):
    for i in rr(pc_Data(op(230))):
        sendMessage(i)
        print(i)
