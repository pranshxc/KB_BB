---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-27_how-i-found-ssrf-on-thefacebookcom.md
original_filename: 2017-12-27_how-i-found-ssrf-on-thefacebookcom.md
title: How I found SSRF on TheFacebook.com
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
language: en
raw_sha256: 3db78d92d2229267eb8c30fd44cbd375ce363b59bbccdd40c92f12fe233e71c3
text_sha256: 9cc5041cfa56d164433015742dbc2b736e1aaa93c9a750319d45de2797eae897
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I found SSRF on TheFacebook.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-27_how-i-found-ssrf-on-thefacebookcom.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `3db78d92d2229267eb8c30fd44cbd375ce363b59bbccdd40c92f12fe233e71c3`
- Text SHA256: `9cc5041cfa56d164433015742dbc2b736e1aaa93c9a750319d45de2797eae897`


## Content

---
title: "How I found SSRF on TheFacebook.com"
page_title: "Security Research * Penetration Testing Blog: How I found SSRF on TheFacebook.com"
url: "https://w00troot.blogspot.com/2017/12/how-i-found-ssrf-on-thefacebookcom.html"
final_url: "https://w00troot.blogspot.com/2017/12/how-i-found-ssrf-on-thefacebookcom.html"
authors: ["Thunder"]
programs: ["Meta / Facebook"]
bugs: ["SSRF"]
publication_date: "2017-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6022
---

Hello World,

  

Hope you'll are doing well & I know you are reading this post after reading the post title, SSRF on Thefacebook.com's server? dafaq? seriously?

  

Trust me the POC is quiet simple, Only thing is I was lucky enough to enumerate & find the domain vulnerable to this attack.

  

####  How I found this domain!

  

I got a WhatsApp message in one of the Cyber Security groups about " [Facebook Internal IP Disclosure](https://datarift.blogspot.in/p/facebook-internal-ip-disclosure.html) ". I visited the page to get myself motivated to do some bug hunting. 

  

To my surprise the website mentioned in the article was hosting a page with Universal Description Discovery and Integration (UDDI) functionality running on Oracle WebLogic web server.

  

If you guys are aware Weblogic server is known to have been vulnerable to SSRF. I was aware of the known vulnerability as I had encountered it in one of the security assessment done for a client.

  

Then I had mixed thoughts, facebook would have definitely patched the vulnerability and so on, but what's the harm in trying.

  

Soon I fired up laptop and the tools to check if the site was vulnerable to SSRF.

  

####  Step to reproduce submitted to Facebook.

  

