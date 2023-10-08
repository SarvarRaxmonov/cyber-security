FROM python:3.10
ENV PYTHONUNBUFFERED=1
LABEL authors="sarvarrahmonov"
WORKDIR /code
COPY ./requirements/base.txt ./requirements/base.txt
COPY ./requirements/prod.txt ./requirements/prod.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements/base.txt
RUN pip install -r ./requirements/prod.txt
COPY . .
RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
