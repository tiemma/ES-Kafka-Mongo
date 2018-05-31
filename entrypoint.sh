#!/bin/bash

DB_PATH="dump/$DB_NAME";


if [ -d "$DB_PATH" ]; then

	cd $DB_PATH;

    for i in *.bson
    do

        echo "Restoring $i to db $DB_NAME";
        
        mongorestore $i --db $DB_NAME -h mongo;

    done

fi

exit 0

