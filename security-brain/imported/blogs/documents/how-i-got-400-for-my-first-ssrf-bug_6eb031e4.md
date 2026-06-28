---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-01_how-i-got-400-for-my-first-ssrf-bug.md
original_filename: 2021-05-01_how-i-got-400-for-my-first-ssrf-bug.md
title: How I got $400 for my first SSRF bug?
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 6eb031e46b2c034b11941ca38b0a6546a1224c0eb4d7a1ba74cf7bd067b6a46d
text_sha256: 4a1d8ce96b1bba31109e51fb1f01f972943046abc534e0e1c3915a12074a3948
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $400 for my first SSRF bug?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-01_how-i-got-400-for-my-first-ssrf-bug.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `6eb031e46b2c034b11941ca38b0a6546a1224c0eb4d7a1ba74cf7bd067b6a46d`
- Text SHA256: `4a1d8ce96b1bba31109e51fb1f01f972943046abc534e0e1c3915a12074a3948`


## Content

---
title: "How I got $400 for my first SSRF bug?"
url: "https://blog.usamav.dev/how-i-got-400-usd-for-my-first-ssrf-bug"
final_url: "https://blog.usamav.dev/how-i-got-400-usd-for-my-first-ssrf-bug"
authors: ["Usama Varikkottil (@usama_dev)"]
bugs: ["SSRF"]
bounty: "400"
publication_date: "2021-05-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3688
---

# How I got $400 for my first SSRF bug?

An easy-to-exploit SSRF vulnerability.

PublishedMay 1, 2021

•3 min read•[ __View as Markdown](/how-i-got-400-usd-for-my-first-ssrf-bug.md)

![How I got $400 for my first SSRF bug?](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1619895368945%2Fedp26jxVy.png&w=3840&q=75)

[ U](https://hashnode.com/@usamav)

[Usama Varikkottil](https://hashnode.com/@usamav)

[ __](https://twitter.com/usama_dev)[__](https://www.linkedin.com/in/usama-varikkottil)

A story about my first SSRF finding on a bug bounty target web app, where I further exploited the SSRF bug into reading internal server files, which leads to AWS instance secret leakage. There were no filtering or firewalls on my target. So let's jump straight into the bug exploitation.

The target was a productivity app. There was a feature to create and manage projects in it. After spending almost 8+ hours exploring app.target.com features, I came to notice a button that prints the projects created on my account. 

![Untitled.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618731184323/ME5EiUYyZ.png)

When I clicked the button, a PDF was generated with my project in it. Okay, enough for opening up Burpsuite, it seems interesting to dive deep into it. And I intercepted the HTTP request that is going to the server when I click on the `Print` button. And it was very interesting.

![Untitled 1.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618737098087/ewQ3FKOB_.png)

There was an `html` parameter, which contains a whole bunch of HTML codes, which the PDF generates from it. 

I tried sending the request by entering some random HTML codes as the `html` parameter value, and it generated the PDFs successfully. 

![Untitled 2.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618732236151/MzppRnQK6W.png)

![Untitled 3.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618737158606/f5TWromwc.png)

Alright, now let's try sending some `iframe` tags as the `html` parameter's value. I tried embedding my personal website using the `<iframe>` tag.
  
  
  <iframe src=https://www.usamav.dev width=100% height=100%>
  

The generated pdf contained my personal website embedded in it. Cool...

The next step is to access the internal files using `<iframe>` tags. First, let's start with `/etc/passwd`.
  
  
  <iframe src=file:///etc/passwd width=100% height=100%>
  

This generated a pdf with the following content.

![Untitled 4.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618737186476/a2EK1xZsl-.png)

The target was running on an AWS EC2 server. So it's time to access AWS EC2 server meta-data. As per [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html), 

> "To view all categories of instance metadata from within a running instance, use the following URI. <http://169.254.169.254/latest/meta-data/>. The IP address 169.254.169.254 is a link-local address and is valid only from the instance."

We can try embedding the above URI in the PDF using the `<iframe>` tag to access the meta-data.
  
  
  <iframe src="http://169.254.169.254/latest/meta-data"+width="100%"+height="100%"></iframe>
  

This was also successful. I immediately got the pdf with the meta-data in it.

![Untitled 5.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618737208263/ttwN3L5K8.png)

I was able to access some confidential data such as secret_key, private access key, internal server files, mac address, user details, instance details, etc.

The whole process took a little while than I expected. Because whenever I sent a request with the HTML codes to the server, I get a unique code for that PDF, to access the generated PDF, I needed to copy that unique code and paste it on another endpoint on that API. So to automate this boring task, I made a quick python script to automate the PDF generation. 

And finally, I spend almost 1 day alone writing a bug report and sent it to the responsible security team. Within a few hours, they responded to my report. I also sent the python script along with the report. I was so excited as this is my first ever SSRF finding on a real-world target. 

![Untitled 6.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1618737233606/yM4e2urdB.png)

Although, the bug was not a critical finding as I expected. ![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1619723399611/5LS2X_9zn.png)

And finally, I received the bounty amount of $400 on 22nd April 2021.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1619724049130/ntk5LysHy.png)

* * *

As you have read till here, you would've noticed that this bug is such an easy-to-exploit bug. No firewall, no fancy bypassing techniques, not so complicated, just a straightforward bug.

However, writeups of easy findings motivate me oftentimes. Every time I read similar writeups of some kind of easy bugs, I feel like I have enough skill to start hunting a target application. Usually, those writeups help me to escape from the tutorial hell and push me to start doing the work.

I hope this write-up will also motivate someone to hunt your target for bugs. You can always reach out to me on Twitter at [@usama_dev](https://twitter.com/usama_dev)

Good luck... and Thanks for reading till here...

[#security](/tag/security)[#webdev](/tag/webdev)[#hacking](/tag/hacking)[#hack](/tag/hack)

 __1.6K views
