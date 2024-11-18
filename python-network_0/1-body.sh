#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -sL "$1"
