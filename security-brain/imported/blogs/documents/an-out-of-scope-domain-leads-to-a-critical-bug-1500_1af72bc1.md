---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-24_an-out-of-scope-domain-leads-to-a-critical-bug1500.md
original_filename: 2022-06-24_an-out-of-scope-domain-leads-to-a-critical-bug1500.md
title: An Out Of Scope domain Leads To a Critical Bug[$1500]
category: documents
detected_topics:
- access-control
- csrf
- api-security
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- access-control
- csrf
- api-security
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 1af72bc109ed2fdf6b5571e2af672649c203e8bbff7387f4b16518d5c5182a09
text_sha256: 81884df26b9be8f62fbb31d2cfb91d250ef6e37864a4a567effb6b0892d04115
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# An Out Of Scope domain Leads To a Critical Bug[$1500]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-24_an-out-of-scope-domain-leads-to-a-critical-bug1500.md
- Source Type: markdown
- Detected Topics: access-control, csrf, api-security, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `1af72bc109ed2fdf6b5571e2af672649c203e8bbff7387f4b16518d5c5182a09`
- Text SHA256: `81884df26b9be8f62fbb31d2cfb91d250ef6e37864a4a567effb6b0892d04115`


## Content

---
title: "An Out Of Scope domain Leads To a Critical Bug[$1500]"
url: "https://medium.com/@shakti.gtp/an-out-of-scope-domain-leads-to-a-critical-bug-1500-f228d2c7db4b"
authors: ["Shakti Mohanty (@3ncryptSaan)"]
bugs: ["Broken authorization", "Broken Access Control"]
bounty: "1,500"
publication_date: "2022-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2520
scraped_via: "browseros"
---

# An Out Of Scope domain Leads To a Critical Bug[$1500]

An Out Of Scope domain Leads To a Critical Bug[$1500]
shakti mohanty
Follow
5 min read
·
Jun 24, 2022

320

3

Hello All, I am Shakti Ranjan Mohanty (3ncryptsaan). Hope all are having a good day. In this write-up, I will be sharing how I have found a critical bug from a place that is not in scope. Feedback Is appreciated.

Often I don’t post writeups for bugs that don’t have any uniqueness, because being a writer I always prefer posting such findings which will be unique and informational. As I Got lots of comments and dm for this writeup, here it is.

Being a penetration tester and bug hunter, I always prefer targeting and hunting in one program until I feel I am done with finding bugs out there. I have been testing one program for the last 1 month and also found a lot of bugs. I got too much familiar with all the functionalities. The major thing here is only app.domain.com is in scope and all other domains with *.domain.com are out of scope. I tested everything there, I was thinking I am done testing that app. But somewhere I wanted to test there more. While testing I observed one API endpoint having a request

GET /app/target/configuration HTTP/1.1 
Host: app.target.com
X-Csrf-Token: value
Cookie: value

By removing that x-csrf-token header we can still access the information for /app/target/configuration. That means the cookie is the only thing that is responsible for the authentication here.

I tried for other bugs like CORS and CSRF but failed. I kept note till this and moved on to test further.

On the next day, I reminded one domain that is booking.target.com

before that let me brief the main application functionality.

The application manages created jobs and This job creation can be done via two method ,

Either Being an organizational owner, you can create job and assign them to your employee and this will be reflected on https://app.target.com/app/jobs

or

there is a feature for online booking on the application, which will generate a unique url like https://booking.target.com/comany-name/some-hashed-value. This url will be available automatically for public on yourcompany.target.com with a button online booking. Through this anyone visting yourcompany.target.com(available for public) can request a new job and that will be reflected on https://app.target.com/app/jobs too.

Both Yourcompany.target.com and booking.target.com are out of scope. But still i thought and questioned myself how the job request submitted from booking.target.com is getting stored and reflected on the main app i.e. https://app.target.com/app/jobs , For clearing that confusion , being a normal visitor user I have navigated to “online booking” (https://booking.target.com/comany-name/some-hashed-value) and created a job request. This will initiate a POST request and The request was

