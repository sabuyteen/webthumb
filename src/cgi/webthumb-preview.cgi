#!/bin/sh

INSTANCE_COUNT=10

error() {
    echo "Status: 500 Foobar"
}

### BEGIN CUSTOM VARIABLES ###

URLBASE=/webthumb
TMPDIR=/var/www/webthumb

for i in `seq $INSTANCE_COUNT` ; do

    #set display to use XVFB
    export DISPLAY=:$i

    #FIXME: replace with updated code..  This needs to spin until Mozilla logs that
    #it has written the file.

    sleep 1 && /usr/bin/X11/xrefresh #for safety

    #FIXME: if we can't write to this file it won't error
    import -quality 100 -window root $TMPDIR/webthumb-preview-$i.jpg || error "Couldn't write to image."

done 

echo "Content-Type: text/html"
echo 
echo "<html>"
echo "<body>"
echo "<center>"

for i in `seq $INSTANCE_COUNT` ; do
    echo "<p>"
    echo "<a href='/webthumb-preview-$i.jpg'>"
    echo "<img width='320' height='256' border='1' src='$URLBASE/webthumb-preview-$i.jpg'>"
    echo "</a>"
    echo "</p>"

    echo "<p>"
    echo "DISPLAY $i"
    echo "</p>"
done

echo "</center>"
echo "</body>"
echo "</html>"
