---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-30_abusing-the-serelabelprivilege.md
original_filename: 2024-05-30_abusing-the-serelabelprivilege.md
title: Abusing the SeRelabelPrivilege
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: b1597282569422723cf7a1dcbae8db14ba8d33bec3e47b2d1b735b72e4fbecd2
text_sha256: a1fefc597abd3dd6b5a7bf48b9e716f32323daecf909c270f66558112a1ae218
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing the SeRelabelPrivilege

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-30_abusing-the-serelabelprivilege.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `b1597282569422723cf7a1dcbae8db14ba8d33bec3e47b2d1b735b72e4fbecd2`
- Text SHA256: `a1fefc597abd3dd6b5a7bf48b9e716f32323daecf909c270f66558112a1ae218`


## Content

---
title: "Abusing the SeRelabelPrivilege"
page_title: "Abusing the SeRelabelPrivilege – Decoder's Blog"
url: "https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/"
final_url: "https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/"
authors: ["ap (@decoder_it)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2024-05-30"
added_date: "2024-06-05"
source: "pentester.land/writeups.json"
original_index: 271
---

In a recent assessment, it was found that a specific Group Poilcy granted via “User Right Assignments” the **SeRelabelPrivilege** to the built-in Users group and was applied on several computer accounts.

I never found this privilege before and was obviously curious to understand the potential implications and the possibility of any (mis)usage scenario.

Microsoft [documentation ](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/modify-an-object-label)is as usual not very clear and helpful, to summarize:

“ _Anyone with the**Modify an object label** user right can change the integrity level of a file or process so that it becomes elevated or decreased to a point where it can be deleted by lower integrity processes._“

Luckily, a [post](https://www.tiraniddo.dev/2021/06/the-much-misunderstood.html) from James Froshaw published in 2021 gave much more details and useful information on possible abuse 😉 . I highly recommend reading it before going on.

I decided to do some experiments to understand how “far” I could go. 

I started by assigning to a standard user the _SeRelabelPrivilege_ via group policy:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-2.png?w=1024)

The privilege is only available in High Integrity Level (in the case of cmd.exe -> run as administrator):

![](https://decoder.cloud/wp-content/uploads/2024/05/image-3.png?w=1024)

But what does this privilege grant to you? Well, a lot of interesting permissions!

  * It allows you to **take ownership** of a resource
  * Furthermore, unlike the _SeTakeOwnsership_ privilege, it allows you to own resources that have an**integrity level even higher than your own**
  * Once you have taken the ownership, you can grant yourself**full control** over the resource (process, tokens,…)
  * Quick & dirty: Same as abusing the _SeDebugPrivilege_ 🙂

My goal was to take ownership of a SYSTEM process, grant myself full control, and then create a process under the NT AUTHORITY\SYSTEM account. 

Perfect Local Privilege Escalation… pardon, just a “Safety Boundary” violation 😉

For this purpose, I created a simple POC:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-4.png?w=1024)

First of all, I needed to get the current user SID and enable the specific privilege. After this, I took the ownership of the process:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-5.png?w=1024)

I needed to open the process with WRITE_OWNER access. In the _SetSecurityInfo_ call, the “LABEL_SECURITY_INFORMATION” flag is mandatory, otherwise, I was not able to own a process with an Integrity Level higher than my High IL process.

Once I took the ownership, it was super-easy to grant full control:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-6.png?w=1024)

In this case, I needed to open the process with WRITE_DAC access, and after setting the explicit access to PROCESS_ALL_ACCESS, I gained full control of the process!

_Side note: this is just an example, the same results can be accomplished in different ways by using other API calls._

Let’s see if it works… 7116 was the winlogon process, which ran under System Integrity and was owned by SYSTEM:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-7.png?w=1024)

Ownership changed and full control was successfully granted:

![](https://decoder.cloud/wp-content/uploads/2024/05/image-8.png?w=1024)

The easiest way to abuse this was to perform a parent process injection. For this purpose, I used my old [psgetsystem](https://github.com/decoder-it/psgetsystem/blob/master/psgetsys.ps1) tool (remember to comment out _Process.EnterDebugMode()_)

![](https://decoder.cloud/wp-content/uploads/2024/05/image-9.png?w=1024)

Et voilà! Got SYSTEM access 🙂

Just for fun, I also took ownership of the token, granted full access to the token, and lowered the IL from System to Medium 😉

![](https://decoder.cloud/wp-content/uploads/2024/05/image-11.png?w=1024)

## Conclusion

From what I understood of this really strange privilege:

  * It allows you to take ownership of a resource even if it’s IL > of yours. 
  * Once you take ownership you can grant yourself full access to the process and tokens. 
  * The result, from an abuse perspective, is then quite similar to the Debug Privilege
  * Manipulating the mandatory label is just a consequence.
  * I still don’t understand why MS implemented it 

The source code of simple and stupid POC can be found [here](https://github.com/decoder-it/RelabelAbuse)

Thanks to James Forshaw for his useful hints and for helping me demystify this privilege 

That’s all 🙂

### Share this:

  * [ Share on X (Opens in new window) X ](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/?share=facebook)
  * 

Like Loading...
