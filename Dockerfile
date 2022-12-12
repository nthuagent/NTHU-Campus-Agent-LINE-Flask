FROM python:3.9-buster
WORKDIR /usr/src/app
ENV GINIP=${GINIP}
ENV PORT=${PORT}

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . ./

EXPOSE 5000

# CMD ["python", "run.py"]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
