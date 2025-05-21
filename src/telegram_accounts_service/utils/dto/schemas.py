from datetime import datetime
from typing import Annotated, Union
from uuid import UUID

from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator
from pydantic import Field

from src.telegram_accounts_service.domain.models import enums


PhoneNumberE164 = Annotated[
    Union[str, PhoneNumber],
    PhoneNumberValidator(number_format="E164")
]


class Account:
    id = Annotated[UUID, Field()]
    phone = Annotated[PhoneNumberE164, Field(examples=["+998987654321"])]
    created_at = Annotated[datetime, Field()]


class TelegramSession:
    account_id = Account.id
    session = Annotated[str, Field()]
    created_at = Annotated[datetime, Field()]
    updated_at = Annotated[datetime, Field()]
