# Made by © Vigo Walker

from fastapi import FastAPI

app = FastAPI(__name__) # TODO: Ver si asi se hacia

@app.route(path="/", methods=["GET", "POST"])
def root():
    """Root call"""
    pass

