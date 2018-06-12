<p align="center">
  <img src="/web_client/src/assets/logo.png?raw=true" height="100">
</p>

![Screenshot](/polyledger.png?raw=true)

> Cryptoasset portfolio management platform

---

## Prerequisites

- [Docker](https://www.docker.com/community-edition) installed on your system.
- An account on [npmjs.org](https://www.npmjs.com/). Ask to be added to the Polyledger organization so you can generate an NPM token.
- A GitHub account with read/write access to this repository in the Polyledger organization.

## Quick Start

Clone this repository:

```
❯ git clone https://github.com/polyledger/polyledger.git
```

You must also install web dependencies before running the application in Docker. To install the private packages, you have to export `NPM_TOKEN` as an environment variable (see [Docker and private packages](https://docs.npmjs.com/private-modules/docker-and-private-modules)). Export it in your shell. Now install on the dependencies locally:

```
❯ cd ./polyledger/web_client && npm install
```

You will need a file containing your environment variables (either `.env.development` or `.env.production`) at the project root. The contents should contain these variables:

```
NPM_TOKEN=<npm_token>
SECRET_KEY=<secret_key>
PYTHON_ENV=<development|production>
EMAIL_HOST_PASSWORD=<email_host_password>
DJANGO_SETTINGS_MODULE=polyledger.settings.<local|production>
BITBUTTER_API_KEY=<bitbutter_api_key>
BITBUTTER_API_SECRET=<bitbutter_api_secret>
BITBUTTER_BASE_URI=<bitbutter_base_uri>
BITBUTTER_PARTNERSHIP_ID=<bitbutter_partnership_id>
BITBUTTER_PARTNER_ID=<bitbutter_partner_id>
```

Now you can build the Docker containers:

```
❯ cd .. && docker-compose build --build-arg NPM_TOKEN=${NPM_TOKEN}
```

## Development

Start the development services:

```
❯ docker-compose up
```

If you have fresh volumes and containers, you can pre-populate the database. It will create a user that can log into the [app](http://localhost:3000/login) and [admin interface](http://localhost:8000/admin/login). Just run these commands in a separate shell:

```
❯ container_id=$(docker-compose ps -q server)
❯ docker exec -it $container_id python manage.py loaddata initial_data.json --app api
```

If you pre-populate the database, 10 coins will also be created. To fetch prices, run the following:

```
❯ docker exec -it $container_id python manage.py shell
```

This will launch an interactive Python shell. You can call the task to fetch prices:

```python
>>> from api.tasks import fill_historical_prices
>>> fill_historical_prices()
```

---

## Production

Start the production services:

```
❯ docker-compose -f production.yml up
```