POST /company/add_scheduled_job_for_user HTTP/1.1
Host: booking.target.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0
Content-Type: application/x-www-form-urlencoded;charset=utf-8
Authorization: Token token=xxxxxxxxxxxxxxxxxxxxxxxxxxx
Content-Length: 1179
DNT: 1
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
name=sds&street=sss&street_line_2=ss&city=ss&state=ss&postal_code=12222&mobile_number=700-897-8755&email=shakti.gtp1@gmail.com&scheduled_end_time=&scheduled_start_time=&services[0][organizational_line_item_template_id]=43660983&services[0][name]=Custom+Job&services[0][description]=company+will+provide+you+a+quote+if+the+work+you+need+does+not+fit+into+one+of+our+standard+categories.Please+provide+as+much+detail+as+possible,+including+pictures.&services[0][default]=false&services[0][amount]=$0.00. 

Wow!!! things to be noted here. The “Authorization: Token token=xxxxxxxxxxxxxxxxxxxxx” used for online booking is being used as a form of authentication for requesting a new job on that organisation. That means the Authorization: Token got from booking.target.com must have some corelation with app.target.com

So can we use that “Authorization: Token token=xxxxxxxxxxxxxxxxxxxxxxxxxxxx” to access other authenticated data or perform any state changing function for that organisation. The ans is a Big Yess…..

To confirm first i have initiated a request to /app/target/configuration endpoint by using that Authorization: Token

GET /app/target/configuration HTTP/1.1 
Host: app.target.com
Authorization: Token token=xxxxxxxxxxxxxxxxxxxxxxxxxxxx

Hollaaa, The request got successful and i was able to view the configuration data for the respective organisation and i was viewing it from an anonymous user without log in.

Then i have checked all other functionalities and found that being a normal non logged-in user i can use “Authorization: Token token=xxxxxxxxxxxxxxxxxxxxxxxxx” which i got from online booking request, i can do a lots of more thing like getting employee list, Deleting or restoring existing employee, getting invoice settings, getting organisational profile, getting all job list, getting customers , creating customer/creating jobs etc and etc.

REPRODUCING THIS BUG:

1- Being an anonymous user navigate to target organisation’s online booking url https://booking.target.com/comany-name/some-hashed-value. This is meant for public which will be helpful for getting new jobs from the website, the organisation which are on paid plan often uses this feature and avail the link on their business website ).

Get shakti mohanty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2- Now while creating a booking capture the request and note the “Authorization: Token token=xxxxxxxxxxxxxxxxxxxxx”

3- All you need to use the above “Authorization: Token token=xxxxxxxxxxxxxxxxx” value in all the API endpoints you want to access for that organisation. This will replace the need of x-csrf-token and cookie.

To access employee list of that victim organisation

GET /app/organization/employees?expand[]=reviews&expand[]=device_info&expand[]=permissions HTTP/1.1
Host: app.target.com
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36
Authorization: Token token=xxxxxxxxxxxxxxxxxxxx

From the response you can gain all the employee data including their id, email, name etc. As you have the employee id you can delete that employee by using the Authorization: Token from online booking.

To delete employee

DELETE /app/organization/employees/zzzzzzzzzzzzzzzz HTTP/1.1
Host: app.target.com
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36
Authorization: Token token=xxxxxxxxxxxxxxxxxxxx

Like the above two examples you can do everything( access/create/delete customers, access/create/delete jobs, access/create/delete invoices etc) what an admin of that organisation can do.

ISSUE BACKGROUND:

The online booking request done from booking.domain.com has one form of authentication that is Authorization: header, As this token is responsible for creating jobs, mistakenly the developers gave the token read write permissions globally for all endpoints. As a result any one with the token from online booking can access/add/delete anything from that respective organisation.

IMPACT:

As the online booking is available for each organisation publicly, the online job creation for each organisation will have a respective Authorization: Token token=xxxxxxxxxxxxxxxxxxxx and as this is public it will take less than a minute for an attacker to get any organisation’s Authorization: Token. So an unauthenticated user without login or without being a member can Taking over control of any organisation for changing data, creating data, editing AND ACCESSING data, more over deleting administrative users or restoring deleted users.

Reported: Jun 4th (20 days ago)

Severity as per CVSS: Critical (9.7)

Triaged : Jun 9th (15 days ago)

Rewarded: $1500 Jun 9th (15 days ago)

Press enter or click to view image in full size

Resolved: 22 Jun (2 days ago)

Follow me for more write-ups and information sharing, I will be happy to share my knowledge and my DMs are always open for the genuine help seekers.

Instagram: https://www.instagram.com/3ncryptsaan/

Twitter: https://twitter.com/3ncryptSaan

Linkedin: https://www.linkedin.com/in/shakti-ranjan-mohanty/
