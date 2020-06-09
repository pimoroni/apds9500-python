# APDS9500

[![Build Status](https://travis-ci.com/pimoroni/apds9500-python.svg?branch=master)](https://travis-ci.com/pimoroni/apds9500-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/apds9500-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/apds9500-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/apds9500.svg)](https://pypi.python.org/pypi/apds9500)
[![Python Versions](https://img.shields.io/pypi/pyversions/apds9500.svg)](https://pypi.python.org/pypi/apds9500)

# Pre-requisites

You must enable (delete where appropriate):

* i2c: `sudo raspi-config nonint do_i2c 0`
* spi: `sudo raspi-config nonint do_spi 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library from PyPi:

* Just run `sudo pip install apds9500`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/apds9500-python`
* `cd apds9500-python`
* `sudo ./install.sh`

