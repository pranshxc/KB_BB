---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-16_a-5000-idor.md
original_filename: 2019-04-16_a-5000-idor.md
title: A $5000 IDOR…
category: documents
detected_topics:
- access-control
- idor
- command-injection
tags:
- imported
- documents
- access-control
- idor
- command-injection
language: en
raw_sha256: df9fd630116c1402393c7e3e8362668ccd1f03796c6a7f32bfcebc3c065c7e02
text_sha256: 5117c52138a872985d0b6b69985a562dc1c0b2c3e926177eed2be8bf0b53b4ab
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A $5000 IDOR…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-16_a-5000-idor.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `df9fd630116c1402393c7e3e8362668ccd1f03796c6a7f32bfcebc3c065c7e02`
- Text SHA256: `5117c52138a872985d0b6b69985a562dc1c0b2c3e926177eed2be8bf0b53b4ab`


## Content

---
title: "A $5000 IDOR…"
url: "https://medium.com/@mr_hacker/a-5000-idor-f4268fffcd2e"
authors: ["Mr.Hacker (@mr_hacker0007)"]
bugs: ["IDOR"]
bounty: "5,000"
publication_date: "2019-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5306
scraped_via: "browseros"
---

# A $5000 IDOR…

A $5000 IDOR…
?Mr.Hacker
Follow
4 min read
·
Apr 16, 2019

680

6

Hello Everyone!! Mr.Hacker here, in this article I’m going to describe about a critical vulnerability I found in one of the program.

Without wasting your precious time, the vulnerability which rewarded me the bounty was a Critical Idor which lead to broken access control to read messages, send messages, download all files of any user with the customer support.

Hacking Time

So once any user sends a message in the customer support chat box the following request was generated :

Press enter or click to view image in full size
Fig: Request to send messages

As shown in the above image the user has sent “testing by john wick2!” text message which goes in the “text” parameter.

The response from the server was as shown below :

Press enter or click to view image in full size
Fig: Response from server

The sent message was reflected back in the response sent by the server.

Test Case-I : The first test case is obvious one, as seen in the request there is “id” parameter and I tried changing it to other users id and received the following response.
Press enter or click to view image in full size
Fig: Error response from server

2. Test Case-II : I kept the id parameter unchanged and removed the hash value from the “user_hash” parameter, following was the response from server.

Press enter or click to view image in full size
Fig: User hash is invalid

This means user hash value is mapped with the user id and hash is mandatory until I found the idor 😜.

Get ?Mr.Hacker’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Test Case-III : Now I removed the values of “id” and “user_hash” parameters and still received same error from the Fig: User hash is invalid.

4. Test Case-IV : Now only two parameter were remaining “email” and “anonymous_id”, i even made the value of “anonymous_id” to null and received the below response. 😭😭😭😭

Press enter or click to view image in full size
Fig: F*CK!!! YAAA!! IDOR
IDOR!! IDOR!! IDOR!!

Finally IDOR!!.. So this means that the web application was some how misconfigured and on removing the values of all parameters excluding the “email” parameter, the server gave valid response, as shown in the above Fig: Response from server.

Hence now I came to know that the web application only verifies the email id of the user and returns the valid response.

Press enter or click to view image in full size
Fig: Email Id is the IDOR-Request
Press enter or click to view image in full size
Fig: Email Id is the IDOR-Response from server

Hence now if I change the email parameters value to any other users email id then I can read and send messages in his conversation, upload or download files. All I had to do is just shorten the post url till = /messages/web_v1/conversations_parent and the server would politely respond with all the conversation id’s, later I would just append the conversation id to get the conversations of the user, post url would be = /messages/web_v1/conversations_parent/[conversation-id]

Conclusion

Take away points from this article is, even if the server shows an error message on the first test case (Test Case-I), i.e changing the user id to any other users (default case for idor). Here most of them would think that it is not vulnerable to idor and give up.

But try to escalate it further by eliminating all the parameters values one by one and you might hit your target like I did and also it is not necessary that idor is only followed by any numeric value, like in this case the idor was the email, changed to other users email and you would see his conversations. So idor can be anything not mandatory it has to be incremental number only.

That’s it, I hope you liked this article and Happy Hacking!.
