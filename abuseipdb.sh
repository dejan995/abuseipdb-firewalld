#!/bin/bash
while IFS= read -r line; do
    sudo firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='$line' reject"
done < abuseipdb.txt
sudo firewall-cmd --reload
