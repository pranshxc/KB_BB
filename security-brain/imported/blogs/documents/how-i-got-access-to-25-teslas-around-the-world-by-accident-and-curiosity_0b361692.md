---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-23_how-i-got-access-to-25-teslas-around-the-world-by-accident-and-curiosity.md
original_filename: 2022-01-23_how-i-got-access-to-25-teslas-around-the-world-by-accident-and-curiosity.md
title: How I got access to 25+ Tesla’s around the world. By accident. And curiosity.
category: documents
detected_topics:
- api-security
- oauth
- supply-chain
- jwt
- idor
- access-control
tags:
- imported
- documents
- api-security
- oauth
- supply-chain
- jwt
- idor
- access-control
language: en
raw_sha256: 0b3616929f0e6351d19ddced75b5f15399d54e3b5f48e4d7af74bd32eac42b32
text_sha256: b0c795edb0e174f26d9f0c90510a43f408cebb81afec830af8b183e8cadf268e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I got access to 25+ Tesla’s around the world. By accident. And curiosity.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-23_how-i-got-access-to-25-teslas-around-the-world-by-accident-and-curiosity.md
- Source Type: markdown
- Detected Topics: api-security, oauth, supply-chain, jwt, idor, access-control
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `0b3616929f0e6351d19ddced75b5f15399d54e3b5f48e4d7af74bd32eac42b32`
- Text SHA256: `b0c795edb0e174f26d9f0c90510a43f408cebb81afec830af8b183e8cadf268e`


## Content

---
title: "How I got access to 25+ Tesla’s around the world. By accident. And curiosity."
url: "https://medium.com/@david_colombo/how-i-got-access-to-25-teslas-around-the-world-by-accident-and-curiosity-8b9ef040a028"
authors: ["David Colombo (@david_colombo_)"]
programs: ["Tesla"]
bugs: ["Default credentials"]
publication_date: "2022-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2986
scraped_via: "browseros"
---

# How I got access to 25+ Tesla’s around the world. By accident. And curiosity.

David Colombo
 highlighted

How I got access to 25+ Tesla’s around the world. By accident. And curiosity.
David Colombo
Follow
22 min read
·
Jan 24, 2022

392

2

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

How the heck did a 19 year old from Germany manage to be able to take over more than 25 Tesla’s around the world?

This is quite a story so buckle up and get in for a good read!

Important: This is not a vulnerability in Tesla’s infrastructure directly, but Tesla is still responsible for many security shortcomings.

What am I even talking about?

In short: I was able to run remote commands such as “disable Sentry Mode”, “unlock the doors”, “open the windows” and even “start Keyless Driving”.

Press enter or click to view image in full size

You see where this is going? Someone with malicious intent could even steal the car.

I, fortunately, did not have any access to the steering, accelerator & brakes and any other driving safety critical feature (although I might have been able to use the summon feature to get the car moving, but I cannot confirm if this would have been possible).

Nonetheless, there should be no way at all that someone could literally walk up to some Teslas they do not own and take them for a drive.

I also think it potentially could result in some dangerous situations on the road. For example, if someone with remote access starts blasting music on max volume while the driver is on the highway, or randomly and uncontrollable remotely flashing the lights of the Teslas at night.

I would prefer that not to happen.

Press enter or click to view image in full size
Feel free to ignore this image. It is only here to be displayed in thumbnails.

Legal Disclaimer, before I proceed: This is all part of Security Research and I purely have good intent. As soon as I can confirm a vulnerability exists I immediately report it to the affected and involved parties. This writeup is part of responsible disclosure to the third-party maintainer and the Tesla Security Team.

Full Timeline

To get a quick overview of all important events. Detailed report below.

Timestamp Format (yyyy-mm-dd). All dates are in CET.

2021–10–29: First got aware of this issue (found the first affected third-party instance).

2021–10–29: Contacted the owner.

2021–11–01: Got the instance taken down.

2022–01–09: Searched internet-wide for affected third-party instances.

2022–01–10: Found more than 20+ in 12 countries.

2022–01–10: Tried to find owner-identifying information.

2022–01–10: Reported this to two Tesla owners I was able to find.

2022–01–10: Tweeted about it, because I was frustrated that I couldn’t identify more Tesla owners.

2022–01–10: The Tweet exploded.

2022–01–10: Number of found instances grew to 25+ in 13 countries.

