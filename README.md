DDNS Updater
============

DDNS Updater is a Python program to update a dynamic IP address on a DNS server using the NIC V2.0 protocol. An optional e-mail notification can be enabled.

Installation
------------

There are two ways of installing DDNS Updater: Installation of the stable or latest version. The stable version is distributed through the PM Code Works APT repository and is fully tested but does not contain the latest changes.

### Installation of the stable version

Add PM Codeworks repository

    ~# wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.d/

Add PM Codeworks key

    ~# wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -
    ~# apt-get update

Install the packages

    ~# apt-get install ddns-updater

### Installation of the latest version

The latest version contains the latest changes that may not have been fully tested and should therefore not be used productively. It is recommended to install the stable version.

Install required packages for building

    ~# apt-get install git devscripts

Clone this repository

    ~$ git clone https://github.com/philippmeisberger/ddns-updater.git

Build the package

    ~$ cd ./ddns-updater/
    ~$ dpkg-buildpackage -uc -us

Install the package

    ~# dpkg -i ../ddns-updater*.deb

Setup
-----

Edit the file */etc/ddns-updater/ddns.conf*.

### Section [DDNS]
* `server`: The domain name of DNS server providers (without "http://") e.g. *dyndns.strato.com*.
* `server_path`: The URL path to the DNS server directory e.g. */nic/update*.
* `username`: Account name at DNS server provider.
* `password`: Password for account at DNS server provider.
* `hostname`: The domain that should be provided.
* `ip`: **DO NOT EDIT THIS**: It is maintained by DDNS Updater and contains the current IP address.
* `external_ip_server`: An public available webserver that sends the current IP, e.g. *checkip.dyndns.com*. Self-hosted servers are also possible by using the simple PHP script *checkip.php* provided by DDNS Updater.
* `external_ip_server_path`: URL path to the directory where the PHP script is located e.g. */*
* `use_regex`: (Optional) Set to `True` to extract the IP address out of HTML formatted HTTP response e.g. when using *checkip.dyndns.com* in `external_ip_server`. When using self-hosted server with *checkip.php* script set to `False`.

### Section [Mail]
* `notify`: (Optional) Set to `True` to enable e-mail notifications like successful IP address updates or errors. Please configure following value or set to `False` to disable notifications. Then the following configuration is not necessary.
* `smtp_server`: SMTP Server to send the e-mails from.
* `port`: Port of the SMTP server e.g. 587 or 465.
* `username`: E-mail account name.
* `password`: E-mail account password. Don't worry: TLS is used during exchange!
* `recipient`: E-mail account that should receive the notifications.

DDNS Updater verifies every 10 minutes if the IP address has changed and performs an update if necessary. The interval can be changed by editing file */etc/cron.d/ddns-updater*.

Questions and suggestions
-------------------------

If you have any questions to this project just ask me via email:

<team@pm-codeworks.de>
