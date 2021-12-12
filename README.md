# Shelm

Shelm is a command line utility written in python 3 which lets users download secure by design helm charts. All our helm charts are tested strictly, using Datree.
When using helm charts developers and administrators often neglect the security best practices that are essential, negligence of security best practices can result in severe vulnerabilities which can be exploited by an attacker to either take control of your Kubernetes cluster or to destroy/damage your application data.

---

### Installation
    curl https://raw.githubusercontent.com/viploveb/shelm/master/install.sh | /bin/bash

 ### Usage 
 
 👉  `shelm list`
 
 This will list all the available shelm charts.
 
 👉 `shelm search <chart_name>`
 
Example - "shelm search haproxy" This will tell the user if the specified chart is available or not.
 
 👉 `shelm install <chart_name>`

This will download the specified chart.

### Author 👨‍💻
Viplove Bansal \\ [viploveb](https://github.com/viploveb)

---
Don't forget to ⭐the repo. 😃
