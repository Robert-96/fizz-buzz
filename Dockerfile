FROM robert96/tox

COPY . /source
WORKDIR /source

RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install setuptools wheel
RUN tox