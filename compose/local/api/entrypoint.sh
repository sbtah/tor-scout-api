#!/bin/ash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${API_DB}",
        user="${API_USER}",
        password="${API_PASSWORD}",
        host="${API_SERVER}",
        port="${API_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
  >&2 echo 'Waiting for scout-api-db to become available...'
  sleep 1
done
>&2 echo 'Success, scout-api-db  is available!'

exec "$@"