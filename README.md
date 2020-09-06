<p align="center">
  <h3 align="center">Fail2ban Attack monitor</h3>
  <p align="center">Fail2ban Attack Monitor allows you to see the source of the attacks that fail2ban blocks.</p>

  <p align="center">
    <a href="https://twitter.com/bsd0x1">
      <img src="https://img.shields.io/badge/twitter-@bsd0x1-blue.svg">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
  </p>
</p>

<hr>

## Abstract

> This is a personal project that I am developing to improve the blocking capacity that the firewalls that I manage have. It has no intention of becoming a popular tool and I also cannot guarantee that it will work for your scenario.

## Preview

![preview](https://i.imgur.com/He5F0iR.png)

## Tools used

| Tool      | Version |
|-----------|---------|
| Python    | 3.8     |
| InfluxDB  | 0.10.0  |
| Grafana   | 7.1.5   |
| IPinfo API| -       |

<hr>

## How to configure (Ubuntu)

### Install influxDB

```
apt install influxdb influxdb-client
```

### Create database

```
curl -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE fail2ban"
```

<hr>

## Install script

### Clone project

```
git clone github.com/bsd0x/fail2ban-attack-monitoring
```

### Install requirements

```
pip install -r requirements.txt
```

### Add your jails name in config.ini

```
[FAIL2BAN_JAILS]
jails = sshd, ftpd
```

### Execute script

```
python main.py
```

### Crontab example

```
0 */1 * * * root cd /root/fail2ban-attack-monitor/ && python3 main.py && echo $(date) >> /var/log/fail2ban-monitor-log.log
```

<hr>

## Grafana with wordmap panel

### Query example

![Imgur](https://imgur.com/HC2uS0W.png)

### Wordmap example

![Imgur](https://imgur.com/HDAhOyM.png)

### Geohash field example

![Imgur](https://imgur.com/eao33nF.png)

