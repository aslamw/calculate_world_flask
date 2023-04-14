FROM python:3.6.8-alpine3.9

#WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN flask db upgrade

#EXPOSE 6060

CMD [ "python", "./app.py" ]