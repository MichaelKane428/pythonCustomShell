# pythonCustomShell
System integration assignment

Michael Kane DT211C C14402048
https://github.com/MichaelKane428/pythonCustomShell

Introduction:
The purpose of this program is to create a custom shell, which will limit a users ability to input shell commands.
The user will be restricted to six commands. These are:

1. pw: The purpose of this command is to display the user current working directory and ignore any tail commands.
2. ifc: The default functionality of this command is to display the eth0 adapter. A user can enter in any adapter they like as a tail,
and this command will display the entered adapter instead of the default one.
3. dt: Display the current date/time in the form year+month+day+hour+minute+second
4. ud: Display the userId, groupId, username, groupnames and inode of working directory in this order.
5. help: Display information about the commands available to the user
6. shell: User is prevented from using this command or its shortcut ! as it allows the user to bypass the shell in python cmd2.
7. exit: Exits the shell.

Setup:
//Installing nessesary packages.
1. As a root user (su -) enter the following commands.
2. Install python    - sudo apt-get install python3 .
3. Install pip       - sudo apt-get install python-pip .
4. Install cmd2      - sudo pip install cmd2 .
5. Install net-tools - sudo apt-get install net-tools .

NOTE - If you have issues connecting to gb.archive.ubuntu.com I found my fix at this site.
https://askubuntu.com/questions/892569/apt-get-update-not-working-in-ubuntu-16-04

//Creating the blank file.
1. su -
2. cd /bin
3. sudo touch shell.py
   These commands will move the root user to the /bin folder and create a new file called shell.py

//Creating a user.
Enter the following commands:
1. sudo useradd -m john
   useradd creates a new user and the -m creates a working directory for the user.

2. sudo passwd john
   passwd allows you to create a password for the new user

//Changing the users shell.
1. sudo nano /etc/passwd
   This file stores each user and what shell they can use.

2. navigate through the file untik you find the desired username e.g. john 
   It will look somthing like john:x:1002:1002::/home/john:

3. Modify the line by adding /bin/shell.py.
   change john:x:1002:1002::/home/john: to john:x:1002:1002::/home/john:/bin/shell.py
   if a user already has a shell assigned replace e.g. /bin/bash with /bin/shell.py

4. As root allow the file to be executed with chmod 777 shell.py 
   
Step-by-Step Guide to the creating of the shell:

1. Create a class for the shell
	class shell(cmd):
2. Create a main function outside of the class to continuously loop the shell.
	if __name__ == '__main__':
		myShell = shell()
		myShell.cmdloop()
3. The basic import needed to run the shell is: from cmd2 import Cmd as cmd
4. Create an __init__ method in the class to set the shell prmpt and welcome message.
	def __init__(self):
        cmd.__init__(self)
		self.prompt = "=>> "
        self.intro = "Welcome to the shell. To view the help screen type help."
5. Create the functions.
	def functionName(self)
6. def do_pw
	NOTE! creating a function name with do_ means the shell will run this as a command and also overwrite an existing command.
	for this function I called the linux command pwd using subprocess.call. 
	To prevent the tail being used I just didint include it in the command execution.
7. def	do_ifc
	The tricky part about this one was that I couldnt just call ifconfig. I had to put in the path /sbin/ifconfig.
	Im not fully sure why it didint work as intended, as my root and normal login account could use it without /sbin at the begining.
8. def do_dt
	To complete this task I created a python datetime object. I then took the output of the object and split it on a period.
	The reason for this was that the numbers after the period represent miliseconds and I did not need them for the program.
	Next I used re.sub to replace -,: and whitespace with nothing so the strings would be concatinated together.
	
References:

[1]
Code.activestate.com. (2017). Console built with Cmd object Python recipes ActiveState Code. 
[online] Available at: http://code.activestate.com/recipes/280500-console-built-with-cmd-object/ [Accessed 24 Oct. 2017].

[2]
hg.python.org (2017). View lib/cmd.py
[online] Available at: https://hg.python.org/cpython/file/3.3/Lib/cmd.py [Accessed 24 Oct. 2017].

[3]
kushaldas.in. (2017). Developing Command Line Interpreters using python-cmd2
[online] Available at: https://kushaldas.in/posts/developing-command-line-interpreters-using-python-cmd2.html [Accessed 24 Oct. 2017].

[4]
media.readthedocs.org. (2017). cmd2 Documentation.
[online] Available at: https://media.readthedocs.org/pdf/cmd2/latest/cmd2.pdf [Accessed 24 Oct. 2017].

[5]
docs.python.org. (2017). 17.5. subprocess — Subprocess management. 
[online] Available at: https://docs.python.org/3/library/subprocess.html [Accessed 24 Oct. 2017].

[6]
github.com. (2017). python-cmd2/cmd2
[online] Available at: https://github.com/python-cmd2/cmd2/blob/master/cmd2.py [Accessed 24 Oct. 2017].

[7]
docs.python.org. (2017). 16.9. getpass — Portable password input. 
[online] Available at: https://docs.python.org/3/library/getpass.html [Accessed 24 Oct. 2017].

[8]
stackoverflow.com. (2017). How to get the owner and group of a folder with Python on a Linux machine?
[online] Available at: https://stackoverflow.com/questions/927866/how-to-get-the-owner-and-group-of-a-folder-with-python-on-a-linux-machine [Accessed 24 Oct. 2017].

[9]
linuxquestions.org. (2017). Why "-bash: ifconfig : command not found" when typing "$ifconfig" 
[online] Available at: https://www.linuxquestions.org/questions/linux-server-73/why-bash-ifconfig-command-not-found-when-typing-%24ifconfig-687928/ [Accessed 24 Oct. 2017].

stackoverflow.com. (2017). Python: How to get group ids of one username (like id -Gn )
[online] Available at: https://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn [Accessed 24 Oct. 2017].
