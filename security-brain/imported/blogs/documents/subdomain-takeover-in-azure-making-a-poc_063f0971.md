---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-01_subdomain-takeover-in-azure-making-a-poc.md
original_filename: 2020-11-01_subdomain-takeover-in-azure-making-a-poc.md
title: 'Subdomain Takeover in Azure: making a PoC'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cloud-security
- supply-chain
language: en
raw_sha256: 063f0971966d6ca37819ff3acdf96a4966c358b06f615f81523b07f948bf1eed
text_sha256: b0d49dff5dfec708008cce75d5ed9349bfae988a7f4220e379be64ab15521b88
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Takeover in Azure: making a PoC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-01_subdomain-takeover-in-azure-making-a-poc.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `063f0971966d6ca37819ff3acdf96a4966c358b06f615f81523b07f948bf1eed`
- Text SHA256: `b0d49dff5dfec708008cce75d5ed9349bfae988a7f4220e379be64ab15521b88`


## Content

---
title: "Subdomain Takeover in Azure: making a PoC"
page_title: "Subdomain Takeover in Azure: making a PoC | GoDiego"
url: "https://godiego.co/posts/STO-Azure/"
final_url: "https://godiego.co/posts/STO-Azure/"
authors: ["Diego Bernal Adelantado (@secfaults)"]
bugs: ["Subdomain takeover"]
publication_date: "2020-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4163
---

![](/assets/posts_details/STO-Azure/images/takeover-main.png)

As a bug bounty hunter, one of the vulnerabilities that are learned at the beginning of the road is a subdomain takeover. While the concept of it is simple, just register some domain that hasn’t been claimed but it’s being pointed to, the chances of finding one is nowadays difficult due to the automation some have developed. That’s why most people, even though experienced, have never found one. Up until recently, one of those people was me.

The basics for me were clear, I registered the dangling domain and then uploaded a proof of concept (PoC). However, in practice, this turned out to be more difficult than expected and I spent quite a bit of time learning how to upload a PoC to a few different Microsoft Azure services. Seeing there wasn’t too much I could find online and the fact that it can be a bit confusing I decided to write this to help others in that position.

The services I’ll go over were the ones I’ve come across (so far):

  * Azure CloudApp: `cloudapp.net`.
  * Azure Websites: `azurewebsites.net`.
  * Azure VM: `cloudapp.azure.com`.
  * Azure TrafficManager: `trafficmanager.net` (added on 19/12/2020).

# Azure CloudApp

* * *

I’ll start with the one I first came across: Azure CloudApp. The first thing I did was validate with `dig` that the subdomain, which I’ve redacted, points to an Azure CloudApp domain. It can be seen from the output that the `CNAME` record indeed points to an app that seems to be unclaimed, otherwise the `NXDOMAIN` status wouldn’t show up at the top.

_Using dig to check DNS resolution_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_dig_1.png)

Now I want to go to the Azure portal at <https://portal.azure.com/?quickstart=True#create/Microsoft.CloudService> and create a new instance, setting the unclaimed domain as the name of my app.

_Azure portal Cloud Service dashboard_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_init.png)

 _Registering the unclaimed domain_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_register.png)

Cool! That means that I can take over the domain.

## PoC creation

I couldn’t find much online on how to make a working proof of concept even though it is the most important part, as it helps triagers quickly confirm that the submission is valid. Eventually, I found this website, <https://www.c-sharpcorner.com>, that had two articles with what I was looking for.

  * <https://www.c-sharpcorner.com/article/azure-cloud-services-create-hello-world-cloud-service-using-visual-studio/> is about how to create a simple service using Visual Studio.
  * <https://www.c-sharpcorner.com/article/azure-cloud-service-create-package-using-visual-studio/> explains how to package the service into the two files required by Azure.

After following the posts I had my `.cspkg` and `.cscfg` files to upload. First I created a storage account and then I was able to deploy the app!

_Deployment successful_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_deploy.png)

![Img](/assets/posts_details/STO-Azure/images/cloudapp_running.png)

Now that I’ve created the subdomain `dig` shows an extra line with the IP of my application and I no longer get `NXDOMAIN`, but `NOERROR`.

_Proving the takeover with dig_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_dig_2.png)

Finally, I can just visit the vulnerable subdomain and see my proof of concept works:

_PoC on the subdomain_

![Img](/assets/posts_details/STO-Azure/images/cloudapp_takeover.png)

