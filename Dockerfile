FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements/base.txt ./requirements/base.txt
COPY ./requirements/production.txt ./requirements/production.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements/base.txt
RUN pip install -r ./requirements/production.txt
COPY . .
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
