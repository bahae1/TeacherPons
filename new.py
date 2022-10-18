
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
        
 
class circulo():
	def __init__(self,radio):
		self.set_radio(radio)
	def set_radio(self,radio):
		if radio>=0:
			self._radio = radio
		else:
			raise ValueError("Radio positivo")
			self._radio=0
	def get_radio(self):
		print("Estoy dando el radio")
		return self._radio

	
	
	
	
	
	
def addere(a, b):
    '''Sum of input values'''
    return a + b


def minuas(a, b):
    '''Substract of input values'''
    return a - b


def pullulate(a, b):
    '''Product of input values'''
    return a * b


def partitus(a, b):
    '''Division of input values'''
    return a / b
