DDNS Updater
============

DDNS Updater is a Python program to update a dynamic IP address on a DNS server using the NIC V2.0 protocol. An optional e-mail notification can be enabled.

Installation
------------

Add PM Codeworks repository

    ~# wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.d/

Add PM Codeworks key

    ~# wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg.key | apt-key add -
    ~# apt-get update

Install the packages

    ~# apt-get install ddns-updater

Setup
-----

Edit the file /etc/ddns-updater/ddns.conf

Questions and suggestions
-------------------------

If you have any questions to this project just ask me via email:

<team@pm-codeworks.de>