#!/bin/sh
echo "Recording sound for $1 seconds to $2 file"
#arecord -f cd -d $1 -c 1 -t wav | oggenc -r -o "~/rapp/communication/data/sound.ogg"
#arecord -f S16_LE -c1 -r22050 -d $1 -t raw #| oggenc - -r -C 1 -R 22050 -q 2 -o $2
arecord -r 16000 -f S16_LE -d $1 -c 1 -D plughw:0,0 -t wav $2
echo "Recording finished"
