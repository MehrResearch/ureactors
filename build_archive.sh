#!/usr/bin/env bash

find data -type f -regextype posix-extended -regex '.*/LZ-([0-9]{2}[a-zA-Z] |[0-9]{2}[a-zA-Z]{2} ).*_.*-.*-.*\.jpg' -print0 | xargs -0 zip -v "Microscope images.zip"