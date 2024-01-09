# Made by © Vigo Walker

from typing import Optional
from fastapi import FastAPI, Body, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
import requests

from content import Html

from backend import Profile

app = FastAPI()
app.title = "Chipa API"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        return await super().__call__(request)

@app.get('/', tags=['Home'])
def root():
    """Root call"""
    return HTMLResponse(content=Html.ROOT_HTML, status_code=200)


# -------------------------------------------- profile -------------------------------------------- #

@app.get('/porfile', tags=['Profile'], summary="Get the profile of the user")
def GetProfile(uid):
    """GET profile data, Example usage: https://chipa.api.vigodev.net/profile?id={UID}"""
    prfl = Profile()
    data = prfl.GetProfile(id=uid)
    return {"Message" : data}

@app.post('/profile/add', tags=['Profile'], summary="Create profile")
def CreateProfile(name: str = Body(), email: str = Body(), password: str = Body()):
    """Create a profile"""
    prfl = Profile()
    data = prfl.CreateProfile(name=name, email=email, password=password)
    token = prfl.CreateUID(email=email, password=password)
    return JSONResponse(content={"Message" : "Done"}, status_code=200)

@app.put('/porfile/edit', tags=['Profile'], summary="Edit profile")
def EditProfile(id: str = Body(), name: str = Body(), email: str = Body(), password: str = Body()):
    """Edit profile"""
    return "Profile Edited"

@app.delete('/profile/delete', tags=['Profile'], summary="Delete profile")
def DeleteProfile(id):
    """Delete Profile"""
    return "Profile Deleted"


# -------------------------------------------- Trading -------------------------------------------- #
# TODO:
#   GetCryptoByID --> GET - NotDone
#   GetAllCryptosIDs --> GET - NotDone
#   GetAllCryptos --> GET - NotDone
#   GetBalance --> GET - NotDone
#   GetCryptoPrice --> GET - NotDone
#   GetProfitByID --> GET - NotDone
#   GetAllProfit --> GET - NotDone
#   GetTradeHistory --> GET - NotDone
#   GetOpenOptions --> GET - NotDone
#   BuyCrypto --> POST - NotDone
#   SellCrypto --> POST - NotDone
#   AddBalance --> POST - NotDone

@app.get('/trading/GetCryptoByID/{id}', tags=['Trading'], summary="Get the crypto by it's ID")
def GetCryptoByID(id):
    """Get Crypto By it's ID"""
    try:
        response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en")
        data = response.json()
        if response.status_code == 200:
            for i in data:
                if i['id'] == id:
                    return JSONResponse(content=i, status_code=200)
            return JSONResponse(content=f"No crypto found for id: {id}", status_code=404)
        return JSONResponse(content="Something when wrong", status_code=response.status_code)
    except Exception as e:
        return JSONResponse(content=f"A error ocured: {e}", status_code=400)

@app.get('/trading/GetAllCryptosIDs', tags=['Trading'], summary="Get all the cryptos id's")
def GetAllCryptosIDs():
    """Get all the cryptos id's"""
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en")
    data = response.json()
    ALLDATA = []
    if response.status_code == 200:
        for i in data:
            ALLDATA.append({"id" : i['id'], "name" : i['name']})
        return JSONResponse(content=ALLDATA, status_code=response.status_code)
    else:
        return JSONResponse(content={"error" : "A error ocured"}, status_code=response.status_code)

@app.get('/trading/GetAllCryptos', tags=['Trading'], summary="Get all the crypto")
def GetAllCryptos():
    """Get all the crypto"""
    try:
        response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en")
        data = response.json()
        return JSONResponse(content=data, status_code=response.status_code)
    except Exception as e:
        return JSONResponse(content=f"A error ocured: {e}", status_code=400)

@app.get('/trading/GetBalance', tags=['Trading'], summary="Get the balance")
def GetBalance(uid):
    """Get the balance"""
    return "GetBalance"

@app.get('/trading/GetCryptoPrice', tags=['Trading'], summary="Get the crypto price")
def GetCryptoPrice(id):
    """Get the crypto price"""
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en")
    data = response.json()
    try:
        if response.status_code == 200:
            for i in data:
                if i['id'] == id:
                    return JSONResponse(content={"Price" : i['current_price']}, status_code=200)
            return JSONResponse(content='Crypto with that ID was not found', status_code=404)
    except Exception as e:
        return JSONResponse(content=f"A error ocured: {e}", status_code=response.status_code)

@app.get('/trading/GetProfitByID', tags=['Trading'], summary="Get the profit of a specific trade")
def GetProfitByID(id):
    """Get the proift of a specific trade"""
    return "GetProfitByID"

@app.get('/trading/GetAllProfit', tags=['Trading'], summary="Get all the profit")
def GetAllProfit():
    """Get all the profit"""
    return "GetAllProfit"

@app.get('/trading/GetTradeHistory', tags=['Trading'], summary="Get the trade history")
def GetTradeHistory():
    """Get the trade history"""
    return "GetTradeHistory"

@app.get('/trading/GetOpenOptions', tags=['Trading'], summary="Get the open options")
def GetOpenOptions():
    """Get the open options"""
    return "GetOpenOptions"

@app.post('/trading/BuyCrypto', tags=['Trading'], summary="Buy crypto")
def BuyCrypto(CryptoID: int = Body(), amount: float = Body()):
    """Buy crypto"""
    return "BuyCrypto"

@app.post('/trading/SellCrypto', tags=['Trading'], summary="Sell crypto")
def SellCrypto(CryptoID: int = Body(), amount: float = Body()):
    """Sell Crypto"""
    return "SellCrypto"

@app.post('/trading/AddBalance', tags=['Trading'], summary="Add balance")
def AddBalance(amount: float = Body(), uid: str = Body()):
    """Add Balance"""
    prfl = Profile()
    prfl.AddBalance(uid=uid, amount=amount)
    return JSONResponse(content="Added balance!")

# -------------------------------------------- Admin -------------------------------------------- #
@app.post('/admin/trading/crypto/add', tags=['Admin'], dependencies=[Depends(JWTBearer())])
def AddCrypto(token):
    """Add crypto"""
    if token == "4d0dacb16570b8c82b6bd5bd01342dd2b7b63c7bf95b9e9bbe2d41eca8bf59d61820b161d596693443d7e2ea84f1a3a6abddeb9b6eb0c1730b8910db53b2a04f":
        return "Authenticated"
    return "Not authenticated"