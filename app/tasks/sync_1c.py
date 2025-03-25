from celery import Celery

celery = Celery(
    "sync_1c",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@celery.task
def sync_data():
    # Ваш код для синхронизации
    pass