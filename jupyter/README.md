# Lacework Jupyter Helper

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lacework/python-sdk/blob/master/jupyter/notebooks/colab_sample.ipynb)

**laceworkjupyter** is a community developed Python library for interacting with the Lacework APIs in a
Jupyter notebook environment.

The purpose of this library is to simplify using the Lacework SDK in a Jupyter notebook environment. This allows
users to more easily work with the output of all API calls to the SDK in a notebook environment.

To get a data frame with the events within a time range one can simply write this code:

```
import laceworkjupyter

with laceworkjupyter.LaceworkHelper() as lw:
    client = lw.get_client()
    df = client.events.get_for_date_range('2021-08-25T00:00:00', '2021-08-27T23:59:23')
```

And to get events from the last 5 days:

```
import laceworkjupyter

with laceworkjupyter.LaceworkHelper() as lw:
    client = lw.get_client()
    start_time, end_time = lw.parse_date_offset('LAST 5 DAYS')

    df = client.events.get_for_date_range(start_time=start_time, end_time=end_time)
```

## Requirements

- Python 3.6 or higher
- Lacework API Credentials
  - Account Name
  - API Key
  - API Secret
- Lacework Python SDK
- Pandas version 1.0.1 or higher

## Lacebook - Docker Container

The easiest way to start using the Lacework Jupyter helper is to make use of the docker notebook container called
`lacebook`. To run the container fetch the docker-compose file:

```shell
$ curl -O https://raw.githubusercontent.com/lacework/python-sdk/master/jupyter/docker/docker-compose.yml
```

Or you can create your own docker config file, create the file `docker-compose.yml` with the content of:

```
version: '3'
services:
  lacebook:
    container_name: lacebook
    image: docker.io/lacework/lacebook:latest
    ports:
      - 127.0.0.1:8899:8899
    restart: on-failure
    volumes:
      - $HOME/.lacework.toml:/home/lacework/.lacework.toml
      - /tmp:/usr/local/src/lacedata/
```

The next step is to pull the image and run the container:

```shell
$ docker-compose pull
$ docker-compose up -d
```

This will start up a lacebook container which starts a Jupyter container listening on port 8899.
To access the lacebook container visit http://localhost:8899. When prompted for a password
use `lacework`.

### Customize Container

The compose file will map up a drive on your host machine that is used as a persistent drive. That way the notebooks
you create in the container will not be deleted once you upgrade the container. This also gives you option to
share files with the container (CSV files for instance). By default this points to `/tmp/`, which is not a persistent
folder on a Linux system.

Therefore if you want a true persistent storage you will need to change the line in the docker-compose file into
another folder of your choice. Edit the file `docker-compose.yml' and change the line:

```
      - /tmp/:/usr/local/src/lacedata/
```

To a directory that persists through reboots. This can be any folder on your host system,
the only limitations are that the folder needs to be readable and writeable by a user 
with UID/GID 1000:1000 for the container user to be able to make use of it.

### Upgrade Container

The container gets rebuilt with each commit to the codebase. To upgrade the container run the following commands:

```shell
docker-compose down
docker-compose pull
docker-compose up -d
```

(*This assumes you are running the command in the same folder as the docker-compose.yml file*)

### Use Lacebook with Colab

The lacebook container can also be used with Colab notebooks. Select `Connect to a local runtime`
and enter the backend URL: `http://localhost:8899/?token=lacework`

## How-To

The docker container will by default initialize few things, among them is to expose a variable called `lw`, which
is an instance of the LaceworkHelper object. 

One way to explore what features the `lw` object has is to run inside a container:

```python
lw.*?
```

Or by typing `lw.` and then hit the `<TAB>` key for an autocomplete.

Most of the documentation will be written with notebook demonstrations. Here is a list of available notebooks to
start exploring `lacebook`:

+ [The first notebook sample](https://colab.research.google.com/github/lacework/python-sdk/blob/master/jupyter/notebooks/colab_sample.ipynb)
