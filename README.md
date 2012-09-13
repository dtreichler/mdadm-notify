mdadm-notify
============

A simple notification script for `mdadm` that allows notifications to outside email addresses


Configuration
-------------

Edit the mdadm-notify script to set the following variables

* `SERVER`: The SMTP server being used to send email
* `USERNAME`: The username used to log into `SERVER`
* `PASSWORD`: The password for `USERNAME`
* `SENDER`: The email sender. Usually along the lines of `USERNAME`@`SERVER`
* `RECIPIENTS`: Those who will receive notifications

Optional:
* `MDSTAT`: The location of `mdadm`'s status file. Should usually be `/proc/mdstat`

As this file contains plain-text passwords, it's recommended that you run

    chmod 700 mdadm-notify

and verify that the permissions look like the following

    -rwx------ 1 dtreichler users 1063 Sep 13 07:44 mdadm-notify
 
Installation
------------

To install, run

    python setup.py install

as root to install mdadm-notify to /usr/bin.

Edit your `mdadm` configuration file (e.g. `/etc/mdadm.conf`) and change the `PROGRAM` variable, usually at the very end of the file

    PROGRAM /usr/bin/mdadm-notify

Test
----

Verify that installation and configuration have worked by running the following

    mdadm --monitor --test --oneshot /dev/mdX

where X is replaced by an `mdadm` device
