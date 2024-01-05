# Made by © Vigo Walker

from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

from content import Html

from backend import Profile

app = FastAPI() # TODO: Ver si asi se hacia
app.title = "Chipa API"

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
    return {"Message" : data}

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
    return "GetCryptoByID"

@app.get('/trading/GetAllCryptosIDs', tags=['Trading'], summary="Get all the cryptos id's")
def GetAllCryptosIDs():
    """Get all the cryptos id's"""
    return "GetAllCryptosIDs"

@app.get('/trading/GetAllCryptos', tags=['Trading'], summary="Get all the crypto")
def GetAllCryptos():
    """Get all the crypto"""
    return "GetAllCryptos"


# -------------------------------------------- Admin -------------------------------------------- #
