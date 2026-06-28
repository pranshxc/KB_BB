---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-04_how-i-accessed-the-sensitive-document-which-i-had-already-deleted_2.md
original_filename: 2021-12-04_how-i-accessed-the-sensitive-document-which-i-had-already-deleted_2.md
title: How I accessed the Sensitive document which I had already deleted
category: documents
detected_topics:
- sso
- command-injection
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- cloud-security
language: en
raw_sha256: 06292413de02d87ebe81c7332a86d7098763f4f14d9d4fff90bdaafba3b58dc9
text_sha256: deeb0a72afee6ab6258e5530f9dfaaa1df89cac666cdf9dea2c930a383696cba
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I accessed the Sensitive document which I had already deleted

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-04_how-i-accessed-the-sensitive-document-which-i-had-already-deleted_2.md
- Source Type: markdown
- Detected Topics: sso, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `06292413de02d87ebe81c7332a86d7098763f4f14d9d4fff90bdaafba3b58dc9`
- Text SHA256: `deeb0a72afee6ab6258e5530f9dfaaa1df89cac666cdf9dea2c930a383696cba`


## Content

---
title: "How I accessed the Sensitive document which I had already deleted"
url: "https://pawanchhabria.medium.com/how-i-accessed-the-sensitive-document-which-i-had-already-deleted-adbc1e6fbb25"
authors: ["Pawan Chhabria (@heybenchmarkkk)"]
bugs: ["Privacy issue"]
publication_date: "2021-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3116
scraped_via: "browseros"
---

# How I accessed the Sensitive document which I had already deleted

Pawan Chhabria
 highlighted

How I accessed the Sensitive document which I had already deleted
Pawan Chhabria
Follow
4 min read
·
Dec 4, 2021

48

Hello All, this is my third writeup. I have already published two writeups which are How I was able to access a properly Configured S3 Bucket and My First Pre-Auth Account Takeover in 20 secs. Do check them out if you haven’t read them.

So, Let’s Begin!!!

Press enter or click to view image in full size
Data Leak

“Data” is very hot topic when it comes to security. There is always a debate on how companies store and handle “Customer Data”. To solve this debate, various compliances and regulations came into picture. This writeup focuses on how important it is to handle the sensitive data and how important it is to dispose it with care.

Please note: The domain and other details have been masked for Confidentiality Purpose.

I came across an application where it had an option of uploading documents for KYC. Aadhar Card, PAN Card, Driving License and Passport were the documents that can uploaded on the website. There documents are “Sensitive” in nature and utmost care must be taken while handling them.

I tried a few attacks to compromise the website but couldn’t succeed. So, I though let’s try to play with data. Let’s analyze how the PII data is being handled by the website.

I tried uploading a dummy image and captured the request. The request looked like this:

Press enter or click to view image in full size

Once the image got uploaded, the server returned a success response with the link of the uploaded image. It is shown in the screenshot below.

Press enter or click to view image in full size

Here, I noticed something strange. The image was getting uploaded on some S3 bucket and it had a few Amazon headers. Take a note of file name. It starts with “022eae” and ends with “fd55”. I tried accessing URL (Just the URL as highlighted in the above screenshot).

Boooom!!!

The document was accessible publicly. Imagine if some one might have uploaded their “Passport” or “Other Sensitive” document 😉.

Get Pawan Chhabria’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the frontend it showed me the uploaded document. Then, I thought, lets try to delete the document and check whether it gets deleted from the UI only or gets deleted from the server as well. I captured the delete request and it looked like this:

Press enter or click to view image in full size

The uploaded image had “Document ID” associated with it. I forwarded the request and waited for the response. The response is shown in the below screenshot. Notice the file name of the deleted file. It is the same file which was uploaded (Starting with “022eae” and ending with “fd55”).

Press enter or click to view image in full size

This was clear enough that we have successfully deleted the uploaded document. But wait!!!!!

Coming to the question whether it was deleted only on the UI or from the server as well. I tried pasting the entire URL of the uploaded document again to check whether it was deleted from the server.

Guess What! The document was still present on the server. It only disappeared from the front end. It’s the same document which started with “022eae” and ending with “fd55”) and publicly accessible.

Press enter or click to view image in full size

Business impact: It is a privacy violation wherein user thinks that he has deleted the document, but the document is still available in the S3 bucket and it is accessible without authentication. It is a privacy compromise of the user.

Golden Tip: Make sure to keep yourself updated. This thing would not have struck my mind if I hadn’t read about some compliance stuff online. Everything is vulnerable, you just need some knowledge to find the vulnerable point.

That’s it for this writeup.

Happy Testing!

Make sure you say a “Hi” to me if I could be of some help!

Twitter: @heybenchmarkkk

LinkedIn: Pawan Chhabria
