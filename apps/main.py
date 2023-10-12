from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from apps.routes.login import login_router
from apps.routes.chart_of_account import chart_of_account_router



from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="apps/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(login_router)
app.include_router(chart_of_account_router)
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}