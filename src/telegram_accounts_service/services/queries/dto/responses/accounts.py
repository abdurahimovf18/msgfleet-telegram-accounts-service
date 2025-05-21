from src.telegram_accounts_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    id: s.Account.id
