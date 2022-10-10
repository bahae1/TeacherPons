
import json
import requests
import time
import os
from threading import Timer

#new class leader
class Leader:

    def __init__(self, symbol="BTC", period=15):
        self.url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        self.time = period * 60 #in seconds *60
        self.alert = 2 #notify in 2% move
        self.set_limit = 5 #attempts in every candle
        self.symbol = symbol
        self.chat_id = "-1001672482817" #TOP/BOT signals

    def notify(self, signal, current_price):
        tp = 0
        sl = 0

        current_price = float(current_price)

        if signal == "SHORT📉":
            tp = current_price - current_price*1.5/100
            sl = current_price + current_price/100
        elif signal == "LONG📈":
            sl = current_price - current_price/100
            tp = current_price + current_price*1.5/100

        #text = "### "+signal+ " " + self.symbol + " ###" +"\nTP: "+ str(tp) + "\nSL: "+ str(sl)
        text = '"### "' +signal+ '" "' + self.symbol +'": "' + str(current_price) + '" ###"' +'"\n✅TP: "'+ str(tp) + '"\n⛔️SL: "'+ str(sl)
        os.system('./senderbot/src/senderbot -c ' + str(self.chat_id))
        os.system('./senderbot/src/senderbot -m ' + text)
