---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-05_how-i-hacked-40000-user-accounts-of-microsoft-using-2fa-bypassoutlooklivecom.md
original_filename: 2019-02-05_how-i-hacked-40000-user-accounts-of-microsoft-using-2fa-bypassoutlooklivecom.md
title: How I hacked 40,000 user accounts of Microsoft using 2FA bypass(outlook.live.com)
category: documents
detected_topics:
- mfa
- mobile-security
- password-reset
- command-injection
tags:
- imported
- documents
- mfa
- mobile-security
- password-reset
- command-injection
language: en
raw_sha256: bedbae905553ab2312622c46648c27f2b6206df7d0b14fa66a6a75862bd8d4a0
text_sha256: 68cf7559d69a6f7478628b7d4950922d162386a633d6eac846f6693e23426303
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked 40,000 user accounts of Microsoft using 2FA bypass(outlook.live.com)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-05_how-i-hacked-40000-user-accounts-of-microsoft-using-2fa-bypassoutlooklivecom.md
- Source Type: markdown
- Detected Topics: mfa, mobile-security, password-reset, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `bedbae905553ab2312622c46648c27f2b6206df7d0b14fa66a6a75862bd8d4a0`
- Text SHA256: `68cf7559d69a6f7478628b7d4950922d162386a633d6eac846f6693e23426303`


## Content

---
title: "How I hacked 40,000 user accounts of Microsoft using 2FA bypass(outlook.live.com)"
url: "https://medium.com/@goyalvartul/how-i-hacked-40-000-user-accounts-of-microsoft-using-2fa-bypass-outlook-live-com-13258785ec2f"
authors: ["Vartul Goyal (@hackvartul)"]
programs: ["Microsoft"]
bugs: ["2FA / MFA bypass"]
publication_date: "2019-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5432
scraped_via: "browseros"
---

# How I hacked 40,000 user accounts of Microsoft using 2FA bypass(outlook.live.com)

How I hacked 40,000 user accounts of Microsoft using 2FA bypass(outlook.live.com).
vartul goyal
Follow
4 min read
·
Feb 5, 2019

132

4

Web.archive.org is my favourite tool and so I thought to choose outlook.live.com to make my target component.

Microsoft Outlook is a personal information manager from Microsoft, available as a part of the Microsoft Office suite. Although often used mainly as an email application, it also includes a calendar, task manager, contact manager, note taking, journal, and web browsing.

It can be used as a stand-alone application, or can work with Microsoft Exchange Server and Microsoft SharePoint Server for multiple users in an organization, such as shared mailboxes and calendars, Exchange public folders, SharePoint lists, and meeting schedules. Microsoft has also released mobile applications for most mobile platforms, including iOS and Android. Developers can also create their own custom software that works with Outlook and Office components using Microsoft Visual Studio. In addition, Windows Phone devices can synchronise almost all Outlook data to Outlook Mobile.

This is more secured platform used by million of users on daily basis at corporate and personal use level.

When I was searching for archived directories in web.archive.org, it suddenly strikes with some common parameter like below:

/owa/username@hotmail.com/

and then my second step is to check that whether these username are expired one or active users, when put the first username, it gives me link that username is valid and redirected to password page. I tried many attempts to reset the password but no success. Then I tried one last option “I do not have any of these”. Afterwards you will redirected to next page where it will ask you to send the authentication code in any mail id.

Now you have valid Microsoft username and your valid email id to receive the authentication code.

At last I got the below authentication code:

Microsoft account

Password reset code:

Please use this code to reset the password for the Microsoft account go*****@gmail.com.

Here is your code: 0470572

If you don’t recognise the Microsoft account go*****@gmail.com, you can click here to remove your email address from that account.

Thanks,

The Microsoft account team

I simply put the authentication code and redirected to security question where I need to answer very basic question, this is below screenshot and half of the information, you can get from username and other from social engineering.

Press enter or click to view image in full size

One can easily bypass these scenarios and I found more than 40,000 active users through waybackurls utility when I asked the Microsoft security team to reset the password for any active users, hence they did not allow me to do so and created their test accounts to allow me to reset their passwords. This is very basic security questionnaire, if you can compare with Google account recovery page, as they have put it over there and one can easily bypass it.

Get vartul goyal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I asked to Microsoft security team that this is high critical bug and impacted large number of Microsoft users and simply ignored. This is below reply got from Microsoft.

Microsoft Reply:
Hello Vartul
As stated earlier, these are not password reset codes, but just the codes to check if the email provided is valid. These cannot be used to reset password. Also, once the email has been confirmed, an attacker needs to provide verification information about the account for resetting password. That information is then verified. The attack mentioned in the report is not a security bypass.
Please let me know if you have more questions. We have closed the case.
Thanks
MSRC
Reproducing Steps:
Go to below URLs and pick all emails and collect it one tex file.

2. Collect it all emails which contains all emails after /owa/evangelinedobney@hotmail.com/ in this pattern.

3. All URL’s, I have collected from web.archive.org.

4. Let collect the six emails and try to exploit it.

evangelinedobney@hotmail.com — → can reset the password for this account.

evanieves269@msn.com — — → can reset the password for this account also.

evaserio@hotmail.it — — — ->can reset the password for this account also.

evuong@hotmail.com — — →can reset the password fo this account also.

explicitsoundz@hotmail.com — →can reset the password fo this account also.

fernandosoares121253@hotmail.com — ->last one access code I received and can reset the password for it.

5. I got the 6 mails and let try to show in video how to exploit it. I will take email id one by one.

6. Go to https://outlook.live.com, lets make the video.

7. From video, it has been clearly shown that I can able to reset the password for any user mail mentioned in below mails.

here is below video link for more description:

https://www.youtube.com/watch?v=mzxX1h9sG9Y
