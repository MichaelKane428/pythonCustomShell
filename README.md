# pythonCustomShell
System integration assignment

Introduction:

Setup:
//Installing nessesary packages.
As a root user (su -) enter the following commands.
Install python    - sudo apt-get install python3
Install pip       - sudo apt-get install python-pip
Install net-tools - sudo apt-get install net-tools

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

http://code.activestate.com/recipes/280500-console-built-with-cmd-object/

https://hg.python.org/cpython/file/3.3/Lib/cmd.py

https://kushaldas.in/posts/developing-command-line-interpreters-using-python-cmd2.html

https://media.readthedocs.org/pdf/cmd2/latest/cmd2.pdf

https://docs.python.org/3/library/subprocess.html

https://github.com/python-cmd2/cmd2/blob/master/cmd2.py

https://docs.python.org/3/library/getpass.html

https://stackoverflow.com/questions/927866/how-to-get-the-owner-and-group-of-a-folder-with-python-on-a-linux-machine

https://www.linuxquestions.org/questions/linux-server-73/why-bash-ifconfig-command-not-found-when-typing-%24ifconfig-687928/
