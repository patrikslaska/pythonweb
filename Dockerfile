FROM python:2-onbuild

COPY secrets.sh /secrets.sh

ENTRYPOINT ["secrets.sh"]

CMD [ "python", "./webapp.py" ]
