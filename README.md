# plumbing-iplookup-server

This is a stripped down verion of the Mozilla
[geodude](https://github.com/mozilla/geodude) code which is a small
WSGI-compliant HTTPony for doing IP lookups.

I (re)wrote this during a telco because it seemed like a useful thing to have
around.

## How do I use this thing?

First fetch the [MaxMind GeoIP Country Lite
database](http://dev.maxmind.com/geoip/geolite) by running:

	$> make geoip

This will fetch the GeoIP database and store it in the `data` directory.

Next copy `iplookup.cfg.example` to `iplookup.cfg` (or whatever you want to call
it and update the path for the `geoip.db` config parameter:

	[geoip]
	db=/path/to/iplookup-httpony/data/GeoIP.dat

Now run the server using [Gunicorn](http://www.gunicorn.org/). Gunicorn specific
configs (port, worker type, etc.) are left as an exercise to the reader.

	$> cd bin

	$> gunicorn 'iplookup:httpony("../iplookup.cfg")'

Now perform an IP lookup (if you don't pass an `ip` CGI parameter then the
remote address of the requesting client will be used) :

	$> curl 'http://127.0.0.1:8000?ip=8.8.8.8' | python -mjson.tool

	{
	    "ip": "8.8.8.8",
	    "iso": "US"
	}
