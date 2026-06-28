---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-19_local-file-inclusion-at-ikeacom.md
original_filename: 2018-09-19_local-file-inclusion-at-ikeacom.md
title: Local file inclusion at IKEA.com
category: documents
detected_topics:
- command-injection
- path-traversal
- file-upload
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- path-traversal
- file-upload
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 72977fd4f42061ce62c04fc9b6ef247859b022e1c891cdc405afa084f3909661
text_sha256: f67f44e097f1cb0c97bc5542e5f05fe67043f128d19b24916f7a83c0bac4ec4e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Local file inclusion at IKEA.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-19_local-file-inclusion-at-ikeacom.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, file-upload, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `72977fd4f42061ce62c04fc9b6ef247859b022e1c891cdc405afa084f3909661`
- Text SHA256: `f67f44e097f1cb0c97bc5542e5f05fe67043f128d19b24916f7a83c0bac4ec4e`


## Content

---
title: "Local file inclusion at IKEA.com"
url: "https://medium.com/@jonathanbouman/local-file-inclusion-at-ikea-com-e695ed64d82f"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Ikea"]
bugs: ["LFI"]
bounty: "250"
publication_date: "2018-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5690
scraped_via: "browseros"
---

# Local file inclusion at IKEA.com

Local file inclusion at IKEA.com
Jonathan Bouman
Follow
11 min read
·
Sep 20, 2018

1.3K

4

Press enter or click to view image in full size
Proof of concept

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
With a local file inclusion (LFI) attack you trick the server into sharing its private files. Think of the configuration, log and source code files of the website. Sometimes it can even lead to Remote Code Execution. LFI attacks are therefore considered to be high impact.

Most of the LFI attacks are caused by code that dynamically loads images or other files. If the requested filename or path is not properly validated it will serve you the private files you requested. Let’s learn more about it!

IKEA.com
One of the strongest brands in the world is IKEA; it’s in the Top 50 of Forbes. Besides that, about everyone has at least one IKEA product at home; I love my IKEA LATTJO brain hat! What about you? Leave your favourite IKEA product in the comments below ;-)

Another good thing about IKEA is that they’ve got plenty of properly designed websites and apps. They look good, are consistent and serve a big audience. To make it even better, they have a Bug Bounty Program that allows us to safely test their security and publish about it afterwards; as long as we follow the rules of Responsible Disclosure. So let’s give it a try!

Finding targets
Most of the times I start with enumerating all the (sub)domains of the target. To make life easier I use Aquatone. This tool looks up the domain in different public domain databases and returns a nice list of active subdomains, including screenshots. Please check the Unrestricted File Upload at Apple.com report in order learn more about Aquatone.

Press enter or click to view image in full size
Aquatone found 418 active subdomains

Bathroom planner
One of the subdomains we find is Bathroomplanner.IKEA.com, a tool that allows you to look up products and add them to your own bathroom product list.

You are able to email this product list or to download it locally as a PDF. The generated PDF file consists of a some text and product images, nothing special you might think.

Press enter or click to view image in full size
The Bathroom Planner
Press enter or click to view image in full size
Example of the PDF shopping list

But how is this PDF generated?

Intercepting network traffic
If I say intercepting, you say… Burp Suite! We start Burp Suite and start intercepting the traffic between our browser and the IKEA web server.
We open the frontpage and try to add a product to our list.

Press enter or click to view image in full size
The request our browser sents to IKEA if we add a product to our list

As we can see there are multiple interesting fields:
- data; a JSON blob containing product and image codes, no file paths
- shopping; a JSON blob containing our product list, no file paths
- pdf: a long string of characters, contents unclear
- images: some base64 encoded images

Recognize Base64 strings
If you ever run into a long string of alphanumeric characters, always check if it’s a Base64 encoded string. Base64 encoding is used for data transport of files. A handy tool to decode base64 strings is http://decodebase64.com/

Press enter or click to view image in full size
Decode Base64 strings

If we paste this string into the decoder it gives an error; it contains invalid characters like %. Mmm. This smells like the string is also URL encoded, so let’s URL decode the string first, before we put it into our Base64 decoder. You may use https://meyerweb.com/eric/tools/dencoder/ for URL decoding and encoding.

Press enter or click to view image in full size
URL decoder and encoder

If we URL decode first and Base64 decode afterwards we will end up with the following string

Press enter or click to view image in full size
Output after URL en Base64

This looks interesting. If we add a product to our list it also supplies the IKEA web server with some template that is used for generating the PDF shopping list.

What if we are able to include local server files into this PDF. For example as an image? Good idea, let’s add <img src=”/etc/passwd”> to this template, Base64 encode and URL encode it again, replace the pdf parameter in Burp Suite and press Forward.

Long story short, that doesn’t work. The PDF generator does not recognize this file as an image and it won’t parse it in the output…

Plan B; identify the PDF Library, search for flaws in library
Maybe we can find another way to include files in the PDF? First we need to discover the tool that is used for PDF generation. Google is your friend. Just search on some unique strings found in the template and see what Google thinks.

Press enter or click to view image in full size
Node-html-pdf or mPDF

We’ve got two options, a node-html-pdf library or the mPDF library. After quickly reading the documentation of both we discover it is actually the mPDF library being used in this project.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Identifying security issues in mPDF
We immediatly make a local copy of mPDF in order to examine it for security bugs. The best place to start is the CHANGELOG, a file being used by developers to keep track of the changes in between versions.

Press enter or click to view image in full size
Search for the word Security in the CHANGELOG, it will save you plenty of time

As we can see mPDF changed the way they handled annotation tags. The change was made on 19/10/2017. So lets have a closer look at this tag in the documentation.

Press enter or click to view image in full size
The possibility to include files is not mentioned in the documentation, strange.

No mentions about file inclusion. Mmm. Let’s Google again and see if someone else wrote about it.

Press enter or click to view image in full size
Gotcha, it was reported as an issue!

There is a serious security problem in the older versions of mPDF as we can read in the issue being reported by h0ng10; one is able to include files through the annotation tag.

If we take a closer look at the Github commits of this project we will discover this commit, it shows us the vulnerable mPDF code.

So we are able to change the template of the PDF and we may have the possibility to include a tag that includes files. Perfect. Lets see if IKEA forgot to update the library to the latest version.

The Attack
We add the following tag to the template:

<annotation file=\”/etc/passwd\” content=\”/etc/passwd\” icon=\”Graph\” title=\”Attached File: /etc/passwd\” pos-x=\”195\” />

Send the new template with the Burp Suite Repeater and download the PDF file. We open the file with Foxit Reader and start looking for the yellow annotation marker.

Press enter or click to view image in full size
We’ve got the /etc/passwd file included in our PDF file

A double click on this marker is enough to open the stolen server file, our attack is successful. Time to submit a bug report and wait for the response from IKEA!

Press enter or click to view image in full size
/etc/passwd file contents

Conclusion
IKEA.com allows one to manipulate the PDF template being used in one of their shopping list exports. The used PDF library contains (hidden) functionality that allows one to embed files into the PDF by adding a specific tag in the template. This functionality was disabled in the latest version of this library, IKEA did not update so they were vulnerable to this bug. This resulted in the creation PDF containing the /etc/passwd file of one of the IKEA production servers.

Solutions
- Never allow the users to manipulate the template of a PDF
- Render the PDF containing the shopping list on the client-side, for example with jsPDF
- Update to the latest version of the mPDF library, disable the annotation code

Rewards
€250

Discussion, what is Responsible Disclosure?
Below you can read the timeline of the bug report. It’s quite long this time. Most of the time my reports go without any hassle, Bol.com is a great example. But sometimes it takes more time.

This time we ran into an interesting situation; we were forced by IKEA to report our bug through a Bug Bounty Platform: Zerocopter. But we were not allowed by Zerocopter to have an account at the time of submission. So we had to email Zerocopter for updates and the coordination of the disclosure. We did not have a direct communication channel with IKEA. The initial fix took a few weeks and the coordination of the disclosure three full months and ~30 emails.

Press enter or click to view image in full size
Policy for Responsible Disclosure (UPDATE 04–10–2018: New guideline published) by Ministry of Security and Justice, The Netherlands

The Dutch Governement created a policy (UPDATE 04–10–2018: New guideline) that explains in a few pages how to setup a proper responsible disclosure. Direct communication between a security researcher and the organisation that has a security vulnerability is key.

Furthmore it is important to have a clear procedure of how the disclosure works. Only in rare situations a researcher and organisation may decide to do a non-disclosure (PDF, page 7, UPDATE 04–10–2018: PDF, Page 13):

If a vulnerability is difficult or impossible to resolve, or if resolving it will involve high costs, the disclosure and the organisation may agree to not disclose the vulnerability.

These days plenty of bug bounty programs are private and non-disclosure is part of their rules. But is this in the public interest? What if a company does not fix the bug in time, what if customers are affected by the bug (a data leak) but they are not informed, what if a researcher got threatened afterwards by lawyers because the researcher revealed its name?

This non-disclosure rule is not part of any ISO recommendations. Also the European Task Force does not advice any non-disclosure rules in their June 2018 report on Software Vulnerability Disclosure in Europe. The opposite, they advice to forbid governments to sign non-disclosure agreements; see page 84.

If Bug Bounty Platforms don’t change, security researchers may start avoiding these platforms and companies and they may start publishing full disclosures again. And that is exactly what we try to avoid.

Bug Bounty Platforms have a big responsibility these days; they advice organisations how to setup a proper responsible disclosure program. However they should also defend the public interest and their security researchers at the same time. Pushing for public disclosure should be part of that.

Hackerone is a good example, their public disclosures are a great resource to learn more about specific bugs and at the same time they inform the public about potential leaks in the past.

Other bug bounty platforms like Bugcrowd and Zerocopter miss a public disclosure feed like the one Hackerone has. Would be great if this changes and platforms start pushing more for public disclosure instead of non-disclosure.

In a perfect world private programs would not exists; everything is public at a certain moment. There need to be clear procedures of what to do if a report is not fixed in time and researchers should be protected from (civil) prosecution if they follow the rules. Reporting bugs should be without any hassle. What do you think? Please leave a comment below.

Happy that IKEA fixed the bug and is supporting coordinated responsible disclosure, thanks!

Andras fel lär bäst.

Timeline
16–06–18 Discovered the bug, used Zerocopter submission form as a guest (no signup allowed)
17–06–18 Discovered that PDF generation is now disabled (By IKEA after tripping their IDS? High five to their devs!)
18–06–18 Zerocopter could not confirm bug (because pdf generation was disabled), but accepts report based on provided evidence, informs IKEA
25–06–18 Requested Zerocopter for updates
27–06–18 Answer from Zerocopter: IKEA busy with fix since 19–06–18
08–07–18 Requested update by email, requested if they could ask IKEA if they mind if I disclose this bug as part of a print magazine article that would be published in October 2018, asked if bug is eligible for any rewards
09–07–18 Zerocopter informed me that bug is fixed, Zerocopter told me I do not have permission for publication (‘ IKEA does not allow their name to be used by other companies/people for commercial or other purposes’).
09–07–18 Informed Zerocopter that I won’t use the name or logo of IKEA for this time in this specific print article, but will not censor it from my regular online reports. Notified Zerocopter that the Bug Bounty Rules IKEA has on their website do not mention any non-disclosure rules after a bug fix.
09–07–18 Zerocopter confirmed that non-disclosure is not part of the current rules as published on the IKEA website. They will remind IKEA again to add this to their rules.
13–07–18 Zerocopter informed me that they will ask IKEA about the rewards when all my other reported bugs are resolved.
30–07–18 Requested Zerocopter update by email
02–08–18 Answer from Zerocopter: file inclusion bug should be resolved now, although status of report is not changed to resolved, I have to wait on a reply from IKEA themselves.
02–08–18 Informed Zerocopter that I don’t have a Zerocopter account, so impossible for IKEA to reach me. Informed Zerocopter that I plan to do a responsible disclosure on 15–08–18 (60 days after submission is considered to be enough time), asked for direct contact with IKEA to coordinate disclosure. Explained that I dislike this way of follow-up by email, difficult to do proper responsible disclosure without any direct contact with IKEA. Requested if IKEA is aware of this suboptimal situation.
03–08–18 Zerocopter acknowledges that they understand my frustration, no update from IKEA (‘IKEA is a big company and have plenty of other bugs to fix’). Zerocopter promises that any new bug reports will be part of a personal account so follow-up to Zerocopter is easier in the future (Good news: signups are open again for everyone. You are now able to follow-up your reports. Side-Note: Research accounts that give access to other private programs are still on hold.)
09–08–18 I confirmed Zerocopter that the bug is resolved.
09–08–18 Requested Zerocopter to share this post (draft) with IKEA for review, requested direct contact for futher coordination of disclosure; email or Zerocopter platform is fine for me.
13–08–18 Answer from Zerocopter: informed IKEA about the blog and shared my confirmation of the bug fix. Zerocopter adviced me to remove IKEA from the report in order to avoid any problems with IKEA.
13–08–18 Informed Zerocopter that non-disclosure after a fix was not part of the rules on time of report submission and IKEA did not update the submission rules after Zerocopters reminder on 09–07–18. Suggested to meet in person and have a conversation over a cup of coffee; as I live 2000 meters from Zerocopters office. Requested Zerocopter to ask IKEA to contact me to discuss any problems they might have with disclosure.
14–08–18 Zerocopter shared IKEA contact details with me, they mentioned their Confidentiality clause in their terms I agreed on when submitting the bug.
17–08–18 Emailed IKEA and requested bug report updates, requested coordination of disclosure of this report, shared my frustration that it is quite difficult to do proper responsible disclosure with them.
20–08–18 IKEA confirms frustration, explains they are new to responsible disclosure programs and need to coordinate plenty of teams world wide. IKEA is going to request the different teams involved for updates.
21–08–18 Emailed IKEA I just submitted a new bug through the Zerocopter platform, using my new account. It works well.
30–08–18 Zerocopter asked me if contact is setup between me and IKEA.
30–08–18 Emailed Zerocopter to thank them for the introduction and the properly working account.
06–09–18 Requested IKEA for an update; requested coordination of disclosure of this report.
11–09–18 IKEA informed me they changed the status of this bug to Resolved on Zerocopter.
11–09–18 Zerocopter sent me a €250 Reward
11–09–18 Emailed IKEA to thank for the reward, requested coordination of disclosure of this report.
17–09–18 IKEA informed me I’m allowed to disclose this report.
19–09–18 Published this report.
04–10–18 Added links to the report to the new Coordinated Vulnerability Disclosure Guideline (Dutch Governement)
