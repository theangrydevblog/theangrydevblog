FROM python:3.6

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000

ENTRYPOINT ["./entrypoint.sh"]
