#!/bin/bash

source /home/alu3175/.virtualenvs/vmweb/bin/activate
uwsgi --ini /home/alu3175/webapps/vmweb/uwsgi.ini
