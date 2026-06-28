---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-20_exposing-185m-indians-personal-information-and-much-more.md
original_filename: 2023-02-20_exposing-185m-indians-personal-information-and-much-more.md
title: Exposing 185M+ Indians’ Personal Information and much more
category: documents
detected_topics:
- access-control
- rate-limit
- password-reset
- otp
- sso
- jwt
tags:
- imported
- documents
- access-control
- rate-limit
- password-reset
- otp
- sso
- jwt
language: en
raw_sha256: 63a9fd19ba021cc5017fd8d0b2d35c2bfe80e2ff31a8a0c1eea6385279cf2354
text_sha256: bef8f5b11ae2bfb7d73d487956cf5f3de401d76d51ccdf3d982d3eed6e3135c9
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Exposing 185M+ Indians’ Personal Information and much more

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-20_exposing-185m-indians-personal-information-and-much-more.md
- Source Type: markdown
- Detected Topics: access-control, rate-limit, password-reset, otp, sso, jwt
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `63a9fd19ba021cc5017fd8d0b2d35c2bfe80e2ff31a8a0c1eea6385279cf2354`
- Text SHA256: `bef8f5b11ae2bfb7d73d487956cf5f3de401d76d51ccdf3d982d3eed6e3135c9`


## Content

---
title: "Exposing 185M+ Indians’ Personal Information and much more"
page_title: "Exposing 185M+ Indians’ Personal Information and much more | blog.robinjust.in"
url: "https://blog.robinjust.in/gov-in/2023/02/Exposing-Indian-Citizens-Sensitive-PII-and-more/"
final_url: "https://blog.robinjust.in/gov-in/2023/02/Exposing-Indian-Citizens-Sensitive-PII-and-more/"
authors: ["Robin Justin (@_robinjustin_)"]
programs: ["Aadhaar", "CERT-In"]
bugs: ["Broken Access Control", "IDOR", "Information disclosure"]
publication_date: "2023-02-20"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1508
---

What if I told you that with just your phone number, or even better, with just your name, I could tell you everything there is to know about you?

