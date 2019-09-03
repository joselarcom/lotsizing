FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements_base.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_base.txt

COPY . .

EXPOSE 8000

CMD [ "otree", "devserver", "8000" ]