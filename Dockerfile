FROM python
WORKDIR /mnt/d/code/testing/myproject
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /mnt/d/code/testing/myproject
CMD ["python3", "./manage.py"]
