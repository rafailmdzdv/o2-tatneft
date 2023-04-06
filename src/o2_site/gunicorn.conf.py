bind = "127.0.0.1:8001"
workers = 4
worker_class = "sync"
timeout = 120
accesslog = './gunicorn.log'
errorlog = './gunicorn_error.log'
loglevel = 'info'
