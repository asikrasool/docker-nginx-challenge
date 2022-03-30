FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
COPY run.sh run.sh
RUN pip install -r requirements.txt
COPY . .
CMD ["/bin/sh", "-l", "run.sh"]
