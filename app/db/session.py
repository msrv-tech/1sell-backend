# Добавить динамическое управление подключениями к БД (app/db/session.py)
from sqlalchemy.orm import sessionmaker
from contextvars import ContextVar

tenant_db_ctx = ContextVar("tenant_db_url")

def get_db_session():
    engine = create_engine(tenant_db_ctx.get())
    return sessionmaker(bind=engine)