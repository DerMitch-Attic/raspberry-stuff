wait_for_mount.py
=================

Waits for one or more mountpoints or directories to exist and contain at least one file, then it's exevc() to a specified executable.

Created for supervisor in combination with slow NFS mounts.

Usage
------

    $ ./wait_for_mount.py [mount point 1] [mount point X] - [executable] [arguments]

Example
-------

    # Executes mpd with a custom config file as soon as /daten and /mnt/music
    # are ready and contain at least one file
    $ ./wait_for_mount.py /daten /mnt/music - /usr/bin/mpd --no-daemon /daten/HomeRadio/mpd/mpd.conf

Example: MPD
-------------

This script was primarily created to work around slow NFS mounts using wireless
connections. Configure it as supervisor program and let it wait for your
mount points to appear.

_We assume here that you're using the latest [Raspbian](http://www.raspbian.org/)._

1. **Disable system-wide MPD**

    Edit the file `/etc/default/mpd` and change:

        START_MPD=false

2. **Install supervisord if not needed**

        sudo apt-get install supervisor

3. **Create a supervisor configuration file**

    Create the file`/etc/supervisor/conf.d/mpd.conf` with the following content (adapt to your environment!):

        [program:mpd]
        command=/opt/HomeRadio/scripts/wait_for_mount.py /daten /mnt/music - /usr/bin/mpd --no-daemon /daten/HomeRadio /mpd/mpd.conf

4. **Load config and test**

        $ sudo supervisorctl
        supervisor> reread; update
        mpd: available
        (wait a few seconds...)

        supervisor> status
        (check if mpd is in RUNNING state)

5. **???**

6. **Music!**

