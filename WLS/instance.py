connect('weblogic','admin1234','t3://10.241.13.199:11100')

print '====> Checking if server UWU01_1301 is already associated with machine arqopwst13.'
ref = getMBean('/Servers/UWU01_1301')

if(ref != None):
    print '====> Server UWU01_1301 already associated with machine arqopwst13. Aborting association.'
else:
    print "====> Server UWU01_1301 not associated with machine arqopwst13, associating it."
    edit();
    startEdit();

    cd('/')
    cmo.createServer('UWU01_1301')
    cd('/Servers/' + 'UWU01_1301')
    cmo.setListenAddress('10.16.162.186')
    cmo.setListenPort(11101)
    cmo.setMachine(getMBean('/Machines/' + 'arqopwst13'))
    save();

    # add instance in cluster

    cd('/')
    cd('/Servers/UWU01_1301')
    bean = getMBean('/Clusters/UWU01')
    cmo.setCluster(bean)

    # create log access

    cd("/Servers/UWU01_1301/WebServer/UWU01_1301/WebServerLog/UWU01_1301")
    print "setting attributes for mbean type WebServerLog"
    set("FileCount", "90")
    set("RotationType", "byTime")
    set("FileName", "logs/access_%yyyy%_%MM%_%dd%_%hh%_%mm%.log")
    set("LogFileFormat", "extended")
    set("FileMinSize", "500")
    set("ELFFields", "c-ip cs-username date time cs-method cs-uri cs-version sc-status bytes time-taken")
    set("RotateLogOnStartup", "true")
    set("NumberOfFilesLimited", "true")

    # create log instance

    cd("/Servers/UWU01_1301/Log/UWU01_1301")
    print "setting attributes for mbean type Log"
    set("LogFileSeverity", "Trace")
    set("FileName", "logs/UWU01_1301_%yyyy%_%MM%_%dd%_%hh%_%mm%.log")
    set("FileMinSize", "500")
    set("RotateLogOnStartup", "true")
    set("NumberOfFilesLimited", "true")
    set("StdoutSeverity", "Notice")
    set("FileCount", "90")
    set("RotationType", "byTime")

    # applyJRF wil call save and activate
    startEdit()
    save();
    activate(block='true');
disconnect();