Step 1 - https://esbmbltest.thefacebook.com/uddiexplorer/SearchPublicRegistries.jsp

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_850lkbhqnATMAows4xrYyQYBn8smmiJ7P_MDVyIKvR0v9voLK_WxvwrvIwqPR-X66kNpf9NI4CY-M_4VRiFYP8fGSy_26j7V5cujlvOywJBNxMTvmD0wKq1JW20S0dDu1qM3D905NC55/s640/ssrf-001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_850lkbhqnATMAows4xrYyQYBn8smmiJ7P_MDVyIKvR0v9voLK_WxvwrvIwqPR-X66kNpf9NI4CY-M_4VRiFYP8fGSy_26j7V5cujlvOywJBNxMTvmD0wKq1JW20S0dDu1qM3D905NC55/s1600/ssrf-001.png)

  

  
  
  
  
  
  
  
  
  
  
  
  
  
Step 2 - Enter any information and capture the request into the proxy tool like burp suit or IronWASP.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAriTIst-1aj2tnHCAO3tS35UP4QBiuh4GSJZ8RS922bPeLdkLyYIzCOu0rlSjiSzyNStR4OZAu_XqyfXAat-hq81gerAZ3_EysU_31ePkW92bqV_aEPc4TOH_potVAnb98kTuZaVJQAcU/s640/ssrf-002.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAriTIst-1aj2tnHCAO3tS35UP4QBiuh4GSJZ8RS922bPeLdkLyYIzCOu0rlSjiSzyNStR4OZAu_XqyfXAat-hq81gerAZ3_EysU_31ePkW92bqV_aEPc4TOH_potVAnb98kTuZaVJQAcU/s1600/ssrf-002.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  
Step 3 - The operator parameter must be changed to any Internal IP range or any public IP.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP22f2tAZeBXmdNRPpNH4iqpFwI1aGSJX0paaJkJs-9FbyzV99qM36-cKetPQdfsYv0mffpW98dOSwwX60f13AI-r5gHHfTYLgHypE4Z6AXNKujtJpHPsxQpfSvvqcOWplvcYs4VM06yPv/s640/ssrf-003.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP22f2tAZeBXmdNRPpNH4iqpFwI1aGSJX0paaJkJs-9FbyzV99qM36-cKetPQdfsYv0mffpW98dOSwwX60f13AI-r5gHHfTYLgHypE4Z6AXNKujtJpHPsxQpfSvvqcOWplvcYs4VM06yPv/s1600/ssrf-003.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  
Step 4 - The application server successfully connects to the external IP sent in the operator. This shows external SSRF vulnerability is preset.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBoyaYB7iBkbldsEGdjqaOITn5dep-TEGyT3TMV1z1cEWJkRFQLMeoaILeWNpdO3NIqQ9vpyGG-FQGBjI8qzk4eatrxsnKJrQDXSutlSIQ4HbeKoOOQJtCQNa2pwzneGS3TVhsLzilM0ep/s640/ssrf-005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBoyaYB7iBkbldsEGdjqaOITn5dep-TEGyT3TMV1z1cEWJkRFQLMeoaILeWNpdO3NIqQ9vpyGG-FQGBjI8qzk4eatrxsnKJrQDXSutlSIQ4HbeKoOOQJtCQNa2pwzneGS3TVhsLzilM0ep/s1600/ssrf-005.png)

  

  

  

  

  

  

  

  

  

  

  

  

  
Step 5 - To test internal SSRF we input an internal IP range and forward the request. The server will respond with a time delay if the connection is made. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqlm4HBfkOzEAybDTtc0n6xkKtPhccvcrGLWaMd8Jvm2iZ4gDEW8PdBSNbCk8YYJIwMvKlLalxMCRoZS_2pJFLNYimcjlTjSHY9J8EHQFhZyhJtQwJQQI6RYdwhUK2DHF15E5jC8cjA8rT/s640/SSRF-001-active-ip.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqlm4HBfkOzEAybDTtc0n6xkKtPhccvcrGLWaMd8Jvm2iZ4gDEW8PdBSNbCk8YYJIwMvKlLalxMCRoZS_2pJFLNYimcjlTjSHY9J8EHQFhZyhJtQwJQQI6RYdwhUK2DHF15E5jC8cjA8rT/s1600/SSRF-001-active-ip.png)  
---  
The time delay in response is around 800-900 milliseconds when the host is up and running.  
  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-hswhQvP2DkZmDw1m_M7q4yHJbelnGeBIJA30WSqMXvEB-CQM7TrgM_Nz3WNLvi-nzbEXtT6sXK8QpuZQx6dEP-KrMTmQCaKJHrprJsWi52tDa5cW_jgRYwif7M12DIBIl0NZXFWTCFg-/s640/SSRF-002-inactive-ip.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-hswhQvP2DkZmDw1m_M7q4yHJbelnGeBIJA30WSqMXvEB-CQM7TrgM_Nz3WNLvi-nzbEXtT6sXK8QpuZQx6dEP-KrMTmQCaKJHrprJsWi52tDa5cW_jgRYwif7M12DIBIl0NZXFWTCFg-/s1600/SSRF-002-inactive-ip.png)  
---  
The time delay in response is 120,000 milliseconds when the host is down.  
  
  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

With this information we can enumerate the Internal infrastructure behind a firewalled environment.

  

Step 6 - For further understanding. Intercept in IronWasp and browse the page. 

  

