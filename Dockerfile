FROM python:3

WORKDIR /usr/src/app

RUN pip install flask joblib scikit-learn

COPY demo.py .

COPY demo.pkl .

CMD ["python", "./demo.py"]