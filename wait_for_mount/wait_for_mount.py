#!/usr/bin/env python

"""
    wait_for_mount.py
    ~~~~~~~~~~~~~~~~~

    Waits for one or more mountpoints or directories to exist
    and contain at least one file, then it's exevc()
    to a specified executable.
    Created for supervisor together with slow NFS mounts.

    Example:
    $ ./wait_for_mount.py /daten /mnt/music - /usr/bin/mpd --no-daemon /daten/HomeRadio/mpd/mpd.conf
    # Executes mpd if /daten and /mnt/music is ready

    :author: Michael Mayr <michael@michfrm.net>
    :licence: Public Domain
"""

from __future__ import print_function

import os
import sys
import time

paths = []
command = []

if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
    print("usage: {} [path1] [path2] ... - [command]".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

for i, part in enumerate(sys.argv[1:]):
    if part == "-":
        command = sys.argv[i + 2:]
        break
    else:
        paths.append(part)

#print("Paths: {!r}".format(paths))
#print("Command: {!r}".format(command))
print('Waiting for {0!r} before running "{1}"'.format(paths, " ".join(command)))

while True:
    if not paths:
        break

    # Wait for all paths
    for path in paths:
        if os.path.isdir(path):
            if len(os.listdir(path)) > 0:
                print("Ready: {}".format(path))
                paths.remove(path)
    time.sleep(1)

# Run command
os.execv(command[0], command)