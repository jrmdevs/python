import sys

username = 'weblogic'
password = 'admin1234'
url_admin = 't3://%s:%s' % ('10.241.13.199','11100')
instances_list = ["UWU01_1301"]

connect(username, password, url_admin)

for server in cmo.getServers():
  if server.getName() in instances_list:
    start(server.getName(), 'Server', block='false')

disconnect()
