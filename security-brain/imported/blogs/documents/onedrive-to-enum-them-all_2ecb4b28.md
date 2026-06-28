---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-06_onedrive-to-enum-them-all.md
original_filename: 2023-06-06_onedrive-to-enum-them-all.md
title: OneDrive To Enum Them All
category: documents
detected_topics:
- sso
- idor
- sqli
- command-injection
- rate-limit
- cloud-security
tags:
- imported
- documents
- sso
- idor
- sqli
- command-injection
- rate-limit
- cloud-security
language: en
raw_sha256: 2ecb4b28d820fa503f3e7b0999e9d57cc3dfa2486ea245c7fdf3faf2bd66cf84
text_sha256: 894fc8f1e10f63a0de5f99097d5c76b9975b2b873820ccc7d34349e976c69d97
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# OneDrive To Enum Them All

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-06_onedrive-to-enum-them-all.md
- Source Type: markdown
- Detected Topics: sso, idor, sqli, command-injection, rate-limit, cloud-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `2ecb4b28d820fa503f3e7b0999e9d57cc3dfa2486ea245c7fdf3faf2bd66cf84`
- Text SHA256: `894fc8f1e10f63a0de5f99097d5c76b9975b2b873820ccc7d34349e976c69d97`


## Content

---
title: "OneDrive To Enum Them All"
page_title: "TrustedSec | OneDrive to Enum Them All"
url: "https://www.trustedsec.com/blog/onedrive-to-enum-them-all/"
final_url: "https://www.trustedsec.com/blog/onedrive-to-enum-them-all"
authors: ["nyxgeek (@nyxgeek)"]
programs: ["Microsoft (OneDrive)"]
bugs: ["Username enumeration"]
publication_date: "2023-06-06"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1074
---

* [Blog](https://trustedsec.com/blog)
  * [OneDrive to Enum Them All](https://trustedsec.com/blog/onedrive-to-enum-them-all)

June 06, 2023

# OneDrive to Enum Them All

Written by @ nyxgeek 

Cloud Penetration Testing Office 365 Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OneDriveToEnumThemAll_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767068906&s=daedd810d43a95dc0d12dbe0db41c4a8)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#132c606671797670672e507b7670783621237c6667362123677b7a603621237261677a707f7636212375617c7e3621234761666067767740767036212235727e6328717c776a2e5c7d7657617a6576362123677c362123567d667e362123477b767e362123527f7f3620523621237b67676360362052362155362155676166606776776076703d707c7e362155717f7c743621557c7d7677617a65763e677c3e767d667e3e677b767e3e727f7f "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=OneDrive%20to%20Enum%20Them%20All%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all&mini=true "Share on LinkedIn")

THIS POST WAS WRITTEN BY [@NYXGEEK](https://twitter.com/nyxgeek?lang=en)

Greetings fellow hackers,

Today we'll be diving into the topic of user enumeration via OneDrive. I wrote a blog post on this topic a few years back when I first identified the technique. Since then, I've learned more about it, and the onedrive_enum.py tool has been updated and is more powerful than ever!

In short, OneDrive can be the best way to do user enumeration because:

  * It doesn't require a login attempt
  * It's completely silent (companies cannot see the requests)
  * There's no rate-limiting

It's a perfect enumeration method, **IF** they use OneDrive.

## Overview of OneDrive Enumeration

OneDrive is a part of SharePoint. It is designed for personal file storage and linked directly to an Azure/M365 account. Whenever a user logs in to various Microsoft services such as Excel or Word, OneDrive is activated, and a personal URL containing the user's email address is created. To be more precise, this personal URL is actually the account's UPN, or User Principal Name.

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig1.png)Figure 1 - Example of OneDrive URL Containing Account

Since this personal URL is directly tied to the user's account, it is then possible to enumerate users simply by looking for web directories in a specific format, similar to using DirBuster/dirb.

Below is a chart showing various services and whether each activates OneDrive.

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig2.png)Figure 2 - M365 Services and OneDrive Activation

