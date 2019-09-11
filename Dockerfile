FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements_base.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_base.txt

COPY . .

EXPOSE 8000

ENV OTREE_ADMIN_PASSWORD="admin"
# ENV OTREE_PRODUCTION=1
ENV OTREE_AUTH_LEVEL="DEMO"
ENV REDIS_URL="redis://redis_db:6379"

CMD [ "otree", "runprodserver", "0.0.0.0:8000" ]