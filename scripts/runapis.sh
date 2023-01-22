#!/usr/bin/env bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export LOGDIR=../log

start_cashier_api()
{
    cd ../core

    uvicorn cashier_api:app --reload --host 0.0.0.0 --port 4200 > $LOGDIR/api/cashier_api.log 2>&1
}

start_store_api()
{
    cd ../core

    uvicorn store_api:app --reload --host 0.0.0.0 --port 4300 > $LOGDIR/api/store_api.log 2>&1
}

start_cashier_api &
start_store_api

echo "API's running, let's rock"

while tail -f $LOGDIR/api/*api.log; do
    sleep 1;
done