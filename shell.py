#!/usr/bin/env python

from cmd2 import Cmd as cmd
import subprocess
import datetime
import re
import pwd
import getpass
import grp
import os

class shell(cmd):

    def __init__(self):
        cmd.__init__(self)
	self.prompt = "=>> "
        self.intro = "Welcome to the shell."

    def do_pw(self, line):
	subprocess.call(['pwd'])

    def do_ifc(self, input):
	subprocess.call("ifconfig")

    def do_dt(self, line):
	date = datetime.datetime.now()
	date = str(date).split('.')
	print(re.sub('[-:. ]','',str(date[0])))

    def do_ud(self, line):
	username = getpass.getuser()
	group = [groups.gr_name for groups in grp.getgrall() if username in groups.gr_mem]
	userid = pwd.getpwnam(username).pw_uid
	groupid = pwd.getpwnam(username).pw_gid
	inode = os.stat('.')
	print(str(userid)+ ',' +str(groupid)+','+username+','+','.join(group)+','+str(inode.st_ino))

if __name__ == '__main__':
    myShell = shell()
    myShell.cmdloop()