Step 7 - Select the logs and the request made. And select Run Modules on this Request/Response. And select SSRF Exploitation Frame work.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJvt17WuwqYG2ZnSSEWntfjtycMwz_S4cpwZDF0K9rqH5yUpk0JS5jjPwXUYUKwPhfBOTADqbuF0uHbMuLNIvizSfiwu28bKUWNVoIozeIiWquyJUOhrbS_UdlxVGMyYt-gs-F2gElV7fS/s640/ssrf-final-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJvt17WuwqYG2ZnSSEWntfjtycMwz_S4cpwZDF0K9rqH5yUpk0JS5jjPwXUYUKwPhfBOTADqbuF0uHbMuLNIvizSfiwu28bKUWNVoIozeIiWquyJUOhrbS_UdlxVGMyYt-gs-F2gElV7fS/s1600/ssrf-final-1.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  
Step 8 - Select the Set Injection Points and select Operator parameter in the body and click on Done.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmtQvEJtW7-SolRbWQg6m38VH2xjmFZEdHQXUFzEwo_28IUq2GjKl4R8kdJtrdNiwqQmhv2zOpOnIXACDHcqVU6ZcnrpeuHxuP6EQbEIn0ARPt9598701VzXlHSS3WulnuyfkJeGVCGeFu/s640/005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmtQvEJtW7-SolRbWQg6m38VH2xjmFZEdHQXUFzEwo_28IUq2GjKl4R8kdJtrdNiwqQmhv2zOpOnIXACDHcqVU6ZcnrpeuHxuP6EQbEIn0ARPt9598701VzXlHSS3WulnuyfkJeGVCGeFu/s1600/005.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  
Step 9 - Select Port Scan or Network Discovery and then we need to input a IP range. 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQiKFmqWwqYDXXxpyxgtJXM0Fusv3tcgBpp8_MqPEtPHKAZEVzstJQ_ammVfJcazJZPB6989Yf2wk-kgiM80WSx_G7QOHV9q9aM0WGlrWp3IB8yhPpQMYE0YGf-vGOs7_O6ZiL1jx0Av2j/s640/007.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQiKFmqWwqYDXXxpyxgtJXM0Fusv3tcgBpp8_MqPEtPHKAZEVzstJQ_ammVfJcazJZPB6989Yf2wk-kgiM80WSx_G7QOHV9q9aM0WGlrWp3IB8yhPpQMYE0YGf-vGOs7_O6ZiL1jx0Av2j/s1600/007.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiECFxQ9Re0cdppsw21i5iMCfQcE5C-wJi9oG6zLPaYLKm8wOjPXeja7koLhCLIqfT_IINiy8WlyGc1SS2ZanGhGpbCU_vWH3Owo4XLqBYBeICGetGS5vvQ62x4tnMRWnTJhmDryj-mYKCv/s640/008.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiECFxQ9Re0cdppsw21i5iMCfQcE5C-wJi9oG6zLPaYLKm8wOjPXeja7koLhCLIqfT_IINiy8WlyGc1SS2ZanGhGpbCU_vWH3Owo4XLqBYBeICGetGS5vvQ62x4tnMRWnTJhmDryj-mYKCv/s1600/008.png)

Step 10 - We can enumerate the Internal IP which are active.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhifFkBANgA1eNNKX0HbZKDJQ5zoCss0Eb4TdbLzBz0lpC7YNFdRIrpcjhsfL9aA2GcmLharToJEUkps7t-18_zSUkeuJtFm6b_V4yzS8sSepBScoBveSdv3x-1bvT_9y-WSarrxR5fCxmQ/s640/SSRF-003-list-ip.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhifFkBANgA1eNNKX0HbZKDJQ5zoCss0Eb4TdbLzBz0lpC7YNFdRIrpcjhsfL9aA2GcmLharToJEUkps7t-18_zSUkeuJtFm6b_V4yzS8sSepBScoBveSdv3x-1bvT_9y-WSarrxR5fCxmQ/s1600/SSRF-003-list-ip.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  
I also submitted a video POC for the vulnerability. 

  

  

Facebook accepted the vulnerability and awarded me with a good bounty as I reported the SSRF vulnerability on 2 Hosts. :D

  

  

  
I hope you liked the write up , I would appreciate your feedback in the comments down below ;)

  

Opinions are mine on the blog.
