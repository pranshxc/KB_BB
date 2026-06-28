---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-13_how-i-bypassed-ebay-process-on-redirect.md
original_filename: 2018-04-13_how-i-bypassed-ebay-process-on-redirect.md
title: How I bypassed Ebay process on redirect
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 867fbe6d2af246c1a8c7a5ba8ff4eeee62c65bf51764a30cfac703435037cafd
text_sha256: 191b60a50c2622fb4a249ee59290f797e8104053a1ade6c528b117d38380bbe9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed Ebay process on redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-13_how-i-bypassed-ebay-process-on-redirect.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `867fbe6d2af246c1a8c7a5ba8ff4eeee62c65bf51764a30cfac703435037cafd`
- Text SHA256: `191b60a50c2622fb4a249ee59290f797e8104053a1ade6c528b117d38380bbe9`


## Content

---
title: "How I bypassed Ebay process on redirect"
url: "https://medium.com/@flex0geek/how-i-bypassed-ebay-process-on-redirect-98739384b4bc"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
programs: ["Ebay"]
bugs: ["Open redirect"]
publication_date: "2018-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5921
scraped_via: "browseros"
---

# How I bypassed Ebay process on redirect

How I bypassed Ebay process on redirect
Mohamed Sayed
Follow
2 min read
·
Apr 13, 2018

75

2

hey guys this is my first blog so be free to comment any suggestion to improve my blog in the next time.

Ebay is a web application like Amazon to buy or sell some thing on it should has more security to save the users information because the website has a sensitive information.

So i started testing the site and when i enter my account to log in i notice tat in the GET request (in the link) the the website redirect me after the login so i tried to change the host to another one but it’s not work so i started looking for a bypass for this filter so i enter the link like that http://ebay.com@google.com but unfortunately it’s not work.

So i don’t give up and tried to bypass it again so i add the link like that http://test.ebay.com/ so it’s work and i redirected to ( test.ebay.com ) but it’s not open redirect but it’s helped me a lot now I can redirect the user to a subdomain so in this time thinking about how i can make this useful for me and i enter this URL in the redirect http://google.com.ebay.com/ and it’s redirected me to ( google.com.ebay.com ) and i notice that if i add a character with URL-encode it’s will decoded so i think if i can make a part of the URL commented it’s will redirected to the other part and the ebay process on redirect it’s the ebay domain should be in the redirect so in this time i thinking how i can comment the last part which include the ebay domain and i got it and add this ( # ) after the host which i want to redirect the user to it but when i enter it with out URL-encode it’s will not work so i add it in this form (%23) and the last URL is http://google.com%23.ebay.com/ and Booom it works and i was so happy.

Get Mohamed Sayed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This bypass works in any redirect in Ebay but when i send it i got duplicate so in this time i was sad ~_~

the message from Ebay security team

Press enter or click to view image in full size

this is how i bypassed the Ebay process on redirect,

Thanks for reading.