2022–01–10: I talked to the renowned cyber security export John Jackson, who recommended I get a CVE-ID assigned for this, so the issue can be handled more efficiently.

2022–01–11: Requested a CVE-ID from MITRE. Providing preliminary information.

2022–01–11: Prepared this detailed writeup to describe the full situation.

2022–01–11: Contacted the Tesla Product Security Team to get the affected owners notified asap.

2022–01–11: Contacted the third-party maintainer to possibly get a patch ready.

2022–01–11: Shared additional information regarding affected owners with the Tesla Product Security Team.

2022–01–11: MITRE granted the CVE-ID request. CVE-2022–23126 pending.

2022–01–11: The Tesla Product Security Team confirmed they are investigating the case.

2022–01–12: The third-party maintainers released version 1.25.1 with a partial fix.

2022–01–12: Tesla revoked thousands of potentially affected API tokens at 6:30 UTC / 7:30 CET.

2022–01–12: Tesla actively forced some affected users to reset their passwords.

2022–01–12: Waiting on further response from the Tesla Product Security Team.

2022–01–12: Worked with the third-party maintainer to explore potential further patches (encrypting the critical access tokens).

2022–01–13: The Telsa Security Team confirmed they revoked all affected API access tokens and all the affected Tesla owners have been notified by email and push notification.

2022–01–13: Some of the previous affected Tesla owners still seem to be affected.

2022–01–18: In contact with Tesla again, waiting on clarification from the Tesla Security Team.

2022–01–19: Tesla revoked another batch of access tokens.

2022–01–19: Discovered and reported an additional vulnerability, this time affecting Teslas API directly.

2022–01–22: Tesla confirmed the additional vulnerability and rolled out a fix into production.

2022–01–24: Public Release of this Writeup.

2022–01–24: Provided all information to MITRE / the CVE assignment team.

2022–01–24: CVE-2022–23126 published.

2022–05–12: More in-depth into the CVE: https://www.youtube.com/watch?v=fG9ySnNQVxI

But now: Who even am I?

I’ll keep it short, I promise.

So, I’m David Colombo, 19 years and from the beautiful state of Bavaria in Germany (to be a bit more exact, around 2 hours from Munich).

I started coding back when I was around 10 and then somehow dived into cyber security (my school wasn’t very happy when their info screens didn’t display school information anymore).

With 15 I basically dropped out of school (with special permission from the German chamber of commerce to only go to school 2 days a week) to educate myself even more in that area and start a company with the goal to improve the current cyber security landscape. The company is now known as Colombo Technology, providing Security Audits, Penetration Tests & Cyber Security Consulting among other services.

Since then I’ve found various security vulnerabilities at e.g. RedBull, the U.S. Department of Defense and numerous more organizations under NDAs.

Now, what’s the issue with the Tesla’s? The fun part.
Press enter or click to view image in full size
When did I get aware of this for the first time?

That’s the fun background story about how I initially got aware of this issue. Feel free to skip this, the more recent events are further below.

It started last year actually. I was about to get in contact with a client for my company regarding a Security Audit. A pretty cool SaaS company from Paris.

And then, you know how it is, curiosity kicked in. I already wanted to take a peek look at their infrastructure to get some basic information about what services and platforms they use, I didn’t even start a full fledged Security Audit yet. Maybe, I thought, I’d even very quickly find some outdated software or exposed backup database that I could show them in the next meeting. Oh boi, was I wrong. It was about to get much better.

When doing some basic subdomain enumeration, I found a backup.redacted.com domain. Looks interesting, right?

But there wasn’t anything running besides a plain “this works” page.

The end.

Hm, really? I mean I wouldn’t be good at my job, if I stopped right there. The exposed database would likely not run on the web ports either way.

A very light nmap scan produced some results, but did only find remoteanything and some “game server” ports. Strange enough.

The, for a backup server, weird namp scan

Connecting via telnet didn’t work.

Telnet didn’t quite work

But… simply accessing those ports now in the browser brought up something interesting.

Let me introduce you to TeslaMate:

Press enter or click to view image in full size

This already looked a lot more interesting now.

But trying to access the Dashboards or anything didn’t work.

Press enter or click to view image in full size
Accessing Dashboards only gave me an error.

So I thought yeah, this is nice, I can see where this Tesla is parked. Let’s go and report this.

But once again, curiosity came in to play. I must say, I am a huge Tesla fan myself. So I really wanted to know what exactly this thing was.

