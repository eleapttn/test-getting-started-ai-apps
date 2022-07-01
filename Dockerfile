FROM python:3.9

WORKDIR /workspace

RUN pip install flask==2.1.2
ADD app.py /workspace/

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

EXPOSE 5000

CMD [ "python3" , "/workspace/app.py" ]
