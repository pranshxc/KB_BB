---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-23_how-i-found-multiple-bugs-on-facebook-in-1-month-and-a-part-for-my-methodology-t.md
original_filename: 2021-07-23_how-i-found-multiple-bugs-on-facebook-in-1-month-and-a-part-for-my-methodology-t.md
title: How I Found Multiple Bugs On FaceBook In 1 Month And a Part For My Methodology
  & Tools
category: documents
detected_topics:
- xss
- cloud-security
- access-control
- sqli
- command-injection
- mfa
tags:
- imported
- documents
- xss
- cloud-security
- access-control
- sqli
- command-injection
- mfa
language: en
raw_sha256: 37b8ac2fe42453721157770bf6f1bdd85969a3714a288c21142b3f2207909a8b
text_sha256: f2b516800ed787d504146475df58c61fd6da3141ab841b6df9e4d7795c13b2c3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: true
---

# How I Found Multiple Bugs On FaceBook In 1 Month And a Part For My Methodology & Tools

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-23_how-i-found-multiple-bugs-on-facebook-in-1-month-and-a-part-for-my-methodology-t.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, access-control, sqli, command-injection, mfa
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: True
- Raw SHA256: `37b8ac2fe42453721157770bf6f1bdd85969a3714a288c21142b3f2207909a8b`
- Text SHA256: `f2b516800ed787d504146475df58c61fd6da3141ab841b6df9e4d7795c13b2c3`


## Content

---
title: "How I Found Multiple Bugs On FaceBook In 1 Month And a Part For My Methodology & Tools"
url: "https://orwaatyat.medium.com/how-i-found-multiple-bugs-on-facebook-in-1-month-and-a-part-for-my-methodology-tools-58a677a9040c"
authors: ["Orwa Atyat (@GodfatherOrwa)"]
programs: ["Meta / Facebook"]
bugs: ["SSTI", "SQL injection", "Authentication bypass", "Privilege escalation", "Reflected XSS"]
publication_date: "2021-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3484
scraped_via: "browseros"
---

# How I Found Multiple Bugs On FaceBook In 1 Month And a Part For My Methodology & Tools

Orwa Atyat
 highlighted

Top highlight

How I Found Multiple Bugs On FaceBook In 1 Month And a Part For My Methodology & Tools
Orwa Atyat
Follow
6 min read
·
Jul 22, 2021

2.6K

9

Hay Hunters , Hello Infosec Community

