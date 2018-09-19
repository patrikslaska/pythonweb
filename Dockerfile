FROM python:2-onbuild

COPY secrets.sh /secrets.sh

CMD ["/secrets.sh"]

CMD [ "python", "./webapp.py" ]
