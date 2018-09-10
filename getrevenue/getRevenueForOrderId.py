#/data/retail_db/order_items/port_0000
#opening the file in reading mode
import sys


def getRevenueForOrderId(path,orderid):
    orderItemsFile = open(path,"r")
    #reading the file using the read() or use help(read)
    orderItemsFileRead = orderItemsFile.read()

    type(orderItemsFileRead)
    #this is string type so we need to check the string functions using the help(str)
    #we will find the splitlines() to split the lines based on the newline character.
    #also we will find the split() which seperates the given string using the given delimiter.

    orderItems = orderItemsFileRead.splitlines()

    orderItemsfilter = filter(lambda rec:int(rec.split(",")[1]) == orderid,orderItems)
    orderItemsmap = map(lambda rec:float(rec.split(",")[4]),orderItemsfilter)
    orderItemsRevenue = reduce(lambda total,element:total+element,orderItemsmap)
    return orderItemsRevenue
  
  
path = sys.argv[1]
orderid = int(sys.argv[2])
print(getRevenueForOrderId(path,orderid))