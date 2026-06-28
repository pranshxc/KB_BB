---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-03_from-a-500-error-to-django-admin-takeover.md
original_filename: 2020-11-03_from-a-500-error-to-django-admin-takeover.md
title: From a 500 error to Django admin takeover
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- rate-limit
- mobile-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- rate-limit
- mobile-security
language: en
raw_sha256: 59997d5336ec85227bb0c9bcf3a3671100a8ba93a984b676118fb2ed8f8de149
text_sha256: 2ee26aed099572d3446a4f527e2456a0190fb09909e268857910765f3d8b342e
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# From a 500 error to Django admin takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-03_from-a-500-error-to-django-admin-takeover.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, rate-limit, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `59997d5336ec85227bb0c9bcf3a3671100a8ba93a984b676118fb2ed8f8de149`
- Text SHA256: `2ee26aed099572d3446a4f527e2456a0190fb09909e268857910765f3d8b342e`


## Content

---
title: "From a 500 error to Django admin takeover"
page_title: "Shashank's Security Blog: From a 500 error to Django admin takeover"
url: "https://blog.shashank.co/2020/11/from-500-error-to-django-admin-takeover.html"
final_url: "https://blog.shashank.co/2020/11/from-500-error-to-django-admin-takeover.html"
authors: ["Shashank (@cyberboyIndia)"]
bugs: ["Authorization bypass", "Account takeover"]
bounty: "3,000"
publication_date: "2020-11-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4159
---

This bug is about a private target I was hunting. I passed all the subdomains to [FFUF](https://github.com/ffuf/ffuf), a great tool written in GoLang to brute force directories. 

Since there were no interesting 200 responses against my wordlist. I started checking other responses like 302, 403, etc. 

I noticed one of the subdomains (let that be sub.vulnerable.com) gave a 500 error for the endpoint 

/api-docs/

  

This was interesting because when tried an endpoint /anything, it returned 404. So I was quite sure that /api-docs existed but needs more privileges or something like that...

I tried lots of methods, but nothing worked. So I just went back to test the main application. I signed up, and I had an intuition to refresh the page in the next tab, which was /api-docs/

PFFF, to my surprise, I could see the API docs now, which was a swagger UI. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwNRorXEKj73HQSsrecxNqbwM53ZCXAV6HSutb4c7kyveI6MhgCIdkFYXZMzEXSzzLpVm2IFlXEUVMS6_A7I9Z0kl97Y_c1wgbgfE5qf0tqryRf66jfD9iC053TlgprPPxhuohC8L_eVkT/w640-h108/Screenshot+2020-10-08+at+12.58.17+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwNRorXEKj73HQSsrecxNqbwM53ZCXAV6HSutb4c7kyveI6MhgCIdkFYXZMzEXSzzLpVm2IFlXEUVMS6_A7I9Z0kl97Y_c1wgbgfE5qf0tqryRf66jfD9iC053TlgprPPxhuohC8L_eVkT/s2874/Screenshot+2020-10-08+at+12.58.17+AM.png)

  

I after seeing the admin-api, I thought I had hit a goldmine. But that was not the case. None of the admin-API's were working. So I started looking at the normal API endpoints. 

  

Two of the endpoints were interesting:

1\. /api/panel/v1/users/{id}/

Where the {id} value is an integral value. I automated the request for 1 to 100 numerical values, and I was able to fetch other user's email addresses, DOB, name, etc. by filtering all 200 responses.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjzEFHG9ezjurkZkh_Be5_Lk7RaRx2uWkOfLtw3oq97f4s0Dgvn0ms_u-AYboOpetoMTNEka5jasvHFfNm7d92ODu5CtkG-sSid1EswGC6dUV5PbYfwIb3l3Ev6aHuGTihuQiopyMFB1hn/w640-h190/Screenshot+2020-10-08+at+1.06.49+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjzEFHG9ezjurkZkh_Be5_Lk7RaRx2uWkOfLtw3oq97f4s0Dgvn0ms_u-AYboOpetoMTNEka5jasvHFfNm7d92ODu5CtkG-sSid1EswGC6dUV5PbYfwIb3l3Ev6aHuGTihuQiopyMFB1hn/s1676/Screenshot+2020-10-08+at+1.06.49+AM.png)

  
2\. A similar endpoint and similar leak with search functionality

> /api/panel/v1/users/?page=1&page_size=1&search=cyberboy

  

I reported the bug, and the team asked me if I could raise the severity. 

Challenge accepted!

  

I started digging the endpoint again /api/panel/v1/users/{id}/

and notice a JSON value in response "is_staff:false"

So it is pretty easy to guess that there are different roles for the website. I wanted to know more about the roles, so I thought of looking at the admin account's privileges, and they would-be some developers of the company. It was easy to find the developers' names in public places and then pass the name to the search API and fetch their data if I get lucky.

So when I did this, one of the names worked, and I got an admin account information.

> /api/panel/v1/users/?page=1&page_size=1&search=NAME_OF_A_DEV_I_KNEW

  

Now I have a few more interesting roles. 

> "is_superuser":true
> 
> "is_staff":true
> 
> "lms_role":"super_admin"

  

But again, how do I access an admin account. I tried and failed. So I thought, what if I am modified to these privileges. The first thing I tried was making a POST request with the above JSON value to my own ID

  

  

> > POST /api/panel/v1/users/{id}/ HTTP/1.1
>> 
>>  
> 
>> 
>> {
>> 
>> "is_superuser":true
>> 
>> "is_staff":true
>> 
>> "lms_role":"super_admin"
>> 
>> }

  

Unfortunately, a 500 error.

  

The next thing would be to try the PATCH method. 

  

> > PATCH /api/panel/v1/users/{id}/ HTTP/1.1
>> 
>>  
> 
>> 
>> {
>> 
>> "is_superuser":true
>> 
>> "is_staff":true
>> 
>> "lms_role":"super_admin"
>> 
>> }

  

I got 200, okay. 

  

I logged into my account, and I was a staff and a superuser who could edit and modify contents. 

  

My curiosity did not stop so, I searched for "lms_role" turns out; it's a learning management system and had something to do with Django. So I just opened /admin. And I was greeted with welcome "Cyberboy."

  

Here we go.. I am the admin now :)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd-9eATgdzxusBh7IauS3ceZRpGGfyO7bDEnk6lyRKsz0Auk8ONlkVdZ2o39kfgN5ISin0r2mxfc8CvBUeB38mHzPNLJoOcphbLRHKzxOLZwRyyEU8mf1DS63j-0ESfQJIazDsauj1dVdX/w640-h58/Screenshot+2020-10-08+at+1.22.59+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd-9eATgdzxusBh7IauS3ceZRpGGfyO7bDEnk6lyRKsz0Auk8ONlkVdZ2o39kfgN5ISin0r2mxfc8CvBUeB38mHzPNLJoOcphbLRHKzxOLZwRyyEU8mf1DS63j-0ESfQJIazDsauj1dVdX/s2558/Screenshot+2020-10-08+at+1.22.59+AM.png)

  

  

Mission accomplished!

I informed the team that I would like to stop here, and they agreed. 

  

Bounty reward 3000$
