FROM registry.access.redhat.com/ubi9/python-39:1-68

ADD . .
RUN pip install -U "pip>=19.3.1" && \
    pip install -r requirements.txt

CMD python -m gunicorn app -b 0.0.0.0 --access-logfile /dev/stdout
