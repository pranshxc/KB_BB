---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-05_whatsapp-bug-bounty-bypassing-biometric-authentication-using-voip.md
original_filename: 2022-03-05_whatsapp-bug-bounty-bypassing-biometric-authentication-using-voip.md
title: 'WhatsApp Bug Bounty: Bypassing biometric authentication using voip'
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: de8b28c91a8bd8e431c17e4ea5f59a5235e360a5c57a27dfbc2bbf0995a94ffc
text_sha256: 9d60394ce7e3a2c282800072587969ad498fc991f6a1fcff4f56c51796603e08
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# WhatsApp Bug Bounty: Bypassing biometric authentication using voip

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-05_whatsapp-bug-bounty-bypassing-biometric-authentication-using-voip.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `de8b28c91a8bd8e431c17e4ea5f59a5235e360a5c57a27dfbc2bbf0995a94ffc`
- Text SHA256: `9d60394ce7e3a2c282800072587969ad498fc991f6a1fcff4f56c51796603e08`


## Content

---
title: "WhatsApp Bug Bounty: Bypassing biometric authentication using voip"
url: "https://infosecwriteups.com/whatsapp-bug-bounty-bypassing-biometric-authentication-using-voip-87548ef7a0ba"
authors: ["Arvind (@ar_arv1nd)"]
programs: ["Meta / Facebook"]
bugs: ["Authentication bypass"]
publication_date: "2022-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2850
scraped_via: "browseros"
---

# WhatsApp Bug Bounty: Bypassing biometric authentication using voip

WhatsApp Bug Bounty: Bypassing biometric authentication using voip
Arvind
Follow
3 min read
·
Mar 6, 2022

168

4

Press enter or click to view image in full size

Note: This is being published with the permission of Facebook under the responsible disclosure policy. The vulnerability is now fixed.

In Android, WhatsApp “Screen Lock” feature allows the user to lock the app using available device biometric credentials (Fingerprint, Face ID, PIN, and Pattern).

The “Auto Lock” feature will lock the app automatically after user-specified duration. If the user opted for “1 minute”, then the app will be locked after 1 minute of inactivity.

The issue here is, if the user receives a WhatsApp call from someone after 1 minute or later, then the app FAILS to lock. So an attacker can easily bypass the biometric lock just by making a call and rejecting it to access the app completely (read chats, send messages…).

Bypass steps:

Enable biometric lock and set auto lock duration (1 min or any).
Close the app.
After 1 minute or later, make a call to that device.
Reject the incoming call and open WhatsApp.
Technical root cause

tl;dr

Auto-lock implementation sample code:

public class App extends Application {
  public void onCreate() {
  super.onCreate();
  registerActivityLifecycleCallbacks(activityLifecycleCallbacks);
  }

  ActivityLifecycleCallbacks activityLifecycleCallbacks = new ActivityLifecycleCallbacks() {

  public void onActivityResumed(Activity activity) {
  if(!excludedActivityList.contains(activity)) &&  
  SystemClock.elapsedRealtime() - getAppClosedTime() >=  USER_SPECIFIED_DURATION) {
  lockTheApp();
  }
  }

  public void onActivityPaused(Activity activity) {
  saveAppClosedTime(SystemClock.elapsedRealtime());
  }
  };

}

“Any screen inactivity listener”: WhatsApp will be auto-locked after timeout even if the user minimized it from any activity like chat, home, or settings screen. To implement this, WhatsApp registers “Activity Lifecycle Callback” in the {Application.class}.

Get Arvind’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Code Flow:

When the call is received, {CallActivity.class} is started.

2. After the call is ended, {CallActivity.class} is closed and the method {onActivityPaused()} is called.

Method: onActivityPaused()

Stores the current “device up time” {SystemClock.elapsedTime()} as {app closed time}.

3. Now when the app is reopened, method {onActivityResumed()} is called.

Method: onActivityResumed()

It calculates the “time difference” between current “device up time” and the stored {app closed time}. If it is > {user specified duration}, then only it will lock the app.

It fails to lock now because the {app closed time} is saved after the call is ended and the “time difference” is < {user specified duration}.

public void onActivityPaused(Activity activity) {
  if(!excludedActivityList.contains(activity)) {  
  saveAppClosedTime(SystemClock.elapsedRealtime());
  }
}

Fix:

The method {onActivityPaused()} and {onActivityResumed()} will be called whenever any activity of the app is paused/resumed.

So this issue can be fixed by checking the activity class name and not saving the {app closed time} if it is {CallActivity.class}.

Press enter or click to view image in full size

Thanks for reading this article.

Twitter: https://twitter.com/ar_arv1nd

The Infosec Writeups team just completed our first Virtual Cybersecurity Conference and Networking event. We had 16 amazing speakers who conducted super valuable and inspiring sessions. To check the list of speakers and topics, and to get lifelong access to recorded versions of all 16 talks, click here.

IWCon2022 — Infosec WriteUps Virtual Conference
Network With World’s Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.liv
