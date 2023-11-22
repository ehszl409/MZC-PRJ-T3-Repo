#!/bin/bash
cd /home/ec2-user/django-ecommerce/
source venv/bin/activate
python3 manage.py runserver 0.0.0.0:8000
