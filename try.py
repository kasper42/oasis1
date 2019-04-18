import time
from pprint import pprint
from zapv2 import ZAPv2

api = '9dk3g223t3pk57oubeer7h3bc9'
local = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}
target = 'http://bwapp.blackbox.id'

zap = ZAPv2(apikey=api)

print 'Accessing target %s' %target
zap.urlopen(target)
time.sleep(2)

print 'Spidering target %s' %target
scanid = zap.spider.scan(target)
time.sleep(2)
while (int(zap.spider.status(scanid))<100):
	print 'Spider progress %: ' + zap.spider.status(scanid)
	time.sleep(2)
print 'Spider completed'
time.sleep(5)

print 'Scanning target %s' % target
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)
print 'Scan completed'

print ('Hosts: ' + ', '.join(zap.core.hosts))
print ('Sites: ' + ', '.join(zap.core.sites))
print ('Urls: ' + ', '.join(zap.core.urls))
print ('Alerts: ')

pprint (zap.core.alerts())

# Writes the XML and HTML reports that will be exported to the workspace.
f = open('${workspace}/xmlreport.xml','w')
f2 = open('${workspace}/htmlreport.html','w')
f.write(zap.core.xmlreport(apikey = api))
f2.write(zap.core.htmlreport(apikey = api))

f.close()
f2.close()
