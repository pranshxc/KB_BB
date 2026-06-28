---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-23_do-not-trust-this-group-policy.md
original_filename: 2024-01-23_do-not-trust-this-group-policy.md
title: Do not trust this Group Policy!
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: d37e75b3f8f904ca6b93dcca8276a5456a42a80ca7ec7c2109c46ef4a73412cb
text_sha256: 164c20eb587f38d2e892c4c03c83f29b557d5aaf2e1865e9544a5fc9dfcb2842
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Do not trust this Group Policy!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-23_do-not-trust-this-group-policy.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `d37e75b3f8f904ca6b93dcca8276a5456a42a80ca7ec7c2109c46ef4a73412cb`
- Text SHA256: `164c20eb587f38d2e892c4c03c83f29b557d5aaf2e1865e9544a5fc9dfcb2842`


## Content

---
title: "Do not trust this Group Policy!"
page_title: "Do not trust this Group Policy! – Decoder's Blog"
url: "https://decoder.cloud/2024/01/23/do-not-trust-this-group-policy/"
final_url: "https://decoder.cloud/2024/01/23/do-not-trust-this-group-policy/"
authors: ["ap (@decoder_it)"]
programs: ["Microsoft (Windows)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2024-01-23"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 510
---

Sometimes I think that starting with a hypothetical scenario can be better than immediately diving into the details of a vulnerability. This approach, in my opinion, provides crucial context for a clearer understanding, especially when the vulnerability is easy to understand but the scenario where it could apply is not.

This post is about possible abuse of a group policy configuration for Local Privilege Escalation, very similar to the one I already [reported](https://decoder.cloud/2023/02/16/eop-via-arbitrary-file-write-overwite-in-group-policy-client-gpsvc-cve-2022-37955/) and MS fixed with [CVE-2022-37955](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37955).

## First scenario

So we have our Active Directory domain **MYLAB.LOCAL** with several Group Policies. Any domain user can by default access the **SYSVOL** share, stored in this case **\\\mylab.local\sysvol\mylab.local\Policies** , and read the configurations of the group policies.

At some point, our attention is caught by a “Files” preference group policy identified by the **Files.xml** file and located under the **Machine** context:

![](https://decoder.cloud/wp-content/uploads/2024/01/image.png?w=1024)

The Files policy is used for performing file operations such as copying or deleting one or more files from a source folder to a destination folder. The source and destination can be paths or **UNC names** and the operation can be performed under the **Machine** context or the logged-on user context if you specify it.

What actions does this policy perform on files? A thorough analysis of the contents of Files.xml can offer a clear understanding:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-9.png?w=1024)

The configuration specifies that the file **agentstartup.log** , residing in the local **C:\ProgramData\Agent\Logs** directory, should be copied to a hidden server share **logfilecollector$** within the **agentstartup** folder on the server. The destination filename on the server will be derived from the computer name.

This policy has been configured to copy the log files produced during the startup phase of an agent running on the domain computers to a centralized location. Alternatively, a group policy startup script executing identical copy operations could also be employed and would yield the same outcome.

When will the policy be processed? Running under the Machine context, at startup, and also on demand by performing a **gpudate /force** command. This share should be writable by the computer accounts where the policy is applied.

This is how the policy, configured by an administrator, would look like:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-8.png?w=1024)

And this is how the file server should have been configured. In this case, the directory located on the share is accessible by **Domain Users** in read-only but **Domain Computers** have modify permissions as expected:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-3.png?w=913)

There’s also another interesting user **logfileoperator** who also has modify permissions:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-4.png?w=820)

This account is responsible for managing log files. As a Domain User we can also look at the contents of the folder:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-5.png?w=1024)

The policy is also applied to the file server share which hosts the destination files.

By putting all the pieces together the question is: what potential consequences could arise if this user account, **logfileoperator,** is compromised by an attacker? Is there any possibility of privilege escalation? 

The **l****ogfileoper****ator** account can rdp to the file server (SRV1-MYLAB in this case) as a low-privileged user for performing his maintenance tasks. 

Let’s assume that our attacker, impersonating **logfileoper****ator** gains access to SRV1-MYLAB 

Let’s check the source directory:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-10.png?w=1024)

The default security settings of the **ProgramData** directory have not been modified, so low-privileged users can modify the contents of the Logs directory…

This scenario would be perfect for a very simple and easy escalation path by abusing the well-known [symlinks creation via NTObjectmanager](https://github.com/googleprojectzero/symboliclink-testing-tools) tricks.

To summarize:

  * Delete **c:\programdata\Agent\Logs\agentstartup.log**
  * Put a malicious dll in this folder and name it**agentstartup.log**
  * Delete contents of **c:\logfilecollector\agentstartup**
  * create a symlink for the target file **SRV1-MYLAB.log** pointing to destination **C:\windows\System32\myevil.dll**

![](https://decoder.cloud/wp-content/uploads/2024/01/image-11.png?w=1024)

  * Performing then a **gpupdate /force** will trigger the group policy which will copy our malicious **agentstartup.log** by following the symlink configured in **SRV1-MYLAB.log** to the destination **c:\windows\system32\myevil.dll** with**SYSTEM** privileges, given that the entire file copy operation is performed locally under the Machine context.

However, we currently face an issue. A few years ago, MS introduced the “Redirection Trust” feature to address redirection attacks, particularly during group policy processing. This feature prevents a privileged process from reparsing a mount point created by a lower privileged process:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-12.png?w=1024)

In Group Policy Client policy service (gpsvc) this feature is enforced.

But wait, our destination file is specified as UNC share and not a local drive, will Redirection Trust still work in this local scenario?

Guess what, it does not work! Our dll has been successfully copied:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-13.png?w=780)

