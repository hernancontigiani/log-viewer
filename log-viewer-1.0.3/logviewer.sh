#!/usr/bin/env bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
java -ea \
   -Dlog-viewer.config-file=$SCRIPT_DIR/config/config.conf \
   -jar $SCRIPT_DIR/lib/log-viewer-cli-1.0.3.jar startup
