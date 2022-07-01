FROM python:3.9

WORKDIR /workspace

RUN pip install flask==2.1.2
ADD app.py /workspace/

CMD [ "python3" , "/workspace/app.py" ]
