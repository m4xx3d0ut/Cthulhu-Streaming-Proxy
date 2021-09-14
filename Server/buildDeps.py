#!/usr/bin/env python3

"""
General purpose *nix package manager updater and installer.  Runs update command
from upd_cmd var and install command from inst_cmd var.  Will prompt for sudo
password if needed.  Requires user input before installing, comment out line 38
to bypass.

https://twitter.com/m4xx3d0ut
https://github.com/m4xx3d0ut
"""

import subprocess
import shlex
import sys

upd_cmd = 'sudo apt update'
inst_cmd = 'sudo apt-get -y install build-essential libpcre3 libpcre3-dev \
libssl-dev'


# Prints stdout of subprocess Popen
def cmd_out(proc):
    for line in iter(proc.stdout.readline, b''):
        sys.stdout.buffer.write(b'[$] '+line)

# Runs update and install command, requires user input at install step
def apt_upd_inst(upd, inst):
    print('[*] Preparing to install dependencies.')
    print('[+] Updating apt...')

    apt_upd = subprocess.Popen(shlex.split(upd), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(apt_upd)

    print('[+] Apt will install/update: %s' % (inst.split('install')[1]))
    input('[!] Hit enter to continue...')

    apt_inst = subprocess.Popen(shlex.split(inst), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(apt_inst)

    print('[!] Dependencies have been installed!')


if __name__ == '__main__':

    apt_upd_inst(upd_cmd, inst_cmd)
    exit(0)