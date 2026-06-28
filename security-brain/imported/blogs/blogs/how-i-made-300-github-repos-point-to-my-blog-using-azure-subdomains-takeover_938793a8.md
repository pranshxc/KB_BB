---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-23_how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover.md
original_filename: 2022-07-23_how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover.md
title: How I made 300 GitHub repos point to my blog using Azure subdomains takeover
category: blogs
detected_topics:
- command-injection
- otp
- cloud-security
tags:
- imported
- blogs
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 938793a81ee6e8f840cd8028e3d7b68b3b80c166750f38ba1e8ebbf2d5e4007c
text_sha256: 7e19805a92a02250826e1452affc6716d7c24d62ba984dffda83f5f666c0134e
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I made 300 GitHub repos point to my blog using Azure subdomains takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-23_how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `938793a81ee6e8f840cd8028e3d7b68b3b80c166750f38ba1e8ebbf2d5e4007c`
- Text SHA256: `7e19805a92a02250826e1452affc6716d7c24d62ba984dffda83f5f666c0134e`


## Content

---
title: "How I made 300 GitHub repos point to my blog using Azure subdomains takeover"
page_title: "How I made 300 GitHub repos point to my blog using Azure subdomains takeover – > TRIPLA SECURITY"
url: "https://0xpwn.wordpress.com/2022/07/23/how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover/"
final_url: "https://tripla.dk/2022/07/23/how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover/"
authors: ["0xPwN (@msd0s7)"]
bugs: ["Subdomain takeover"]
publication_date: "2022-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2410
---

## How I made 300 GitHub repos point to my blog using Azure subdomains takeover

Playing around in Azure portal, I saw that it is pretty easy to register/unregister an azurewebistes.com subdomain while deploying an application. The idea that came into my mind was “how many references to azurewebistes.com are out there which are no longer maintained, and are available for takeover?”

So I decided to look through GitHub repos, collect the URLs, check them, register them myself, and redirect the traffic to my own blog. 

## 1\. Find *.azurewebsites.com references

I didn’t feel like spending too much time on this PoC project, so I just intercepted the GitHub search request for “azurewebsites.com” in Burp and sent it to intruder to go over all the pages (around 75). This could have probably be done in a smarter way using GitHub API and tokens. Each page had ~10 references to Azure subdomains, so roughly 750 potential subdomain takeovers.

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-15.png?resize=931%2C664&ssl=1)

## 2\. Collect ’em all

Once intruder was done, I saved all the HTTP response bodies to a file and using some `grep-regex-bash-fu` I extracted the subdomains.
  
  
  cat azure_github.txt | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep azurewebsites | cut -d "/" -f 3-10 | sort -u

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-17.png?resize=700%2C449&ssl=1)

## 3\. Check availability

Since not all subdomains I found were available for registration (either owner of the repo or someone else has registered them), I used the Azure Portal functionality to check which ones I can take over. Again, this can probably be done using Azure API, but the quick-and-dirty solution worked just fine so I intercepted the request in Burp and checked the availability for each domains I found.

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-13.png?resize=726%2C521&ssl=1)The green mark indicates available, while the red cross the opposite.

In the response we can see that the `"nameAvailable":true` indicates that the subdomain is available for registration:

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-18.png?resize=1135%2C675&ssl=1)

I send the request to intruder, and once it finished running and checking the whole list of subdmomains, I was left with around 300 subdomains that are referenced in GitHub repos, but are available for registration in Azure Portal. Neat 😎

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-19.png?resize=859%2C723&ssl=1)

## 4\. Create a static web page

My first thought was to register each one of these domains and redirect the users to my own blog. I decided to use a simple static web page with JavaScript redirection as it requires little to no compute power which is what Azure charges on.
  
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
  </head>
  <body>
  <script src="https://subdomainsjs.blob.core.windows.net/scripts/javascript.js"></script>
  </body>
  </html>

## 5\. Hosting the payload

Additionally, I created a Blob Container to host the JS payload, and be able to easily change it dynamically on all subdomains if needed.

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-9.png?resize=1127%2C507&ssl=1)

## 6\. Pew-Pew 🔫 Deploy 

Once the HTML web page and the payload were ready, I wrote a script that went through each one of the subdomains and registered it. Initially I used the free tier service plan (F1) but that one is limited to less than 10 static web apps, so I had to upgrade to Basic plan (B3) which allowed me to host unlimited static web apps (unless they all exceed 10Gb which was not the case). 

This costs around 80$ a month so I’m still considering whether it is worth it (at least for the subdomains I found on GitHub).
  
  
  PS E:\azure_subdomains\html-docs-hello-world> foreach($line in  Get-Content "..\subdomains_takeover.txt"){az webapp up --sku B3 --name $line --resource-group 0xpwnlab --plan 0xpwnserviceplan --location "West Europe" --html}

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-11.png?resize=841%2C829&ssl=1)Taking over the domain and pushing the HTML redirect page

## 7\. Results 

Finally, after several hours of registering and pushing HTML pages my Azure Portal was full of App Services:

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-20.png?resize=942%2C821&ssl=1)

Shortly after I started to see traffic coming from these domains:

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-21.png?resize=508%2C297&ssl=1)

## 8\. Conclusion

Did it work? Yes. Was it worth it? I wouldn’t say so. The fact that most of these repso are old/unpopular/unkonwn/hobby-projects makes the amount of traffic gained pretty low compared with the price required to hosts the static pages on Azure. I would say a better approach is to use google dorks and hunt for dead links from more popular websites. 

For example I found a (quite old) PDF documentation from Microsoft that’s referencing scientificwebsite.azurewebsites.net which is available for registration

![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-22.png?resize=751%2C408&ssl=1) ![](https://i0.wp.com/tripla.dk/wp-content/uploads/2022/07/image-23.png?resize=708%2C154&ssl=1)

### Share this:

  * [ Share on X (Opens in new window) X ](https://tripla.dk/2022/07/23/how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://tripla.dk/2022/07/23/how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover/?share=facebook)
  * 

### Like this:

Like Loading…

[Uncategorized](https://tripla.dk/category/uncategorized/)

[July 23, 2022](https://tripla.dk/2022/07/23/how-i-made-300-github-repos-point-to-my-blog-using-azure-subdomains-takeover/)

* * *
