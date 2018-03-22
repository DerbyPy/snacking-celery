# By using the name "celery" `celery worker` command will find the instance.
from snacking.celery.app import app as celery, apply_config


apply_config(celery)
