mdadm-notify
============

A simple notification script for `mdadm` that allows notifications to outside email addresses


Configuration
-------------

Edit the mdadm-notify script to set the following variables

* `SERVER`: The SMTP server being used to send email
* `PORT`: Open port for login on SMTP server, usually 587
* `USE_TLS`: Put the SMTP connection in encrypted TLS mode (required for gmail)
* `USERNAME`: The username used to log into `SERVER`
* `PASSWORD`: The password for `USERNAME`
* `SENDER`: The email sender. Usually along the lines of `USERNAME`@`SERVER`
* `RECIPIENTS`: Those who will receive notifications

Optional:
* `MDSTAT`: The location of `mdadm`'s status file. Should usually be `/proc/mdstat`

Installation
------------

To install, run

    python setup.py install

as root to install mdadm-notify to /usr/bin (or /usr/local/bin, depending on your system).

As this file contains plain-text passwords, it's recommended that you run

    chmod 700 /usr/bin/mdadm-notify

and verify that the permissions look like the following

    -rwx------ 1 root root 1063 Sep 13 07:44 mdadm-notify
 
Edit your `mdadm` configuration file (e.g. `/etc/mdadm.conf`) and change the `PROGRAM` variable to match the install location, usually at the very end of the file

    PROGRAM /usr/bin/mdadm-notify

Older versions of `mdadm` (pre 3.0, I believe) don't seem to have the program option. On Ubuntu/Debian systems, the variable `DAEMON_OPTIONS` is set in `/etc/default/mdadm`. To use `mdadm-notify`, modify that variable to add the `--program` option

    DAEMON_OPTIONS="--syslog --program /usr/local/bin/mdadm-notify"

Test
----

Verify that installation and configuration have worked by running the following

    mdadm --monitor --test --oneshot /dev/mdX --program /usr/local/bin/mdadm-notify

where X is replaced by an `mdadm` device

License
-------
Copyright (c) 2012, dtreichler
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
