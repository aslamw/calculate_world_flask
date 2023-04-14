FROM python:3.10.11-alpine3.16

#WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN flask db upgrade

#EXPOSE 6060

CMD [ "python", "./app.py" ]