In reality, due to the large number of triggers for OneDrive URL creation, almost anybody who has actually used an Azure/M365 account will have a OneDrive URL.

Once OneDrive is activated, a unique URL is created that is associated with that user. The URL is in the following format:
  
  
  https:<strong>//<tenant></strong>-my.sharepoint.com/personal/<strong><UserPrincipalName></strong>/_layouts/15/onedrive.aspx

This is illustrated in the screenshot below, where you can see the tenant name is 'acmecomputercompany' and the User Principal Name is a translation of '[[email protected]](/cdn-cgi/l/email-protection)'. When a UPN is translated to a OneDrive URL, periods and symbols are stripped and replaced with underscore ("_") characters.

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig3.png)Figure 3 - Example of OneDrive URL with Tenant and Account

So, in this way, it is trivial to make a web request and identify whether a username is valid (or rather, whether a user exists who has logged in to their account at least once).

This enumeration is undetectable, as it is a simple HTTP HEAD request to a Microsoft server. No authentication is ever attempted.

Note: Since OneDrive enumeration can only enumerate accounts with licenses, results may be subpar at certain organizations. If they limit Microsoft 365 licenses to specific departments or do not provision them, enumeration coverage will be affected. Examples might be department store sales floor employees and cashiers or non-technical jobs where employees do not use a computer. However, this also means you're identifying live, actual users with OneDrive Enum—users who might have access to Azure resources.

## Identifying Azure Tenant Names

For OneDrive enumeration to be successful, you need to know the Azure tenant name. An Azure tenant name is a short name associated with an Azure tenant.

Many times, the tenant name for an organization would match the domain name. For example, 'microsoft.com' has an associated tenant of 'microsoft'. But this is often not the case. Sometimes it will be an alternate name, or an abbreviation of an organization's full legal name.

For a long time, I had searched for a method of identifying the Azure tenant names directly. Without knowing the tenant name or having a means of looking it up, you could easily hit a dead-end with OneDrive enumeration.

Little did I know, Dr. Nestori Syynimaa (@DrAzureAD) had identified just such a method, shared via AADInternals tools ([https://github.com/Gerenios/AA...](https://github.com/Gerenios/AADInternals)). This was brought to my attention by @thetechr0mancer, with the release of TREVORspray ([https://github.com/blacklanter...](https://github.com/blacklanternsecurity/TREVORspray)).

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig4_update2.png)Figure 4 - Lookup via TREVORspray

This was it! The missing piece of the puzzle! With this new technique, we can reliably use the OneDrive enumeration technique!

## Updated OneDrive_Enum Tool v2.0

I have released an updated version of the ondrive_enum.py script which can be found here:

<https://github.com/nyxgeek/onedrive_user_enum>

A number of improvements have been made. More are in the pipeline.

New features:

  * Local DB - Logging of valid accounts, previous enumeration runs
  * Auto-lookup - Automatic Tenant lookup, thanks to Dr. Nestori (@DrAzureAD) and TREVORspray (@thetechr0mancer)
  * Read directory - Read in all files in a directory; useful for multiple similar files (e.g., 'john.smith' or 'jsmith' formatted user lists)
  * Append - Easily append digits or words to usernames ('jsmith1', 'jsmith2', etc.)
  * Skip-Tried - Dedupe: checks the run log and ensures that you only run NEW usernames against a particular domain/tenant combination
  * Kill-After - Cancels a userlist if no usernames identified with 'x' number of tries

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig5_update3.png)Figure 5 - OneDrive_Enum_v2.py

## Enumerating Users with OneDrive

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig6_update2.png)Figure 6 - OneDrive User Enumeration

Remember, to create the OneDrive URL, we need to know the tenant name AND the domain name. If only a domain is supplied to the tool, then it will attempt to look up the associated tenant automatically, using the lookup method from AADInternals/TREVORspray.

Here is an example of a lookup against Microsoft.com:

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig7_update.png)Figure 7 - Example

