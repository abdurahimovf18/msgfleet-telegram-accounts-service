from src.telegram_accounts_service.utils.dto import BaseDTO, s


class CreateAccountDTO(BaseDTO):
    phone: s.Account.phone
    

class GetOrCreateSessionDTO(BaseDTO):
    account_id: s.TelegramSession.account_id


class SendCodeDTO(BaseDTO):
    account_id: s.TelegramSession.account_id
