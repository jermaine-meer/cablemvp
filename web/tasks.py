# web/tasks.py
from celery import Celery
import time
import os

# broker URL gebruikt service-naam 'redis' zoals in docker-compose
broker = os.environ.get("REDIS_URL", "redis://redis:6379/0")
cel = Celery('tasks', broker=broker)


@cel.task
def long_calc(a, b):
    # simuleer lange taak
    time.sleep(5)
    return a + b
