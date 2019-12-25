FROM python:3.6
COPY . /app
WORKDIR /app
ARG flask_app=application.py
ENV FLASK_APP=$flask_app 
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "application:app", "--reload"]