FROM python:3.10-slim

#Set Env variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1
ENV APP_ENV dev

#Create the working directory
WORKDIR /app
COPY . /app

#Install required packages
RUN pip install --no-cache-dir -r /app/requirements.txt

#Expose port
EXPOSE 8080
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]