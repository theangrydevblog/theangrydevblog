FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000

ENTRYPOINT ["./entrypoint.sh"]
