FROM python
WORKDIR C:\Users\Admin\Desktop\Abhilash\DevOps
ADD . /calculator
EXPOSE 5000
CMD [ "python" "calc.py" ]
