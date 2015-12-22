#!/bin/env python
import sys
import pexpect

cmd=" ".join(sys.argv[1:])
print "cmd=[{0}]".format(cmd)

pswd=raw_input("pass: ")

c=pexpect.spawn(cmd)
c.logfile_read = sys.stdout
while True:
    i=c.expect(["[\r\n]","(?P<user>.*)@(?P<host>[^']*)'s [pP]assword: ","Are you sure you want to continue connecting \(yes/no\)\? ",pexpect.EOF,pexpect.TIMEOUT],timeout=3)
    if i==0:
        print "before: {0}".format(c.before.strip())
    elif i==1:
        print "before: {0}".format(c.before.strip())
        print "match: {0}".format(c.match.groupdict())
        c.send("{0}\n".format(pswd))
    elif i==2:
        print "before: {0}".format(c.before)
        c.send("yes\n")
    elif i==3:
        print "before: {0}".format(c.before)
        print "EOF closing..."
        c.close()
        break
    elif i==4:
        print "before: {0}".format(c.before)
        print "Timed out. continue"
    
