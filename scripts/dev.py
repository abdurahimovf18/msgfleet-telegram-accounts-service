import uvicorn

def main():
    uvicorn.run("src.telegram_accounts_service.main:app", host="127.0.0.1", port=8004, reload=True)
