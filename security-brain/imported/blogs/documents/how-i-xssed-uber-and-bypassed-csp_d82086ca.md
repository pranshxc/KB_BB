---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-22_how-i-xssed-uber-and-bypassed-csp.md
original_filename: 2018-09-22_how-i-xssed-uber-and-bypassed-csp.md
title: How I XSS’ed Uber and Bypassed CSP
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- api-security
language: en
raw_sha256: d82086cab1b80ebaecee90ca7834078ac9dca9511586ab684d3a30ac0476d659
text_sha256: e892e50ed3453620c4a0b0d9a79396d6681ae4f441d35b6e5b1ea31eab96f588
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I XSS’ed Uber and Bypassed CSP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-22_how-i-xssed-uber-and-bypassed-csp.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `d82086cab1b80ebaecee90ca7834078ac9dca9511586ab684d3a30ac0476d659`
- Text SHA256: `e892e50ed3453620c4a0b0d9a79396d6681ae4f441d35b6e5b1ea31eab96f588`


## Content

---
title: "How I XSS’ed Uber and Bypassed CSP"
url: "https://medium.com/@efkan162/how-i-xssed-uber-and-bypassed-csp-9ae52404f4c5"
authors: ["Efkan (@mefkansec)"]
programs: ["Uber"]
bugs: ["Reflected XSS"]
bounty: "2,000"
publication_date: "2018-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5685
scraped_via: "browseros"
---

# How I XSS’ed Uber and Bypassed CSP

Efkan
 highlighted

How I XSS’ed Uber and Bypassed CSP
Efkan
Follow
5 min read
·
Sep 22, 2018

1.2K

7

Hi hunters,

Before we start,I’d like to talk about myself a bit.

First of all,I’m not a security researcher/security engineer or anything similar,I’m just a guy who learns new things and who tries to improve himself every day.Due to some school related reasons I couldn’t write any of my findings,but since I’m in some kind of resting period and since I believe “Sharing is caring” it’s time to write about them,I will publish a write-up every week ! My journey started 2 years ago with Uber.But,while I’m not a new person in this bug bounties,I’m definitely a newbie,so maybe my blogs might not be very interesting for experts.Anyway,let’s come to the point.

The Story

I was looking for some open redirect vulnerabilities on subdomains of Uber,I know they don’t see “Open Redirect” as a vulnerability but I thought “Why not chain it with other vulnerabilities ? Maybe it could lead to account takeover or something ? “ My thoughts triggered my ambition.When I was looking for endpoints on partners.uber.com this URL got my interest

https://partners.uber.com/carrier-discounts/att/redirect?href=http://www.wireless.att.com/

I saw this URL in a forum then I found a similar one with a help of Google dorks.Was it vulnerable for open redirect ? Yes ! Then,there was one job to do,find another vulnerability in login section to combine it.I looked for it,really,hours and hours but I wasn’t lucky at all.So there is no need to report it, they say :

“Open redirects. 99% of open redirects have low security impact. For the rare cases where the impact is higher, e.g., stealing oauth tokens, we do still want to hear about them.”

After one week I checked this URL and it wasn’t working,as now,whatever you put to http parameter,it will redirect you to https://www.wireless.att.com

So they fixed it,Did they realize it by themselves or somebody reported it ? I don’t know and I don’t care.But,you know the feeling you are starting with a goal of something big,in the end all you have is a tired, frustrated person.After this,I was upset but triggered second time to find something,and now the time is coming to trigger XSS,not myself !

The Vulnerability

If I would ask “ What are the most known URL’s,links of Uber” to you,probably your answer will be invitation links.You can see these links everywhere,In a forum post,in Twitter,in Facebook,in Instagram…

There are different URL’s for invitation links :

https://www.uber.com/a/join?exp_hvp=1&invite_code=bq6ew1w9ue

