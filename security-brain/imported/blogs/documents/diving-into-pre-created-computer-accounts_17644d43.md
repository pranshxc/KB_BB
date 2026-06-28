---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-10_diving-into-pre-created-computer-accounts.md
original_filename: 2022-05-10_diving-into-pre-created-computer-accounts.md
title: Diving Into Pre-created Computer Accounts
category: documents
detected_topics:
- sso
- access-control
- command-injection
- password-reset
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- password-reset
- automation-abuse
- api-security
language: en
raw_sha256: 17644d431845ed32d5d5b527dcb3c24c59490f105ead3fce3f52ef03f4e48868
text_sha256: 92e63c04823e9946ddbd73fb766e3c6c310f581d23dcd7628ee5fd1fa75e0646
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Diving Into Pre-created Computer Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-10_diving-into-pre-created-computer-accounts.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, password-reset, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `17644d431845ed32d5d5b527dcb3c24c59490f105ead3fce3f52ef03f4e48868`
- Text SHA256: `92e63c04823e9946ddbd73fb766e3c6c310f581d23dcd7628ee5fd1fa75e0646`


## Content

---
title: "Diving Into Pre-created Computer Accounts"
page_title: "TrustedSec | Diving into Pre-Created Computer Accounts"
url: "https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts/"
final_url: "https://www.trustedsec.com/blog/diving-into-pre-created-computer-accounts"
authors: ["Oddvar Moe (@Oddvarmoe)"]
bugs: ["Active Directory", "Local Privilege Escalation", "Windows"]
publication_date: "2022-05-10"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 2647
---

* [Blog](https://trustedsec.com/blog)
  * [Diving into Pre-Created Computer Accounts](https://trustedsec.com/blog/diving-into-pre-created-computer-accounts)

May 10, 2022

# Diving into Pre-Created Computer Accounts

Written by Oddvar Moe 

Penetration Testing Red Team Adversarial Attack Simulation Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PreCreatedCompAccounts_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767065537&s=449a93527c299fa01cdeaf75914f0053)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#77480402151d1214034a341f12141c524547180203524547031f1e045245471605031e141b125245471105181a5245472305020403121324121452454651161a074c1518130e4a331e011e19105245471e1903185245472705125a3405121603121352454734181a070203120552454736141418021903045244365245471f03030704524436524531524531030502040312130412145914181a524531151b1810524531131e011e19105a1e1903185a0705125a140512160312135a14181a07020312055a1614141802190304 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Diving%20into%20Pre-Created%20Computer%20Accounts%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts&mini=true "Share on LinkedIn")

I was on an engagement where I simply could not elevate privileges, so I had to become creative and look deep into my old bucket (bucket being my head) of knowledge, and this resulted in some fun stuff. I had found that the client had a vulnerable certificate template also known as [ESC1](https://posts.specterops.io/certified-pre-owned-d95910965cd2) that allowed domain computers to request certificates based on it. I then tried all the normal things such as creating a computer account as a normal user. The **SeMachineAccountPrivilege** was, however, adjusted in the Domain Controller Policy and only allowed a few specific groups to Add Computers to the Domain. This led me down the road of trying to escalate on the host itself. However, proper hardening was in place, so no apparent escalation path was clear. Looking through the data I had collected already from Active Directory, I started to form a new theory based on some old legacy knowledge.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004206.png)

My theory was that since this domain had a lot of history and I could tell that the domain was created back in 2004, there would probably be some pre-created computer accounts. And if I got lucky, maybe one of them even had the **Assign this computer account as a pre-Windows 2000 computer** checkmark enabled upon creation. I will come back to why this is important a little later in the post. Below is a screenshot highlighting the setting I am talking about.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004231.png)

## Background About Computer Accounts

Back when I was younger, I worked a lot with OS deployment and automation. One thing you start to learn when you do a lot of setups with Remote Installation Services or Windows Deployment Services is that when you pre-create computer accounts with the **Assign this computer account as a pre-Windows 2000 computer** checkmark, the password for the computer account becomes the same as the computer account in lowercase. For instance, the computer account _DavesLaptop$_ would have the password **daveslaptop**. This useful piece of information can also be found in an old KB article through the Wayback Machine: <https://web.archive.org/web/20080205233505/http://support.microsoft.com/kb/320187>.

The interesting piece of information is:
  
  
  The **Assign this computer account as a pre-Windows 2000 computer** check box assigns a password that is based on the new computer name. If you do not select this check box, you are assigned a random password.

This means that if someone at one point in time created a computer account with this option set, and then never onboarded it (by joining it to the domain), you know the password for this account. Okay, so how do we get a list of pre-created computer accounts that has never been used? Turns out that this is pretty simple. In this blog post, I am going to show the searches using ADExplorer, but you can basically use any other LDAP tool you want that allows you to search the UserAccountControl Attribute.

## Finding Pre-created computer accounts

Whenever a computer account is created, it has the following UserAccountControl flags set:

\- **32 - PASSWD_NOTREQD**  
\- **4096 - WORKSTATION_TRUST_ACCOUNT**

That means that accounts with the value of 4128 (4096 | 32) are pre-created computer accounts. After a computer account has joined the domain, it will just have the **WORKSTATION_TRUST_ACCOUNT** flag set (4096). All the different UserAccountControl flags can be found [here](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties).

To search specifically for pre-created computer accounts, we also want to find only the accounts that have been authenticated against. If a successful authentication has been made for a computer account, it means that account has probably been used already and the password has changed. So, to reduce the list of possible targets, we can search like this in ADExplorer:

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004246.png)

