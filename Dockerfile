FROM python

WORKDIR /home/dearfad

RUN pip install flask joblib scikit-learn

COPY ./demo.py .

COPY ./demo.pkl .

CMD ['python', 'demo.py']