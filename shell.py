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
	cmd.shortcuts = ""
	self.prompt = "=>> "
        self.intro = "Welcome to the shell. To view the help screen type help."

    def do_pw(self, tail):
	subprocess.call(['pwd'])

    def do_ifc(self, tail):
	default = "eth0"
	if not tail:
	    command = "/sbin/ifconfig " + default
	else:
	    command = "/sbin/ifconfig " + tail
	subprocess.call(command.split(), shell=False)

    def do_dt(self, tail):
	date = datetime.datetime.now()
	date = str(date).split('.')
	print(re.sub('[-:. ]','',str(date[0])))

    def do_ud(self, tail):
	username = getpass.getuser()
	group = [groups.gr_name for groups in grp.getgrall() if username in groups.gr_mem]
	userid = pwd.getpwnam(username).pw_uid
	groupid = pwd.getpwnam(username).pw_gid
	inode = os.stat('.')
	print(str(userid)+ ',' +str(groupid)+','+username+','+','.join(group)+','+str(inode.st_ino))

    def do_help(self, tail):
	print("Welcome to the help screen!")
	print("Please find a list of available commands below.")

	print("\npw: This command will display your current working directory.")
	print("Please note that any tail commands entered will be ignored.")

	print("\nifc: The default behaviour of this command is to")
	print("display the eth0 adapter. A user can also enter an adapter")
	print("name to see if it is present on the system. e.g. ifc lo")

	print("\ndt: This command will display the cureent date/time in the form:")
	print("(year+month+day+hours+minutes+seconds")

	print("\nud: This command will display: userId, GroupId, Username,")
	print("group names, and inode address for the users home directory.")

	print("\nshell:")
	print("Prevent a user from using cmds built in shell command.")

	print("\nexit: This command exits the shell")

    def do_shell(self, tail):
	print("Warning User does not have permission to use this command.")

    def do_exit(self, tail):
	print("Exiting the shell.")
	return -1

if __name__ == '__main__':
    myShell = shell()
    myShell.cmdloop()
