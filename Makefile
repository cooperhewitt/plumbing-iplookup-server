geoip:
	wget -O data/GeoIP.dat.gz http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
	gunzip data/GeoIP.dat.gz