TeslaMate is a pretty cool application. A self-hosted data logger for Tesla’s. And it’s open source, so you can find everything on GitHub.

It’s only intended for pulling data and storing as well as displaying them. You can not run any commands like unlocking doors using the TeslaMate Dashboard. (We’ll get to how running commands is still possible later.)

By taking a look into the Dockerfile you’ll see it also brings a Grafana installation with it. Hah — the inaccessible Dashboards.

The port 5555. Let’s try to access that.

Press enter or click to view image in full size
Upsie, I know where you went on vacation. It’s definitely not freeciv as nmap claimed.

Me after seeing that: sorry what? 0.o

I was able to see a large amount of data. Including where the Tesla has been, where it charged, current location, where it usually parks, when it was driving, the speed of the trips, the navigation requests, history of software updates, even a history of weather around the Tesla and just so much more.

Update: Unauthorized guest access to the Grafana dashboards containing these sensitive information is now disabled. Fixed with TeslaMate release v1.25.1, that got released after I notified the maintainers of the issues.

This was… not good. And now I definitely knew this is an issue that I should report. I should not be able to know where the CTO of this SaaS company went on vacation last year.

But now curiosity strikes for the third time. Or the fourth time?

I really wanted to know how TeslaMate works. Because… if it is able to pull all the vehicle data it might also have a way to send commands to the Tesla?

After that thought I spent some time reading the TeslaMate source code in order to figure out how the authentication works, how the Tesla credentials flow through the app and where it stored the user’s API key.

Long story short, it does save the API key where it also stores all the other data. The API key is neither stored separate nor is it encrypted.

So, if Grafana can access the vehicle data, and the API key is stored next to the vehicle data, can Grafana read and output the API key?

Well, there is Grafana Explore to run custom queries. This needs authentication tho. What a bummer.

Ever heard about this distant cyber security issue called… “default passwords”? Yep, TeslaMate Docker’s Grafana installation comes with default credentials.

It also is possible to query the tokens as an unauthorized anonymous user without logging in through a Grafana endpoint (see CVE-2022–23126 further below as well as TeslaMate patch v1.25.1 released after private disclosure and the screenshot that is included further below).

For that please watch the webinar released in cooperation with the Automotive Security Research Group: https://www.youtube.com/watch?v=fG9ySnNQVxI

I took the shot and tried logging in with admin:admin which, kinda unsurprisingly, but still hilariously it worked.

Building a Query String for Grafana (Explore) and querying the API tokens wasn’t magic after that.

That was the point where I was able to fully confirm that in this case it is indeed possible that some external attacker could do these steps and end up having substantial control over the CTO’s Tesla.

Which I deemed a high to critical security issue. No one should be able to unlock the SaaS company’s CTO’s Tesla doors… So I immediately stopped there and contacted the organization and get this resolved.

With that the whole thing was done for me. Last year.

This weekend a random thought crossed my mind.

TeslaMate is basically Insecure-By-Default, that means if it is deployed with it’s default Docker configuration or the docker image with default configuration is used then TeslaMate is exposed and vulnerable to this.

Get David Colombo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

CWE-1188 has a perfect description for it:

The software initializes or sets a resource with a default that is intended to be changed by the administrator, but the default is not secure.

Developers often choose default values that leave the software as open and easy to use as possible out-of-the-box, under the assumption that the administrator can (or should) change the default value. However, this ease-of-use comes at a cost when the default is insecure and the administrator does not change it.

What if… there are more of such exposed instances on the internet?

I was pretty busy and didn’t have time for it but I couldn’t get rid of the thought. So I had to take a look. And I searched the internet for exposed stuff once again, yay. Just that it this time was exposed access to vehicles.

Another thing that made me start searching for this again was, that you apparently no longer need the users password to issue a Keyless Driving API call.

Press enter or click to view image in full size
As of Dec 1, 2021 you apparently no longer need a password to start Keyless Driving.
How to gain access to random Tesla’s all the around the world:
Run an internet-wide search for TeslaMate instances (search e.g. for the MQTT brokers).
Make sure they run with the insecure default Docker configuration (this should be fixed by now, as user please pull the latest version asap).
Go to port 3000 to access the Grafana dashboard.
Login using default credentials (of course only do that with explicit authorization).
Go to the Explorer tab.
Use the Query Builder to extract the API and refresh tokens.
Have fun playing around with a Tesla (of course only with vehicles you own).

