FROM python:3.9-slim-buster
WORKDIR /app
COPY /app/app.py /app
COPY /app/url_map.txt /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
