from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import timedelta
from datetime import datetime, date

from apps.basemodel.balancesheet_type import BalanceSheetType
from apps.database.mongoDB import create_mongo_client
mydb = create_mongo_client()


from jose import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
JWT_SECRET = 'myjwtsecret'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

chart_of_account_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


# how to get the user through authentication
@chart_of_account_router.get("/current-user/")
async def get_current_user(request:Request):

    try :
        token = request.cookies.get('access_token')
        
        # print(token)
        if token is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Not Authorized",
            # headers={"WWW-Authenticate": "Basic"},
            )
        else:
            scheme, _, param = token.partition(" ")
            payload = jwt.decode(param, SECRET_KEY, algorithms=ALGORITHM)
        
            username = payload.get("sub")    
            
            expiration_time = datetime.fromtimestamp(payload.get("exp"))
            # print(expiration_time)
            # print(datetime.utcnow())

            
            if datetime.utcnow() > expiration_time:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired. Please login again.",
                )

            # response_data = {"username": username}
            return username

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Session has expired",
            # headers={"WWW-Authenticate": "Basic"},
        )


@chart_of_account_router.get("/chart-of-account/", response_class=HTMLResponse)
async def api_login(request: Request, username: str = Depends(get_current_user)):

    return templates.TemplateResponse("chart_of_account/chart_of_account.html", {"request": request})

@chart_of_account_router.post("/api-insert-balance-sheet-type")
async def api_add_balancesheetType(item: BalanceSheetType, username: str = Depends(get_current_user)):# this is for inserting balancesheet type
    """This function is for inserting """
    try:

        dataInsert = dict()
        dataInsert = {
            "bstype": item.bs_type
            }
        mydb.bs_type.insert_one(dataInsert)
        return {"message":"User has been save"} 

    except Exception as ex:
                error_message = f"Error due to: {str(ex)}"
                return {"error": error_message}
    