Hi! My name is [**Robin Justin**](https://blog.robinjust.in/about/) and I am a 20 year old student who’s a musician and a security researcher. I do bug bounties to help make the internet secure just a _little_ bit more each day :)

## Summary

In a nutshell, I had direct access to critical documents like [Aadhaar Cards](https://en.wikipedia.org/wiki/Aadhaar) and Passports of all 185 million+ Indians that holds a drivers license, and all I needed to access your documents was either your full name or your phone number. I could’ve also generated as many valid government approved drivers licenses as I wanted to for anyone of my choosing. This is only the tip of the iceberg and there was a lot more that was possible. Oh and also, the entire process of finding and exploiting these vulnerabilities took me just about **three hours** in total. _*Sigh…_ *

> _Note: The vulnerabilities disclosed here have already been reported to[CERT-IN : Indian Computer Emergency Response Team](https://www.cert-in.org.in/RVDCP.jsp), tracked under reference ID’s CERTIn-53609122 and CERTIn-79067922. This blog is published only after the explicit confirmation from CERT-IN stating that these vulnerabilities are remediated and are no longer reproducible_
> 
> This blog is written with the goal of being very beginner friendly, with simplification of technical terms wherever possible to encourage learning about fundamental security measures that are a bare minimum in critical environments. So yes, feel free to go ahead and give this a read regardless of your technical skill level ;)

It was possible for a threat actor to disclose [Sensitive PII](https://www.investopedia.com/terms/p/personally-identifiable-information-pii.asp#toc-sensitive-vs-non-sensitive-personally-identifiable-information) of Million’s of Indian Citizen’s that hold a Driver’s License, Learner’s License, or even people that merely just started the process to apply for a license on [Sarathi Parivahan](https://sarathi.parivahan.gov.in/sarathiservice/).

It was also possible for a threat actor to log in as **Administrator** into the portal. This allowed a TON of sensitive actions such as approving or denying all pending driver license applications, disclosing the list of ALL government employees that work in the department and SO MUCH more (Click [here](https://blog.robinjust.in/gov-in/2023/02/Exposing-Indian-Citizens-Sensitive-PII-and-more/#what-were-my-super-powers-as-admin) to jump to a more comprehensive list of actions)

#### So wait, what is Sarathi Parivahan even?

[**Sarathi Parivahan**](https://sarathi.parivahan.gov.in/sarathiservice/) is the Indian government’s official website responsible for issuing Driver’s Licenses to Indian citizens accross the nation. It’s managed by the [National Informatics Centre (NIC)](https://en.wikipedia.org/wiki/National_Informatics_Centre). If you are an Indian Citizen and are hoping to drive on Indian Roads, you inevitably have to go through this website atleast once to get your Learner’s/Driver’s License.

As of Feb 2023, there are about 185 Million unique people holding active/valid driver’s Licenses (which explains the number on the title :D), and about 163 Million Learner’s License holders (a few probably overlaps with the Driver’s License data, so I didn’t add that number to the 185M) according to the Indian Government (Refer [Stats of Driver’s Licenses](https://sarathi.parivahan.gov.in/SarathiReport/DashBoardGr.do))

## The Journey

It all began when I had to apply for a Driver’s License for my dad since his previous one expired, probably even disintegrated at this point (He’s held onto it for the last 20 years :P)

The process seemed quite straightforward. I had to

  * Create an application on the portal, apply for a Learner’s License under the _Contactless_ category (which was an option available in my state “[Tamil Nadu](https://en.wikipedia.org/wiki/Tamil_Nadu)”, which meant that I didn’t have to visit the [RTO](https://en.wikipedia.org/wiki/Regional_Transport_Office) \- Regional Transport Office in person),
  * Appear for an online test to show that I understand the basic rules of the road,
  * Get the Learner’s License and then,
  * Apply for the Driver’s License.

Sadly, it wasn’t all that straightforward afterall.

After successfully applying for a Learner’s License, I tried to set up the online test for dad, but the link for the test was simply inaccessible. We headed straight out to the RTO to find what’s going on. It was a Friday at around 3 PM then and the Government official told us that this happens every now and then to reasons unknown, and asked us to come back on Monday to fix this. However, the website says this:

> Citizens would be able to apply for these services online and without needing to visit RTO offices multiple times. Only for picking up modified or renewed Driving licence would citizens need to go to the RTO office after getting an intimation that their “Driving Licence has been activated and is ready for pick up”.

The whole experience just seemed quite illogical and I honestly wanted a license as quick as possible. So as your friendly neighbourhood “tech enthusiast”, I dug in a little deeper to try and reverse engineer the problem and make things work. (Spoiler alert, the security geeky head of mine ended up finding some pretty cool vulnerabilities instead xD )

## The first couple of finds

> It took me a GRAND TOTAL of just about **10 minutes** of using the website to spot these vulnerabilities. _*Deep Sighs…_ * well, moving on,

Going through the flow of creating a driver’s license application, most of the sensitive actions initially seemed well protected, which seemingly required an application number (can be anywhere between 1-10 digits) with the applicant’s date of birth to proceed further. I dug in just a little deeper to only find out that the application had a couple of endpoints with [Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) flaws. More specifically, missing authorization checks one level down.

A **non-technical** example to explain what’s happening here is: Imagine you managed to get a “visitor” pass to enter the [Pentagon](https://en.wikipedia.org/wiki/The_Pentagon), and let’s say that you are only allowed to be in the “visitor’s lounge” and nowhere else. However, what actually happens is, once you pass the super rigorous checks of your visitor pass by the security at the entrance to prove that you are indeed a legitimate visitor and not an adversary by any means, you are able to just casually walk about anywhere you want, like for instance, into high-security military-guarded rooms, happily steal military secrets and walk right out, with absolutely no one to stop and check you anywhere along the way.

That in summary is pretty much exactly what was happening here. Once authenticated through what seems to be a secure endpoint, other endpoints with sensitive actions were available to use with the previously authenticated JSESSIONID cookie. This gave us a LOT of vulnerable endpoints to play with.

1) One such endpoint found was responsible for fetching the “state” of a Learner’s/Driver’s License application. This gave us an interesting response
  
  
  An except of the json response:
  ["30-06-2001","TN01",null,null,"completeFlow","data:image\/jpeg;base64,\/9j\/4AAQSkZJRgAB...]
  

It was therefore possible to supply a random application number to this endpoint to get the date of birth associated with the application along with the picture of the applicant in [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64) format.

This was impactful as most actions (when it comes to proceeding further with an application’s flow as an applicant) simply required the ten-digit application number with the associated date of birth to authenticate. To top it off, there was no visible [rate limiting](https://en.wikipedia.org/wiki/Rate_limiting) enforced anywhere on the website.

At this point, the most I could get out of this (post-exploitation of the endpoint) was very basic information associated with a particular application number such as the Name, Address, Driver License “number” and a picture of the applicant. It also allowed me to proceed with the application flow (which isn’t all that exciting, i mean like, why would I ever want to sit and fill up a driver’s license application for someone else xD)

Now comes the catch. The application numbers weren’t exactly issued sequentially. So, despite the fact that I could theoretically sit and brute-force all existing application numbers, that’s still a LOT of requests! atleast that’s what i’d assume according to [the government statistics](https://sarathi.parivahan.gov.in/SarathiReport/DashBoardGr.do), which suggests that I’d have to send out about 10 BILLION requests (i.e. 10^10: 10 digits, with 10 options for each digit 0-9) to identify about 185+163 Million valid records.

This would make the attack unnecessarily noisy and result in a huge waste of requests (and time) to begin with; and for the basic PII at stake here, while it may bear some impact in the real world, it really didn’t seem all that appealing to me because there was an obvious lack of ability to target people, and it seemed like I was going through a million deck of cards blindfolded trying to find the right card.

2) Fast forward to a few minutes later and I am introduced to another endpoint who’s sole purpose is to fetch the corresponding application number when an applicant’s phone number and Date of Birth is supplied. Targetting individual people finally seems possible afterall :)

But before proceeding further, I think it’s worth taking a step back to try and understand “WHY” these super vulnerable endpoints came into existance in the first place. It could be due of a lot of factors but the obvious explanation is the fact that the developers did a lousy job organizing the flow of these processes in the first place, which ultimately created dependancies on such endpoints which have to make explicit calls like this to the backend, all to simply just make the application “work”.

Coming back to the second vulnerable endpoint, this would now mean that all that an adversary needed was the mobile number of an Indian citizen, along with their date of birth to potentially get access to basic information such as their Name, Address, Driver License number and a picture of themselves. However, this still didn’t seem like enough impact to me simply due to the lack of information disclosed.

#### It couldn’t get any funnier than this i promise:

At this point, I was just going through random features available on the portal. As I was hovering over the nav bar of the website, I noticed an option which was quite literally named “View Documents” :D

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-public.jpg)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-public.jpg)

Which when clicked on, gives us this:

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-fields-public.jpg)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-fields-public.jpg)

Options available:

  * Application Number,
  * Learner’s License number, or
  * Driver’s License number.

Let’s just take a random application number for instance, enter it and click on submit like any normal user would. What would you expect the portal to ask us at this point? An OTP to authenticate? Atleast the date of birth that corresponds with the application number?

Surprise surprise, it asks for neither! It goes out of the way for me and automatically fetches the Date of Birth associated with the application, and proceeds to do something that I could only assume is the portal automatically self-authorizing itself somehow?

From there it’s as easy as just clicking on Submit again to be welcomed into a page full of hyperlinks, linking to all the documents the applicant used while applying for their license. Go ahead, click on the picture below and take a closer look into what it actually looked like.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-sample-blurred.jpg)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-sample-blurred.jpg) The above picture is a screenshot of my very own application (with all the details blurred out ofcourse ;) 

It’s funny to see that such a critically vulnerable endpoint has been hiding quite literally in plain sight for all to use! At this point, I am convinced that this must have been extensively exploited at scale by threat actors. I mean, it took me about 10 minutes to find the previous vulnerabilities and about 4 minutes for this one. How is it not already being actively exploited?

(Oh and I later deduced that this endpoint was originally supposed to be an “admin-only” feature, but somehow ended up on the public portal by accident ; More on this in just a bit, keep reading! :)

Anyways, to attain maximum impact here, we ought to chain this vulnerable endpoint with the one we found earlier which gave us the application number of an indian user with just their phone number and date of birth. This ultimately gives us the ability to access sensitive personal documents of any Indian that we know the phone number and date of birth of.

This was when I decided that it’s time to report this to [CERT-IN](https://www.cert-in.org.in/RVDCP.jsp) to prevent any further abuse. I made the initial report on the 7th of November, 2022 and was under the assumption that it would atleast be partialy remediated asap. But after the initial acknowledgement, there were no updates from CERT-IN for over a month, and neither was the vulnerability remidiated.

The goal was clear to me now; Find a vulnerability with more impact than this one to force a quick fix and to further strengthen the government website.

Amidst all of this, there was one recurring thought running laps in my mind. It was the question of “What if I don’t know their phone number? Why do I need to have a person’s phone number to be able to exploit this? Could there be a better way?”

## Administrator is god

> Yet again, this one took me about half an hour to find and another hour and a half to exploit. _*A HUGE Deep Sigh again…_ * let’s get into it now,

All through this process, there was this one thing lurking at me from the top-right corner of the screen, which was the “Login” feature of the portal. You see, normal applicants don’t get any credentials to login there. So it was fair to assume that it was used to authenticate actual government employees/administrators to manage the portal, make entries, approve applications and the likes.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/login-form.jpg)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/login-form.jpg)

Seems pretty straightforward, except the fact that I don’t have any username to login with. So I did the next best thing and clicked on the “Forgot your password” button. This endpoint will take in a valid username and proceed to the password reset login flow. Turns out, the infamous **“SYSADMIN”** user (short for System Administrator) was valid.

When we submit a valid username to the Forgot Password endpoint, an OTP is generated and sent to the user’s phone as a text message. During the verification of said OTP, a POST request (to the “/cas/login” endpoint) is sent with the parameters below:
  
  
  passCode=83ef0dbd05929cb12718589d***REDACTED-SUSPECT-TOKEN***  logmode=1az6om
  submit=NEXT
  execution=3112c9d9-841f-44ba-ca75-895f2de26053_ZXlOaGJHY2lPaUpJVXpVeE1pSjkuQ1pMdk1yRUQ5K0xOM29uWDdjR3lJRUJGaFFONno0UmZsSkk3UGNma3l1Myt3dk9jN0Y3UVREbHltTkF2dm2sR2xtTTIzUnhKa085bkFxdUpkZFRWdDV5MutNUEdLWVlxUEdJYldwekVQY25GQ2wxamlhd0Y2RlBBNGgwVjEyRDF5S3MxQzlJSjdKYVBnN3k3SlBETVZuZW9hTERKQnpjdUdtaEliTzZLaXZYU080a0taNWVjR00wSVowSTcweXZKamNyYU5rMEpONGVmRTBGcWtkbXJMNXFmWVRLOUVxREgrQzM2OGRDWWhyS1Z5NENIcXpLQm11dGxlbHpuTFVFTE15RU94MHoxUDdwaUg0Q3hnVG84VEJrVFhwT2lIT3Z3NHBQWlRrSHRRWHJsUkh0REFSQTFUeiswRDJKczRqUDJqcjRTUEFvb0RqeE9JTWJrdlVtSlVOSmRDc29NbHFIQ2dNT1NDNmdSSlU3bVZ6T1JqNm9ubWVObzVwUER4QVZhQWNkcHcxdVczMnFTVzV5UWhBIjZVeklHTXp0OHJxUm9hL2FObElkeUE1dkc3eGIvVnlOR0ZGN09ncmN6UXJZcFNEV1NFaU5XVVdIRmxTbWl6UnQvVUN3M1BRY2ZOc0UwUhgxZFBVQkptaDNBcVY5Z29CcW5KQmhUcDQwcExpSGxSK1ZZQ3ZsZ1dwQzdlSlJWdVdVT1hJSnV3KytLbm50UW9STGNuTkZMSDVIWkFPSXJhVXNoMUxQbVJmam1MczhGOFZ4QjNreHA0OHNJRDdHejFjWERZNS9Xc1pOVnJxb21ucDZ4QnZGY245QlF4dGVuRzB2c3pLcHVDZ3JQZXg2MCtKNEFPUzFDSUlVZmdlZE1KejVmYlllS29CREhpNVpIV013ZlMxWVpaa3AvOEFjMlNrMXpJN1Y2NTI5VXZERFdFQzFYY0xGTUEybkFXL1FCTnJnSWtydkZEd0NYNVpTaHJxYkt2cndRbktHWHk1UVJmRmVmUVFIc1BnTXJjQ2V1WTdyb1M4UDFRRjlGYWJaNkVOSHlnbFNtMnlEUzJmQVpxZ2NHbnN2ajFmampIV3FSeFY2RlAzR25iVWgwUUpoQWdLOFRoZFNQWkdDclh3WGtEd2NLT0hsOENET1JiQm1rRTcwb2ZBMzh0N3pEd2VXLytmQ3lwdmhVajErOG1oaGUwSGtLSHFET2thWDNWT3g0ZmhHRyt1ekI5REIvM1VIVmZPRTdIOVdiTjlpK29tYmluZU8rdEx4eFZhU1Vpa2FzYTR2dU9CN0o2OSsxbk92dFZIVnR1M1pLQWkyOVBzeDd0VzVmZjBDbjJOeWcvV0JhK1J0cEgrck1JSVZPZ0orUmt4QXJzalU3VUNVbVFHWUlwaHZsbXRnZzl2dW9yUlpDSmI0alZMeEpiWC9raks2eUNrT0hwYkRXalF2OVpZNTlEcDFWc2p0SWpaMU1TaTU5dFF4QVhwbUF4Um1HZEdzVnkvUWQwT3liYnVdSE9WNDZza0wwcWs0dzNreVk2eG5BVE9IQm5KajZKdFZIU0FnZksvUWlOQXJFeVkzZWJqSmw1VlRuU3hoUzVmemZKRW4vQS9lcDZFbGNvNEgxZktuUjdDQm9pcE5ZWjk3K3hYc010dW1KeXo4eWtwWTcyY295SmZSL201WGFwZGdlSElHMjFvcEU5bmxVQ09CNW1KRm4rY3F6YlRmcXdldHltSVFhSHZLNHpkVU0ycm13TWh2SXpkKzVVVy9RNXBNUm1GR3lYalNxbVZjVEUzNjgzbzAzRi9DMkl2UmNZbTZwa3VTS2VOaVVHb1dXaVArUi9BYlhmeXY0ZEMzSU5PQ1VTGjJIM3hPdDZKZzNxQTNWeHk5c1RRZjBBRk1uazVZNDRUekZOc0t6OXk5TzJuNXRIWnNTNWYvS3NqNTMwbHpTVEdLQmlRU1paV09LaHM5WWkxcmxIZjl1SURVZGVqZkRRcVovZVFPQXlraysvMTAzbzV4UXBOZ0NMYUFpM3hhNGRJY2F5Y0V5WjZPWWVnczQvZmJrU2xBMy9hZEFWThRmcHFxMmkrQndQWmlLLzBJYTdZVFArNFRnZk1rZ1JOaEJYbUdWYUZCTnk1OEtKTUE0MXhQTit2Ui9jOHswc2xTbXRwSE1mTG1NM29sZnpyN2lvNUkyS1c2UmRvSVNXODA0M21LQVNzOVZSVitOc00rL1l6ME9HRnYxV3h3d0swd0t2dTFrbnpmNXF6N1JZd08rRWVrVzZBd3BoT2VEQlVJR20zbU8rWUo4NDAxRmpuN3hWZ2dwSzU5dmJmQXp1ZkNraE5COUlCczZqV1ErVWlzSWwvazN1NVVzMVZlSUZTRWtLemtoV0xLWmlxcUR0MnRZWW9ub3hIcnJ6dWZOMVU4d3Y3QmxmZkUwRktoV2k3MHVzSWZyaWZHSC9oTWcrR2NTN3AwS3AzNkdkS0Q2dnZGeXpzVEZId2NOd2Zab1ZzTGlFYmRXSWl0VlQybGFlMkFKNXZXbWdic3RNZ3dQcVNtS2haUFk3dHNaM3RjbnZ4TTVHcXR5Mm15WWRBYzhsekYrUkVmNXZkcC84WXVYWDdFTEw0SGdlMVZheCt4Z1ZBaEpleU5MTXpYckZDTXMvMUxZR2NpOHdpcHhNOHVPWFQ5cTYyQk8zdThzZUNHRnA4cGI3cTJ2UFBUam5BU05US25oVFBLVW13RXJ3M2J4dmcxR3g0QW4zMXB5VjlibE1qd2cyVFlhUjBra3pGV3pJSlRQWFAyVzdtclNxbnZNMnkrdGVpSm1TdDFRb3dmMS93NTVDd0t4NFcwVS8yMGxZV3BKSWhaRm1KWHZGS2ZTeTZDcG9abEpQN1pJR0d0Y0xUVHVBUkZEb3NjazJ3RE9PUjZlQnBYRUxldFl5ZjNoRC9Bb2NJdG5RbGVvZ3dEcmdtUlQ5NDUzODRuWGZ1bEFUbHpJbmI5MmczcTBadTRmWTVVWEp3dXluOUhzL0lTTnF1cDFjZVpHR2c2dzhYWWRZdzJmVFJKRnNmVFBXRFlMM1JYRkNXbjhnYUUwN3NER01LT3M1c2p1VGtEQnBZSzBuUkpvUlluN0h1RW84YUhvOTdTd3Vxa0lGZHEyL3BvOERRT09aYTkwcVVCRWhLZDd3MWZ1Wm5wWEgyWXRJcmVoTGpVakZKaStRcGZxaTBUM05CZEdpUVpYcjZOZ0dOZUFPMUVCY3ZMU2NXeFdlNUFObGl0ZVl6bDUzMUJbT0lRVmpmYVIxZGwrV3ZOZm5sanh1NWE1YkZYSlNWdkloRDRJNkJ6bHFCcFRnM2xVd2dtYzFPOElYUHk1ODI3R3VXVjY4VVdlK0ExaVFSY25tTW43cGdGazF6R083L0k3T1FrVUFJQ09vc3dlYzNuZ0FKWm1jGmZCSUllMWQwU2ZTUjRRRlkyMkQycGh6bEx5Q0E0eC9FaFVaREJGaVlsb3FnTml4ZEhjZm5EWjhpblqSQnJBc2daaEtDZTQ2d3BKSU9BdkZRQ0dvU2JzalhvWFArZHlBbXRxQXZyWGlKYXNNdEhDVmRJYUdnTDM5Z1Y0T2tJd2M0bVdaNHE4VXJlSmUwaGpsTUN2bjUzckRYRFVudWFndWQ4azZ3cWhsaDJzdDJpbm85SmNiOGIvVmYwUlRwdEtQT2trOEdmM0RSVW52eVdFUzNVRFBnM01jRGpaQzJFGGQyLzAvY0M0VVdVNzNGQ05WVVJ2cmU1Uk9hbXNOTkpRZE5hRE14cTJNQk9lbnh4bURTZUpWUFU3d2VEUDJtK1FNd0FScXpCTGNPMUlRRU5VZUNpaHFlQWI3V3NLWWRuMURDWVBPcGVkYlRVakh3KzkyT3I1bDY1OGxsZm1Mb0dHNDd0OVFRSWEreS9aYkRlMVlSRnJ3d21CUFRFWDdiWlpLeDZJdTc5Q0pjeEw4NGRVcE1rd2tWMkE1Rk1RZHRHNlUwamFwcEZRaldMOHNQQU9mbE92dm9jeHprQU5aS0UyYTlhUVk1ZkJUTm9pUElZYWxPMElxZ09id2pzWVN6Ymo3Qkw5QTBuRHppNzN2ZUh0UFVUMktlZEJlYk13U2h6cGRiR2FUZm1MbkREeGkzY0g1SFg1w1dQMmdLSkNyQ0xUNzhsS3c1T1hvTGloSmwzTURDNmFYeXZwMkF2OC9HbG96ak9uWFJLZ1NIVWtxMWVab2pOS1NFQmxxU0FSWVd1MDFwbDFOdFhobFFYWmhoeGU4ZVdQeStyVzl6aUhPMUsyV2FwQTVZMjR3UnhqcDE0bmJERlVzN0Q2S015SmtxNVpxd3dBYkRNWEtkd3NCTnhNbk43OFMwQ0M5N2o2MkFYSHpkNVYyQ1lRLmR5RRZCWnVVS0NfeUEtbWE1aVBQaU9DbnNzNWR0OVFNLWFYZEVLZjVSajZWX3hOQW1hY29lakkz***REDACTED-SUSPECT-TOKEN***  _eventId=vpassword
  randamGenNum=1983
  param=validatePassword
  as_sfid=AAAAAAWoPv8x9y44VWn0m8_ilwUaKyOFQ2c8BBFgzasgoSq2glmYVaoJ5emHYVQP0GvvvzE8jS2Awz4csOXOV1D3ZUsQdn-l-5qnMMfrx9Q4D1viPmYdLk039IQubj-81qURESc%3D
  as_fid=***REDACTED-SUSPECT-TOKEN***Let’s try to break down what all these parameters are about. At first sight, the “passCode” seems to be an encrypted hash of the numerical OTP that is supplied, and “logmode” contains the captcha that is used for “each” login attempt.

To get a better sense of what the other parameters meant, the “fgauthentication.js?v=5.3” script could help us as it contained the code to perform basic front-end validation before supplying the OTP to the server. This excerpt from the script has exactly what we are looking for:
  
  
  var randomnumber=Math.floor(Math.random()*10000);
  var plainSec=$('#securityCode').val();
  if(plainSec != "") {
  $('#securityCode').val(sha256(sha256($('#securityCode').val()) + randomnumber));
  $('#randamGenNum').val(randomnumber); }  
  

This tells us that the OTP (referenced by #securityCode) is SHA-256 encoded twice over (of its concatenation) before being sent to the server. We can also see that a random four digit number is generated every time by the application on the front-end and it essentially acts as the “[salt](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/)” (No, NOT the ingredient!) to the encryption. The randomly generated salt is then passed onto the “randamGenNum” (in love with their spelling :D) parameter of the request that’s sent to the server, while the encrypted hash is passed on to the “passCode” parameter.

Oh and if you were wondering how many digits the OTP should be, this html excerpt tells us that it’s exactly 6 digits long:
  
  
  <h5>OTP Authentication</h5>
  <section class="form-group row">
  <label for="logmode" class="col-sm-4 col-form-label"><span class="accesskey">OTP</span>:</label>	
  <div class="col-sm-8">
  <input class="form-control required" type="text" id="securityCode" name="passCode" size="6" tabindex="1" maxlength="6" accesskey="otp" placeholder="OTP" autocomplete="off"/>
  </div>
  

I also noticed that the captcha is very poorly implemented. I tried making two consecutive OTP verification attempts with the same captcha, and it goes through just fine, which meant that the captcha isn’t tied to every request, which by extention meant that I could use the same “essentially redundant” captcha for multiple requests of OTP validation. The same goes with the random salt value.

Considering all these factors, I went ahead and typed out a simple python script to generate all possible encrypted hashes, by supplying a random salt value:
  
  
  import hashlib
  
  randnum = str(1983)
  
  with open('6digitcodes_hash.txt', 'a', newline='') as shacodelist:
  with open('6digitcodes_plain.txt') as codelist:
  for code in codelist:
  code = str(code)[0:6]
  hashed = hashlib.sha256(((hashlib.sha256(code.encode('utf-8')).hexdigest()) + randnum).encode('utf-8')).hexdigest()
  shacodelist.write(hashed+"\n")
  

With these hashes at hand, all that was left to do was brute-force all possible hashes to find the one that’s right. Note that we have to supply the salt we used in the python script to the requests under the “randamGenNum” parameter. The rate of requests sent seemed pretty decent consistantly at five hundred per second on average and does the job relatively quickly. Nevertheless, slightly higher speeds are possible for when the servers feel happy, joyful and gracious :D (extremely rare, albeit possible)

If you were wondering how long the generated OTP was valid for, I tested it later to find that it was valid for around 2 hours (which is a REALLY LONG time) after generation, after which another OTP has to be requested.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/password-changed.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/password-changed.png)

Once I found the right hash, I was automatically directed to change the password of the SYSADMIN account, and so I did (and took a note of it too, to include it in the report to CERT-IN). After the reset, I logged into the portal with ease as the SYSADMIN :)

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/logged-in.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/logged-in.png)

I wanted to make my report to CERT-IN the very second I was able to log in, but at the same time, I needed to make sure that there was atleast some impact to having logged in as SYSADMIN. Boy oh boy was I not disappointed.

### What were my super powers as admin?

The amount of functionality the administrator has is just purely insane. I will try and highlight the most critical ones that caught my eye before I rushed in to send the report to CERT-IN:

1) **Search for an applicant** : There was a feature in the administrative panel that served as a search tool to find applicants with just their name and Date of Birth. Note that there exists a search tool with similar looking UI available in the public version of the application as well, but it does not work functionally anywhere close to this. This one is much more powerful in accurately finding records.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/advanced-search.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/advanced-search.png)

