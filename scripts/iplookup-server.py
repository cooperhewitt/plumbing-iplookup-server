#!/usr/bin/env python

import pygeoip
import os
import logging

import flask
from flask_cors import cross_origin 

import cooperhewitt.flask.http_pony as http_pony

app = http_pony.setup_flask_app('IPLOOKUP_SERVER')
geoip = pygeoip.GeoIP(db, pygeoip.MEMORY_CACHE)

@app.route('/ping', methods=['GET'])
@cross_origin(methods=['GET'])
def ping():

    return flask.jsonify({'stat': 'ok'})

@app.route('/lookup', methods=['GET'])
@cross_origin(methods=['GET'])
def lookup():

    ip = flask.request.get('ip')

    try:
        iso = self.geoip.country_code_by_addr(ip)
    except Exception, e:
        logging.error("failed to lookup %s, because %s" % (ip, e))
        flask.abort(500)

    rsp = { 'ip': ip, 'iso': iso }
    return flask.jsonify(**rsp)

if __name__ == '__main__':

    http_pony.run_from_cli(app)