This search should then provide a list of computer accounts that have been pre-created but have never been used. One thing I am still researching is a way to find the computer accounts that have been created with the **_Assign this computer account as a pre-Windows 2000 computer_** checkmark. Based on what I see, I cannot identify an LDAP attribute that is used to separate the computer accounts with and without that option set. However, Active Directory knows what machines have this checkmark on creation and not, so I am assuming it is some kind of hidden attribute that is not exposed without doing some reversing. I know this because I tested creating a few accounts with and without the checkmark set. If I then set a different password on all accounts and reset them, the ones that had the flag initially set will have the password set back to the same as the computer name in lowercase, which proves that it knows how to differentiate the two types of accounts (checkmark or not) somehow. I compared attribute by attribute and never found any difference, so I assume it is hidden somewhere inside the Active Directory Database. If anyone knows how to figure this out, I am very interested in learning about it, so reach out.

Alright, we now have a list of possible computer accounts—how do we test to find a valid password? When I did this on the engagement, I simply used Impacket’s smbclient.py script to authenticate to a target computer account. You will see the error message **STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT** when you have guessed the correct password for a computer account that has not been used yet. The same error can also be seen with other tools such as CrackMapExec.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004257.png)

## Changing the Password

Great, we now know the password for an account that we can use to exploit the certificate template flaw identified earlier, but you cannot use this computer account before the password has been changed. And get this: you cannot change the password over SMB (based on my research). This is due to the fact that you need to authenticate to the IPC$ share, and our identified computer account cannot be a pre-created computer account that has not had its password changed.

The good news for us is that there are many different ways to change the password for an account in Windows. According to the [official documentation](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/password-change-mechanisms), there are six (6) different password change protocols:

  1. The NetUserChangePassword protocol
  2. The NetUserSetInfo protocol
  3. The Kerberos change-password protocol (IETF Internet Draft Draft-ietf-cat-kerb-chg-password-02.txt) - port 464
  4. Kerberos set-password protocol (IETF Internet Draft Draft-ietf-cat-kerberos-set-passwd-00.txt) - port 464
  5. Lightweight Directory Access Protocol (LDAP) write-password attribute (if 128-bit Secure Sockets Layer (SSL) is used)
  6. XACT-SMB for pre-Microsoft Windows NT (LAN Manager) compatibility

Note that important terms we need to be aware of when dealing with password resets are "change" and "set". With a "change", you need to know the previous password, but with the "set," you will need to be granted with the appropriate permission to do so (reset password permission). The LDAP protocol requires the reset password (set password) permission, and this is something a default computer account does not have on its own object. The XACT-SMB is a method used by Windows 95/98 and I have not found any useful information on how to leverage it. So effectively, we can only use either NetUserChangePassword or the Kerberos change-password protocol in our scenario.

Just to give you a little understanding of some of the currently available tools and how they fit into the Microsoft password change protocol documentation, I have summarized a list below:

  * Smbpasswd / rpcclient (chgpasswd, chgpasswd2, chgpasswd3) uses the NetUserChangePassword protocol using the SAMR ChangePasswordUser2.
  * Kpasswd uses the Keberos change-password protocol on port 464.
  * Ldappasswd and Windows LDP use the LDAP method, but as stated before, in order to set the password through LDAP, you will need the reset password permission (set password), and by default a computer account does not have that on its own object.

When I was looking in to this on my engagement, I was not aware of the Kpasswd method, so I instead ended up writing a custom Impacket script (rpcchangepwd.py) that leverages MS-RPC (port 135+high dynamic port) to change the password. This bypasses the error you get when doing it over SMB. The code is based on the smbpasswd and other Impacket scripts. I have created a pull request that can be found [here](https://github.com/SecureAuthCorp/impacket/pull/1304) for now. Hopefully it will be included in the main repo at some point.

In the screenshot below, you can see how I used this script in a lab. First I tried to connect to the domain controller using the smbclient.py script without success, then ran my script rpcchangepwd.py to change the password, and then re-ran smbclient.py to connect and list out the shares successfully. Note that when dealing with computer accounts, it is smart to escape the $ with a \\.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004449.png)

As mentioned before when I started to write this blog post, I also discovered that kpasswd (binary inside krb5-user or heimdal) can be used to change the computer password, but it requires you to do some configuration and possibly edit your host file. In my lab, I installed the krb5-user using apt install and configured it by editing the `/etc/krb5.conf` file. The file for my lab looks like this:
  
  
  [libdefaults]
  default_realm = VALHALL.INT
  dns_lookup_realm = false
  ticket_lifetime = 24h
  renew_lifetime = 7d
  rdns = false
  kdc_timesync = 1
  ccache_type = 4
  forwardable = true
  proxiable = true
  
  
  [realms]  
  VALHALL.INT = {
  kdc = DC01.VALHALL.INT 
  admin_server = DC01.VALHALL.INT  }

