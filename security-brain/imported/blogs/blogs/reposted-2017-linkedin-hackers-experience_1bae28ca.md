---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-30_reposted-2017-linkedin-hackers-experience.md
original_filename: 2019-07-30_reposted-2017-linkedin-hackers-experience.md
title: 'Reposted [2017]: LinkedIn Hacker’s Experience'
category: blogs
detected_topics:
- xss
- csrf
- oauth
- access-control
- command-injection
- file-upload
tags:
- imported
- blogs
- xss
- csrf
- oauth
- access-control
- command-injection
- file-upload
language: en
raw_sha256: 1bae28ca1fb1d72d0088689dcf458a11b3da738c452572c40dcd2923e2271260
text_sha256: e3bf226cfe24dba6e514aef7af28e3f84d409405528e3ec34efa223f5b73b30c
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Reposted [2017]: LinkedIn Hacker’s Experience

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-30_reposted-2017-linkedin-hackers-experience.md
- Source Type: markdown
- Detected Topics: xss, csrf, oauth, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1bae28ca1fb1d72d0088689dcf458a11b3da738c452572c40dcd2923e2271260`
- Text SHA256: `e3bf226cfe24dba6e514aef7af28e3f84d409405528e3ec34efa223f5b73b30c`


## Content

---
title: "Reposted [2017]: LinkedIn Hacker’s Experience"
url: "https://medium.com/@dekeeu/reposted-2017-linkedin-hackers-experience-8465c1848c88"
authors: ["Alexandru Coltuneac (@dekeeu)"]
programs: ["LinkedIn"]
bugs: ["Stored XSS"]
publication_date: "2019-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5111
scraped_via: "browseros"
---

# Reposted [2017]: LinkedIn Hacker’s Experience

Reposted [2017]: LinkedIn Hacker’s Experience
Hi readers,
Alexandru Coltuneac
Follow
6 min read
·
Jul 31, 2019

5

Today I want to talk to you about a tricky Stored XSS Vulnerability that I found here, in LinkedIn, 2 months ago.

Press enter or click to view image in full size
Description

LinkedIn “allows members to write, edit, and distribute articles” on its platform and you can do that easily, by opening this URL in your browser: https://www.linkedin.com/post/new . You can basically customize everything you want in your article and also you can embed resources like images, videos or slides. From all of these, the image upload feature caught my attention, as you will see below.

Step by step

If you want to add a new image to your article, you have the possibility to upload it by clicking on the “+” sign and then selecting which type of content you want to include in your article, in this case an image.

Press enter or click to view image in full size

Then, as you click on Upload from computer and choose an image, a new POST request will be made to the /mupld/megaImageUpload endpoint as you can see in this image:

Press enter or click to view image in full size

The response of this request will be in JSON format and will contain a field called value . This will act like a unique identifier for my image and will represent its new name, once it was uploaded on the server.

Press enter or click to view image in full size

After the upload process is finished, the image will be available on https://media.licdn.com/ and in my case it was: https://media.licdn.com/mpr/mpr/AAMAAgDGAAgAAQAAAAAAAAtSAAAAJDBhMTg2ZWNiLWUwYzktNGMyNi05OWUxLTFlOWI0YmU0MmQzNg.jpg .

I felt that I could find something interesting here, so I started to tamper with the upload request. Firstly, I changed the extension of the image that I uploaded to .html, .htm, .xml, .svg etc. , hoping that this would make the server to deliver valid HTML content using my image. Unfortunately, this change always threw an INVALID_MEDIA error and my actions were in vain.

Press enter or click to view image in full size

Then, I chose to look a bit at the value of the Content-Type parameter that corresponded to the uploaded image and was always sent in the upload request. Initially, I tried to change this value to text/html, but, as expected, it did not work and I was faced with the same error message as before.

After several tests, I discovered that only the hardcoded value text/html was blacklisted. This means that I could change the Content-Type of my image to I/hackYou and once the file is served by LinkedIn’s server, it will have my fake header in the response (Content-Type: I/hackYou).

Moreover, the server didn’t check whether the blacklisted Content-Type was written using uppercase letters and I was able to easily bypass the filter by using one of these values: text/htmL, Text/html, tExt/html,… . I didn’t know until that moment, but the browsers ignore the case of the letters when it comes to the Content-Type header and will consider “Text/Html” as an equivalent for “text/html”. As a result, every image that I uploaded, no matter if it had a valid extension, could be used to serve HTML content.

Get Alexandru Coltuneac’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Was it necessary for the image to be valid and all the bytes from its body to be in a right order? Of course not. The backend script that was taking care of the uploaded image checked only the first few bytes of the image, to ensure that it is valid. And this was very helpful !

Now, I had a stored XSS, but my file was located at media.licdn.com, which is a sandboxed subdomain and from what I saw, it is used by LinkedIn to host static files. I began to check every subdomain of linkedin.com to see if I could find one that had a CNAME record that pointed to that domain, but my actions were not successful. Also, I looked for misconfigured CORS headers and incorrect cross-domain messaging just to be sure that I did (almost) all I could.

I was ready to send this vulnerability even if it didn’t impose a high security risk, when a brilliant idea came to my mind: what if my uploaded image could be accessed through the main LinkedIn domain? I tested it and to my surprise, it actually Worked !

Press enter or click to view image in full size
Risks

In order to assess this vulnerability, I thought what an attacker could do with this flaw. Well, it’s on the main domain, https://www.linkedin.com (so I didn’t have any problem with the Same Origin Policy), where I have also found the OAuth Authorization Endpoint (https://www.linkedin.com/oauth/v2/authorization). The most important thing was that this XSS bypassed any CSP restriction, just for the simple fact that the CSP header was not present in the response :D

So, I quickly did a PoC where I demonstrated how I could steal the anti-CSRF token from the OAuth Authorization page and use it in order to make a victim grant permissions to my application without his knowledge. You can have a look at the source code here.

Even if the LinkedIn API for developers does not have so many features, I was able, for example, to create different posts on behalf of a victim and share them on their personal profiles.

In the example from above, the anti-CSRF token was stored as the value of an input tag, but, in general, LinkedIn saves it in a cookie called JSESSIONID which is not marked as httpOnly.

Every important action initiated by the user corresponds to a POST request that has this cookie in a header. As a result, I could, for example, get it from document.cookie using JavaScript and then send these requests using Ajax:

- I(You) could send a Private Message to your BO$$

- I(You) could update your Personal Profile

- I(You) could share “articles, photos, videos or ideas” on your Personal Profile

Video PoC
Conclusion

I feel bad to say this, but LinkedIn disappointed me a lot. Even if they do have a Private Bug-Bounty program on HackerOne and I’m not part of it, I chose to help them and to report 3 different important vulnerabilities in a week. They were very slow to respond and even now, after 2 months after the initial reports, 2 of my vulnerabilities are not fixed and I don’t have a status for them (this XSS is fixed, btw).

I care about our professional profiles because they reflect our experience and, for some of us, they are a great way to find a job. That’s the reason I chose to spend some time trying to help this company and I encourage you if you do find a vulnerability in their products to report it ethically, because that’s what White Hackers Do !

In the end, I wish you all the best and Happy Holidays !
