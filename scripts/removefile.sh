#!/bin/bash

# 파일이 위치한 디렉토리로 이동합니다.
cd /home/ec2-user/django-ecommerce

# 'static' 폴더를 제외한 모든 파일과 디렉토리를 삭제합니다.
sudo rm -rf static/

# 선택적으로, 파일이 삭제되었다는 메시지를 출력할 수 있습니다.
echo "'static' 폴더 삭제"
