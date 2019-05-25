FROM jupyter/tensorflow-notebook

USER $NB_USER

RUN pip install jupyter_contrib_nbextensions && \
    jupyter contrib nbextension install --user

RUN pip install xgboost

RUN jupyter nbextension enable hide_input_all/main && \
    jupyter nbextension enable freeze/main

COPY mmhelper.ipynb /home/jovyan/work/

RUN jupyter trust /home/jovyan/mmhelper.ipynb