#!/bin/sh

function syntax {

    echo "$0 hostname [--reload | --restart]"

}

HOST=$1

if [ "$HOST" = "" ]; then
    syntax
    exit
fi

scp src/cgi/webthumb.cgi \
    src/cgi/webthumb-preview.cgi \
    root@$HOST:/usr/lib/cgi-bin

scp src/mozilla-profile/* root@$HOST:/root/.mozilla/default/5f5dv61a.slt

scp src/startups-scripts/webthumb root@$HOST:/etc/init.d