#!/bin/bash

DB='lift-mongo-app';

DB_PATH="dump/$DB";

cd $DB_PATH;

for i in *.bson
do

    echo "Restoring $i to db $DB";
    mongorestore $i --db $DB -h mongo;

done

