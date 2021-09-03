<img src="https://img.shields.io/github/issues/CultCornholio/solenya">  <img src="https://img.shields.io/github/forks/CultCornholio/solenya">   <img src="https://img.shields.io/github/stars/CultCornholio/solenya">   <img src="https://img.shields.io/github/license/CultCornholio/solenya">

# Solenya - M365 Device Code Phishing Framework

Solenya is a CLI tool which provides a framework to perform M365 device code phishing. As defined in RFC8628, an attacker can perform a social engineering attack by instructing a target to register a malicious application using a device code. 

<p align="center">
    <img src="https://raw.githubusercontent.com/CultCornholio/solenya/dev/images/pickleRick.png" width="50%" height="100%">
</p>

**DISCLAIMER**: The contributors are not responsible for any malicious use of the tool. The tool is developed for educational purposes and should be used solely by defenders or authorized testers.

## Prerequisites
By default, Microsoft allows any user to add new applications to their M365 profile. Below, is a screenshot of a fresh deployment of an Azure subscription. As the setting implies, any user can both add and authorize a new application to their profile. This can be abused by an attacker by creating a "malicious" application and convincing an end user to authorize it by entering a device code. A good analogy to think about is Netflix granting Smart TV's access by generating a device code for the user to enter and sign into their account. A Microsoft endpoint which is used for legitmate purposes can be accessed by anyone to enter such a device code.  

![default_permissions](https://raw.githubusercontent.com/CultCornholio/solenya/dev/images/default_permissions.png)

To create a "malicious" application you need an Azure subscrition. For testing purposes, we recommend signing up for the [Microsoft 365 Developer](https://developer.microsoft.com/en-us/microsoft-365/dev-program) program to create a live environment. This program is free and allows you to populate the tenant with various services and fake users. 

Once created, head to the Azure Portal and search for "App Registrations". Here, you can create a "New Registration" with any arbitrary name. This name will be visible to any user that attempts to authorize the application. You also have the ability to add a logo to create a convincing pre-text. 

![app_registrations](https://raw.githubusercontent.com/CultCornholio/solenya/master/images/app-registrations.png)

1. Choose "Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)" under the account type section.

You now successfully registered an application that can be used to perform device code phishing. The last important change that needs to be made is in the "Authentication" settings of the application. 

![app_settings](https://raw.githubusercontent.com/CultCornholio/solenya/master/images/app-demo.png)

2. Enable public client flows so the application can be accessed remotely without any redirects.

![app_auth](https://raw.githubusercontent.com/CultCornholio/solenya/master/images/app-auth.png)


![app_clientflow](https://raw.githubusercontent.com/CultCornholio/solenya/master/images/public-client.png)

3. Use solenya with the "client_id" of the created application to generate a device code for a target.

![get_clientid](https://raw.githubusercontent.com/CultCornholio/solenya/master/images/getting-client-id.png)

4. Convince a target to enter the user code at the following endpoint using solenya (https://microsoft.com/devicelogin).

## Additional Considerations

You also have the ability to tweak the "API Permissions" of the application. This directly correlates to the device_code_scope within "solenya/msph/clients/constants.py". By default, solenya perfers permissions that do not require admin consent. This ensures an admin will not be notified if a user authorizes an application on their profile. However, this also limits the actions we can perform against the Microsoft Graph API. As each cloud environment is unique, be careful when enabling new permissions as it may lead to poor opsec. 



## Motivation

If you understand the basics of this attack, you may still be left wondering what situation would you perform device code phishing over traditional phishing. In this attack, you only have 15 minutes to convince a user to enter the code before it expires and you don't actually get any credentials that can be used to logon interactively. Instead, you recieve OAuth tokens in the form of an access_token, refresh_token, and id_token. 

The short answer is because we are leveraging pre-built infrastructure. Specifically, we are relying on Microsoft 365 entirely to serve our phishing infrastructure. This builds trust not only with a target but with a vareity of security controls. How many people are actively blocking Microsoft urls? How many people have a spam bypass rule allowing any links from Microsoft to be allowed in? A phishing or vishing pre-text can be made where a plaintext message arrives in a target inbox allowing an attacker can convince the user to authorize the application. There are also better writeups with more detail, see the Acknowledgements section for more resources and information. Without their knowledge this tool would not exist. 

If you are a defender or authorized security tester that only considers users that click a link as "failed" it is time to reconsider security testing and awareness. Too often is training built to showcase the skills of marketing over actually providing valuable and actionable information for end users. Instead of just focusing on clicks (already unrealistic), users need to be trained on valid authentication flows and feel comfortable reporting abnormal requests. More on this has been detailed by [TheParanoids in this article](https://www.yahooinc.com/paranoids/paranoids-phishing-metrics/).

As always with a storng enough pre-text, the majority of users will most likely authorize an application. Do you have confidence in your users and have you tested them?

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

## Defensive Mitigations

1. (Modify the permissions and consent settings to best suite your Organization (Optiv)) [https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent?tabs=azure-portal]
2. (Create an administrative workflow so appropriate individuals are notified when an application is applied to a profile (Optiv))[https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/manage-consent-requests]
3. Train users to better understand the authentication flow in use and implications of misuse 
4. You have the ability to in theory detect/prevent anyone from accessing the device logon endpoint. However, this may be used by legitamate services.

## Contact
- Contact us at cult.cornholio@gmail.com or open up a new Issue on GitHub.

## Acknowledgements
- [Optiv - Microsoft 365 OAuth Device Code Flow and Phishing](https://www.optiv.com/insights/source-zero/blog/microsoft-365-oauth-device-code-flow-and-phishing)
- [SecureWorks - OAuth’s Device Code Flow Abused in Phishing Attacks](https://www.secureworks.com/blog/oauths-device-code-flow-abused-in-phishing-attacks)
- [Jenko Hwong - New Phishing Attacks Exploiting OAuth Authorization Flows](https://www.netskope.com/blog/new-phishing-attacks-exploiting-oauth-authorization-flows-part-1)
- [Dirk-jan Mollema - ROADtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
- [Office 365 Blog](https://o365blog.com/post/phishing/)
- [rvrsh3ll - TokenTactics](https://github.com/rvrsh3ll/TokenTactics)



