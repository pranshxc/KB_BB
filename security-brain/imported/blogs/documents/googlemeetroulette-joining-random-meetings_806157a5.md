---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-04_googlemeetroulette-joining-random-meetings.md
original_filename: 2018-10-04_googlemeetroulette-joining-random-meetings.md
title: 'GoogleMeetRoulette: Joining random meetings'
category: documents
detected_topics:
- sso
- xss
- command-injection
- automation-abuse
- business-logic
- webhooks
tags:
- imported
- documents
- sso
- xss
- command-injection
- automation-abuse
- business-logic
- webhooks
language: en
raw_sha256: 806157a5b55f99771d7b5b037bd4c0fb400cbf401eb5495009c2e47995974f77
text_sha256: d3cb30b9432f00aa7f06552ad2a85b38fd519ae8b0f334a7349bc383063dab15
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# GoogleMeetRoulette: Joining random meetings

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-04_googlemeetroulette-joining-random-meetings.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, automation-abuse, business-logic, webhooks
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `806157a5b55f99771d7b5b037bd4c0fb400cbf401eb5495009c2e47995974f77`
- Text SHA256: `d3cb30b9432f00aa7f06552ad2a85b38fd519ae8b0f334a7349bc383063dab15`


## Content

---
title: "GoogleMeetRoulette: Joining random meetings"
page_title: "GoogleMeetRoulette: Joining random meetings - Martin Vigo"
url: "https://www.martinvigo.com/googlemeetroulette"
final_url: "https://www.martinvigo.com/googlemeetroulette/"
authors: ["Martin Vigo (@martin_vigo)"]
programs: ["Google"]
bugs: ["Bruteforce", "Logic flaw"]
publication_date: "2018-10-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5663
---

