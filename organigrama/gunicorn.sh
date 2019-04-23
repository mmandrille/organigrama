#!/bin/bash
cd /opt/organigrama
source venv/bin/activate
cd /opt/organigrama/organigrama
gunicorn organigrama.wsgi -t 600 -b 127.0.0.1:8003 -w 6 --user=servidor --group=servidor --log-file=/opt/organigrama/gunicorn.log 2>>/opt/organigrama/gunicorn.log

