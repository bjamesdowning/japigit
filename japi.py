import requests
import urllib
import json



def getStockData(symbl):
    url = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols="+symbl+"&apikey=WLQOSD2QF516NC1K"
    conn = urllib.request.urlopen(url)
    resp = conn.read().decode()
    print(resp)
    json2dict = json.loads(resp)
    print("The current price of {} is: ${}".format(symbl, json2dict["Stock Quotes"][0]["2. price"]))
    print("Stock Quotes retrieved successfully!")

if __name__ == "__main__":
    f = open("japi.out", "w+")
    while True:
        answer = input("Enter Stock Ticker (enter quit to exit): ")
        if answer != 'quit':
             getStockData(answer)
        else:
            break
#master version
