#!/bin/bash

source /home/alu3175/.virtualenvs/virtual_machine/bin/activate
uwsgi --ini /home/alu3175/webapps/virtual_machine/uwsgi.ini