All you needed was the full name of the applicant. The approximate range of the date of birth could be guessed and brute-forced with to find the correct record. Or we could go with the name and phone number combo if we know even a part of the phone number (4 digits, which is often shown ciphered out in many recovery forms). Once we find the record, we can use that number with the earlier “View Documents” endpoint to directly extract their Sensitive Documents and more.

2) Application bypasses:

  * **Skip Bio Verification Flow** : The administrator was able to access any application by entering it’s number. Once entered, the administrator gets all info related to the application, and can decide to click on the “**Skip Flow** ” option to skip the in-person Bio Verification checks.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/skipflow.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/skipflow.png)

  * **View all pending and approved applications** : The administrator was able to view all applications which were in the “pending” and “approved” status, along with all the information associated with the application.

  * **DL edit Approval** : If an Indian wants to change the address or anything else on their license, they must apply online and appear at the RTO with all necessary proofs. The administrator was able to approve any such requests to edit the drivers license in an instant, therby completely bypassing verification of the changes made to the license.

Usually, application verification is done “in-person” at the RTO, where a government employee takes a look at you and your original documents and approves you. The fact that I can skip that gives a lot of scope for malicious actors to carry out **unlawful** things.

3) **Access to government employee list** : The administrator had unrestricted access over the Personal Information of all the government staff working at RTO’s accross India.

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/govstaff-pii.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/govstaff-pii.png)

