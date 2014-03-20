# Overview

[Nagios](http://nagios.org) offers complete monitoring and alerting for servers, switches, applications, and services.

This charm is designed to do basic monitoring of any service in the Charm Store that relates to it. There is an [NRPE subordinate charm](https://jujucharms.com/precise/nrpe/) that you can use if you want to use local monitors.

# Usage

This charm is designed to be used with other charms. In order to monitor anything in your juju environment for working PING and SSH, just relate the services to this service. In this example we deploy a central monitoring instance, mediawiki, a database, and then monitor them with Nagios:

    juju deploy nagios central-monitor
    juju deploy mysql big-db
    juju deploy mediawiki big-wiki
    juju add-reation big-db big-wiki
    juju add-relation big-db central-monitor
    juju add-relation big-wiki central-monitor

This should result in your Nagios monitoring all of the service units.

There is an [NRPE subordinate charm](https://jujucharms.com/precise/nrpe/) which must be used for any local monitors.  See the `nrpe` charm's README for information on how to make use of it.

You can expose the service and browse to `http://x.x.x.x/nagios3` to get to the web UI, following the example:

    juju expose central-monitor
    juju status central-monitor

Will get you the public IP of the web interface.

# Configuration

### SSL Configuration

- `ssl` - Determinant configuration for enabling SSL. Valid options are "On", "Off", "Forced". The "Forced" option disables HTTP traffic on Apache in favor of HTTPS. This setting may cause unexpected behavior with existing nagios charm deployments.

- `ssl_cert` - Base64 encoded SSL certificate. Deploys to configured ssl_domain certificate name as `/etc/ssl/certs/{ssl_domain}.pem`

- `ssl_key` - Base64 encoded SSL key. Deploys to configured ssl_domain key as `/etc/ssl/private/{ssl_domain}.key`

- `ssl_chain` - Base64 encoded SSL Chain. Deploys to configured ssl_domain chain authority as `/etc/ssl/certs/{ssl_domain}.csr`


#### Typical SSL Workflow for Self Signed Keys:

    juju deply nagios central-monitor
    juju set ssl=on


If you purchased keys from a certificate authority:

    juju deply nagios central-monitor
    juju set central-monitor ssl_cert=`base64 mykey.pem`
    juju set central-monitor ssl_key=`base64 mykey.key`
    juju set central-monitor ssl_chain=`base64 mykey.csr`
    juju set central-monitor ssl=on


### Known Issues / Caveates


#### Web Interface username/password

Login: nagiosadmin
Password: see below

To fetch the Nagios Administrative password you have to retrieve them from
the nagios host, as it is generated during installation.

```
juju ssh nagios/0
sudo cat /var/lib/juju/nagios.passwd
```


#### Monitors Interface
The monitors interface expects three fields:

- `monitors` - YAML matching the monitors yaml spec. See example.monitors.yaml for more information.
- `target-id` - Assign any monitors to this target host definition.
- `target-address` - Optional, specifies the host of the target to monitor. This must be specified by at least one unit so that the intended target-id will be monitorable.


# Contact Information

## Nagios

- [Nagios homepage](http://nagios.org)
- [Nagios documentation](http://www.nagios.org/documentation)
- [Nagios support](http://www.nagios.org/support)
