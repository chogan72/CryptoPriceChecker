import time, json, requests

#BTC
def bitstamp():
  BitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
  return BitStampTick.json()['last']
def bitfinex(): 
  BitFinexTick = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
  return BitFinexTick.json()['last_price']
def coinbase():
  CoinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy')
  return CoinBaseTick.json()['amount']
  
#Doge
def bittrexdoge():
  BitTrexDogeTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-doge')
  return BitTrexDogeTick.json()['result'][0]['Last']
def cmcdoge():
  CMCDogeTick = requests.get('https://api.coinmarketcap.com/v1/ticker/dogecoin/')
  return CMCDogeTick.json()[0]['price_btc']
  
#DGB
def bittrexdgb():
  BitTrexDGBTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-dgb')
  return BitTrexDGBTick.json()['result'][0]['Last']
def cmcdgb():
  CMCDGBTick = requests.get('https://api.coinmarketcap.com/v1/ticker/digibyte/')
  return CMCDGBTick.json()[0]['price_btc'] 
  
#LTC
def bittrexLTC():
  BitTrexLTCTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-LTC')
  return BitTrexLTCTick.json()['result'][0]['Last']
def cmcLTC():
  CMCLTCTick = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/')
  return CMCLTCTick.json()[0]['price_btc'] 
  
#ETH
def bittrexETH():
  BitTrexETHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ETH')
  return BitTrexETHTick.json()['result'][0]['Last']
def cmcETH():
  CMCETHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
  return CMCETHTick.json()[0]['price_btc'] 
  
#DASH
def bittrexDASH():
  BitTrexDASHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-DASH')
  return BitTrexDASHTick.json()['result'][0]['Last']
def cmcDASH():
  CMCDASHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/DASH/')
  return CMCDASHTick.json()[0]['price_btc'] 
  
#BCH
def bittrexBCH():
  BitTrexBCHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-BCC')
  return BitTrexBCHTick.json()['result'][0]['Last']
def cmcBCH():
  CMCBCHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/')
  return CMCBCHTick.json()[0]['price_btc'] 
  
while True:
  #BTC
  bitstamplive = float(bitstamp())
  bitfinexlive = float(bitfinex())
  coinbaselive = float(coinbase())
  BTCPrice = float((bitstamplive + bitfinexlive + coinbaselive) / 3)
  BTCavg = str(round((BTCPrice), 2))
  
  #BCH
  bittrexBCHlive = float(bittrexBCH())
  cmcBCHlive = float(cmcBCH())
  BCHBTCavg = ((bittrexBCHlive + cmcBCHlive) / 2)
  BCHavg = str(round((BCHBTCavg * BTCPrice), 2))
  
  #ETH
  bittrexETHlive = float(bittrexETH())
  cmcETHlive = float(cmcETH())
  ETHBTCavg = ((bittrexETHlive + cmcETHlive) / 2)
  ETHavg = str(round((ETHBTCavg * BTCPrice), 2))
  
  #LTC
  bittrexLTClive = float(bittrexLTC())
  cmcLTClive = float(cmcLTC())
  LTCBTCavg = ((bittrexLTClive + cmcLTClive) / 2)
  LTCavg = str(round((LTCBTCavg * BTCPrice), 2))
  
  #DASH
  bittrexDASHlive = float(bittrexDASH())
  cmcDASHlive = float(cmcDASH())
  DASHBTCavg = ((bittrexDASHlive + cmcDASHlive) / 2)
  DASHavg = str(round((DASHBTCavg * BTCPrice), 2))
  
  #Doge
  bittrexdogelive = float(bittrexdoge())
  cmcdogelive = float(cmcdoge())
  DogeBTCavg = ((bittrexdogelive + cmcdogelive) / 2)
  Dogeavg = str(round((DogeBTCavg * BTCPrice), 4))
  
  #DGB
  bittrexdgblive = float(bittrexdgb())
  cmcdgblive = float(cmcdgb())
  DGBBTCavg = ((bittrexdgblive + cmcdgblive) / 2)
  DGBavg = str(round((DGBBTCavg * BTCPrice), 4))
  
  print("BTC Price: $" + BTCavg)
  print("BCH Price: $" + BCHavg)
  print("ETH Price: $" + ETHavg)
  print("LTC Price: $" + LTCavg)
  print("DASH Price: $" + DASHavg)
  print("DOGE Price: $" + Dogeavg)
  print("DGB Price: $" + DGBavg)
  print("=-=-=-=-=-=-=-=-=-=-=-=")
  time.sleep(60)