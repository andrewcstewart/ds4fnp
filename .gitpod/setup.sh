docker-compose -f .gitpod/docker-compose.yml \
    exec superset superset fab create-admin \
        --username admin \
        --firstname Superset \
        --lastname Admin \
        --email admin@superset.com \
        --password admin

docker-compose -f .gitpod/docker-compose.yml \
    exec superset superset db upgrade

# docker-compose -f .gitpod/docker-compose.yml exec superset superset load_examples

docker-compose -f .gitpod/docker-compose.yml \
    exec superset superset init

docker-compose -f .gitpod/docker-compose.yml \
    exec superset superset import_datasources -p /setup/datasources.yml