[Home](https://www.martinvigo.com/) » GoogleMeetRoulette: Joining random meetings

[231 Comments](https://www.martinvigo.com/googlemeetroulette/#comments)

October 4, 2018

![Google Meet Roulette logo](https://www.martinvigo.com/wp-content/uploads/2018/03/googlemeetroulette_logo.jpg)

#  GoogleMeetRoulette: Joining random meetings 

A while ago, I was at a friend’s house and he mentioned he had to join a work meeting. He used [Google Meet](https://meet.google.com/_meet) to join. The WiFi was acting weird and he was not able to follow the discussion. Someone suggested that he could “call in” making a regular phone call. I overheard that and immediately found myself wondering if there was a way to join meetings I had not been invited to.

In today’s world and global market it is common to have teams spread all around the world. Corporations have offices everywhere, customers can be located in other countries, vendors operate overseas, and in general we have a need to communicate with people that are not in the same location as us.

Daily meetings are something many in the tech industry can relate to. And with teams, customers and vendors in different physical locations, it is common to use video calls. Many times, sensitive topics are discussed. Security, architectures, all hands, financial results, roadmap plannings, new features… These are only a few of the confidential topics discussed in video calls.

## Google Meet

Google Meet is a re-invention of Google Hangouts with features aimed at businesses. It is part of [G-Suite](https://gsuite.google.com/) which is a set of services in the cloud. [Looking at their website](https://gsuite.google.com/customers/), it is used by many companies including Fortune 500. I can only assume that these companies will use Google Meet to have confidential meetings. Let’s see if we can join them!

I did not focus on the usual way of joining a meeting using the browser and clicking the Google Meet link to join after login in. Instead, I was interested in understanding how the “call in” feature worked as it is a regular phone call and I wanted to know how authentication was handled.

## Calling into meetings

If your company uses G-Suite and pays the Enterprise license, in addition to a link, you will be served a phone number and a 4 digit PIN when you create a new meeting in Google Calendar. Anyone can dial the number + PIN to join the meeting in “voice only” mode. This is very handy as it allows attendees to join even if they don’t have internet or don’t want to use it intensively (if you are traveling internationally, for example).

[![Google Meet information](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/Screen-Shot-2018-03-24-at-12.18.35-AM.png)Google Meet information

Because this is a regular phone call, we can consider the phone number + PIN combination as the secret to authenticate into the meeting. Actually, we can think of the phone number as the username and the PIN as the password (a shared password for all attendees). In other words, **If you know a phone number and the 4 digit PIN, you will be able to join that meeting**. We got ourselves two targets, finding phone numbers and PINs.

## Finding phone numbers

Phone numbers are probably not meant to be a secret but we do need to know the associated number to a meeting in order to be able to join it. Therefore, the first goal is to find a way to locate valid Google Meet phone numbers.

### Oldskool wardialing

Back in the day, the first generation of hackers used wardialing to find mainframes, or any other machines connected to the phone line. Wardialing is a technique in which the attacker dials phone numbers massively looking for a machine to respond rather than a person. You can think of that time you dialed a number and started to hear weird beeping noises because you dialed the Fax number on that business card instead of the actual mobile phone.

Popular tools like [ToneLoc](https://en.wikipedia.org/wiki/ToneLoc) would detect these machines and log the numbers for later inspection. Nowadays, wardialing can be done more efficiently and cheaper using VOIP services. We can use wardialing to find Google Meet phone numbers as it will always respond the same way, starting with a short 2 seconds sound. Still, this would be very noisy as we would be literally dialing all the numbers in the US. We have to do better.

### Guessing

We can try to see if there is a way to guess phone numbers that are assigned to Google Meet. I started by scripting the creation of meetings to generate hundreds of them and scraped the generated phone number. There is a number of things I wanted to find out:

_Are phone numbers reused?_

Yes, they are. It would be difficult to have unique phone numbers for every meeting created given that phone numbers are limited.

_Are phone numbers unique per meeting?_

I found that recurring meetings (for example your weekly 1:1 with your manager) have always the same phone number and PIN combination.

_Are phone numbers random?_

~~I wasn’t able to find any useful pattern among all collected phone numbers.~~ Keep reading :)

The most valuable information I got from this step is that **recurring meetings always have the same phone number and PIN combination.** This is problematic because an employee that leaves the company will know this combination. He will be able to join all recurring meetings forever unless the meeting is deleted and created again.

### HLR registers

HLR registers are stored in global databases and contain information regarding GSM subscribers. HLR registers are queried as part of the SS7 attacks to track victims as they provide, among others, information about the tower to which the mobile phone is connected. There are multiple services online that allow you to query this database but it costs money. We don’t need information about the towers or other sensitive data HLR registers provide, I just want to know if the phone number belongs to Google Meet.

Turns out, [Twilio offers a limited api](https://www.twilio.com/lookup) that allows you to see some of the information related to a phone number. Among others, you can see the carrier to which the phone number belongs to. This is valuable information to help find Google Meet phone numbers. I created several meetings and verified the generated phone numbers with Twilio’s API. **The carrier of phone numbers assigned to Google Meet is “Google (Grand Central) BWI – Bandwidth.com – SVR”.**

Great! We have an API to query any phone number and check if the carrier is “Google (Grand Central) BWI – Bandwith.com – SVR”. But we can do even better…

### Google search

Turns out, one of the easiest way to find Google Meet phone numbers is… to use Google. Since we know the carrier, all we need to do is to [Google it](https://www.google.com/search?q=%22Google+\(Grand+Central\)+BWI+-+Bandwidth.com+-+SVR%22&filter=0&biw=1481&bih=895). There are tons of websites that contain information about specific phone numbers for multiple purposes like tracking spam callers, provide owner information, etc. Best of all, those pages are indexed by Google and other search engines. We can take advantage of this and use it to look for existing phone numbers belonging to “Google (Grand Central) BWI – Bandwidth.com – SVR” carrier. Not all of them will be mapped to Google Meet as Google Voice uses the same carrier, but it will give us a great starting point. Still, the goal is to aim for perfection. We need to do better.

### Abuse international settings

If there is something that amazes me from the security research community is the will to “try harder”. I see it over and over again in conferences where researchers fight their way through to perfection. A 100% reliable exploit, re-engineering a piece of hardware to make it a few bucks cheaper, make an XSS work on every single browser, etc.

Inspired by them, I wanted a truly reliable way of finding Google Meet phone numbers. I sat back and just started thinking about what other things I could try. If you have paid close attention to the image above, you may have noticed the label at the bottom that says: “ _This phone number has been selected based on the Conference creator’s country settings_ “.

Interesting. This means that there must be international numbers I can dial to join meetings. Indeed, [that’s the case](https://support.google.com/meet/answer/7291345#supported). So, let’s start by checking if the carrier is the same. I changed my country settings on Google Calendar to Australia, created a meeting, and got an Australian number to dial. Next, I checked it using Twilio’s API and got that the carrier was “Symbio Networks”.

It was at this point that a happy coincidence happened. I did not know if this was a normal carrier or, like bandwith.com, a special carrier for VOIP services. So I thought I should use Twilio’s API to check the next phone number thinking I would get a different carrier just to compare. Instead of checking the Google Meet meeting number +6129051730**9** , I checked +612905173**10.** The carrier was again “Symbio Networks”. How about +612905173**11**? “Symbio Networks”. +612905173**20**? Again, same carrier.

Let’s see… I generated a meeting, got a Google Meet phone number, and all subsequent phone numbers are also from the same carrier. Let me call and see if I get the Google Meet greeting to confirm. Bingo! **For countries like Australia and Spain, Google Meet phone numbers are assigned in batches that are sequential.** I can generate a meeting myself and just check the subsequent phone numbers to obtain more Google Meet numbers. You can use them to join/find meetings in the US as the phone numbers from other countries are not specific to meetings in that country, they are global.

## Finding PINs

Now that we have effective ways of finding phone numbers, we need a way to find out the associated PIN. A 4 digit PIN gives us 10,000 possible combinations. Manually trying all possible PINs would be too slow and **Google Meet only allows us to try 3 different PINs per call**. You can definitely call again but this is time consuming.

Since manual bruteforcing is not feasible, can we automate it? Nowadays, there are a number of services available online to manage calls programmatically and at scale. Companies like [Twilio](https://www.twilio.com/) or [bandwidth](https://www.bandwidth.com/) offer cheap APIs that allow you to, among others, make multiple calls and interact programmatically with them. It sounds exactly like what we need! **If we know the phone number and we can make hundreds of calls at the same time trying different PINs, it should not take too long to bruteforce all 10k possibilities.**

Something interesting I found while poking at the API, is that [there is a global, per country, phone number that is the same for all Google Meet meetings](https://meet.google.com/tel/xkw-tafu-shj). The difference is that the PIN is 13 digits long instead of only 4 to add entropy. I wonder how many parallel calls this number can support and how easy it would be to perform a DoS. I did not try it as DoS testing is usually discouraged on production services.

Another interesting behavior I found was that **depending in the country you are in, the PIN length varies**. This is odd as all the security relies on the entropy of the PIN. Basically, some countries are more secure than others and USA is the least secure one with only 4 digit PINs.

[![Pin length in USA](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/pin-length-in-usa.jpg)Pin length in USA

[![PIN length in Australia](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/pin-length-in-australia.jpg)PIN length in Australia

### GoogleMeetRoulette.py

I created an account in Twilio, added $20 and wrote a python script that would use their APIs to initiate multiple calls and try 3 different PINs at a time. To my advantage, I realized that I don’t need to wait for the recording to tell me that the first PIN was wrong to try the second and third one**. I can enter 3 PINs at the same time and Google will accept the correct one.** This improves bruteforcing speed significantly. Making a call and trying 3 PINs waiting for the recording to end takes about 25 seconds. Trying 3 PINs at the same time, allows me to do it in just 10.

10 seconds per call, 3 PINs at a time, 10,000 PINs to try. It would take about 9 hours to cover all PIN combinations making one call at a time. **Because Twilio is designed to make calls at scale, we can make hundreds of calls at the same time making the process much faster.** The script fires so many calls that the line will be busy sometimes. Not a problem! The script will detect failed calls and simply retry. Actually, [Twilio notifies of failed calls immediately using webhooks](https://www.twilio.com/docs/glossary/what-is-a-webhook) making the script very efficient handling calls that did not go through.

If you are wondering how the script knows if the PIN is correct or not, I take advantage of the call duration to find out. Instead of doing some fancy sound processing, I figured that Google Meet will end the call if I entered 3 PINs wrong. On the other hand, the call will continue if one of those 3 PINs is correct. Therefore, [I instruct Twilio to wait 10 seconds silently](https://www.twilio.com/docs/api/twiml/pause) on the line before hanging up. This allows me to look at the call duration and figure out if I was able to join a meeting or not. If the call is ~17 seconds long, I know Google ended the call, hence the PIN guessing did not work. If the call is ~10 seconds longer, then I know I joined a meeting and one of the 3 PINs is valid.

I did some benchmarks and **on average it takes 25 minutes to try all 10k PINs and find 15 different valid PINs for 15 different meetings for a cost of $16.** Not bad!

### Demo

To make the demo shorter I am only bruteforcing 100 PINs in this demo, enough to show how it works.

This work was actually the basis of the [research I recently presented at DEF CON](https://www.martinvigo.com/voicemailcracker/).

## Challenges

At this point, we can find phone numbers associated to Google Meet meetings and we can efficiently and economically bruteforce the PIN. This is sufficient to consider it a threat but there are some drawbacks (from attacker’s perspective) you may be thinking of. Let’s discuss them:

### Meetings are short and at a specific point in time

You may be thinking that in order to bruteforce a meeting you need to launch the attack during the meeting. That is not the case. **From the moment a meeting is scheduled, a phone number is associated and anyone can join anytime, even before the meeting begins**.**** This means that if you try to bruteforce a meeting that is scheduled for next week, you don’t need to wait till then to launch the attack, you can start right away and figure out the PIN. This is important because if not, we would not only have to figure out phone number and PIN, but also when the meeting would take place.

### Google Meet displays who is in the meeting

I would claim that nobody pays attention or verifies that there are no unexpected attendees before starting a meeting, specially for longer ones. Still, we want to be as sneaky as possible and I found some interesting behavior that can be exploited.

#### UI displays only a small amount of attendees

[![Google Meet UI on a 15.4-inch MacBook Pro](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/google-meet-ui.jpg)Google Meet UI on a 15.4-inch MacBook Pro

Depending on your resolution, the UI will only display about 5 attendee profiles. You would have to specifically click through the list to see the other attendees.

#### UI displays name and profile picture when joining on a browser

[![Google Meet impersonation](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/google-meet-impersonation.jpg)Google Meet impersonation

While not relevant to our case (we are targeting “calling in”) it is interesting to mention that while you can see the attendees, what you are looking at is full names and profile pictures. Does it sound trustworthy? Think about it, full names and profile pictures, no email. Email is the only piece of information that is unique to a user in Google. Yet **Google only displays full names and profile pictures. It takes one minute to create a Gmail account and set the full name and profile picture of the person we want to impersonate.** If Google Meet would show the email address, it would not be possible to impersonate attendees.

External attendees must be approved before joining a meeting which mitigates this issue to a certain extent, keep reading.

#### External attendees need to be specifically approved before joining a meeting

If you try to join a meeting using the browser, you will need to be approved if you are not logged into an account assigned to the company’s domain. For example, if you are logged in to Gmail and try to join an ACME Inc. meeting, attendees will get a popup warning that someone external (It is a gmail.com account, not acme.com) is trying to join the meeting.

[![Google Meet approval popup](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/Google-Meet-approval-popup.jpg)Google Meet approval popup

This is not the case for attendees calling in.**Because phone calls cannot be authenticated, anyone is able to join over the phone without any previous approval**. This is very relevant because the security bar was significantly downgraded for attendees calling in VS attendees joining using a browser.

#### Phone numbers are masked

This is an interesting one. For some reason, Google decided to mask the phone numbers of attendees calling in.

[![Masked phone number](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/wp-content/uploads/2018/03/Screen-Shot-2018-03-24-at-5.59.15-AM.jpg)Masked phone number

As you can see, the UI displays phone numbers like 555-XXXX-XX55. I don’t know the reason for this decision but it allows me to perfectly impersonate attendees. **I used the[bandwith.com API](http://dev.bandwidth.com/ap-docs/methods/availableNumbers/getAvailableNumbersLocal.html) to search for available phone numbers using regex expressions. I bought a phone number that looks exactly the same as mine when you mask it like Google Meet does.** It cost 35 cents to impersonate myself.

## Recommendations

### For you

If you use G-Suite, there is a number of things you can do. First off, the admin can disable the option to call into meetings. I am not sure if you can disable it for specific meetings but it is something to consider for meetings where confidential information will be discussed.

If you have to keep the call-in feature available, an option is to share a “password” for every attendee over email or include it in the meeting description. Before starting the meeting, attendees have to say the secret word and everyone can verify it. You would have to be on the lookout for new people joining.

### For Google

  * **Increase the PIN size to make bruteforcing not feasible or too expensive**. Given that you can setup the call to automatically dial the PIN for you, it should be no problem to increase the PIN size to 8+ digits. Specially when some countries already have longer PINs than the US. Also take into account that numbers can be easily guessed as they are assigned sequentially in certain countries. It is worth pointing out that competitors like [GoToMeeting](https://www.gotomeeting.com), [GoToWebinar](https://global.gotowebinar.com/) and [ZOOM](https://zoom.us/) are already doing this.
  * **Maintain the same security bar across countries.** If Spain and Australia have 5 digit PINs, so should the US. Attackers will use the weakest link to join the meeting.
  * **Don’t mask the phone number of attendees that call in and show email addresses of those joining using the browser.** It will prevent impersonation.
  * **Attendees that call in need to be approved before joining.** If Google agrees that external attendees need to be approved before joining a meeting, attendees calling in should be considered external by default instead of trusted. This would at least be a chance to verify the phone number.
  * **Rotate PINs for recurring meetings**. This will prevent ex-employees from still being able to join meetings once they have left the company.

## Responsible disclosure

As always, I reached out to Google first to give them a chance to make changes. Working with them was one of the best engagements I have had so far. Very profesional and appreciative. They also granted me an ELEET bounty.

### Timeline

  * 03/29/2018 responsible disclosure
  * 04/13/2018 Google acknowledges issues and files bugs
  * 05/08/2018 Google issues bounty
  * 07/20/2018 Google confirms fixes
  * 07/28/2018 Google reverts some fixes due to customer complaints
  * 10/04/2018 Google gives green light for public disclosure

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)](https://www.martinvigo.com/author/martinvigo/)

by [Martin Vigo](https://www.martinvigo.com/author/martinvigo/)

I am a Red Teamer and researcher with a background in Product Security and Software Engineering. I focus on pure offensive security work, putting on the black hat to emulate the techniques and procedures of the bad guys to help catch them.

I am also the Founder of Triskel Security, a budding security consultant company offering information security solutions.

I host the Spanish cybersecurity news podcast "Tierra de Hackers".

I spend a lot of time on personal projects, hacking "all the things", presenting results at conferences and sharing knowledge in my blog.

### Share this:

  * [ Share on X (Opens in new window) X ](https://www.martinvigo.com/googlemeetroulette/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://www.martinvigo.com/googlemeetroulette/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://www.martinvigo.com/googlemeetroulette/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://www.martinvigo.com/googlemeetroulette/?share=reddit)
  *