Alternatively to logging in, if for example the owner changed the admin password (as they should have), you could also run arbitrary requests to the TeslaMate data source as unauthorized anonymous Grafana user through a Grafana API endpoint. See CVE-2022–23126. This only affects the TeslaMate docker and is patched by now. See the screenshot below.

Press enter or click to view image in full size
Press enter or click to view image in full size
Querying the Tesla API token from Grafana without submitting credentials or login cookies.

Regarding details of the critical vulnerability in the code please watch my session which will be released by the Automotive Security Research Group on May 12th 2022.

Things that are possible using the Tesla API token include, but are not limited to:

Unlocking the doors.
Opening the windows.
Starting Keyless Driving.
Sharing videos to the Tesla.
Changing heater/cooler settings.
Honking the horn & flashing the lights.

Funfact: It even is / would have been possible to open and close some garage doors (if the garage doors are connected to the exposed Teslas, see https://tesla-api.timdorr.com/vehicle/commands/homelink).

A full list can be found here: https://tesla-api.timdorr.com/

As you can see it’s a long list of possible data to query or commands to run.

You could run commands that annoy the shit out of the Tesla owner (imagine music blasts at max volume and every time you want to turn it of it just starts again or imagine every time you unlock your doors they just lock again), you could watch every move the Tesla owner does (it’s kinda strange watching people driving to get groceries or knowing exactly where they live and yet there’s no way you can report that to them) and you could even steal the Tesla as already mentioned in the introduction of this writeup.

And there I was… sitting in front of substantial remote access capabilities to those Tesla vehicles (in one of the later screenshots you’ll see the access_type will be “owner” since it’s the Owner API).

But first let’s take a look at some of these beautiful (exposed) Teslas all around the world!

Press enter or click to view image in full size
Tesla Model Y driving in California.
Press enter or click to view image in full size
Tesla driving in Europe.
Press enter or click to view image in full size
Tesla Model 3 driving in (mainly) in Belgium
Press enter or click to view image in full size
Tesla Model 3 driving in the UK
Press enter or click to view image in full size
Tesla Model Y driving in Florida.
Press enter or click to view image in full size
Tesla Model 3 driving in Denmark.
Press enter or click to view image in full size
Model Y driving in and around Kitchener (Canada).

I actually found 25+ Tesla’s from 13 countries within hours. Including Germany, Belgium, Finland, Denmark, the UK, the US, Canada, Italy, Ireland, France, Austria and Switzerland. There were about at least an additional 30+ from China, but I really did not want to mess with China’s cyber security laws so I left them completely untouched.

My initial scan resulted in 300+ found instances, but I haven’t been able to confirm whether all of these were vulnerable since the Tesla Security Team asked me to not access any more instances until further notice.

Update: Since Tesla revoked thousands of keys this might have been an even more widespread issue.

If you find any confirmed affected instance, please immediately notify the rightful owner or the Tesla Security Team (vulnerabilityreporting@tesla.com).

How did this whole thing unfold?
Well, what do you do if you find such vulnerabilities?

You report it to the responsible owner.

With one Tesla owner it was quite an OSINT journey. Searching through WHOIS records, taking a look at SSL certs, and trying to figure out aliases & online profiles. In the end I luckily managed to find the guy on Twitter. Greetings to Michael and his Model 3 at this point!

But what do you do if you can’t find the responsible owner?

Tweet about it ¯\_(ツ)_/¯

First public Tweet regarding this matter

Jokes aside, I actually posted that Tweet solely because I got frustrated. After a full day of finding exposed Teslas I was only able to find two Tesla owners to report it to them. Remember, two out of more than two dozen Teslas.

And I’m very sorry for all the confusion and/or speculations that this Tweet might have caused. Next time I’ll definitely coordinate this differently.

And then… the Tweet blew up.

To respect the privacy of the affected Tesla owner I have modified the following section to censor owner-identifying information as requested by him. The affected Teslas name has been changed to “Blue Giant” for this writeup.

I actually found another affected Tesla owner from Ireland thanks to the Tweet. I commented about one specific name of a Tesla called “Blue Giant” and after some time later I woke up to this:

Press enter or click to view image in full size
Press enter or click to view image in full size
Verifying it is his Tesla using the VIN.

Turns out the Blue Giant from Ireland on my list actually is his Blue Giant.

Press enter or click to view image in full size
Having Blue Giant honking.
Scary Throw-In:

The API tokens that allowed for this kind of access to “Blue Giant” stayed active and did not get revoked even after the owner explicitly and multiple times reset his Tesla Account password.

4 hours later we finally managed to figure out a way to get the Tesla API to revoke the keys through an undocumented API endpoint (see further below).

Coordinated disclosure with the Tesla Security Team

After I figured out there’s no (legal) way I’d be able to find the contact details of the affected owners (and I really didn’t want to put a “you’re hacked” video on the screen of random Teslas, as some folks on Twitter recommended), I talked to the Tesla Product Security Team.

They confirmed they are investigating the issue and then following on that revoked all affected and legacy tokens shortly after.

As of now 13. January 2021 all of the affected users also should have been notified by email, according to the Tesla Security Team.

So go check your inbox, if you at one point had TeslaMate deployed.

Continuous Token Revocation

Some Tesla access tokens were still exposed to the internet, even after the second token revocation of the Tesla Security Team, probably because the users signed in to the vulnerable TeslaMate instances again.

So I built a quick Python script to automatically revoke exposed access tokens from vulnerable instances myself.

Bad news, there doesn’t seem to be a way to revoke version 3 tokens.

If I‘ll find a way to revoke version 3 tokens, I could simply pipe the internet-wide scans into this script to automatically and continuously revoke any further exposed access tokens from vulnerable instances.

RE: CVE-2022–23126 with CWE-1188
Press enter or click to view image in full size

Since there was quite a number of affected Tesla owners and it would be very useful to be able to share a CVE-ID with all TeslaMate users (and because CWE-1188 fits so perfectly here), I requested a CVE number for this vulnerability.

The CVE request was successful and MITRE published the CVE.

CVE-2022–23126 description (that I suggested, MITRE chose another one):

“TeslaMate’s default Docker configuration prior version 1.25.1 allows for an attacker to obtain a victim’s generated token, giving them the ability to perform unauthorized actions via Tesla’s API such as controlling certain critical features of the vehicle or disclosing sensitive information.”

Released patches for CVE-2022–23126:

Release v1.25.1 · adriankumpf/teslamate
Disable anonymous logins to Grafana by default (when using the teslamate/grafana Docker image) The first time you visit…

github.com

Note: This is not the personal fault of the maintainer! It’s an open source project, that grew over time and something like this can happen.

Please watch the ASRG webinar so learn more about this: https://www.youtube.com/watch?v=fG9ySnNQVxI

Recommendations for mitigating this CVE

Just… don't… connect critical stuff to the internet. It’s very simple.

And if you have to then make very sure it is set up securely and not with insecure defaults. Here are the TeslaMate Docs to setup more advanced auth: https://docs.teslamate.org/docs/guides/traefik

Oh, and please built solid APIs. An API with security in mind could have prevented this with ease.

Update: A patch has been released. Please update to at least version 1.25.1

Additional finding affecting Teslas API

After a Twitter exchange with Tyler Corsair (founder of Teslascope) who mentioned that there should be an endpoint to query owner-identifying information using version 3 tokens, I started searching for that endpoint.

It actually was pretty easy to find it in retrospect. Although there is no official Tesla OAuth documentation, Tesla was nice enough to add the endpoint somewhere else.

Version 3 access tokens, other than version 2 access tokens, are JWTs. And if you decode them you can see this:

Press enter or click to view image in full size
Decoding a version 3 access token for the Tesla API.

Additionally to the https://owner-api.teslamotors.com/ endpoint for the vehicle commands it also shows https://auth.tesla.com/oauth2/v3/userinfo for, well, user information. Yay, finally a way to get the owners email addresses. (Tesla has asked me not to use those email addresses to notify owners of exposed Teslas.)

But, to my very surprise, I noticed I could query the email addresses of Tesla owners using tokens that got already revoked by the Tesla Security Team. See here:

Press enter or click to view image in full size
Querying the emails of Tesla owners using tokens that are revoked by Tesla.

At the beginning of the story I didn’t have any way to find owner-identifying information and now I can query email address even with revoked access. Kind of ironic!

I reported this issue to the Tesla Security Team immediately. They confirmed the vulnerability and rolled out a fix into production shortly after. This one is also eligible for bug bounty from Tesla :D (I hope this pays for all my coffees of the past two weeks.)

Addition on January 26th, regarding Pin-to-Drive

I originally suggested the following to all Tesla owners:

Enable Pin-to-Drive to prevent anyone from stealing your Tesla even with valid API access tokens or account credentials.

But apparently Pin-to-Drive gets bypassed by the Keyless Driving API call.

What should be done to prevent this from happening again?
(Affected) Tesla Owners:
Be very very careful who you give your credentials to.
Update TeslaMate (and any other third-party Tesla software you use) to the latest version and keep an eye on further security updates.
Do not put random stuff on the internet.
We found a way to revoke potentially compromised API tokens (see the image below). This unfortunately only works with version 2 tokens which are deprecated now. There doesn’t seem to be a way to revoke version 3 tokens yet.
Third-Party Maintainers:
Build software with the highest level of security in mind.
All dashboards and databases containing sensitive data should only be accessible with authentication (Update: already fixed with release of TeslaMate v1.25.1, that got quickly released after I shared this writeup privately with the maintainer.)
Do not store critical access tokens accessible. Store it in a way it’s not accessible via external access. At best encrypted. (This is currently under consideration for TeslaMate. See https://github.com/adriankumpf/teslamate/pull/2360)
Tesla:
Press enter or click to view image in full size

Yes, I do think Teslas security measures are okay, but there is room for some major improvement:

Add multiple scopes to the API! People are going to use it anyways make it secure for them. Just add multiple scopes like: Read-Only Scope (for third-party software that only needs to collect data), Non-Critical Scope (seat heater, etc), Critical Scope (unlocking doors, keyless driving, etc).
Require the password for the Keyless Driving API endpoint again (I have no idea why this additional auth step was removed).
Revoke API tokens when the Tesla account password is reset! (Alternatively implement an easy way to revoke API keys manually)
Since Tesla API tokens are basically car keys, but can be generated easily, copied and used multiple times in multiple places, Tesla should/could implement an easy way to keep inventory of & track Tesla API tokens.
Finally add the “press in case of hacked to cut cloud connectivity” button to the cars that Elon Musk mentioned in 2017 ;)
Why did this happen?
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
FAQ
Whose fault is that?

It basically is a concatenation of issues that in the end lead to me being able to have control over those cars. The owners, the third-party maintainer as well as Tesla itself could have done steps to prevent this all from happening.

Would I have been able to move the car?

Not as far as I know, but renowned cyber security researcher John Jackson who had insights on this issue pointed out that it might have been possible to utilize the “summon” feature to get the car moving and potentially even hit something.

Why didn’t I tell Tesla first?

Tesla is not responsible for owner or third-party issues. Luckily they still helped in remediating this and protecting the affected Tesla owners. And maybe they’ll even implement some recommendations to give their users and even more secure experience.

Is there an issue with the initial Tweet?

Kind of, it should have said “remote control over certain (critical) features (including being able to turn off Sentry Mode, unlocking doors and starting Keyless Driving)” rather than simply “full remote control”.

Although I clarified it in the following Tweets and did my best to get the facts to all media who reported on this, I’m sorry for any confusion caused.

Why did it take so long to release the Writeup after the initial Tweet?

Since this is still part of responsible disclosure, I had to talk to the Tesla Security Team as well as the third-party maintainer first and I also had to make sure all of the exposed Teslas (that I was aware of) are no longer affected by the issues.

Is TeslaMate bad software in general?

No! It is an amazing piece of software with an awesome maintainer. And I do not want to put any blame on the maintainer, since he is interested in making it secure for all users as much as I am. Furthermore are primarily the Docker installations affected and every user using the great Advanced Setup Guides (https://docs.teslamate.org/docs/guides/apache) should not be affected.

What’s next?

I’ll definitely continue researching security related to Tesla, since I want Tesla owners and their cars to be as secure as possible. I’d love to get my hands on a Tesla hardware and/or a Tesla MCU.

Automotive security is a very important topic, especially as other automakers, such as VW, join in digitizing their fleets.

If you need to contact me personally, feel free to send me a DM on Twitter (https://twitter.com/david_colombo_) or contact me on LinkedIn (https://linkedin.com/in/david-colombo).

To contact the Colombo Technology Cyber Security Team, please email cybersecurity@colombo.technology or go to our contact form here.

Let’s make the internet out there more secure for everyone!

Special Thanks to: John Jackson (Security Researcher), Adrian (TeslaMate Maintainer), Nathan (Tesla Product Security Team).
