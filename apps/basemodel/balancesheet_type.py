from pydantic import BaseModel
from datetime import datetime, date


class BalanceSheetType(BaseModel):
    bs_type: str