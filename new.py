
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
