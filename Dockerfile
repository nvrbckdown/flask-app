FROM python:3.8-alpine

WORKDIR /app

COPY . /app/

RUN pip install -r req.txt
RUN pip install psycopg2-binary

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD ["python3", "app.py"] 
