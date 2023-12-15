FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install -r reqs.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
