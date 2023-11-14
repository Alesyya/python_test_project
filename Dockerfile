FROM python:3.8

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zipRUN unzip /tmp/chromedriver.zip -d /usr/local/bin

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]