# Import modules
import shutil
import os 
import time

# Define variables
myhostname = os.getenv('HOSTNAME')
myhost = os.uname()[1]
short_hostname = myhost.split(".", 1)[0]
xdays = 15
#path  = '/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp*/log'
now   = time.time()
apps = ['/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp1/log', '/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp2/log','/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp3/log','/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp4/log','/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp5/log','/ehp/latest_ehp/jboss-eap-4.2/jboss-as/server/prapp6/log']
dirpath = '/data1/archived_logs/' + short_hostname
#print "\n Dir path " + dirpath

## Create Dir if not exists
if not os.path.exists(os.path.join('/data1/archived_logs/', short_hostname)):  
    os.mkdir(os.path.join('/data1/archived_logs/', short_hostname))  
# .. 'else: pass' is unnecessary

# List all files older than xdays
for prapps in apps:
  path = prapps
  print "\n" + str(short_hostname) + " List all files in " + str(path) + "  older than " + str(xdays) + " days will be moved to " + dirpath
  print "==========================" + "=" * len(str(xdays)) + "====="
  for root, dirs, files in os.walk(path):
    for name in files:
      filename = os.path.join(root, name)
      if os.stat(filename).st_mtime < now - (xdays * 86400):
        print(filename)
#       os.remove(filename)
        shutil.move(filename,dirpath)

