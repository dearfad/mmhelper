FROM python:3

WORKDIR /usr/src/app

RUN pip install flask joblib scikit-learn

COPY ./project/dmy/moon.py .

COPY ./project/dmy/moon.pkl .

CMD ["python", "./moon.py"]