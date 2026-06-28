---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-31_how-i-was-able-to-modify-and-delete-any-users-data-file-filestack-api.md
original_filename: 2023-08-31_how-i-was-able-to-modify-and-delete-any-users-data-file-filestack-api.md
title: How I was able to modify and delete any user’s data file (filestack API)
category: documents
detected_topics:
- api-security
- file-upload
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- api-security
- file-upload
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: 058863630ccd0aa0618dbfe4cd00861e3a68d63712771dfa31b1fce8ca7ea90c
text_sha256: ea5e755d577292d41d6b851c2e2b4d3117c58f56b139f3d10db65b818883a9a5
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to modify and delete any user’s data file (filestack API)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-31_how-i-was-able-to-modify-and-delete-any-users-data-file-filestack-api.md
- Source Type: markdown
- Detected Topics: api-security, file-upload, access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `058863630ccd0aa0618dbfe4cd00861e3a68d63712771dfa31b1fce8ca7ea90c`
- Text SHA256: `ea5e755d577292d41d6b851c2e2b4d3117c58f56b139f3d10db65b818883a9a5`


## Content

---
title: "How I was able to modify and delete any user’s data file (filestack API)"
url: "https://spideynati.medium.com/how-i-was-able-to-modify-and-delete-any-users-data-file-filestack-api-7377bc52856f"
authors: ["Spideynati (@yashparwekar)"]
bugs: ["Hardcoded API keys"]
publication_date: "2023-08-31"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 820
scraped_via: "browseros"
---

# How I was able to modify and delete any user’s data file (filestack API)

How I was able to modify and delete any user’s data file (filestack API)
Spideynati
Follow
4 min read
·
Aug 30, 2023

46

1

Press enter or click to view image in full size

So,
This is my 2nd blog after nearly two years, yeah yeah I was busy okay doing…. nothing! I found so much to write a blog about but nothing so interesting or rare to actually worth the effort in writing because nearly every info was available on those interesting bugs mostly were access control issue specific to the application and so but this ones interesting and not much info is there other than official documentation. Lets start about main topic now.

As everyone I was collecting info on domain doing recon collecting subdomains and all analyzing request and responses for application, collecting and analyzing js files for endpoints.

I have two burpsuite extensions enabled for Js files i.e. BurpJsLinkFinder and also JSminer. sometimes JSminer collect some good info like api endpoints and api keys and all but api keys are rare to mostly that gets collected are client side apikeys which are of no use. In one subdomain of The Redacted site jsminer collected some apikeys for paypal, datadog and filestack, paypal and datadogs were client side apikeys, initially I ignored filestack one also but it catched my eye when I got an interesting endpoint which the redacted site was using to upload data as “filestack-upload” which were uploading files into S3 portal owned by site, but why filestack-upload as endpoint name then I did some research and got to know about filestack which is a fileuploader api to different and from different platforms like S3, gdrive, onedrive, etc. I then analysed api key found by jsminer which looked like:

secret in subdomains js file

When I visited to filestack documentation I got to know that it can be used to manage and delete files of website and can be verified using:

curl -X POST \
— data-binary @filename.png \
— header “Content-Type:image/png” \
“https://www.filestackapi.com/api/store/S3?key=MY_API_KEY”

but if security measures are there u need policy and signature to upload edit and delete files so request will be like

curl -X POST \
— data-binary @filename.png \
— header “Content-Type:image/png” \
“https://www.filestackapi.com/api/store/S3?key=MY_API_KEY&policy=POLICY&signature=SIGN"

The above request is only for uploading and verifying that keys belong to the application u will get response as:

Press enter or click to view image in full size
filestack upload response

Now I can upload files but what about deleting and viewing other user files for that I once again visited /filestack-upload endpoint and saw upload url there like:

location of file uploaded

Now I got confused and thought how if the site using filestack is uploading file to their own s3 subdomain so after reading more documentation I found about storage aliases supported by filestack.

Press enter or click to view image in full size
storage alias

These are storage alias supported by filestack: Amazon S3, Rackspace, Azure Blob Storage, Dropbox, Google Cloud Storage. once again you have to include policy and sign because of security measure if needed. Now I was able to fetch these files using filestack api and location it was uploaded to using the url in image shown I used S3 bcoz the file was uploaded to S3.

Get Spideynati’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you read the documentation “www.filestack.com/docs/" u will get to know that using DELETE request and modifying different query params as per your use case and files uploaded and managed you can delete the file if its uploaded using filestack. Also it can be edited and managed using the same by reading transformation section.

Now I was able to fetch url of uploaded images in profiles and other section of website by any user and all returned url as:

https://___.production.______________//__________.png

as I found out it was same subdomain url which uploading the media returned as shown in above image “location of file upload” meaning I now can delete and modify any image uploaded by user simply by getting the url of their image.

Not only that I can also upload how much file I want no matter how big using this api and a simple python script(DM or email if u need it) to use company S3 as my personal cloud storage. (obviously if I upload encrypted zip files for privacy reasons)

So thats it there is not much about this on the internet or rather I didn’t find one so thought should do a writeup to help others so that they don’t have to invest time for all this as I did. This was found in a public bug bounty platform and also apikeys by extension used by many but i think others avoided this thinking of it as client side api keys as I mentioned earlier. So, keeping the eye out on everything and analysing application with focus really helps with weird and unique vulnerabilities.

That’s it that was it want some more info? Simply google or you can always ping me (just don’t ask stupid questions though I got friends for that!).

Email: spideynati0@protonmail.com

(no I don’t use Gmail if its not needed)
