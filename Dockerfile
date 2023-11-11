FROM python:3.8
WORKDIR /app
EXPOSE 8080
COPY . .
RUN pip install Flask
RUN pip install -r requirements.txt
CMD ["python", "app.py"]