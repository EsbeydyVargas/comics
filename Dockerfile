FROM python:3.8-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
RUN python3 -m pip install -r requirements.txt  
CMD ["python", "searchComics.py"]