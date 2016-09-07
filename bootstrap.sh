#!/bin/bash
DB_NAME=pqlg_test
echo "DROP DATABASE ${DB_NAME}; CREATE DATABASE ${DB_NAME};" | psql template1
