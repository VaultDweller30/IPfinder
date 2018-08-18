import socket
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u", "--url", dest="url",
              help="specify url to find the IP", action="store")

(options, args) = parser.parse_args()

try:
    if options.url:
        ip = socket.gethostbyname(options.url)
        print("URL: %s IP: %s" %(options.url, ip))
except:
    print("Unable to get IP address for URL %s" %(options.url))
    raise
