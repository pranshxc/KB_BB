---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-05_injecting-punycode-url-within-the-arbitrary-text-via-comment-box-in-google-photo.md
original_filename: 2021-05-05_injecting-punycode-url-within-the-arbitrary-text-via-comment-box-in-google-photo.md
title: Injecting Punycode URL Within the Arbitrary Text via Comment Box In Google
  Photo Sharing Option
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 42067ab670022051a35eaa8abb6c98a2c7c67e523fbb38cb0ef7e191af15f7a3
text_sha256: b8345cf355432dcdb7bce0cdd229236040f84d9517115b0840b182e2306957e3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Injecting Punycode URL Within the Arbitrary Text via Comment Box In Google Photo Sharing Option

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-05_injecting-punycode-url-within-the-arbitrary-text-via-comment-box-in-google-photo.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `42067ab670022051a35eaa8abb6c98a2c7c67e523fbb38cb0ef7e191af15f7a3`
- Text SHA256: `b8345cf355432dcdb7bce0cdd229236040f84d9517115b0840b182e2306957e3`


## Content

---
title: "Injecting Punycode URL Within the Arbitrary Text via Comment Box In Google Photo Sharing Option"
url: "https://justm0rph3u5.medium.com/injecting-punycode-url-within-the-arbitrary-text-via-comment-box-in-google-photos-sharing-option-8b424065deb3"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
programs: ["Google"]
bugs: ["HTML injection"]
publication_date: "2021-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3677
scraped_via: "browseros"
---

# Injecting Punycode URL Within the Arbitrary Text via Comment Box In Google Photo Sharing Option

Injecting Punycode URL Within the Arbitrary Text via Comment Box In Google Photo Sharing Option
Divyanshu
Follow
3 min read
·
May 5, 2021

20

Definition:

HTML injection is a type of injection vulnerability that occurs when a user is controlling an input point and can inject arbitrary HTML code into a vulnerable web page.
It was possible to inject <a> tag along with Punycode domain and creating the phishing comment thus used by an attacker to attack any person by making the image public.

Press enter or click to view image in full size
Attack Scenario:

The Photo sharing allows comment and photo upload with heart emoticon on the https://photos.google.com/direct/AFxxxxxDqUPppXXXXXXXXXXXrAXXXXXXX. While commenting, it is possible to inject any URL with arbitrary text and it behaves as a hyperlink in the comment. The HTML <a> element (or anchor element), with its href attribute, creates a hyperlink to web pages, files, email addresses, locations on the same page, or anything else a URL can address.
In the Firefox browser, Using this arbitrary content injection along with injecting Punycode URL makes it more impactful.

An attacker can share images/videos with multiple people or it is also possible to create a shareable link. Thus making it available to the public.

This injected text content in the comment can be used to redirect a user to a malicious website by an attacker. There is no warning present due to which it is feasible to phishing attacks. Direct injection of the Punycode domain was not possible as it leads to the removal of the URL completely.

It was possible to bypass the restriction and insert Punycode URL by URL encoding the value.

Also in Firefox, IDN_show_punycode is disabled by default. Which makes it more vulnerable to URL redirection and phishing websites via homograph attack. When a user is clicking there is no warning message that the user will be redirected to the attacker’s (Punycode) domain.

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Payload:

<a href=”https://www.аррӏе.com”>iPhone Black Friday sale</a>
Steps to reproduce:
Visit https://photos.google.com/
Select video/image in photos.google.com
Click on the share option then click on Send in Google Photos.
Enter the name of the user whom you want to share. Also, it is possible to generate a shareable link for viewing.
A public link will be similar to: https://photos.app.goo.gl/ophzhxxxxxxxxxx9
Click on say something and enter the comment. Add URL in the comment like https://google.com or https://www.аррӏе.com (This is the Punycode domain).
Intercept the request via Burpsuite and tamper the value of the URL added. Add arbitrary text (<a> tag) along with any malicious URL, where the attacker wants to redirect.
In the case of Firefox. It is also possible to inject Punycode URL and inject the arbitrary text: Click on the comment to like and view more photos.
Request Body:
f.req=[[[“HF8OLc”,”[[\”AF1Qip6767676767676767r_24-KRiu868NGwdddddddddddddddddddddddddddddddddddddA\”],[[[2,\”mypage\”,null,[\”https%3A%2F%2Fwww.%D0%B0%D1%80%D1%80%D3%8F%D0%B5.com\",\"https%3A%2F%2Fwww.%D0%B0%D1%80%D1%80%D3%8F%D0%B5.com\"]]]],\"ZS1CdDZ6dG8yTFBdddddddddddddYS\",null,null,[],null,\"`comment_0\",null,[[\"AF1QipNMmL5__WEl4ODcdOzFEjOeXQRw\",\"99999277788885631999999999995\"],\"https://lh3.googleusercontent.com/JcxcvcvcvbvvbbbbbbbbbbbbbbbbbbbbbwMT-J3vWAycxxxxxxxxxxxxxxxxxxxxxxxxxxx1H-XZU2A\",null,[\"Demo+App\",1,\"male\",\"justmorpheus\"],[null,null,[]],1,\"\",\"\",[],[],null,[\"https://lh3.googleusercontent.com/a/AATXAJxUjjEGFNSdcXVQ_Y5hhhcZ32-b9L7TZw-SeY4\"],2]]",null,"generic"]]]&at=AP9999999999DfSxzVFVXTRacxcxcxcxcx:16979004365222&

8. Sent the request and check for 200 OK.

Press enter or click to view image in full size
Burp Request On Tampering The Input With Malicious Data

9. Reload the page and hover on the hyperlink created with arbitrary text.

10. In Firefox arbitrary text is shown as an original domain instead of Punycode and once the user clicks on the link. It can be redirected or phished.

Press enter or click to view image in full size
Final Attacker Controlled Image With Punycode
Result:

Google marked the issue as Not-Applicable due to social engineering attack., which is not part of the scope.

Press enter or click to view image in full size
Later it was fixed by Google :P.
Press enter or click to view image in full size
On retesting the issue was fixed.

Ciao, Until Next Time.
