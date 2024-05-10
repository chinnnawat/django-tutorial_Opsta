FROM python:3
WORKDIR /usr/src/app/
COPY startDemoProJ/ /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "python", "/usr/src/app/manage.py", "runserver", "0.0.0.0:8000" ]
