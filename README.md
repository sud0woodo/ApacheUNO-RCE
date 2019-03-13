# ApacheUNO-RCE
Apache UNO API Remote Code Execution

PoC script to show the ability to execute code remotely using the Apache UNO API. 

The RCE is present in Windows and Linux distributions that are running the StarOffice manager.

[HackDefense Advisory](https://hackdefense.com/blog/security-advisory-rce-in-apache-uno-api/)

[Finding the RCE](https://hackdefense.com/blog/finding-RCE-capabilities-in-the-apache-uno-api/)

## Prerequisites
You will need to install the PyNO library on the machine that you want to execute the script on, this can be done by issueing the following command:
```sh
sudo apt-get install python3-uno
```

The target machine needs to run the StarOffice manager for the RCE to be present. The presence of the StarOffice manager that is externally reachable can be tested by looking at the banner:
```sh
e'com.sun.star.bridge.XProtocolPropertiesUrpProtocolProperties.UrpProtocolPropertiesTid'
```

## Usage
The script accepts the following parameters:
* --host the host to connect to
* --port the port that the StarOffice manager instance is running on

### Example
```sh
uno-rce.py --host 10.10.10.101 --port 2083
```