I checked this one for XSS but nothing came up :(

https://partners.uber.com/p3/referrals/ms?i=bq6ew1w9ue

What about this one ? It’s the same invite code and if you click you can see that it redirects to other URL,but why not check for other parameters ?

With a help of basic dorks I looked for everything under this subdomain.

site:partners.uber.com

And with this dork you can reach out to a very big list of invite links.My point was to find another parameter and I found one !

https://partners.uber.com/p3/referrals/ms?i=bq6ew1w9ue&m=ANNIVERSARY&v=1

Looks cool,but where is the XSS ? The “v” parameter shows how many years he/she worked as Uber driver,it’s like a celebration of anniversary.As soon as I found this parameter,tried to inject some XSS payload but there was no XSS pop-up,suddenly I checked the source code.

Original Code :

content=”static/images/milestones/anniversary/anniversary_1.png” />

After my payload

content=”static/images/milestones/anniversary/anniversary_1 “><img src=x onerror=alert(document.cookie)>.png” />

As you can see,there was no filtering but in the meantime there was no XSS pop-up,it reminded me Content Security Policy.What is CSP ? As Netsparker’s blog says :

Get Efkan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“ The Content Security Policy (CSP) standard is a way to selectively specify which content should be loaded in web applications. This can be done by whitelisting specific origins, using nonces or hashes”.

So if there will be any whitelisted domains we can try to use them against CSP.Let’s check Uber’s CSP header for partners.uber.com.It’s very long,I will add only the part after “script-src”

script-src ‘self’ ‘unsafe-inline’ ‘nonce-9f4b94bf-a195–4d8c-b474–879ae6d1d471’ ‘self’ ‘unsafe-inline’ https://pullo.uberinternal.com https://apis.google.com https://www.google.com https://d1a3f4spazzrp4.cloudfront.net https://*.uber.com https://rules.quantcount.com https://www.google-analytics.com https://ssl.google-analytics.com https://d3i4yxtzktqr9n.cloudfront.net https://d1a3f4spazzrp4.cloudfront.net;

Firstly,I checked for rules.quantcount.com and looked for json endpoints but there’s nothing much about it.And there’s a huge advantage for us because they whitelisted *uber.com so if we can find any JSON endpoint with callback or anything similar,then we are able to execute XSS.In the meantime,I was reading a blog named “DOM XSS — auth.uber.com”,the guy “stamone” did very good job,and you should read that !

http://stamone-bug-bounty.blogspot.com/2017/10/dom-xss-auth14.html

Check out his write-up,he also bypassed CSP ,how ? In his report CSP was allowing him to get something from *.marketo.com

So he used basic dorks and found out a callback parameter and works great as you can see

Press enter or click to view image in full size

After reading this write-up, I went to Virustotal and checked Uber’s subdomains,one of them got me ! What,mkto ? Is “mkto” the short name for marketo ?!

Press enter or click to view image in full size

YESS! It was.

Go to mkto.uber.com,it will redirect you to “https://app-ab19.marketo.com/index.php”. It is definitely marketo.So now it’s time to use it against CSP.Using a basic payload I created this link and checked,it worked out.

https://partners.uber.com/p3/referrals/ms?i=bq6ew1w9ue&m=ANNIVERSARY&v=1"><script src=”https://mkto.uber.com/index.php/form/getKnownLead?callback=alert(document.domain);"></script>

Press enter or click to view image in full size
This time I triggered XSS !
Timeline

[03–08–2018] Reported to Uber
[07–08–2018] Changed the status to “Triaged”
[22–08–2018] Additional information sent and asked about process
[23–08–2018] Reply from Uber:”Thanks @mefkan! We have passed this information along to the internal team.”
[27–08–2018] Vulnerability fixed
[30–08–2018] Bounty awarded $2,000
[03–04–2018] Limited disclosure on Hackerone

Takeaways

1-Don’t say “This a very known URL,no need to check it for vulnerabilities”.I can guarentee you that you missed a lot of bugs.

2-Always check out for others write-ups,particularly if you’re looking for something special or something detailed.Give your hours for only reading and understanding the logic behind.

3-Never give up,try your best,do your best,you will get what you want at the end.

The End

It was my first write-up folks and as I said I’ll publish another write-up every week.So don’t forget to follow me on Twitter,feel free to share your thoughts or questions with me,and I hope this helps to people like me to improve themselves.

Thank you for reading !
