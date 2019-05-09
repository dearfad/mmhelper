FROM jupyter/scipy-notebook

USER $NB_USER

RUN pip install jupyter_contrib_nbextensions && \
    pip install xgboost && \
    jupyter contrib nbextension install --user && \
    jupyter nbextension enable spellchecker/main --user && \
    jupyter nbextension enable toc2/main --user && \
    jupyter nbextension enable collapsible_headings/main --user && \
    jupyter nbextension enable codefolding/main --user && \
    jupyter nbextension enable codefolding/edit --user

COPY mmhelper.ipynb /home/jovyan/work/