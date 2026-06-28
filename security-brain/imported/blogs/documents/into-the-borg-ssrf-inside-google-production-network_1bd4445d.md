---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-20_into-the-borg-ssrf-inside-google-production-network.md
original_filename: 2018-07-20_into-the-borg-ssrf-inside-google-production-network.md
title: Into the Borg – SSRF inside Google production network
category: documents
detected_topics:
- ssrf
- sso
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- sso
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 1bd4445ded5d276048351077eeb2f83c068a2191cf28acf375a0490359d1c12d
text_sha256: 4f682b509a5a4fc5fd0769938b80b6a2f60b4dea9c0954cdd8af9c3a5866d19d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Into the Borg – SSRF inside Google production network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-20_into-the-borg-ssrf-inside-google-production-network.md
- Source Type: markdown
- Detected Topics: ssrf, sso, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1bd4445ded5d276048351077eeb2f83c068a2191cf28acf375a0490359d1c12d`
- Text SHA256: `4f682b509a5a4fc5fd0769938b80b6a2f60b4dea9c0954cdd8af9c3a5866d19d`


## Content

---
title: "Into the Borg – SSRF inside Google production network"
page_title: "Into the Borg – SSRF inside Google production network | OpnSec"
url: "https://opnsec.com/2018/07/into-the-borg-ssrf-inside-google-production-network/"
final_url: "https://opnsec.com/2018/07/into-the-borg-ssrf-inside-google-production-network/"
authors: ["Enguerran Gillier (@opnsec)"]
programs: ["Google"]
bugs: ["SSRF"]
bounty: "13,337"
publication_date: "2018-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5798
---

July 20, 2018  |  [7 Comments](/2018/07/into-the-borg-ssrf-inside-google-production-network/#comments)

### ![Borglet status monitor](/wp-content/uploads/2018/07/borg2-1024x498.png)

### 

### Intro – Testing Google Sites and Google Caja

In March 2018, I reported an XSS in [Google Caja](https://developers.google.com/caja/), a tool to securely embed arbitrary html/javascript in a webpage.  
In May 2018, after the XSS was fixed, I realised that Google Sites was using an unpatched version of Google Caja, so I looked if it was vulnerable to the XSS. However, the XSS wasn’t exploitable there.

Google Caja parses html/javascript and modifies it to remove any javascript sensitive content, such as iframe or object tags and javascript sensitive properties such as document.cookie. Caja mostly parses and sanitizes HTML tags on the client side. However, for remote javascript tag (<script src=”xxx”>), the remote resource was fetched, parsed and sanitized on the server-side.  
I tried to host a javascript file on my server (https://[attacker].com/script.js) and check if the Google Sites server would fall for the XSS when parsed server-side but the server replied that https://[attacker].com/script.js was not accessible.

After a few tests, I realised that the Google Sites Caja server would only fetch Google-owned resources like https://www.google.com or https://www.gstatic.com, but not any external resource like https://www.facebook.com.  
That’s a strange behavior because this functionality is meant to fetch external resources so it looks like a broken feature. More interestingly, it is hard to determine whether an arbitrary URL belongs to Google or not, given the breadth of Google services. Unless…

### Finding an SSRF in Google

Whenever I find an endpoint that fetches arbitrary content server-side, I always test for SSRF. I did it a hundred times on Google services but never had any luck. Anyway the only explanation for the weird behavior of the Google Caja server was that the fetching was happening on the internal Google network and that is why it could only fetch Google-owned resources but not external resources. I already knew this was a bug, now the question was whether it was a security bug!

It’s very easy to host and run arbitrary code on Google servers, use Google Cloud services! I created a [Google App Engine](https://cloud.google.com/appengine/) instance and hosted a javascript file. I then used the URL of this javascript file on Google Sites as a external script resource and updated the Google Sites page. The javascript was successfully fetched and parsed by Google Caja server. I then checked my Google App Engine instance logs to see from where the resource was fetched and it came from 10.x.x.201, a private network IP! This looked very promising.

I used the private IP as the url for the Google Sites javascript external resource and waited for the moment of truth. The request took more than 30 seconds to complete and at that time I really thought the request was blocked and I almost closed the page since I never had any luck with SSRF on Google before. However, when Google Caja replied, I saw that the reply size wasn’t around 1 KB like for a typical error message but 1 MB instead! One million bytes of information coming from a 10.x.x.x IP from Google internal network, I can tell you I was excited at this point! 🙂  
I opened the file and indeed it was full of private information from Google! \o/

### Google, from the inside

First I want to say that I didn’t scan Google’s internal network. I only made 3 requests in the network to confirm the vulnerability and immediately sent a report to Google VRP. It took 48 hours to Google to fix the issue (I reported it on a Saturday), so in the meantime I couldn’t help but test 2-3 more requests to try to pivot the SSRF vulnerability into unrestricted file access or RCE but without luck.

![Architecture of Borg](/wp-content/uploads/2018/07/borg-1.png)

The first request was to http://10.x.x.201/. It responded with a server status monitoring page of a “Borglet”. After a Google search, I could confirm that I was indeed inside [**Borg, Google’s internal large-scale cluster management system**](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf) ([here](https://www.infoq.com/news/2015/04/google-borg) is a overview of the architecture). Google have open sourced the [successor of Borg, Kubernetes](https://kubernetes.io/blog/2015/04/borg-predecessor-to-kubernetes/) in 2014. It seems that while Kubernetes is getting more and more popular, Google is still relying on Borg for its internal production infrastructure, but I can tell you it’s not because of the design of Borg interfaces! (edit: this is intended as a joke 😛 )  
The second request was to http://10.x.x.1/ and it was also a monitoring page for another Borglet. The third request was http://10.x.x.1/getstatus, a different status monitoring page of a Borglet with more details on the jobs like permissions, arguments.

Each Borglet represents a machine, a server.

On the hardware side, both servers were using Haswell’s CPU @2.30GHz with 72 cores, which corresponds to a set of 2 or 3 Xeon E5 v3. Both servers were using the CPUs at 77%. They had 250GB of RAM, which was used at 70%. They had 1 HDD each with 2TB and no SSD. The HDD were almost empty with only 15GB used, so the data is stored elsewhere.

The processing jobs (alloc and tasks) are very diverse, I believe this optimizes ressource usage with some jobs using memory, others using CPU, network, some with high priority, etc… Some services seem very active : Video encoding, Gmail and Ads. That should not be surprising since video processing is very heavy, Gmail is one of the main Google services and Ads is, well, Google’s core business. 😉  
I didn’t see Google Sites or Caja in the jobs list, so either the SSRF was going through a proxy or the Borglet on 10.x.x.201 was from a different network than the 10.x.x.201 IP I saw in my Google App Engine instance logs.

Regarding the architecture, we can find jobs related to almost all of the components of the [Google Stack](http://malteschwarzkopf.de/research/assets/google-stack.pdf), in particular MapReduce, BitTable, Flume, GFS…  
On the technology side, Java seems to be heavily used. I didn’t see any mention of Python, C++, NodeJS or Go, but that doesn’t mean it wasn’t used so don’t draw conclusions. 😛  
I should mention that Borg, like Kubernetes, relies on containers like Docker, and VMs. For video processing, it seems they are using [Gvisor](https://github.com/google/gvisor), a Google open-source tool that looks like a trade-off between containers performance and VMs security.

Parameters gives some information on how to reach the applications through network ports. On Borg, it seems that all applications on a server share the same IP address and each has some dedicated ports.

Apps arguments were the most fun part for me because it is almost code. I didn’t find Google Search secret algorithm but there was some cool queries like this:
  
  
  MSCR(M(Customer.AdGroupCriterion+Customer.AdGroupCriterion-marshal+FilterDurianAdGroupCriterion+FilterNeedReviewAdGroupCriterion+GroupAdGroupCriterionByAdGroupKey+JoinAdGroupData/MakeUnionTable:3)+M(JoinAdGroupData/MakeUnionTable:2)+M(Customer.AdGroup+Customer.AdGroup-marshal+FilterDurianAdGroup+ParDo(AdGroupDataStripFieldsFn)+JoinAdGroupData/MakeUnionTable)+R(JoinAdGroupData/GroupUnionTables+JoinAdGroupData/ConstructJoinResults+JoinAdGroupData/ExtractTuples+ExtractCreativeAndKeywordReviewables))

If you wonder what’s Gmail system user, it’s 
  
  
  gmail@prod.google.com

There is also a user “legal-discovery@prod.google.com” that has permission “auth.impersonation.impersonateNormalUser” on “mdb:all-person-users”. (edit: for clarification, I just saw these strings close to each other in a big array and assumed that’s what it meant)

There was also a little bit of history which showed that most jobs where aborted before finishing.

At last, there was a lot of url to other servers or applications endpoints. In particular, I tried to access a promising-looking http://wiki/ url but it didn’t work. I tested a 
  
  
  /getFile?FileName=/sys/borglet/borglet.INFO

url but got an unauthorized response. I also tried to change the FileName parameter but got error messages.

### Google VRP response

I reported the issue on Saturday May 12, 2018, and it was automatically triaged as a P3 (medium priority) issue. On Sunday I sent an email to Google Security that they might want someone to have a look at this. On Monday morning the issue was escalated to P0 (critical) then later decreased to P1. On Monday night the vulnerable endpoint was removed and the issue fixed.

It’s not easy to determine the impact of an SSRF because it really depends on what’s in the internal network. Google tends to keep most of its infrastructure available internally and uses a lot of web endpoints, which means that in case of a SSRF, an attacker could potentially access hundreds if not thousands of internal web applications. On the other hand, Google heavily relies on authentication to access resources which limits the impact of a SSRF.  
In this case, the Borglet status monitoring page wasn’t authenticated, and it leaked a lot of information about the infrastructure. My understanding is that in Kubernetes, this page is authenticated.

Google VRP rewarded me with $13,337, which corresponds to something like unrestricted file access! They explained that while most internal resources would require authentication, they have seen in the past dev or debug handlers giving access to more than just info leaks, so they decided to reward for the maximum potential impact. I’d like to thank them for the bounty and for their quick response.

That’s it for this story, I hope you enjoyed it as much I did and feel free to comment!

[Tweet](https://twitter.com/intent/tweet?url=https%3A%2F%2Fopnsec.com%2F2018%2F07%2Finto-the-borg-ssrf-inside-google-production-network%2F&via=opnsec)

[Google](/category/google/) [Borg](/tag/borg/), [Google](/tag/google/), [Kubernetes](/tag/kubernetes/), [SSRF](/tag/ssrf/)