Iam Orwa [https://twitter.com/GodfatherOrwa]

this my 2nd writeup, the first one is about Full Map To Github Recon And Leaks Exposure , seen many people getting hall of fames and bounties from Facebook , Aditi Singh Smart Girl these girl who motivated me to work on this program [https://twitter.com/aditi_singghh]

As you see in the title In these Write up i Will Speak about How I Found Not What I Found

What matters to me here is for the reader to learn

So I will talk about all my discoveries in FaceBook and a part for my methodology

duplicate and accepted

before starting
Everything was done in cooperation with HackerX007
He is a very smart and creative person. I suggest everyone to follow him [https://twitter.com/XHackerx007]

also HackerX007 on bugcrowd Leaderboard rankings Top 10 on P1 , Top 100 on Full Ranking

A: What The Multiple Bugs That found

1 Server-Side Template Injection To RCE (Critical)

2 SQL Injection [2] (Critical)

3 Authentication Bypass(Critical)

4 Privilege Escalation (Critical)

5 Multiple Reflected XSS (Medium)

B: Tools And Extensions You Need it

1 FFUF Or Dirsearch i Like Both

2 Good Word list for me i like to use the legend Random Robbie Word list https://github.com/random-robbie/bruteforce-lists

3 Amass For Sub domain i also check on github for sub domains also you can fuzz for sub domain by using good wordlist the good command that i use for Amass

For List of domains==> amass enum -passive -norecursive -noalts -df list-domains.txt -o subs.txt
For Senile domain==> amass enum -passive -norecursive -noalts -d domain-o subs.txt

4 Httpx and httprobe And Nmap

cat subs.txt | httpx -o live-subs.txt
cat sub.txt | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -p https:10000 -p http:9000 -p https:9443 -c 50 | tee live-subs2.txt

5 Wappalyzer Extensions

6 Burp Pro With These Extensions

Collaborator Everywhere
XSS Validator
Wsdler
.NET Beautifier
Bypass WAF
J2EEScan
Param Miner
Wayback Machine
JS Link Finder
Upload Scanner
Nucleus Burp Extension
Software Vulnerability Scanner
Active Scan++

7 Acunetix Scanner or If you Looking for something free and cool [reNgine]

C: How I Found Multiple Bugs
1 on First Domain

SQL Injection [2] & Authentication Bypass & XSS [2]

Started My Recon By Checking For Some Cool domains by Dorking for Facebook page on Github **Dorking to Find domains and some cool ends

So what that dorks i try

org:facebookresearch ftp
org:facebookresearch Ldap
org:facebookresearch https://
finely after about 30 min dorking last dork i still remmber

org:facebookresearch language:python .php

i get luck to found some interesting End it was

domain/login/_ajax/verify-2fa.php

When i Visit these Domain its Employee Panel It is owned by Instagram

directly Start Looking for SQL testing query 1' Error back with `MySQL' so now its look Parameter usernamevulnerable

so on burp intercept request and make a copy in txtfile

On Sqlmap i run these Command

sqlmap -r request.txt -p username --dbms="MySQL" --force-ssl --level 5 --risk 3 --dbs --hostname

and BooM its done

So after that i `Spider` the Full host and and fuzz for `php` using php word list and after that Active Scan on Burp for ALL the Post Request

`Keep the Maximum insertion pointe per base request 10`

What i found

another SQL
2 XSS payload
"><img src=x onerror=alert(1)>

SQL Close as duplicate because The Security testing know about that and they work to fix it also Xss 1 duplicate and 1 accepted

Here HackerX007 He messed around a bit
as he also an artist with manual Testing Found a vary Cool Authentication Bypass
Authentication Bypass That Allow Unauthenticated User To Take Actions
When visit domain/location/?5 
you will redirect to login page
but on brup when visit one 
will redirect but the Content-Length of redirect response so big 6443
After looking in the response he found out in this 302 response, the panel was without any Authentication. in the 302 response content
so 
after some playing with burp match and replace It was able to bypass Authentication and taking some actions.
at first i was think its just front-end bypass , But i found out i can take action, like enable ,un enable Bucket
#Repro Steps
1. IN burp match and replace add this:
type: response header
match : HTTP/1.1 302 Found
replace: HTTP/1.1 200 ok
__
type: response header
match : Location: ../login/?redirect=//location/?5
replace:
2. now go to domian//location/?5
BooM
4. when you done you can [Logout] 😂

these Authentication Bypass accepted

2 SHODAN IP And SSTI To RCE

Started recon for Ip belongs for Facebook

Get Orwa Atyat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

the good dork you can use in these case

if you looking for domains or Ip belong for program

Org:"FaceBook Inc." without 200 dont need live Ip in these case

if you looking for cool subs or Ip on the domain

Ssl.cert.subject.CN:"facebook.com" 200

so found a interesting Ip that include prot 10000 but not working

so i scan that Ip on Nmap Nmap -sV ip

its show Port 8443 Open

when i check it [ its a AWS host owned by Facebook]

now i collect lot of Ip like these and send them to scan on Acunetix to run in background

after about 1 hour back to check on Acunetix its show these Ip vulnerable with SSTI and payload was set in parameter mode that call debug in python so i try the normal payload {{5*5}} so found in source 25 the easy and fast way here to check use tplmap tool its similar for sqlmap to install

git clone https://github.com/epinna/tplmap.git

after testing these parameter its show its vulnerable with SSTI

so my command was

./tplmap.py -u "https://ip:8443/consent?assignmentId=debugKUymD&hitId=debugiwTmj&mode=debug*"

===>

GET parameter: mode
Engine: Jinja2
Injection: {{*}}
Context: text
OS: posix-linux
Technique: render

what make my happy here that

python code evaluation is Ok

that mean i can

execution command on shell 
and 
Bind and reverse shell
and
File write and read 
but not in all the cases 

so what i need only connect on shell

./tplmap.py -u "https://ip:8443/consent?assignmentId=debugKUymD&hitId=debugiwTmj&mode=debug*" --os-shell  

only check id and ping burp

BooM

these SSTI accepted

3 Privilege Escalation

here i visit crt.sh to tack about 5 interesting domains

https://crt.sh/?q=Facebook+Inc.

but for subdomains gathering i dont wanna the normal way

i fuzz for sub domains with a good and big word list i made it

you can also made one for you

after that filtered to Live using httprobe

cat sub.txt | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -p https:10000 -p http:9000 -p https:9443 -c 50 | tee live-subs2.txt

so found here domain run on Port 10000

so when i visit it was a interesting panel for mange servers and lot of other things

so when check on its run with lot of technologies

dirsearch on the panel and waw misconfiguration that some endpoints is accessible without any login ok its cool find to report but still

without any Privilege like edit , del , add etc..

so i need to keep working to find something good

i also try login with some default Credentials but not working also try to sing up but the register cant be without login using admin Credentials
by check on some endpoints i found server Info with that info full name of the admin who create that

so its take 5 min to find that employee repo on github

so start dorking on employee repo for any password

i try

password
passwd 
pwd
pass
pw
login

found internal host and user and password github leak like these

$host = ************
$User = ************
$pwd=***REDACTED***

scanned the internal host for ports nothing open

so i try to login use the username and the password and BooM 😎🥳 its work with Full Privilege

after Login i can

Full Access and Control
add users
del users

Etc...

also 1 stored XSS in these panel 😎

I Hope you guys have enjoyed the Reading

and hope you learn and found bugs and tweet by that for me that will make my happy

Stay safe dears

Iam not Good in Writes up If there are spelling mistakes please avoid

The biggest Lie
when they told: it’s not simple
if someone telling you it’s not simple 90% will give up

everything simple in these life
its just need 2 things
1- no matter what happens ==> Never Ever give up

2- Arrange your work Arrange your life Arrange your time
Do not work in any field in life in a random way

Thanks all

https://twitter.com/GodfatherOrwa

orwagodfather on Bugcrowd
Bugcrowd's bug bounty and vulnerability disclosure platform connects the global security researcher community with your…

bugcrowd.com

HackerOne profile - mr-hakhak
hacker-gamer-cooker -

hackerone.com

Dont forget also Follow HackerX007 I suggest everyone to follow him

https://twitter.com/XHackerx007
