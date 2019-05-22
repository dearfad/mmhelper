FROM jupyter/scipy-notebook

USER $NB_USER

RUN pip install jupyter_contrib_nbextensions && \
    pip install xgboost && \
    jupyter contrib nbextension install --user && \
    jupyter nbextension enable hinterland/hinterland --user && \
    jupyter nbextension enable toc2/main --user && \
    jupyter nbextension enable collapsible_headings/main --user

COPY mmhelper.ipynb /home/jovyan/work/