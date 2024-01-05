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
def GetProfile(id):
    """GET profile data, Example usage: https://chipa.api.vigodev.net/profile?id={UID}"""
    prfl = Profile()
    data = prfl.GetProfile(id=id)
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
