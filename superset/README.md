## Running supsert

```
superset run -p 8088 --with-threads --reload --debugger
```

## Upgrading superset

To upgrade superset in a native installation, run the following commands:

```
pip install apache-superset --upgrade
superset db upgrade
superset init
```

## Importing and exporting

```sh
# exports
superset export-datasources -f datasources.yml
superset export-dashboards -f dashboards.json

# imports
superset import-datasources -p datasources.yml
superset import-dashboards -p dashboards.json
```