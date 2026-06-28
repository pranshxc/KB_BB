---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-dumped-pii-information-of-customers-in-an-ecommerce-site.md
original_filename: 2020-12-11_how-i-dumped-pii-information-of-customers-in-an-ecommerce-site.md
title: How I dumped PII information of customers in an ecommerce site?
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
- cloud-security
language: en
raw_sha256: 3fbf2e6f71f7f6219929c594888462cf500cdc07ea8f768a922559e692a537c9
text_sha256: 9719d8390856816b8087661d94877e7eea841952ad28e9267f2e5b18ed13c93b
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I dumped PII information of customers in an ecommerce site?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-dumped-pii-information-of-customers-in-an-ecommerce-site.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `3fbf2e6f71f7f6219929c594888462cf500cdc07ea8f768a922559e692a537c9`
- Text SHA256: `9719d8390856816b8087661d94877e7eea841952ad28e9267f2e5b18ed13c93b`


## Content

---
title: "How I dumped PII information of customers in an ecommerce site?"
url: "https://rikeshbaniyaaa.medium.com/how-i-dumped-pii-information-of-customers-in-an-ecommerce-site-237761f813cf"
authors: ["Rikesh Baniya (@rikeshbaniya)"]
bugs: ["AWS misconfiguration"]
publication_date: "2020-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4075
scraped_via: "browseros"
---

# How I dumped PII information of customers in an ecommerce site?

How I dumped PII information of customers in an ecommerce site?
Rikesh Baniya
Follow
2 min read
·
Dec 10, 2020

123

3

Like every website, the most interesting endpoint is always the image upload section.
So I fired my burp and was checking how the images are getting stored.

First thing i noticed was the image was uploaded in aws.So as always i checked for misconfigured aws for read/write access. The bucket looked solid.

The image was stored in the following format.

https://target.s3.us-east1.com/[image-id]?{Signature}

The image-id was a 16 digit alphanumeric value.
How ever in order to access the image, you would require a signature from amazon.

On checking the logs i found an interesting endpoint that was generating signatures for those images based on the image id an user inputs.

Press enter or click to view image in full size

The first I did was supply “1” as the photo id.

The signed URL generated was :
https://target.s3.us-east-1.com/1?{Signature}

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now imagine if you supply a null value as photoID and if the endpoint supplied a signed URL of following format:
https://target.s3.us-east-1.com/?{Signature} you would be able to get access to the entire list of private images that was hosted in that bucket.

As I supplied the a null value it returned an error.

Now I tried different ways to bypass it by encoding the parameters but no success with it and gave up.

After almost a week as i was checking the subdomain of that target, I saw that it was also using bucket to store the images, but this time the images was under a “FOLDER” called static.

Then I was like, why didn't I think of it.

I quickly fired my burp and started bruteforcing the values like admin,admins,user,users etc.
Finally the value “consumers” matched.

Visiting the signed URL gave me access to the images of the ID Card of the users which contained some realllllyyyy sensitive personal information.

Thanks for reading :)
