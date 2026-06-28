---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_hacking-admin-panel-getting-free-subscription.md
original_filename: 2023-03-29_hacking-admin-panel-getting-free-subscription.md
title: Hacking Admin Panel & Getting free subscription
category: documents
detected_topics:
- access-control
- jwt
- command-injection
tags:
- imported
- documents
- access-control
- jwt
- command-injection
language: en
raw_sha256: 03c845d9f7d221e3daf5f25048864cc84dfd045959ac4398f5fcea05555a3052
text_sha256: 5558a345990c32258b3fede7e3d3aac1ce54b0d34ed508a5c03277a34453526a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Admin Panel & Getting free subscription

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_hacking-admin-panel-getting-free-subscription.md
- Source Type: markdown
- Detected Topics: access-control, jwt, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `03c845d9f7d221e3daf5f25048864cc84dfd045959ac4398f5fcea05555a3052`
- Text SHA256: `5558a345990c32258b3fede7e3d3aac1ce54b0d34ed508a5c03277a34453526a`


## Content

---
title: "Hacking Admin Panel & Getting free subscription"
url: "https://z-sec.co/hacking-admin-panel-getting-free-subscription"
final_url: "https://z-sec.co/hacking-admin-panel-getting-free-subscription"
authors: ["Zeeshan Mustafa (@by6153)"]
bugs: ["Exposed registration API", "Privilege escalation", "Account takeover"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1325
---

# Hacking Admin Panel & Getting free subscription

UpdatedJanuary 16, 2026

•4 min read•[ __View as Markdown](/hacking-admin-panel-getting-free-subscription.md)

![Hacking Admin Panel & Getting free subscription](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1768597162191%2F40c03813-3536-4e11-b990-4d6446737ace.png&w=3840&q=75)

[ Z](https://hashnode.com/@zsec)

[Zeeshan M.](https://hashnode.com/@zsec)

[__](https://twitter.com/@by6153)[__](https://www.linkedin.com/in/zeeshanm0x0/)

[__Part of series Writeups](/series/writeups)

On this page

Another methodHTTP request and API URLTakeaways &amp; recommendations

Note: For maintaining the program's privacy I won't disclose the program.

So, a few months back [I](https://www.linkedin.com/in/zeeshanm0x0/) and [Haseeb](https://www.linkedin.com/in/haseeb-tofiq/) were hunting on a private program and the program is a services-based company that has paid services only. So the program had very limited assets in scope and most of them were redirected back to the main domain then we used the main domain and checked every functionality we tried every possible way to manipulate the payment method to get the subscription free of cost and we were able to get the services free of cost by providing negative value but due to bad luck someone had reported this before us and it was marked as duplicate. So getting duplicate motivated us to dig deeper instead of de-motivating and this time we were confident enough that we could get critical vulnerability.

By changing our hunting methodology we focused on this program in the opposite way we collected their in-scope assets and then saved them in a txt file as url.txt and ran "[x-officers.py](https://github.com/zeeshanm0x0/x-officers)" script to quickly collect js files and then search for custom words in those js files luckily we found a dev portal which was "29dev-api-x.target.com" note 29 is not the exact number [😛](https://emojipedia.org/face-with-tongue/) after visiting the URL it prompts us with a login page and after checking their js files we found a registration API and we successfully registered an account via the API with defined parameters. After a successful login, we had access to their developer portal but it had very few functions not very useful according to my experience I felt that there would be an admin panel with lots of working functions so the next step was to find the admin panel. I love FFUF since it's very handy in terms of fuzzing so we found "qa-admin-api.target.com" with a status code of 301 which was redirecting back to the login panel with curl.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1680125544680/a860996f-e993-418d-bdde-4c6af782aabe.png)

But as we were authenticated inside "29dev-api-x.target.com" our session was valid for the admin panel too because of the Authorization header which contained our JWT by the way we found multiple JWT issues but I won't cover that in this article. But we faced another issue "Access Denied" there were several menu none was working because we were not an admin our account was from the developer portal, not an admin account. In the incognito window, we opened the admin panel which prompts us with a login panel and we started to analyze the js files I was hoping for registration API and we could find any mentioned API.

On the authenticated admin panel window I opened chrome's developer tools and in the application tab I was checking the cookies section was had some rubbish and useless parameters and their values not useful but after checking the Local Storage section I found the GEM there were some parameters like "currentuser" and "current_user_role" now the fun parts begin, as it's visible in the below screenshot that the "currentuser" parameter has my account's details and the "current_user_role" has the value of "IsAdmin:false" means my role was not admin role by changing the "IsAdmin:false" to "IsAdmin:true" and refreshing the page I was able to use the admin panel so I escalated my privileges to admin then we browsed all the pages and options and then found the subscription section and we were able to enable paid services for our account on "target.com" and to delete other user's subscription and do other malicious things. Wink Wink

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1680124996414/7c973218-a429-47d2-98b9-d39c322e27b3.jpeg)

## Another method

I guess some of you might think that why we didn't try to register an account on the admin panel with the previously found API URL you are right after performing the above trick we tried to register an account on the admin panel with the same API path and parameters and by adding another parameter "admin" to true.

### HTTP request and API URL

**Developer portal:**

POST /api/user/register HTTP/1.1

Host: 29dev-api-x.target.com

user-agent**:** Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36

Content-Type: application/json

{"username":"test1337","email":"qjimyhwekglh@mymail.com","fname":"george","lname":"frankmiller","password":"Test@123$"}

**Admin Panel:**

POST /api/user/register HTTP/1.1

Host: qa-admin-api.target.com

user-agent**:** Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36

Content-Type: application/json

{"username":"test2","email":"email@email.com","fname":"george","lname":"frankmiller","password":"Test@123$", "admin":"true"}

**FFUF command:**

ffuf -u https://FUZZ.target.com/ -w /usr/share/wordlists/SecLists/Discovery/DNS/dns-Jhaddix.txt

## Takeaways & recommendations

1: Use the application as a normal person and observe all the functionalities.

2: If you get any subscription section do a test for price manipulation with every possible method.

3: Don't get de-motivated if your submission gets duplicated or if you don't find any vulnerability it's a part of this game.

4: Always try at least two different methodologies for hunting your target program.

5: Analyze JS files you never know what's in there so keep your eyes on every JS file.

6: Always test for parameters like admin or role or priv and give admin as value most of the time it works and you can register an admin account.

7: Check for parameters like "isadmin" or other similar things and changing their value to the opposite of that value.

8: Link of [X-Officers.py](https://github.com/zeeshanm0x0/x-officers)

[#hacking](/tag/hacking)[#admin-panel](/tag/admin-panel)[#bugbounty](/tag/bugbounty)[#bugbountytips](/tag/bugbountytips)[#hackerone](/tag/hackerone)
