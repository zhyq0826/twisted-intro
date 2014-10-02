#!/bin/bash

case $1 in
    (s1)
        python blocking-server/slowpoetry.py --port 10001 poetry/ecstasy.txt
        ;;
    (s2)
        python blocking-server/slowpoetry.py --port 10002 poetry/fascination.txt
        ;;
    (s3)
        python blocking-server/slowpoetry.py --port 10003 poetry/science.txt
        ;;
esac
