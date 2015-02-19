<t> USBinteraction </t>
=======

For <b> Effits </b> ltd. needs
---
Prepare for LightDM

------
Installation:
------
Use that commands to install this software remote: 
```
    $ mkdir usb-server
    $ cd usb-server
    $ git clone https://github.com/MikhailMeshcheryakov/usb-server.git
    $ ./install
```
or just use one command if you have this pack physically:
```
	$ ./install
```

------
Description:
------
That pack includes 6 files:
```
"install" - for the installation setup & cleanup scripts into client system
"declogin" - Declare login info (setup script)
"declogout" - Declare logout info (cleanup script)
"initdb" - create initial data base
"usb-server" - server part of USBinteraction Python3 script
"usb-connector" - responsible for final part of interaction: create and remove simlinks
```
-----
Potential errors:
-----
Codes of potential errors:
```
Zero includes:
0 - result code when take incorrect Username or Display number when login
10 - result code when user connection interruped when login
...
90 - result code when take incorrect Username or Display number when logout
100 - result code when user connection interruped when logout

In first decade (Errors after login):
1 - result code is a generic error code that is used when no other more specific error code is available
2 - result code when take Operational Error in SQLite
3 - result code when take Database Error in SQLite

In second decade (Errors after logout):
11 - result code is a generic error code that is used when no other more specific error code is available
12 - result code when take Operational Error in SQLite
13 - result code when take Database Error in SQLite
```


-------------
As just nota bene
When you change something,
Do not use ('cd') directory with "Permision Denied" message for writing
do not use directories inside some temporary directories (such '/tmp')
do not forgot about problems of potential SQL injection
