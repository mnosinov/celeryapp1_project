# celeryapp1_project - django, celelry, redis simple project

.env content:
---
SECRET_KEY=

ALLOWED_HOSTS_LIST=localhost, 127.0.0.1

DEBUG_MODE=True

EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

# How to run
1. django runserver (in vitualenv)
2. redis-server
3. run celery worker (in vitualenv)
4. run celery beat (in vitualenv)
------------------
see corresponding sh scripts