4) **Bypass application fee** : As an administrator, it was possible to mark an application as paid and directly bypass the application fee that is to be paid by the applicant.

Oh and if you remember, I told you that the “View Documents” endpoint was an admin feature? I figured that out because the same endpoint existed in the administrator panel under a category called “Master”. My best guess is that it was obviously never intended to make it to the public website, but an overenthusiastic developer might’ve done the deed :)

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-internal.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/view-documents-internal.png)

There were a LOT more things that was possible as an administrator, but I did not go any further than this as the impact of this could potentially harm millions, and so I prioritized responsibly reporting this to CERT-IN as soon as possible (_insert spiderman quote on great power and great responsibility XD_)

### Timeline:

Submission of Initial Report:  
Nov 7, 2022 - Report Sent to CERT-IN  
Nov 10, 2022 - Acknowledged by CERT-IN  
Dec 2, 2022 - Re-tested to see the vulnerabilities not remidiated

Submission of Second Report:  
Dec 5, 2022 — Report Sent to CERT-IN  
Dec 5, 2022 — Acknowledged by CERT-IN  
Dec 9, 2022 — Asked for an update on both the reports, no response  
Jan 25, 2023 — Both reports marked as fixed

Here is CERT-IN’s fix confirmation:

[![](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/cert-in-fix.png)](/assets/posts/2023-02-20-Exposing-Indian-Citizens-Sensitive-PII-and-more/cert-in-fix.png)

Yep, they ended up removing the entire admin user :) The fact that most of these bugs are laughably easy to exploit, yet severely critical in nature only means that we have to take security as priority and work towards developing more secure websites!

The fix was confirmed on January 25th, 2023, however, I waited for about a month before disclosing because of that last line in their fix confirmation. Either way, according to CERT-IN, none of these vulnerabilities should be reproducible anymore.

Anyways, If you are reading this, congratulations! you’ve made it to the end ^_^ I really hope that this writeup provided some value. I tried to write this blog with the goal of it being as beginner friendly as possible. Now that I finished writing this, It seems like I might’ve over simplified in a few places and left the technical jargon untouched in some. I sincerely apologise for this imbalance. This is my first blog, and I hopefully get to do it a little better next time around :D

* * *

[ robinjustin ](https://www.linkedin.com/in/robinjustin)  
[ _robinjustin_ ](https://twitter.com/_robinjustin_)  
[ _robinjustin_ ](https://instagram.com/_robinjustin_)
