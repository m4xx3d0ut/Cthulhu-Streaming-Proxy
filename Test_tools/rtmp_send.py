#!/usr/bin/env python3

"""
General test script for sending video file or SMPTE bars with tone to RTMP
server from Linux.  Requires Ffmpeg to be installed.  Tested on Debian x86_64.
Run without arguments for help.

The encoder settings are passable, but will probably need some work.
"""

from sys import argv
from subprocess import Popen, PIPE, DEVNULL, STDOUT

if len(argv) == 1 or len(argv) > 3:
    print("For sending test video to RTMP server...")
    print("%s%s" % ("Usage: python3 rtmp_send.py test_video.mp4 ",\
        "rtmp://test_server:test_port/test_app_test_key"))
    print("Or for SMPTE bars with tone...")
    print("%s%s" % ("Usage: python3 rtmp_send.py ",\
        "rtmp://test_server:test_port/test_app_test_key"))
    exit(0)

elif len(argv) == 3:
    print("[+] Sending test video: %s" % (argv[1]))

    rtmp = ['ffmpeg', '-re', '-i', argv[1], '-c:v', 'libx264', '-preset',\
    'ultrafast', '-b:v', '4500k', '-maxrate', '5000k', '-bufsize', '15000k',\
    '-pix_fmt', 'yuv420p', '-tune', 'zerolatency', '-crf', '28', '-g', '60',\
    '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '44100', '-f', 'flv',\
    argv[2]]

    try:
        # Popen(rtmp, stdout=DEVNULL, stderr=STDOUT).wait()
        Popen(rtmp).wait()


    except KeyboardInterrupt:
        exit(0)

else:
    print("[+] Sending SMPTE bars...")

    rtmp = ['ffmpeg', '-re','-f', 'lavfi', '-i',\
    'smptehdbars=rate=30:size=1920x1080', '-f', 'lavfi', '-i',\
    'sine=frequency=1000:sample_rate=44100', '-f', 'flv', '-c:v', 'libx264',\
    '-preset','ultrafast', '-b:v', '4500k', '-maxrate', '5000k', '-bufsize',\
    '15000k', '-pix_fmt', 'yuv420p', '-tune', 'zerolatency', '-crf', '28',\
    '-g', '60', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '44100',\
    '-f', 'flv', argv[1]]

    try:
        # Popen(rtmp, stdout=DEVNULL, stderr=STDOUT).wait()
        Popen(rtmp).wait()


    except KeyboardInterrupt:
        exit(0)