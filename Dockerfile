FROM python:3.8-alpine
RUN apt-get update && apt-get upgrade
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "searchComics.py"]