A good idea when reporting these kinds of vulnerabilities is to also save a snapshot of the subdomain with the [Wayback Machine](https://web.archive.org/save/), that way once the report gets triaged I can safely release the subdomain (Azure is expensive) without fear because I can prove the takeover was possible.

# Azure Websites

* * *

This is another kind of service that can be taken over but in this case we need to watch out for `*.azurewebsites.net` domains. Let’s say I found a vulnerable subdomain, I’ll call it `takeover-subdomain.com` that points to `testing111111.azurewebsites.net` (very creative names, I know). I’ll register the domain in <https://hackerone.com/redirect?url=https%3A%2F%2Fportal.azure.com%2F%23create%2FMicrosoft.WebSite>. However, this time notice I need to specify a runtime stack and a region: I chose Python and the region doesn’t matter too much.

_Azure portal Websites Service dashboard_

![Img](/assets/posts_details/STO-Azure/images/websites_init.png)

 _Registering the unclaimed domain_

![Img](/assets/posts_details/STO-Azure/images/websites_register.png)

 _Registration successful_

![Img](/assets/posts_details/STO-Azure/images/websites_running.png)

Cool, so now I have the service running and need to deploy the PoC.

### PoC creation

When the domain is taken over I can just access <https://testing111111.azurewebsites.net> and get the default landing page.

_Default page_

![Img](/assets/posts_details/STO-Azure/images/websites_default.png)

To create this proof of concept I just followed the documentation and copied the sample Hello World application from GitHub (check it out on <https://github.com/Azure-Samples/python-docs-hello-world>), then I edited `app.py` a bit so it would return my subdomain takeover template.

_Simple app.py PoC_

![Img](/assets/posts_details/STO-Azure/images/websites_github.png)

Now to make that run on Azure I just need to go to `Deployment center` and select `GitHub` as the CI source. Then after setting up the permissions and giving Azure access the PoC will be running.

_Using CI to upload the PoC_

![Img](/assets/posts_details/STO-Azure/images/websites_CI.png)

However, the takeover wasn’t so simple and I was getting different responses from the pages: on <https://testing111111.azurewebsites.net> I got my PoC but on <https://takeover-subdomain.com> I got the default Azure 404 not found page.

_404 page on subdomain_

![Img](/assets/posts_details/STO-Azure/images/websites_404.png)

After a bit of playing with it, I found that by setting the `Host` header when doing `curl -H 'testing111111.azurewebsites.net' https://takeover-subdomain.com` actually returned my PoC! That meant I needed to set up something else in the Azure dashboard. It turns out that the domain needs to be registered on the `Custom domains` section of the dashboard. Normally Azure asks for verification using an `A` or `TXT` record, however in this case that had already been done by the company so I just needed to add it.

_Setting up a custom domain_

![Img](/assets/posts_details/STO-Azure/images/websites_domain.png)

Doing that solved the issue and I get a PoC working flawlessly!

# Azure VM

* * *

This is the easiest one so far, the only caveat about it is that the domains are of the form `*.region.cloudapp.azure.com` so I need to register a VM in that specific region for the PoC to work. Note that the name of the VM is not the name of the domain I’ll assign to it later, so I can name it as whatever I want.

_Registering a new VM_

![Img](/assets/posts_details/STO-Azure/images/vm_init_1.png)

![Img](/assets/posts_details/STO-Azure/images/vm_init_2.png)

Make sure the selected region is the one the subdomain has, otherwise the takeover won’t work! As for the size, I recommend using the `Standard_B1ls`, as it’s the cheapest one. Another important detail is to also open ports 80 and 443, as I’ll want to serve the PoC from these ports later.

_Registration successful_

![Img](/assets/posts_details/STO-Azure/images/vm_running.png)

After registering the VM, I need to go to the `Configuration` section and set our domain name, which is the one that’s pointed to by the subdomain I want to take over.

## PoC creation

The PoC is simple, just SSH into the VM and create a simple HTML file, then serve it. I found it quicker to just run a simple Python server with `nohup` to detach it from the SSH session and keep it running.

_Registration successful_

![Img](/assets/posts_details/STO-Azure/images/vm_poc.png)

 _Takeover complete_

![Img](/assets/posts_details/STO-Azure/images/vm_takeover.png)

# Azure Trafficmanager

* * *

This one is also quite easy actually, we just need to register a new trafficmanager profile with the name that we found on the dangling `CNAME` record. This is a (redacted) example of a real world case I found:

_Using dig to check DNS resolution_

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_dig_1.png)

As you can see above, the domain points to a trafficmanager `CNAME` that doesn’t seem to be registered. To check it, I went to the Azure portal and tried registering it.

_Registering the trafficmanager profile_

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_register.png)

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_running.png)

After it’s registered and active I went to the `Endpoints` section on the left-hand side menu. Here we can configure what we want to point the record to: an Azure instance or an external site. I went with the latter and pointed it to my VPS IP.

_Creating an endpoint to my site_

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_endpoint.png)

To confirm that it works I checked with dig.

_Using dig to confirm the takeover_

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_dig_2.png)

## PoC creation

The last thing to do is to set up a web server that serves our PoC. It’s important to take into account that the requests will have the `Host` header of the vulnerable site. It’s because of that that many tutorials I saw online played with the Apache config to set up a new vhost. I didn’t want to install Apache and opted to go for a simpler approach using a NodeJS snippet.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  

| 
  
  
  http = require('http');
  
  server = http.createServer(function(request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.write('PoC by GoDiego (<a href=https://hackerone.com/diegobernal>https://hackerone.com/diegobernal</a>)');
  response.end();
  });
  server.listen(80);
  
  
---|---  
`

Then I just ran it with `nohup nodejs poc.js &` and had a working PoC.

_Working PoC_

![Img](/assets/posts_details/STO-Azure/images/trafficmanager_takeover.png)

# Takeaways

* * *

This is everything! I hope you learned something useful, I tried to include all the little details that made me spend a lot of time trying to figure out how things worked. Hopefully, this article will grow with time and I’ll add new PoCs so stay tuned!
