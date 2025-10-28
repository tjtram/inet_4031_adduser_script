# inet_4031_adduser_script
inet4031-module8-lab8-part2-AutomatingUserManagement

---

## Program Description
the program is an automated way for the user to accomplish the manual task of adding users. 
Instead of manually executing commands for each individual user, system administrators can prepare
a simple text file containing user information and let the script handle all account creation tasks automatically.

Normally, to add a single user to a Linux system, an administrator would need to execute several commands,
first, they would run /usr/sbin/adduser --disabled-password --gecos 'Full Name' username to create the user account.
Next, they would use /usr/bin/passwd username to set the user's password, which requires typing the password twice for confirmation.
Finally, if the user needs to belong to specific groups, the administrator would execute /usr/sbin/adduser username groupname
for each group membership.

This script automates the exact same commands that would be run manually, but reads all user information from a structured
input file and processes each user systematically. It executes the same /usr/sbin/adduser command to create accounts,
uses the same /usr/bin/passwd utility to set passwords, and runs the same /usr/sbin/adduser username groupname command for
group assignments.

---

## Program User Operation
First, users will input the file of users they want to add, then the script prompts the user to choose between dry-run mode and normal mode. 
Afterwards, it will check if a line in the file has any # or if the fields are not equal to 5. If it does have a # and the field is not 5, 
then will skip that line. If the line does not have a # and the fields equal 5, then these lines extract and format user data to match the
structure of the Linux. Then it convert comma-separated group string to list for processing, inform user that account creation is in progress,
builds a command to create account with disabled password and GECOS info, inform user that password is being set, build command to set user
password by piping password twice, and then checks if group is '-', if not '-' add user to group.

### Input File Format
The input file uses a colon-delimited format with exactly five fields per line, similar to the structure of the Linux /etc/passwd file.
Each line represents one user account to be created, and the fields must appear in the exact order specified below.
General Format:
username:password:lastname:firstname:groups

Lines with a # at the start will be skipped.
Lines not equal to 5 fields will be skipped.
### Command Excuction
Before running the script for the first time, you must make the Python file executable. Linux systems do not automatically grant execute
permissions to new files for security reasons.

Check current permissions:
$ ls -l create-users2.py

If you see -rw-r--r-- (no x for execute), you need to add execute permission.

Make the script executable:
$ chmod +x create-users2.py

Verify it's executable:
ls -l create-users2.py

You should now see -rwxr-xr-x

Basic Execution:
The script uses input redirection to read user data from a file:
./create-users2.py < create-users.input

###"Dry Run"
Dry Run means that the code will run, all the logic will run, but the code won't actually add the users.
