#! /bin/bash
set -e
LOGFILE=/usr/local/virtualenvs/test/hello/hello.log
ERRORFILE=/usr/local/virtualenvs/test/hello/error.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3

#The below address:port info will be used later to configure Nginx with Gunicorn
ADDRESS=127.0.0.1:8002

# user/group to run as
#USER=your_unix_user
#GROUP=your_unix_group

#cd /usr/local/virtualenvs/test/hello/
cd /usr/local/virtualenvs/test/agent/
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE  &
