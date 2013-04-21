#!/bin/sh
echo Creating environment
virtualenv env
#virtualenv -p python2.6 env

echo Install PIP inside virtual environment
./env/bin/easy_install pip

echo Installing dependencies
./env/bin/pip install -r ./build/requirements.txt
