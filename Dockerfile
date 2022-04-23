FROM python:2
WORKDIR /app
COPY . .
RUN pip install selenium
RUN apt-get update
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb
CMD ["python", "./formeArzyabiAsatid.py"]