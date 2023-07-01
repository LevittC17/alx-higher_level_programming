#!/bin/bash
# Send a header variable X-School-User-Id must be sent with the value 98
curl -sSL -X GET -H "X-School-User-Id: 98" "$1"
