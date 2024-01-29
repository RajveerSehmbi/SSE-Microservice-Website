FROM python
WORKDIR /root
COPY . /root
RUN pip install -r requirements.txt
WORKDIR ./app
EXPOSE 80
CMD ["cd", "app"]
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

