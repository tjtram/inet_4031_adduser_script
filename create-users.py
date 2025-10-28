#!/usr/bin/python3

# INET4031
# Your Name
# Data Created
# Date Last Modified

import os
#Provides functions for interacting with the operating system.
import re
#Provides various functions that help search, match, and manipulate strings using regular expressions.
import sys
#Provides access to variables and functions that interact closely with Python interpreter and runtime environment.
#It allows developers to manipulate various aspects of program execution and interpreter itself.

def main():
    for line in sys.stdin:

        #Reads input directly from the standard input stream and supports reading multiple lines or redirected input.
        #Checks if line starts with #
        match = re.match("^#",line)

        #Removes whitespace from both ends of the line with .strip()
        #split(':') Splits the line into a list using the colon (:) as the separator.
        fields = line.strip().split(':')

        #This IF statement skips comment lines and fields that does not equal 5
        if match or len(fields) != 5:
            continue

        #These lines extract and format user data to match the structure of the Linux
        username = fields[0]
        #Extracts the username from the first field
        password = fields[1]
        #Extracts the password from the second field
        gecos = "%s %s,,," % (fields[3],fields[2])
        #Formats the GECOS field (user information)
        #jdoe:x:1001:1001:John Doe,,,:/home/jdoe:/bin/bash
                         #^^^^^^^^^^
                         #This is GECOS

        #Convert comma-separated group string to list for processing
        groups = fields[4].split(',')

        #Inform user that account creation is in progress
        print("==> Creating account for %s..." % (username))
        #Build command to create account with disabled password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Uncomment print cmd to see what commands WOULD be executed
        #Review the output to make sure everthing looks good
        #Only after confirming everything, uncomment os.system(cmd).

        #print cmd
        #os.system(cmd)

        #Inform user that password is being set
        print("==> Setting the password for %s..." % (username))
        #Build command to set user password by piping password twice
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Uncomment print cmd to see the password command that would be executed
        #Keep os.system(cmd) commented so passwords aren't actually set yet
        #Review the output to verify the command looks correct
        #Only uncomment os.system(cmd) after confirming everything is correct

        #print cmd
        #os.system(cmd)

        for group in groups:
            #Checks if group is '-', if not '-' add user to group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
