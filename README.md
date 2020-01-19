# CameraHub

CameraHub is a web app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them. Read the [Concepts](docs/CONCEPTS.md)
section for full details on the capabilities of CameraHub.

It replaces an earlier command-line project, called [PhotoDB](https://github.com/djjudas21/photodb-perl), which has now been deprecated.

## Installing CameraHub

There are several ways of installing CameraHub, depending on your needs:

* With Pip
* [From source](docs/INSTALL_SOURCE.md)
* [With Docker](docs/INSTALL-DOCKER.md)
* [With Kubernetes](docs/INSTALL-KUBERNETES.md)

## Configuring CameraHub

CameraHub requires almost no additional config to run with default settings. However it is insecure in this configuration so at least `CAMERAHUB_SECRET_KEY` and
`CAMERAHUB_PROD` must be set if you are running in production.

The following environment variables are supported:

| Variable                     | Use                                                                                                        | Default                                                         |
|------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `CAMERAHUB_ADMIN_EMAIL`      | email address for the `admin` account                                                                      | `admin@example.com`                                             |
| `CAMERAHUB_ADMIN_PASSWORD`   | password for the `admin` account                                                                           | `admin`                                                         |
| `CAMERAHUB_DB_ENGINE`        | [database engine](https://docs.djangoproject.com/en/3.0/ref/settings/#engine)                              | `django.db.backends.sqlite3`                                    |
| `CAMERAHUB_DB_HOST`          | [database hostname or IP address](https://docs.djangoproject.com/en/3.0/ref/settings/#host)                |                                                                 |
| `CAMERAHUB_DB_NAME`          | [name of database schema or path to SQLite file](https://docs.djangoproject.com/en/3.0/ref/settings/#name) | `db/db.sqlite3`                                                 |
| `CAMERAHUB_DB_PASS`          | [database password](https://docs.djangoproject.com/en/3.0/ref/settings/#password)                          |                                                                 |
| `CAMERAHUB_DB_PORT`          | [database port](https://docs.djangoproject.com/en/3.0/ref/settings/#port)                                  |                                                                 |
| `CAMERAHUB_DB_USER`          | [database username](https://docs.djangoproject.com/en/3.0/ref/settings/#user)                              |                                                                 |
| `CAMERAHUB_PROD`             | enable [Django production mode](https://docs.djangoproject.com/en/3.0/ref/settings/#debug)                 | `false` when running from source, `true` when running in Docker |
| `CAMERAHUB_SECRET_KEY`       | random value to be kept secret. Generate [here](https://miniwebtool.com/django-secret-key-generator/)      | `OverrideMe!`                                                   |
| `CAMERAHUB_SENDGRID_API_KEY` | API key for Sendgrid email backend                                                                         |                                                                 |

## See also

* [Concepts](docs/CONCEPTS.md)
* [Screenshots](docs/SCREENSHOTS.md)
* [Contributing](docs/CONTRIBUTING.md)
* [Icons](docs/ICONS.md)
