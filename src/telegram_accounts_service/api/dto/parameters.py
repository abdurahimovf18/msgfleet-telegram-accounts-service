from src.telegram_accounts_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    phone: s.Account.phone

    
class SendCodeDTO(BaseDTO):
    id: s.Account.id
    