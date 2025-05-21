from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import load_only

from src.telegram_accounts_service.infrastructure.db import models
from src.telegram_accounts_service.domain.models import enums

from ..dto.parameters import accounts as p
from ..dto.responses import accounts as r


async def create(param: p.CreateDTO, session: AsyncSession) -> r.CreateDTO:
    account = models.Account(phone=param.phone)
    session.add(account)
    await session.flush([account])
    return r.CreateDTO.model_validate(account)