The tool looks for any mail sync records, which could indicate a primary tenant. Note that this is not a foolproof method. If it cannot determine the correct tenant, it will show you a list and you will have to pick one.

Below is an example output of the onedrive_enum.py tool:

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Fig7.png)Figure 8 - OneDrive Enumeration

Here we can see that an HTTP status code of '403' (or '401') is what differentiates the VALID account from the invalid accounts.

In the updated OneDrive_Enum script, all enumeration sessions are logged in a onedrive_log table in a local SQLite database. This enables OneDrive_Enum to identify which userlists (and usernames) have been tried. It is also useful for statistics, as it will log the number of 'found' usernames per wordlist. This lets you identify top-performing wordlists over time.

In addition to using an SQLite database for logging sessions, all valid usernames are also stored, along with the tenant and domain with which they are associated.

Valid usernames are also written out to a local file at the end of each session for easy grepping.

## Tips and Tricks

Most organizations will only have one (1) tenant defined, and the tool will not have any problem identifying it. However, in the case of multi-tenant setups, you must make a choice (either pick one or all combinations of tenants/domain).

In OneDrive enumeration, the exact combination of tenant name and domain is important. If 'AcmeComputerCompany.com' has 3 tenants: 'acmecomputercompany', 'acmeEurope', and 'acmeAPC', then users could exist in any of those tenants.

Possible OneDrive URL combinations would include:

acmecomputercompany – [[email protected]](/cdn-cgi/l/email-protection)

acmeEurope – [[email protected]](/cdn-cgi/l/email-protection)

acmeAPC – [[email protected]](/cdn-cgi/l/email-protection)

This can get further complicated if the organization also uses country-specific domains for email. In many cases this won't be an issue, but it is something to be aware of. It is also a double-edged sword. While this division of users might increase enumeration time investments, it also allows for targeting users in specific geographic areas. If you encounter this, I recommend running small survey wordlists against all combinations of domains and tenants. You might be surprised!

If you are not getting any hits anywhere, try the 'tenant.onmicrosoft.com' address as the domain. During user creation, an admin can choose the tenant 'onmicrosoft domain', such as 'acmecomputercompany.onmicrosoft.com' instead of a custom domain like 'acmecomputercompany.com'.

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig8.1_update.png)Figure 9 - User Creation Domain Selection

Lastly, I want to disclose one additional piece of information regarding OneDrive enumeration. When you try to connect to the OneDrive or SharePoint host (e.g., 'acmecomputercompany-my.sharepoint.com'), you will receive a '403' or a '401' error response.

When a username returns a '401', that indicates that SharePoint has been configured to require Modern Auth. (This is specifically in regard to SharePoint and not the organization as a whole.)

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig8_update.png)Figure 10 - Example of Tenant Without Modern Auth Required![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig11_update.png)Figure 11 - Example of Tenant With Modern Auth Required

The associated setting for Modern Auth in SharePoint can be found here:

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig12_update.png)Figure 12 - Modern Auth Controls

If this is set to 'Block Access', the OneDrive enumeration (and any request to that OneDrive/SharePoint host) will result in a '401' error. If it is in the default, 'Allow Access', it will return a '403' error.

## Username Lists

The classic, 'Statistically-Likely-Usernames' is a good starting point. However, it should not be your ONLY wordlist source. At least not directly.

The problem is that the wordlists included with 'Statistically-Likely-Usernames' are small. The wordlists in the SLU total approximately 1.2 million. This may seem like a lot, but it is inadequate in most cases. Instead, you should build your own.

If your targets are based in America, I recommend using US Census data. Here you can find the 1990 census data, including first names and last names:

<https://www.census.gov/topics/population/genealogy/data.html>

Specifically, the 1990 files can be found here:

<https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html>

