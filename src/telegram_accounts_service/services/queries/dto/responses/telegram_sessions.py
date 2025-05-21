from src.telegram_accounts_service.utils.dto import BaseDTO, s


class GetDTO(BaseDTO):
    account_id: s.TelegramSession.account_id
    session: s.TelegramSession.session
    created_at: s.TelegramSession.created_at
    updated_at: s.TelegramSession.updated_at


class CreateDTO(BaseDTO):
    account_id: s.TelegramSession.account_id
    session: s.TelegramSession.session
    created_at: s.TelegramSession.created_at
    updated_at: s.TelegramSession.updated_at
