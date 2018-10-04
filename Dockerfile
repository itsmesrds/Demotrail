FROM python:latest
ADD app.py /
RUN pip3 install requests opencv-python Flask numpy
RUN mkdir input
RUN mkdir output
CMD [ "python3","./app.py"]
