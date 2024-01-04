# Made by © Vigo Walker

from fastapi import FastAPI

app = FastAPI(__name__) # TODO: Ver si asi se hacia

@app.get('/', tags=['Home'])
def root():
    """Root call"""
    return "Home Call"

