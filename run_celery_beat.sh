# before running celery beat - celery worker must be already running - sh run_celery_worker.sh
celery -A celeryapp beat -l debug
