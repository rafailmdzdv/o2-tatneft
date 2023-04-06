WORKDIR=$(pwd)/src

LIMITPARSERDIR=$WORKDIR/limit_parser
LIMITPARSER_DJANGOMANAGE=$LIMITPARSERDIR/manage.py

O2SITEDIR=$WORKDIR/o2_site
O2SITE_DJANGOMANAGE=$O2SITEDIR/manage.py

FRONTENDDIR=$O2SITEDIR/frontend

poetry install

mkdir $WORKDIR/o2_site/excels
mv $WORKDIR/.env.example $WORKDIR/.env

echo "Installing playwright drivers"
poetry run playwright install

echo "Making migrations to projects"
poetry run python3.11  $LIMITPARSER_DJANGOMANAGE makemigrations && \
    poetry run python3.11 $LIMITPARSER_DJANGOMANAGE migrate
poetry run python3.11 $O2SITE_DJANGOMANAGE makemigrations && \
    poetry run python3.11 $O2SITE_DJANGOMANAGE migrate

cat $WORKDIR/db.sql | sqlite3 $LIMITPARSERDIR/db.sqlite3

echo "Migrated. Installing frontend dependencies"
cd $FRONTENDDIR
npm i && npm run build
