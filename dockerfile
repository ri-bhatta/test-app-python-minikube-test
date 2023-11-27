FROM python:3.9
WORKDIR /app
COPY test.py /app/test.py
RUN useradd -m appuser
USER appuser
CMD ["python", "-u", "/app/test.py"]
