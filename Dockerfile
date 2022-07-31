FROM python:3.8.13-buster

RUN set -xe

RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master

ENV PATH="/root/.local/bin:$PATH"

RUN poetry --version

RUN mkdir -p /home/app/dilbert

WORKDIR /home/app/dilbert

COPY . .

RUN poetry install

CMD ["poetry", "run", "start-bot"]
