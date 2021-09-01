# Solyena - Microsoft365 Device Code Phishing Framework



![implication](https://i.imgur.com/Ukr2IcD.gif)



Solyena is a cli tool which provides a framework to perform M365 device code phishing. As defined in RFC8628, an attacker can perform a social engineering attack by instructing a target to register a malicious application using a device code. By default, Microsoft allows any user to add new applications to their M365 profile. Below, is a screenshot of a fresh deployment of an Azure subscription.


![default_permissions](/images/default_permissions.png)

An Organization is vulnerable to this attack if they have 

## Creating a Workspace
```
$ msph 
[INFO] Usage: solyena wsp <client_ID> -t <target_name>
[INFO] Example: solyena wsp fake-azure-app-registration-id -t beavis
```

## Gathering OAuth Access Tokens 
```
$ solyena auth 
[INFO] Example: solyena auth phish -ma
```

## Acknowledgements



