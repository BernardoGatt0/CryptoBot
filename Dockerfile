FROM python:3.8
WORKDIR /app
EXPOSE 8080
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]