We can see the successful operations in Procmon tool:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-15.png?w=1024)

It turns out that the mitigation is not effective on shares. James Forshaw already mentioned this in an old tweet: 

![](https://decoder.cloud/wp-content/uploads/2024/01/image-14.png?w=808)

Yes, it works on all the newest and updated versions of Windows as of now, Insider builds included:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-21.png?w=1024)

And no, I won’t explain again how someone could misuse an arbitrary file write with SYSTEM privileges. 😉

## Second Scenario

Let’s explore another hypothetical scenario. This time the administrator has setup this Folder policy:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-16.png?w=1024)

The policy, executed within the user configuration, will remove the logs folder along with all its files and subfolders located on the share **\\\127.0.0.1\EXPORTS\%username%,** dynamically expanded to match the currently logged-in user. 

The question arises: why does this configuration involve the localhost share?

Consider a scenario in our domain where a special folder containing user data is shared on all domain computers. The share name is **\\\ <computername>\exports\<username>**, but the physical path may vary for each computer. At some point, there is the requirement to create a policy for deleting a folder under this share (in this case, “logs”). The**Folder** preference suits our needs perfectly, but we want to use only one policy configuration and avoid specifying the physical path, which can differ. Instead, we opt for using the common share name **\\\127.0.0.1\…** (localhost).

By default, the delete operation is performed under the SYSTEM account (unless configured to run under the user’s context). This default behavior aligns with our requirement, ensuring a sure folder removal.

But again, this could lead to abuse, right? What if we redirect the folder to be deleted to a target folder inaccessible to the user?

Let’s see what could happen:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-17.png?w=775)

Our user has his own shared folder and contents are under his control.

In this scenario, our previous **c:\programdata\Agent** contains also another subdirectory**Updater** that stores the executable for the Agent updater and is obviously read-only for users, as opposed to the parent folder**Agent,** because the updater runs with SYSTEM privileges….

![](https://decoder.cloud/wp-content/uploads/2024/01/image-18.png?w=712)

So what’s the possible abuse? Can we transform an arbitrary folder delete to a privilege escalation? Let’s try it by creating a junction pointing to the **c:\programdata\agent** and perform **gpupdate:**

![](https://decoder.cloud/wp-content/uploads/2024/01/image-19.png?w=829)

It worked as expected, a share was specified as the target folder and redirection mitigation did not work, so we were able to delete also the **Updater** folder. Now the last step would be to recreate the Updater folder, put a malicious exe inside, name it AgentUpdater.exe, trigger or wait for our agent to perform and update and we have SYSTEM access…

## Conclusions

This was merely a hypothetical scenario, but I presume there are other real-world situations very similar to this, don’t you agree?

For example if “Group Policy Logging and Tracing” log files are saved on a shared folder:

![](https://decoder.cloud/wp-content/uploads/2024/01/image-22.png?w=1024)

Hint: when log file size exceeds 1024kB it will be saved as .**bak** and a new log file will be created. However, I’ll leave this exercise to the reader 😉

There is one limitation to exploiting this security bypass. The shared folder that will be redirected and contains the symlink must be a subfolder of the share; otherwise, you will encounter a “device not ready” error.

![](https://decoder.cloud/wp-content/uploads/2024/01/image-23.png?w=1024)

Should this be considered a misconfiguration vulnerability or software (ie: logic bug) vulnerability?

Hard to say, I obviously reported this to MSRC:

  * December 29, 2023: Initial submission.
  * January 11, 2024: MSRC responded, stating that the case did not meet the criteria for servicing as it necessitates “Administrator and extensive user interaction.” (????) They closed the case but indicated a possibility of revisiting it if additional information impacting the investigation could be provided.
  * January 11, 2024: I answered, providing a more detailed explanation of the scenario and attached a video. I emphasized that it does not require administrator interaction, as the issue revolves around exploiting an existing group policy with this configuration._Side note: If someone could clarify what MSRC means by “Administrator interaction is required”, I would be more than happy to correct my post and give due mention_
  * January 15, 2024: No response from MSRC. I sent an email with the draft of this post attached, informing them that my intention is to publish it in the absence of their feedback
  * January 22, 2024: MSRC told me that “they looked over the article and had no concerns or corrections”. Cool, appreciate it 🙂
  * January 23, 2024: Post published.

I find it perplexing that MSRC couldn’t offer a more comprehensive justification for their decision, instead of the given one that implies it would need Administrator (???) interaction.

Well, it is what it is, I won’t be organizing a dramatic exit just because of this tiny inconvenience 😉 

If MS won’t (silently) fix this issue here are my 2 cents to save the world from potential catastrophe:

  * Carefully evaluate permissions on source and destination files/folders when performing operations that involve creation or deletion operations via group policy
  * If the destination is a share, a red flag should be raised. Possibly avoid this configuration, if really necessary, follow the whole process logic and ask yourself at each step if it could be abused by placing a redirection.

That’s all 🙂 ..and thanks to Robin @ipcdollar1 for the review

### Share this:

  * [ Share on X (Opens in new window) X ](https://decoder.cloud/2024/01/23/do-not-trust-this-group-policy/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://decoder.cloud/2024/01/23/do-not-trust-this-group-policy/?share=facebook)
  * 

Like Loading...
