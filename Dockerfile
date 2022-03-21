FROM python:3.8-alpine
RUN apk --no-cache add --virtual .builddeps gcc gfortran musl-dev     && pip install numpy==1.22.3     && apk del .builddeps     && rm -rf /root/.cache
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "searchComics.py"]