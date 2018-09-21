FROM python:2-onbuild
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py && pip install awscli
CMD [ "python", "./webapp.py" ]
