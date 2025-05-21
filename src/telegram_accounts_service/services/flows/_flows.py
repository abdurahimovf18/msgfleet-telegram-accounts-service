from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc as sa_exc

from telethon.sessions.string import StringSession

from .dto import p, r
from src.telegram_accounts_service.services import queries


async def create_account(param: p.CreateAccountDTO, session: AsyncSession) -> r.CreateAccountDTO:
    account = await queries.accounts.create(
        queries.p.accounts.CreateDTO(phone=param.phone), session)
    
    await session.commit()

    return r.CreateAccountDTO.v(account)


async def get_or_create_session(param: p.GetOrCreateSessionDTO, session: AsyncSession) -> r.GetOrCreateSessionDTO: 
    
    try:
        session = await queries.telegram_sessions.get(
            queries.telegram_sessions.p.GetDTO(account_id=param.account_id), session)
        return r.GetOrCreateSessionDTO.v(session)
    except sa_exc.NoResultFound:
        pass
        
    session = StringSession()

    try:
        session = await queries.telegram_sessions.create(
            queries.telegram_sessions.p.CreateDTO(account_id=param.account_id))
    except sa_exc.IntegrityError:
        pass


async def send_code(param: p.SendCodeDTO, session: AsyncSession) -> r.SendCodeDTO:
    


