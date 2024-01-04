# Made by © Vigo Walker

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from content import Html

app = FastAPI() # TODO: Ver si asi se hacia

@app.get('/', tags=['Home'])
def root():
    """Root call"""
    return HTMLResponse(content=Html.ROOT_HTML, status_code=200)

