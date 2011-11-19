#!/bin/sh
echo Creating environment
virtualenv --no-site-packages env
#virtualenv --no-site-packages -p python2.6 env

echo Install PIP inside virtual environment
./env/bin/easy_install pip

echo Installing dependencies
./env/bin/pip install -E env -r ./build/requirements.txt
