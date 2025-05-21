from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Account:
    id: UUID
    phone: str
    session: UUID
    created_at: datetime
