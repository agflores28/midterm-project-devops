#!/bin/bash
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp rabbit-app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask flask-pymongo pymongo[srv]" >> tempdir/Dockerfile

echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY rabbit-app.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 2828" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/rabbit-app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t rabbitapp .
docker run -t -d -p 2828:2828 --name rabbitapprunning rabbitapp
docker ps -a