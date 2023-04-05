FROM python:3

COPY reader.py /
COPY DockerBasics.docx /

RUN pip install python-docx

CMD ["python", "./reader.py"]