FROM python:3.8-slim

# Create folders and fix permissions.
RUN groupadd --gid 1000 lacegroup && \
    useradd lacework --uid 1000 --gid 1000 -d /home/lacework -m && \
    mkdir -p /usr/local/src/lacedata/ && \
    chmod 777 /usr/local/src/lacedata/ && \
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get install -y --no-install-recommends git dnsutils whois

USER lacework
WORKDIR /home/lacework
ENV VIRTUAL_ENV=/home/lacework/lacenv

RUN python3 -m venv $VIRTUAL_ENV && \
    mkdir -p .ipython/profile_default/startup/ && \
    mkdir -p /home/lacework/.jupyter && \
    mkdir -p /home/lacework/.local/share/jupyter/nbextensions/snippets/ && \
    mkdir -p /home/lacework/.jupyter/custom && \
    cd /home/lacework && git clone https://github.com/lacework/python-sdk.git && mv python-sdk code

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV JUPYTER_PORT=8899

COPY --chown=1000:1000 docker/docker_build/00-import.py /home/lacework/.ipython/profile_default/startup/00-import.py
COPY --chown=1000:1000 docker/docker_build/jupyter_notebook_config.py /home/lacework/.jupyter/jupyter_notebook_config.py
COPY --chown=1000:1000 docker/docker_build/logo.png /home/lacework/.jupyter/custom/logo.png
COPY --chown=1000:1000 docker/docker_build/custom.css /home/lacework/.jupyter/custom/custom.css
COPY --chown=1000:1000 docker/docker_build/lacework /home/lacework/lacenv/share/jupyter/nbextensions/lacework


RUN pip install --upgrade pip setuptools wheel && \
    pip install --upgrade ipywidgets jupyter_contrib_nbextensions jupyter_http_over_ws ipydatetime tabulate && \
    pip install --upgrade scikit-learn matplotlib python-evtx Evtx timesketch_import_client "snowflake-connector-python[secure-local-storage,pandas]" && \
    pip install --upgrade ipyaggrid keras nbformat numpy pandas pyparsing qgrid ruamel.yaml sklearn mitreattack-python && \
    pip install --upgrade tensorflow tqdm traitlets xmltodict ds4n6-lib picatrix timesketch_api_client openpyxl && \
    cd /home/lacework/code && pip install -e . && \
    cd /home/lacework/code/jupyter && pip install -e . && \
    jupyter serverextension enable --py jupyter_http_over_ws && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    #jupyter nbextension enable --py --user ipyaggrid && \
    jupyter nbextension enable snippets/main && \
    jupyter nbextension enable lacework/main && \
    jupyter nbextension install --user --py ipydatetime && \
    jupyter nbextension enable --user --py ipydatetime

COPY --chown=1000:1000 docker/docker_build/snippets.json /home/lacework/.local/share/jupyter/nbextensions/snippets/snippets.json

WORKDIR /usr/local/src/lacedata/
EXPOSE 8899

# Run jupyter.
ENTRYPOINT ["jupyter", "notebook"]
