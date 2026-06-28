---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-24_pen-redirect-in-flock-my-first-swag-pack.md
original_filename: 2017-07-24_pen-redirect-in-flock-my-first-swag-pack.md
title: pen Redirect In Flock | My First Swag pack
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: 85091f943772c434ef1652ae6b6d968ede3e1d27dd89b84ac4e89d94311fbae8
text_sha256: be2b9b5fc1a3b3a44a484f08ecb4125ea9cfabbc542f937809c04f5388464569
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# pen Redirect In Flock | My First Swag pack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-24_pen-redirect-in-flock-my-first-swag-pack.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `85091f943772c434ef1652ae6b6d968ede3e1d27dd89b84ac4e89d94311fbae8`
- Text SHA256: `be2b9b5fc1a3b3a44a484f08ecb4125ea9cfabbc542f937809c04f5388464569`


## Content

---
title: "pen Redirect In Flock | My First Swag pack"
page_title: "Open Redirect In Flock | My First Swag pack"
url: "https://bugbaba.blogspot.com/2017/07/open-redirect-in-flock-my-first-swag.html"
final_url: "https://bugbaba.blogspot.com/2017/07/open-redirect-in-flock-my-first-swag.html"
authors: ["Noman Shaikh (@nomanali181)"]
programs: ["Flock"]
bugs: ["Open redirect"]
publication_date: "2017-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6142
---

###  Open Redirect In Flock | My First Swag pack 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ July 24, 2017  ](https://bugbaba.blogspot.com/2017/07/open-redirect-in-flock-my-first-swag.html "permanent link")

Hello Every one,  
  
  
  
This post is about an [Open Redirect](https://www.netsparker.com/web-vulnerability-scanner/vulnerability-security-checks-index/open-redirection/) that i found in Flock.co back in 2016  
  
  
  
So back then, in 2016 I started finding bugs in various sites  
and all I was getting was duplicate, wont'fix,Thanks and few Hall of Fame :(  
  
One day one of my friend posted about goodies that he has got from Flock  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW-qktPyB2SjaGlUAthzmsBKi6mRttRitK5GdFaNmd89RA6kexTomxGLmlhJ1yAimodOKerfuKHUwHN6VezVRIt1elR_WEXH3Na_8DvqHCp7UmYhyphenhyphenOcT7NIvMXVZ1Sd57zJeK5ffyEX40_/s320/flock.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW-qktPyB2SjaGlUAthzmsBKi6mRttRitK5GdFaNmd89RA6kexTomxGLmlhJ1yAimodOKerfuKHUwHN6VezVRIt1elR_WEXH3Na_8DvqHCp7UmYhyphenhyphenOcT7NIvMXVZ1Sd57zJeK5ffyEX40_/s1600/flock.jpg)

  

  

So i started looking for bugs on it 

  
  
Got one reflected XSS that turned out to be a out of scope site :3  
And one open redirect that got valid :D  
That got me my first swag pack :D  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb-Y1Fs_8Nwrdc5pO82VngEiEa_w0rUSfICEi0bVY552yJnIOzXmLI9VGIiaOU2Gxa32rzdcnnKz84q9Wl8RBXca7COlRxCKyHs2eoueUhhVjFMrRENgMPY4cRVxJw6ana2ax10M15DAr4/s320/flock.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb-Y1Fs_8Nwrdc5pO82VngEiEa_w0rUSfICEi0bVY552yJnIOzXmLI9VGIiaOU2Gxa32rzdcnnKz84q9Wl8RBXca7COlRxCKyHs2eoueUhhVjFMrRENgMPY4cRVxJw6ana2ax10M15DAr4/s1600/flock.png)

  
  
  
Wait a sec ? you didn't came here to read my story :v  
  
  
**Technical part :**  
  
This was there login system  
  
1) User enters login credentials  
2) It gets validated  
3) They Redirect to dashboard  
  
  
This what the redirect url looked liked  
  
https://auth.flock.co/login?auth_token=xyz&platform=BROWSER&redirect_uri=https%3A%2F%2Fflock.co  
  
  
So i changed the redirect_uri parameter value to google.com and it worked ^_^  
  
  
  
  
  
  
  
That's how i got my First Goodie pack.  
  
  
Thanks  
  

[Bugbounty](https://bugbaba.blogspot.com/search/label/Bugbounty)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Ifrah Iman](https://www.blogger.com/profile/18223484683081575239)[26 July 2017 at 03:28](https://bugbaba.blogspot.com/2017/07/open-redirect-in-flock-my-first-swag.html?showComment=1501064886648#c7714157704029964658)

Awsome !

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/7714157704029964658)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Joseph](https://www.blogger.com/profile/15117118685734961265)[10 November 2018 at 15:40](https://bugbaba.blogspot.com/2017/07/open-redirect-in-flock-my-first-swag.html?showComment=1541893223261#c7239807377949776969)

This is awesome! Visit my website https://www.hireprovas.com

Reply[Delete](https://www.blogger.com/comment/delete/6751850223539484706/7239807377949776969)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/6751850223539484706?po=8345941132590864343&hl=en-GB&saa=85391&origin=https://bugbaba.blogspot.com&skin=contempo)
