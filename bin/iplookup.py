#!/usr/bin/env python

import ConfigParser
import pygeoip
import cgi
import json

# gunicorn 'iplookup:httpony("iplookup.cfg")'

class httpony:

    def __init__(self, config, autoreload=False):

        self.config_path = config
        self.config = None
        self.geoip = None

        try:

            self.config = ConfigParser.ConfigParser()
            self.config.read(config)
            db = self.config.get('geoip', 'db')

            self.geoip = pygeoip.GeoIP(db, pygeoip.MEMORY_CACHE)

        except:
            print "Error loading config:"
            raise

    def __call__(self, environ, start_response):

        status = '200 OK'
        rsp = {}

        params = cgi.parse_qs(environ.get('QUERY_STRING', ''))
        ip = params.get('ip', None)

        if not ip:
            ip = environ['REMOTE_ADDR']
        else:
            ip = ip[0]

        try:
            iso = self.geoip.country_code_by_addr(ip)
            rsp = { 'ip': ip, 'iso': iso }
        except Exception, e:
            rsp = {'stat': 'error', 'error': 'failed to locate IP: %s' % e}

        rsp = json.dumps(rsp)

        start_response(status, [
            ("Content-Type", "text/javascript"),
            ("Content-Length", str(len(rsp)))
            ])

        return iter([rsp])
