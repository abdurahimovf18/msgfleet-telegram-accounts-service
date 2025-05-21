from typing import Annotated
from functools import partial
from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, text, ForeignKey
from sqlalchemy import UUID as SQLUUID

from src.telegram_accounts_service.config.settings import TIMEZONE
from src.telegram_accounts_service.infrastructure.db.setup import Base
from src.telegram_accounts_service.domain.models import enums


id_ = Annotated[UUID, mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=lambda: uuid4())]
created_at = Annotated[datetime, mapped_column(DateTime, server_default=text(f"TIMEZONE('{TIMEZONE!s}', NOW())"))]
updated_at = Annotated[datetime, mapped_column(DateTime, server_default=text(f"TIMEZONE('{TIMEZONE!s}', NOW())"), 
                                               onupdate=partial(datetime.now, TIMEZONE))]


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[id_]
    phone: Mapped[str]
    created_at: Mapped[created_at]


class TelegramSession(Base):
    __tablename__ = "telegram_sessions"
    
    account_id: Mapped[UUID] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"), primary_key=True)
    session: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