Note that it is important to write any realm in **uppercase** or else you will experience errors. I also needed to add the IP address for the DC01.VALHALL.INT in my host file so it could be resolved.

Then it was just a matter of running the command and providing input:  
`kpasswd pre2000comp$`

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004612.png)

As a bonus, I also found that someone created an Impacket version and did a [pull request](https://github.com/SecureAuthCorp/impacket/pull/1189), but it has not been added to the main repo yet. I have not had the chance to try this out yet, but it seems very promising.

Sweet, we have now changed the password and I showed you two different approaches. Now I have all the bits that I need to exploit the certificate template issues that originally led me down this path 😊.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004109.png)

## Other Interesting Discoveries

Along the way to discovering this misconfiguration, I found other interesting things that I wanted to share. Many organizations use various scripts and tools to generate computer accounts, and one such legacy tool is dsadd. One way of using this is simply by running `dsadd computer <ComputerDN>` as shown in the screenshot below.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004751.png)

The interesting part here is that the password for the computer account is set to blank and, in the cases I have seen, does not require the password to change in order to use the account. However, if an admin resets the computer account, the password gets set to the same as the computer name in lowercase and does require a password change.

The last thing I discovered is related to BloodHound graphing. Remember when we created a computer account inside Active Directory? There was also this option to allow a group or user to join this computer to the domain, as seen on the following screenshot.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004827.png)

If a sysadmin at some point created a computer account and changed this to a specific group, additional permissions are set to the computer object. In my lab, I added the Domain Users group and the ALL EXTENDED RIGHTS permissions were added to the computer object, meaning reset password, change password, allowed to authenticate, and [many more](https://learn.microsoft.com/en-us/windows/win32/adschema/extended-rights). When I was exploring this, I assumed that this would show up in BloodHound, but to my big surprise, it had been missed.

Since BloodHound did not graph this correctly, I had to dig into the source code a bit. There seems to be a logic error after the LAPS functionality was added at some point.

The source code I am referencing can be found here: <https://github.com/BloodHoundAD/SharpHoundCommon/blob/3d2ccd14f36b7fe2be94bcf7f265582dcde49a16/src/CommonLib/Processors/ACLProcessor.cs#L273>  
You can also see an associated screenshot below.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220427004922.png)

From my understanding, this code seemed as if the AllExtendedRights attribute was only added if the environment had LAPS. In my case, I had not deployed LAPS, so it would not show up. I made a change to the source code and I made a [pull request](https://github.com/BloodHoundAD/SharpHoundCommon/pull/28) to get that added even if LAPS is not in the environment since this can be a very nice thing to find in some scenarios. Below are screenshots of running the original SharpHound with my edits below that. In my lab, I had two (2) computer accounts that were delegated to Domain Users.

![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220429111848.png)![](https://www.trustedsec.com/wp-content/uploads/2022/05/Pasted-image-20220429111904.png)

## Outro

This was an interesting adventure and I hope you found it interesting too. Since we are dealing with computer accounts, it is important for me to also tell you that randomly resetting computer account passwords is something you should only do if you fully understand what you are doing. Doing this on a system that is actively used could halt production in worst cases and we don't want that.  
That’s all I had for this post, hopefully this is useful for someone. Feedback is always appreciated!

## TLDR

If you need to find a valid computer account that has never been used, you could try the computer name in lowercase as the password or a blank password. If you are lucky, it might just work (and also you should never blindly trust tools that map things out for you). Always check things yourself. In this post, I showed you how I actually found an attack path that was missed by BloodHound/SharpHound that could be very useful in some scenarios.

## Update 

12 May, 2022 - After publishing [this post](https://twitter.com/filip_dragovic/status/1524730451826511872) on Twitter [@filip_dragovic](https://twitter.com/filip_dragovic?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) showed that you can basically just use getTGT.py to get a kerberos ticket and use that instead of the password. Doing it that way you do not have to change the actual password for the account in order to use it.

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#f4cb8781969e919780c9b79c91979fd1c6c49b8180d1c6c4809c9d87d1c6c49586809d979891d1c6c492869b99d1c6c4a0868187809190a79197d1c6c5d2959984cf969b908dc9b09d829d9a93d1c6c49d9a809bd1c6c4a48691d9b7869195809190d1c6c4b79b998481809186d1c6c4b597979b819a8087d1c7b5d1c6c49c80808487d1c7b5d1c6b2d1c6b280868187809190879197da979b99d1c6b296989b93d1c6b2909d829d9a93d99d9a809bd9848691d997869195809190d9979b998481809186d99597979b819a8087 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Diving%20into%20Pre-Created%20Computer%20Accounts%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiving-into-pre-created-computer-accounts&mini=true "Share on LinkedIn")
