WORKDIR=$(pwd)/src

LIMITPARSERDIR=$WORKDIR/limit_parser
LIMITPARSER_DJANGOMANAGE=$LIMITPARSERDIR/manage.py

O2SITEDIR=$WORKDIR/o2_site
FRONTENDDIR=$O2SITEDIR/frontend

export PYTHONPATH="$WORKDIR/"
sleep 4 && poetry run python3.11 $LIMITPARSER_DJANGOMANAGE runserver &
poetry run python3.11 $O2SITEDIR/manage.py startmonthlyparsing &
sleep 4 && cd $O2SITEDIR && poetry run gunicorn o2_site.wsgi:application -c gunicorn.conf.py &
cd $FRONTENDDIR && npm run serve -- --port 4173 &
sleep 5 && poetry run python3.11 $WORKDIR/number_sender/main.py &
