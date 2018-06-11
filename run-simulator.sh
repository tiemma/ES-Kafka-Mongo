#!/bin/bash

pip install pipenv 

cd simulator

pipenv --three install 

pipenv run python run.py

