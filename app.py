# Made by © Vigo Walker

from typing import Optional
from fastapi import FastAPI, Body, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from content import Html

from backend import Profile

app = FastAPI() # TODO: Ver si asi se hacia
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
@app.post('/admin/trading/crypto/add', tags=['Admin'], dependencies=[Depends(JWTBearer())])
def AddCrypto(token):
    """Add crypto"""
    if token == "4d0dacb16570b8c82b6bd5bd01342dd2b7b63c7bf95b9e9bbe2d41eca8bf59d61820b161d596693443d7e2ea84f1a3a6abddeb9b6eb0c1730b8910db53b2a04f":
        return "Authenticated"
    return "Not authenticated"