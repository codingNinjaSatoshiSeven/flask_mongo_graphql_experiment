FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv

# make directory /app on docker image
RUN mkdir /app
# default root folder
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]