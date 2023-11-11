FROM python:3.8
WORKDIR /app
EXPOSE 8000
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]