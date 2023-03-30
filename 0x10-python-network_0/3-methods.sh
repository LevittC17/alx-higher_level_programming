#!/bin/bash

url=$1
curl -sI $url | grep 'Allow:' | cut -d ' ' -f 2-

