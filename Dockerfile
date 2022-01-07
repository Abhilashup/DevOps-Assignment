FROM python
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
CMD [ "python","calc.py" ]
