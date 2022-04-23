FROM python:2
WORKDIR /app
COPY . .
RUN pip install selenium
CMD ["python", "./formeArzyabiAsatid.py"]