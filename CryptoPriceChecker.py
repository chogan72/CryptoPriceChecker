import time, json, requests, colors

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
def bittrexBTC():
  BitTrexBTCTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=USDT-BTC')
  return BitTrexBTCTick.json()['result'][0]['Last']
def cmcBTC():
  CMCBTCTick = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
  return CMCBTCTick.json()[0]['price_usd']
def krakenBTC():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker',data=json.dumps({"pair":"XXBTZUSD"}),
        headers={"content-type":"application/json"})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]
  
#BCH
def bittrexBCH():
  BitTrexBCHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-BCC')
  return BitTrexBCHTick.json()['result'][0]['Last']
def cmcBCH():
  CMCBCHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/')
  return CMCBCHTick.json()[0]['price_btc']
def bitfinexBCH(): 
  BitFinexBCHTick = requests.get("https://api.bitfinex.com/v1/ticker/bchbtc")
  return BitFinexBCHTick.json()['last_price']

#ETH
def bittrexETH():
  BitTrexETHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ETH')
  return BitTrexETHTick.json()['result'][0]['Last']
def cmcETH():
  CMCETHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
  return CMCETHTick.json()[0]['price_btc'] 
def bitfinexETH(): 
  BitFinexETHTick = requests.get("https://api.bitfinex.com/v1/ticker/ETHbtc")
  return BitFinexETHTick.json()['last_price']

#LTC
def bittrexLTC():
  BitTrexLTCTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-LTC')
  return BitTrexLTCTick.json()['result'][0]['Last']
def cmcLTC():
  CMCLTCTick = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/')
  return CMCLTCTick.json()[0]['price_btc'] 
def bitfinexLTC(): 
  BitFinexLTCTick = requests.get("https://api.bitfinex.com/v1/ticker/LTCbtc")
  return BitFinexLTCTick.json()['last_price']
  
#DASH
def bittrexDASH():
  BitTrexDASHTick = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-DASH')
  return BitTrexDASHTick.json()['result'][0]['Last']
def cmcDASH():
  CMCDASHTick = requests.get('https://api.coinmarketcap.com/v1/ticker/DASH/')
  return CMCDASHTick.json()[0]['price_btc']
  
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

turns = 0
while True:
  #BTC
  bitstamplive = float(bitstamp())
  bitfinexlive = float(bitfinex())
  coinbaselive = float(coinbase())
  bittrexBTClive = float(bittrexBTC())
  cmcBTClive = float(cmcBTC())
  krakenBTClive = float(krakenBTC())
  BTCPrice = float((bitstamplive + bitfinexlive + coinbaselive + bittrexBTClive + cmcBTClive + krakenBTClive) / 6)
  BTCavg = str(round((BTCPrice), 2))
  
  #BCH
  bittrexBCHlive = float(bittrexBCH())
  cmcBCHlive = float(cmcBCH())
  bitfinexBCHlive = float(bitfinexBCH())
  BCHBTCavg = ((bittrexBCHlive + cmcBCHlive + bitfinexBCHlive) / 3)
  BCHavg = str(round((BCHBTCavg * BTCPrice), 2))
  
  #ETH
  bittrexETHlive = float(bittrexETH())
  cmcETHlive = float(cmcETH())
  bitfinexETHlive = float(bitfinexETH())
  ETHBTCavg = ((bittrexETHlive + cmcETHlive + bitfinexETHlive) / 3)
  ETHavg = str(round((ETHBTCavg * BTCPrice), 2))
  
  #LTC
  bittrexLTClive = float(bittrexLTC())
  cmcLTClive = float(cmcLTC())
  bitfinexLTClive = float(bitfinexLTC())
  LTCBTCavg = ((bittrexLTClive + cmcLTClive + bitfinexLTClive) / 3)
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
  
  
  avgPrice = [BTCavg, BCHavg, ETHavg, LTCavg, DASHavg, Dogeavg, DGBavg]
  CoinColor = [colors.black, colors.black, colors.black, colors.black, colors.black, colors.black, colors.black,]
  CoinName = ['BTC', 'BCH', 'ETH', 'LTC', 'DASH', 'DOGE', 'DGB']
  
  if turns >= 1:
    index = 0
    while index < 7:
      if avgPrice[index] > LastPrice[index]:
        CoinColor[index] = colors.green
        index += 1
      elif avgPrice[index] < LastPrice[index]:
        CoinColor[index] = colors.red
        index += 1
      else:
        CoinColor[index] = colors.black
        index += 1
  
  if turns >= 0:
    index = 0
    while index < 7:
      print(CoinColor[index](CoinName[index] + ": $" + avgPrice[index]))
      index += 1
  print("=-=-=-=-=-=-=-=-=-=-=-=")
  
  LastPrice = [BTCavg, BCHavg, ETHavg, LTCavg, DASHavg, Dogeavg, DGBavg]
  turns += 1
  time.sleep(10)