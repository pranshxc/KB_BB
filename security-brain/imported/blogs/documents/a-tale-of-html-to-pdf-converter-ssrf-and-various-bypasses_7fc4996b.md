---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-29_a-tale-of-html-to-pdf-converter-ssrf-and-various-bypasses.md
original_filename: 2021-04-29_a-tale-of-html-to-pdf-converter-ssrf-and-various-bypasses.md
title: A tale of Html to Pdf converter ssrf and various bypasses
category: documents
detected_topics:
- ssrf
- cloud-security
- idor
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- ssrf
- cloud-security
- idor
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 7fc4996bd41789925d7af90a269159e4a092f15077380a3ad6d16b46de9745d9
text_sha256: 2b270fc259334955b568d81832990a00598a4674cd5af52bbbecc45cc992c726
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of Html to Pdf converter ssrf and various bypasses

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-29_a-tale-of-html-to-pdf-converter-ssrf-and-various-bypasses.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, idor, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `7fc4996bd41789925d7af90a269159e4a092f15077380a3ad6d16b46de9745d9`
- Text SHA256: `2b270fc259334955b568d81832990a00598a4674cd5af52bbbecc45cc992c726`


## Content

---
title: "A tale of Html to Pdf converter ssrf and various bypasses"
url: "https://bughunter25.medium.com/a-tale-of-html-to-pdf-converter-ssrf-and-various-bypasses-4a3e11030c77"
authors: ["Jatin Aesthetic (@techyfreakk)"]
bugs: ["SSRF"]
publication_date: "2021-04-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3695
scraped_via: "browseros"
---

# A tale of Html to Pdf converter ssrf and various bypasses

A tale of Html to Pdf converter ssrf and various bypasses
Jatin Nandwana
Follow
5 min read
·
Apr 28, 2021

262

Press enter or click to view image in full size

Hey hackers, hope you are all doing good in this pandemic, this is a story of a ssrf I found in a private program through the html to pdf converter functionality and was able to read internal files, aws metadata and some internal debug ports with juicy customer information. I will divide the various bypasses and exploitation I found in 3 parts.

SSRF TO AWS KEYS AND SENSITIVE INFORMATION DISCLOSURE

So I started testing the web application and after seeing the pdf converter functionality I quickly tested for some quick ssrf payloads. The application was fetching url from a remote location so I setup a remote http server and stored a html file with below payload and set the parameter ‘source’ to my server url.

<iframe src=”file:///etc/passwd” />

But I was not able to see any response in the converted pdf. Then I poked the parameters a little more and send an invalid url in the parameter source like this ‘dasdad’ and was able to see a juicy error which caught my eyes

Press enter or click to view image in full size

So this error itself is big hint for the next exploitation steps :p

Infact there might be two exploitation ways as we can see Doctype(xxe) as well but xxe was not possible here, I guess they had right protection in the place for it. But html can be sent in the parameter and so I quickly send this payload in the source parameter

source=<html><iframe+src=”file:///etc/passwd”+style=”width:100%;+height:100%” /></html>

And I was able to see the content of passwd file in the converted pdf.

Now most of you will stop here, but I wanted to go more deep so I looked for the users in the passwd file, and read all files of the users in their home directory, in .bash_history file of an user I saw some juicy commands which led me two things one was an interesting port and one was an environment file. The environment file /var/www/<REDACTED>/.env contained the working aws keys of the organization and I could place files , delete files, read customer data , in the organizations buckets. I tried rce as well but it was not working.

and the interesting port was 9192 which was a chrome debugging port. I quickly remembered the h1–415 2020 challenge which I read earlier and it had this chrome debug port in the ctf which contained an interesting endpoint. I quickly went through some writeups and found that endpoint 127.0.0.1:9222/json/list . By default the port is 9222 but in my case it was changed to 9192 but I eventually found it through the .env file :p . Now I sent this payload

source=<html><iframe+src=”http://127.0.0.1:9192/json/list”+style=”width:100%;+height:100%” /></html>

Note : style was used to render the generated pdf properly so that it could fit the page and show the required data on the screen.

And saw the various urls which were thrown by all users in the live pdf conversion application. I was able to see various payment receipts with name,number,addresses,emails , session tokens in url, and it was continuously updating.

I stopped here as I had got enough impact now, I made a report and sent it to the security team. Got a nice bounty $$$$ for it :) So this was the first part.

SSRF BYPASSES

Now after sometime the program fixed the vulnerability and told me to retest. The fix they applied were to block the file:/// protocol and local address like http://127.0.0.1 and http://localhost.

Get Jatin Nandwana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

BYPASS 1

I bypassed the localhost url with this technique http://0.0.0.0:9192/json/list and http://0:9192/json/list , just send this payload in source parameter

source=<html><iframe+src=”http://0.0.0.0:9192/json/list”+style=”width:100%;+height:100%” /></html>

BYPASS 2

They fixed it again by blocking all 0.* and 127.* addresses. I also shared them various bypass techniques mentioned in the awesome swisskyrepo but they somehow missed the alternate IP encoding. This time they disabled the /json/list endpoint in the chrome debug port. So I randomly tried the address 169.254.169.254(which was not working earlier in the first phase!) and to my surprise its ip encoded equivalent worked now and I could fetch their aws keys again. I guess they made the aws meta data accessible or some configuration got messed up during their fix of previous ssrf.

So now my bypasses looked like this

http://2852039166/ - http://169.254.169.254

http://7147006462/ - http://169.254.169.254

source=<html><iframe+src="http://2852039166/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role"+style="width:100%;+height:100%;"></iframe></html>

In this manner I was able to bypass the ssrf protection. The next fix they made was very secured , I tried a hell lot of bypasses like the dawgyg ssrf trick and many other tricks but none of them worked.

SECOND SSRF

Now after the source parameter got fixed, I looked for other parameters and one more parameter which took my attention was header[source]. This was used to add any remote hosted image on the header of the pdf generated. I tried for the aws metadata and was able to access the aws keys again with this .

&header[source]=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role&header[height]=111

Note : Height was used to render the generated pdf properly so that it could fit the page and show the required data on the screen.

They applied all the fix of the first ssrf to this one as well and made it super secured and awarded a nice bounty $$$ for both 2nd and 3rd one combined.

Key Takeaways :

Always try to escalate a local file read by doing proper enumeration like seeing all the files of the users, conf files, .bash_history files etc.
Keep reading and reading other articles and ctf challenges . If I dont knew about the h1 ctf which included chrome debug port with /json/list endpoint I cant show them impact about the users info leakage.
If their is a fix applied, always try to bypass it.

I want to thank Harsh manas for the proofreading, thank you bro :)

Thats it .If you like the article please share it with your friends. I have some more pending writeups which I will publish soon here so make sure you follow me on twitter where I will keep updating :)

Twitter : https://twitter.com/techyfreakk

If any recruiters reading this, I am also available for any position of web application pentesting or network pentesting, you can dm me on twitter.

Stay safe, wear a mask :)

Thanks
