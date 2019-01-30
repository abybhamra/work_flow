from celery_client import app


@app.task
def add(x, y):
    return x + y
