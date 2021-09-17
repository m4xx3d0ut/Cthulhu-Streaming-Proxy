#!/usr/bin/env python3

"""
A simple logging module for subprocess Popen commands.  Displays output in
terminal.  It writes to output.log by default, you can change this by setting
log_file while intantiating, or you can turn logging off by setting log_on='n'.

https://twitter.com/m4xx3d0ut
https://github.com/m4xx3d0ut
"""

import subprocess
import shlex
import os
import sys
from datetime import datetime
from getpass import getuser


class sublogger:

    default_log = 'ouput.log'

    # If you don't set log_file when instantiating it will write to output.log
    def __init__(self, log_file=default_log, log_on='y'):
        # self.cmd = cmd
        self.log_file = log_file if log_file is not None else default_log
        self.log_on = log_on if log_on == 'y' else None


    # Prints stdout of subprocess Popen and if log_on='y' writes to log file
    def cmd_out(self, cline):

        cmd = subprocess.Popen(shlex.split(cline), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        if self.log_on == 'y':
            tstamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
            username = getuser()
            cmd_line = '%s-%s-[$] %s\n' % (tstamp, username, cline)
            with open(self.log_file, 'a') as log:
                log.write(cmd_line)
            log.close

        for line in iter(cmd.stdout.readline, b''):
            sys.stdout.buffer.write(b'[$] '+line)
            if self.log_on == 'y':
                line = '%s-%s-[$] %s' % (tstamp, username, \
                    str(line.decode('utf-8')))
                with open(self.log_file, 'a') as log:
                    log.write(line)
                log.close
            else:
                pass