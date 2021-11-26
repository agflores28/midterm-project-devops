FROM python
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY rabbit-app.py /home/myapp/
EXPOSE 2828
CMD python3 /home/myapp/rabbit-app.py
