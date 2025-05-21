from fastapi import APIRouter, Depends

from src.telegram_accounts_service.services import flows
from .dto import p, r

from src.telegram_accounts_service.services.dependencies import db


router = APIRouter()


@router.post("/create")
async def create(param: p.CreateDTO,
                 session = Depends(db.session)) -> r.CreateDTO:
    
    created_account = await flows.create_account(
        flows.p.CreateAccountDTO(phone=param.phone), session)
    
    return r.CreateDTO.v(created_account)


@router.post("/send-code")
async def send_code(param: p.SendCodeDTO,
                             session = Depends(db.session)) -> r.SendCodeDTO: 
    
    sent_code = await flows.send_code()
