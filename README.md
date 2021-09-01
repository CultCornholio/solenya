# Solyena - Microsoft365 Device Code Phishing Framework



![implication](/images/implication-dennis.gif)



Solyena is a cli tool which provides a framework to perform M365 device code phishing. As defined in RFC8628, an attacker can perform a social engineering attack by instructing a target to register a malicious application using a device code. By default, Microsoft allows any user to add new applications to their M365 profile. Below, is a screenshot of a fresh deployment of an Azure subscription.


![default_permissions](/images/default_permissions.png)



## Creating a Workspace
```
$ solyena 
[INFO] Usage: solyena wsp <client_ID> -t <target_name>
```

## Gathering OAuth Access Tokens 
```
$ solyena auth 
```

## Acknowledgements



