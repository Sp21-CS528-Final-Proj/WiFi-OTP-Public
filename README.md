# Setup
 - Tested on Raspberry Pi 3 B+ Linux raspberrypi 5.10.17-v7+ #1403 SMP Mon Feb 22 11:29:51 GMT 2021 armv7l

## Enable SSH
 - put a empty file `ssh` to boot folder

## Enable WLAN
 - raspi-config 

## Dependencies
 - sudo apt install libnl-3-dev libssl-dev libnl-genl-3-dev

## DHCP
 - https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md

# Code

## Config File Parsing
 - hostap/hostapd/config_file.c
## Auth
 - hostap/src/ap/wpa_auth.c
