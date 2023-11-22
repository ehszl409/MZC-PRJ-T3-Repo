import multiprocessing

# Gunicorn을 실행할 호스트 및 포트 설정
bind = "0.0.0.0:8000"

# 작업자 프로세스 수 설정 (CPU 코어의 2배 추천)
workers = multiprocessing.cpu_count() * 2 + 1

# 작업자 타입 및 동작 설정 (여기에서는 gevent를 사용하도록 설정)
worker_class = "gevent"

# 애플리케이션의 WSGI 모듈 설정
# 여기에서는 "your_project_name.wsgi"를 적절히 변경
# your_project_name: Django 프로젝트의 폴더 이름
# wsgi: Django 프로젝트의 wsgi.py 모듈
app_module = "django_ecommerce.wsgi:application"

