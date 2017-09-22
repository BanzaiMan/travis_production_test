#!/bin/bash

set -v

if [ "${TRAVIS_OS_NAME}" = "linux" ]; then
    DISPLAY=:99
    export DISPLAY

    # Xvfb sends SIGUSR1 to its parent when it finished startup, this causes the 'wait' below to stop waiting
    trap : USR1
    (trap '' USR1; Xvfb $DISPLAY -screen 0 640x480x8 -nolisten tcp > /dev/null 2>&1) &
    XVFBPID=$!
    wait || :
    trap '' USR1
    if ! kill -0 $XVFBPID 2> /dev/null; then
        echo "Xvfb failed to start" >&2
        exit 1
    fi
fi