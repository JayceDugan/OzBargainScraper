FROM python:3.9.1

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

WORKDIR /usr/src

COPY . .

CMD ["python", "./oz_bargain_scraper.py"]
