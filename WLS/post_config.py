import os, sys

username = 'weblogic'
password = 'admin1234'
admin_address = '10.241.13.199'
admin_port = '11100'
admin_url = 't3://%s:%s' % (admin_address, admin_port)

connect(username, password, admin_url)

domain_name = cmo.getName()

def logging_config():

  edit()
  startEdit()

  cmo.getLog().setRotateLogOnStartup(True)

  for instance_mbean in cmo.getServers():
      instance_mbean.getLog().setRotateLogOnStartup(True)
      instance_mbean.getWebServer().getWebServerLog().setRotateLogOnStartup(True)

  save()
  activate()

def disable_autorestart():

  edit()
  startEdit()

  for instance_mbean in cmo.getServers():
    instance_mbean.setAutoRestart(False)

  save()
  activate()

def startup_config():

  edit()
  startEdit()

  for instance_mbean in cmo.getServers():
    instance_name = instance_mbean.getName()
    args = instance_mbean.getServerStart().getArguments()
    if args:
      args = args.split()
    else:
      args = []
    for x in ['SystemOut.log', 'SystemErr.log']:
      if x == 'SystemOut.log':
        new_arg = '-Dweblogic.Stdout=/logs/apps/weblogic/%s/SystemOut.log' % instance_name
      elif x == 'SystemErr.log':
        new_arg = '-Dweblogic.Stderr=/logs/apps/weblogic/%s/SystemErr.log' % instance_name
      if new_arg not in args:
        args.append(new_arg)
    instance_mbean.getServerStart().setArguments(' '.join(args))

  save()
  activate()

def main():
  try:
    cancelEdit('y')
  except:
    pass
  try:
    startup_config()
    logging_config()
    disable_autorestart()
  except Exception, ex:
    print('ERROR' + ex.toString())
    dumpStack()
    exit()

main()