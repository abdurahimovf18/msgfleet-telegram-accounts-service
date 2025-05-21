from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import load_only

from src.telegram_accounts_service.infrastructure.db import models
from src.telegram_accounts_service.domain.models import enums

from ..dto.parameters import telegram_sessions as p
from ..dto.responses import telegram_sessions as r



async def get(param: p.GetDTO, session: AsyncSession) -> r.GetDTO:
    query = (
        sa.select(models.TelegramSession)
        .where(models.TelegramSession.account_id == param.account_id)
    )
    response = await session.execute(query)
    return r.GetDTO.model_validate(response.scalar_one())


async def create(param: p.CreateDTO, session: AsyncSession) -> r.CreateDTO:
    session = models.TelegramSession(account_id=param.account_id, session=param.session)
    session.add(session)
    await session.flush([session])
    return r.CreateDTO.model_validate(session)
