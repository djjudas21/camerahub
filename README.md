# CameraHub

CameraHub is a web app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them.

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

| Variable                        | Use                                                                                              | Default                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `CAMERAHUB_ADMIN_EMAIL`         | email address for the `admin` account                                                            | `admin@example.com`                                |
| `CAMERAHUB_ADMIN_PASSWORD`      | password for the `admin` account                                                                 | `admin`                                            |
| `CAMERAHUB_DB_ENGINE`           | [database engine](https://docs.djangoproject.com/en/3.0/ref/settings/#engine)                    | `django.db.backends.sqlite3`                       |
| `CAMERAHUB_DB_HOST`             | [database hostname or IP address](https://docs.djangoproject.com/en/3.0/ref/settings/#host)      |                                                    |
| `CAMERAHUB_DB_NAME`             | [database schema or path to SQLite db](https://docs.djangoproject.com/en/3.0/ref/settings/#name) | `db/db.sqlite3`                                    |
| `CAMERAHUB_DB_PASS`             | [database password](https://docs.djangoproject.com/en/3.0/ref/settings/#password)                |                                                    |
| `CAMERAHUB_DB_PORT`             | [database port](https://docs.djangoproject.com/en/3.0/ref/settings/#port)                        |                                                    |
| `CAMERAHUB_DB_USER`             | [database username](https://docs.djangoproject.com/en/3.0/ref/settings/#user)                    |                                                    |
| `CAMERAHUB_PROD`                | enable [Django production mode](https://docs.djangoproject.com/en/3.0/ref/settings/#debug)       | `false`                                            |
| `CAMERAHUB_SECRET_KEY`          | random secret value. Generate [here](https://miniwebtool.com/django-secret-key-generator/)       | `OverrideMe!`                                      |
| `CAMERAHUB_EMAIL_BACKEND`       | [email backend](https://docs.djangoproject.com/en/3.1/topics/email/#email-backends)              | `django.core.mail.backends.filebased.EmailBackend` |
| `CAMERAHUB_SENDGRID_KEY`        | API key for Sendgrid email backend                                                               |                                                    |
| `CAMERAHUB_EMAIL_USE_TLS`'      | enable TLS for SMTP                                                                              |                                                    |
| `CAMERAHUB_EMAIL_USE_SSL`'      | enable TLS for SMTP                                                                              |                                                    |
| `CAMERAHUB_EMAIL_HOST`          | SMTP server hostname                                                                             |                                                    |
| `CAMERAHUB_EMAIL_HOST_USER`     | SMTP server username                                                                             |                                                    |
| `CAMERAHUB_EMAIL_HOST_PASSWORD` | SMTP server password                                                                             |                                                    |
| `CAMERAHUB_EMAIL_PORT`          | SMTP server port number                                                                          |                                                    |
| `CAMERAHUB_FROM_EMAIL`          | [from email address](https://docs.djangoproject.com/en/3.0/ref/settings/#default-from-email)     | `noreply@camerahub.info`                           |
| `CAMERAHUB_DOMAIN`              | [site domain](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts)                 | `camerahub.info`                                   |
| `CAMERAHUB_REDIS`               | enable [Redis caching](https://docs.djangoproject.com/en/3.0/topics/cache/)                      | `false`                                            |
| `CAMERAHUB_REDIS_HOST`          | Redis hostname or IP address                                                                     | `127.0.0.1`                                        |
| `CAMERAHUB_REDIS_PORT`          | Redis port                                                                                       | `6379`                                             |

## See also

* [Screenshots](docs/SCREENSHOTS.md)
* [Contributing](docs/CONTRIBUTING.md)
* [Changelog](https://github.com/djjudas21/camerahub/releases)
* [Icons](docs/ICONS.md)