I have included these as the 'firstnames1990.txt' and 'lastnames1990.txt' in my GitHub: ([https://github.com/nyxgeek/one...](https://github.com/nyxgeek/onedrive_user_enum)).

Using these lists, we can generate all of our usernames.

I have included a shell script that can be run, titled 'generate_usernames_f17.sh'. It will create a 'USERNAMES' folder within the project folder, and then proceed to create sub-folders for various username formats.

`./generate_usernames_f17.sh firstnames.c2010.txt lastnames.c2010.txt`

For easier processing, the files are split up into 175k chunks. This should be a size that is digestable even to smaller machines with less memory. OnedDrive_Enum can take a directory as a source and will iterate through the files within.

File will be written out in the following format:
  
  
  USERNAMES/john.smith_1kx10k_c2010/xaa
  USERNAMES/john.smith_1kx10k_c2010/xab
  USERNAMES/john.smith_1kx10k_c2010/xac
  USERNAMES/john.smith_500x20k_c2010/xaa
  USERNAMES/john.smith_500x20k_c2010/xab
  USERNAMES/john.smith_500x20k_c2010/xac
  USERNAMES/jsmith_c2010/xaa
  USERNAMES/jsmith_c2010/xab
  USERNAMES/jsmith_c2010/xac

**Note: This will take approximately 8GB of space.**

## Notes for Defenders

Unfortunately, there is no way to detect this, that I'm aware of. Microsoft does not consider user enumeration to be a vulnerability.

Your only option is to disable the OneDrive personal sites.

![](https://www.trustedsec.com/wp-content/uploads/2023/06/Burkeland_fig13.png)Figure 13 - Disabling OneDrive Personal URL

If you do this, existing users will still have OneDrive URLs that can be enumerated and will need to be cleaned up. This is not an ideal solution, but it is the most you can do until Microsoft takes user enumeration more seriously. Even if you do this and disable OneDrive, there are other methods of user enumeration. Microsoft Graph and Microsoft Teams are major methods.

If we really want to get serious about user enumeration, we need to stop making our usernames the same as our email addresses. Email addresses are by definition a public piece of information that you give out. Usernames don't have to be public.

Username format also makes a real difference in enumeration resistance. Numeric usernames are the worst, as these are the easiest to enumerate once identified. Simple combinations like 'jsmith' or 'smithj' are easy to enumerate. While 'john.smith' and 'john.j.smith' formats offer a greater variety, they also disclose the most PII.

I believe that a format such as 'jsmith192837', where the numeric portion is random, would be a palatable yet strong username format. By adding six (6) digits to the end of a normal 'jsmith' username, you increase the enumeration resistance by a million. An attacker would then need to iterate through A MILLION attempts just to get any 'jsmith' matches. And so on, with 'jsmith', 'ssmith', 'rsmith', etc. This would make massive enumeration unfeasible. For outward-facing employees, mail aliases could be created to allow easy contact with the outside world.

## Conclusion

OneDrive adoption is at an all-time high. So many actions will inadvertently create a OneDrive URL, whether users are actually using it or not. Couple this with the relative unawareness of most companies about this exposure and the inability to detect it, and we have an ideal enumeration method.

Happy Hacking!

## Shoutouts

Thanks to Dr. Nestori Syynimaa ([@DrAzureAD ](https://twitter.com/DrAzureAD)\- AADInternals), [@thetechr0mancer](https://twitter.com/thetechr0mancer) and Black Lantern Security with TREVORspray, SkullSecurity (statistically-likely-usernames), [@rootsecdev](https://twitter.com/rootsecdev) (since HE in turn showed me TREVORspray) and [@HackingLZ](https://twitter.com/HackingLZ).

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#320d414750585751460f715a5751591700025d4746170002465a5b411700025340465b515e5717000254405d5f1700026640474146575661575117000314535f4209505d564b0f7d5c5776405b4457170002465d170002775c475f170002665a575f170002735e5e1701731700025a46464241170173170074170074464047414657564157511c515d5f170074505e5d551700745d5c5756405b44571f465d1f575c475f1f465a575f1f535e5e "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=OneDrive%20to%20Enum%20Them%20All%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fonedrive-to-enum-them-all&mini=true "Share on LinkedIn")
