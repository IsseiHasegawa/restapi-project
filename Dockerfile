FROM python:3.13
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
