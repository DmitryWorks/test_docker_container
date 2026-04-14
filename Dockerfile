# FROM python:3.12
FROM python:3.12-slim
WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
# Ensure your application listens on 0.0.0.0, not 127.0.0.1 (localhost), otherwise it will only be accessible inside the container.
CMD ["flask", "run", "--host=0.0.0.0", "--port=1000"]

# test