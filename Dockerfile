FROM python:3
WORKDIR /app
COPY startDemoProJ/ /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
