FROM python:3
RUN apt-get update
RUN  pip3 install --upgrade jupyter && \
    pip3 install --upgrade \
    numpy \
    scipy \
    scikit-learn \
    matplotlib \
    tensorflow \
    keras \
    pandas
VOLUME /notebook
WORKDIR /notebook
COPY ./siva_hands_on_files /notebook
EXPOSE 8888
ENTRYPOINT jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
