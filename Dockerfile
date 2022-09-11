FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /car_manager_django_app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .