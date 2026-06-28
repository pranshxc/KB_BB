---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_bragging-rights-killing-file-uploads-softly.md
original_filename: 2021-02-28_bragging-rights-killing-file-uploads-softly.md
title: 'Bragging Rights: Killing File Uploads softly'
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- api-security
- mobile-security
language: en
raw_sha256: 6131ae509821fb63cb5689cdb5e85be4fb64e154dd63e9bb207c4f35361e81c6
text_sha256: 258b5d026422a97e2e24267f43f01c6ded6fe608e2d0d4b58563616580d7c127
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Bragging Rights: Killing File Uploads softly

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_bragging-rights-killing-file-uploads-softly.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `6131ae509821fb63cb5689cdb5e85be4fb64e154dd63e9bb207c4f35361e81c6`
- Text SHA256: `258b5d026422a97e2e24267f43f01c6ded6fe608e2d0d4b58563616580d7c127`


## Content

---
title: "Bragging Rights: Killing File Uploads softly"
url: "https://infosecwriteups.com/bragging-rights-killing-file-uploads-softly-fba35a4e485a"
authors: ["Manas Harsh (@ManasH4rsh)"]
bugs: ["Unrestricted file upload", "Stored XSS"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3855
scraped_via: "browseros"
---

# Bragging Rights: Killing File Uploads softly

Bragging Rights: Killing File Uploads softly
Manas Harsh
Follow
4 min read
·
Feb 28, 2021

269

Press enter or click to view image in full size

Hi buddies, I hope you all are doing great and breaking internet on regular basis. I have started hacking on Synack since a month or so and I must say it has been a great journey so far. In recent days, I have worked on file upload functionality a lot and in this writeup-cum-blog, I will be discussing some recent unrestricted file upload findings. I hope this helps you in some way. Let’s move forward.

If you are unfamilier or quite new with the file upload functionalities, here is the resource which will help you to understand this better: FileUpload.

So, on a weekend, I thought to give a whole day to file uploads and searched all the programs on Synack where we can upload files. I got some 4–5 programs and decided to check them all. On 2 programs, file uploads were already reported so I couldn’t move forward. Remaining 2 targets were quite new and you can call it my luck since nobody had reported anything like file uploads there. I started playing with the functinalities to see if we can do somethng weird with it. This website was accepting only PDFs so I tried the classical way to upload a php file with burp and it didn’t work:( It was not accepting anything other than PDF there.

Here comes the bypass! Thanks to writeups and blogs available already. At first I tried to uplaod a file with changing it’s name to a XSS payload. Silly, didnt work. Wait, what if we can use a SVG file with an PDF extension. Does that work? What if we move forward and add a nullbyte into extension? Well, that works actuallly :) Curious to see the full extension? Here it is:

prompt.SVG%00.pdf

So, the app was accepting the files and after upload, anyone could download your uploaded stuff. As soon as they open the file, XSS pops up. It took some time but payout was worthy.

2nd case was quite same where we can upload our reciepts and the admin will approve it. I applied the same method but somehow it didn’t work. I went back to Google and searched some more resources where we can bypass the restrictions. However, I observed that we can upload the PDF reciept with malicous content and payload executes when someone opens the report. Thanks to Payloadallthethings :) Here is the whole content:

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

%PDF-1.3
%âãÏÓ
1 0 obj
<</Pages 2 0 R /Type /Catalog>>
endobj
2 0 obj
<</Count 1 /Kids [3 0 R] /Type /Pages>>
endobj
3 0 obj
<</AA
<</O
<</JS
(
try {
app.alert\(document.cookie\)
} catch \(e\) {
app.alert\(e.message\);
}
)
/S /JavaScript>>>>
/Annots [] /Contents 4 0 R /MediaBox [0 0 612 792] /Parent 2 0 R
/Resources
<</Font <</F1 <</BaseFont /Helvetica /Subtype /Type1 /Type /Font>>>>>>
/Type /Page>>
endobj
4 0 obj
<</Length 21>>
stream

BT
/F1 24 Tf
ET

endstream
endobj
xref
0 5
0000000000 65535 f
0000000015 00000 n
0000000062 00000 n
0000000117 00000 n
0000000424 00000 n
trailer

<</Root 1 0 R /Size 5>>
startxref
493
%%EOF

As soon as admin opens the report, he gets a pop-up. Well, you will need to check if the victim has to download it on his system and if it happnes, it doesn’t make sense. In my case, it was getting executed on a new tab of the same target and was considered as a valid bug.

These were not the out of the world findings but it always makes sense to go a few miles extra to think differently. Sometimes you know how to exploit the stuff and sometimes you don’t. Here comes Google which will help you in everything and finding something new. File uploads are quite simple and all it takes is a different approach. I am still looking for a webshell with the help of it :( However, I felt awesome after finding these two bugs and I’m sure this small writeup helps you to craft your own methods.

This will be it for this time and I hope you get something from this read. If you liked it, you can appreciate me with hitting the clap icon below :) Suggestions are welcome as always and I invite you to my twitter DM if you have questions/suggestions regarding anything in bounties/hacking. I will try my best to help you :) You can find my twitter handle with this username: @manasH4rsh.

Stay curious, Stay hungry! Happy hacking :)

Adios ❤
