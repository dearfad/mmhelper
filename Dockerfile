FROM python

RUN pip install flask joblib

COPY demo.py /home/

COPY demo.pkl /home/