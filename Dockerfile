FROM python:3.9

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
ENV CHROMEDRIVER_VERSION 2.19

RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

ARG CI_COMMIT_SHORT_SHA=unknown
ARG CI_COMMIT_REF_SLUG=unknown

ENV CI_COMMIT_SHORT_SHA=${CI_COMMIT_SHORT_SHA}
ENV CI_COMMIT_REF_SLUG=${CI_COMMIT_REF_SLUG}

COPY . /opt/sibedge_automation_tests
WORKDIR /opt/sibedge_automation_tests

RUN python -m pip --no-cache-dir install --upgrade pip setuptools
RUN python -m pip install -r requirements.txt
        
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:$(pwd)"

EXPOSE 8000

CMD sleep 1200
