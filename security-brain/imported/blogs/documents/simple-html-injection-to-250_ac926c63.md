---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-14_simple-html-injection-to-250_2.md
original_filename: 2021-08-14_simple-html-injection-to-250_2.md
title: Simple HTML Injection to $250
category: documents
detected_topics:
- rate-limit
- business-logic
- idor
- access-control
- xss
- command-injection
tags:
- imported
- documents
- rate-limit
- business-logic
- idor
- access-control
- xss
- command-injection
language: en
raw_sha256: ac926c6353045f8f3019d97a7b3d144671b46e93466b0b74bb218d7ad422c271
text_sha256: 8a73a692d47822a198b0472d9d2b83e01b868b71e10d3a56af06b7a6d1ac1cb4
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Simple HTML Injection to $250

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-14_simple-html-injection-to-250_2.md
- Source Type: markdown
- Detected Topics: rate-limit, business-logic, idor, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `ac926c6353045f8f3019d97a7b3d144671b46e93466b0b74bb218d7ad422c271`
- Text SHA256: `8a73a692d47822a198b0472d9d2b83e01b868b71e10d3a56af06b7a6d1ac1cb4`


## Content

---
title: "Simple HTML Injection to $250"
page_title: "Taking Over Employee Accounts by Managers with Zero Employee Interaction | by Ahmad Halabi | Medium"
url: "https://ahmdhalabi.medium.com/taking-over-employee-accounts-by-managers-with-zero-employee-interaction-b60784c3ad84"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["Account takeover", "Mass assignment"]
bounty: "600"
publication_date: "2021-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3419
scraped_via: "browseros"
---

# Simple HTML Injection to $250

Taking Over Employee Accounts by Managers with Zero Employee Interaction
Ahmad Halabi
Follow
7 min read
·
Aug 13, 2021

546

Hello,

My name is Ahmad Halabi. I used to do bug bounty hunting a lot in the previous months. In this writeup I will discuss a Security Misconfiguration that leads to Business Logic Error and caused Account Takeover.

Overview ::

In April I was invited to a new private program on HackerOne. I found some cool bugs related to Privilege Escalation, CSRF and Information Disclosure of PII information but sadly all were duplicate by other hackers. After that I realized that all usual bugs will end up duplicates, So I decided to avoid wasting additional time and look for a unique bug related to Application Logic.

Target App Structure ::

The application has two types of users:
1. Admin/Manager
2. User/Employee.

Manager creates a Group which plays a role of a Company. And he can invite Employees to his Company/Group.

The important thing to note: Manager can’t change any other Manager or Employee Email address inside his Company. So Manager can just change his email address.

There is a protection on the Email Address input where they don’t allow you to change the email address.

I found a business logic flaw in the Change Email endpoint that allowed me to change the email of any Employee and then reset the password leading to complete Account Takeover without the Employee’s knowledge.

Proof Of Concept ::

Suppose that I am an Admin in this organization and I want to change the email of an Employee in order to steal some info from his account or insert some data that put him in trouble with the manager.

Below are the steps how I was able to bypass the security configuration on email address input and obtain successful account takeover.

I logged in with my admin credentials then navigated to Users section.
I clicked on the Employee profile and I noticed that the email input cannot be edited or modified.
Press enter or click to view image in full size

See the color of the Email Address input is Gray and cannot be modified.

3. I added random characters in First name and Last name inputs and clicked Save and intercepted the request.

4. In the request, I added additional parameter for email to study the response status and body.

So I added a parameter for email to the request body like the following: "email":"ahmd_halabi+test@wearehackerone.com" .

I assumed that the email parameter is active in the server side and added my email as a new modification. Then I forwarded the request.

Press enter or click to view image in full size

5. As you see in the above image, I got a response with 200 OK status code and body showing me the original email address that belongs to the Employee.

6. This didn’t make sense for me because the response was successful. I was sure there is something weird happening in the backend. Because if not, the application should either show an error in the response, or not proceed with the request, or proceed the request without showing a response because it is not successful. But since I got this response I was sure that my email may passed to the backend successfully.

7. I started thinking about ways to verify my theory. So here what I did. I logged out from my admin account. And I tried to login with the target Employee credentials (FYI: in a real attack scenario you will not have employee credentials but here I am testing ethically so I have to identify the mistake happening). And here I was surprised that the employee credentials didn’t succeed in logging in after I made the email change request.

I got an error stating: Information provided does not match our records .

Press enter or click to view image in full size

8. After seeing this, I was sure that my email will work with the employee password but I was also surprised that they didn’t have successful login and the same error message appeared.

9. I have the last option left which is checking the Reset Password functionality, So I clicked on Reset Password and added my email but sadly I got this error message stating: We don't have that email address on file which means the email is incorrect or not belongs to an account.

10. I was confused about this logical bug that just happened. I tried to change the employee email with my email, the request got successful response but the email stayed the same, at the same time the employee is not able to login using his email nor my email. And the forget password is not working for my email. Then I realized I should try resetting the password using employee email and see what will happen.

11. I added employee email and hit on Send Email to Reset Password. I got successful response stating A reset password email has been sent .

12. The funny thing is that nothing was sent to the Employee email. I was kind of crazy about what is happening with this application 😂.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

13. I waited for 5 mins and didn’t receive any email. The time was late around 3:00 AM so I shutdown the laptop and told myself I will check it again tomorrow.

14. After I turned off my laptop, I got an email to my email inbox ahmd_halabi+test@wearehackerone.com containing the reset password link related to the Employee account. I started laughing 😂.

15. I reopened the laptop and checked the email and yes I changed employee password and was inside his account.

16. After accessing Employee account, I was also shocked! In profile section, the email input was showing the Employee email and not my email even though the valid email now is my email.

Press enter or click to view image in full size

So it is like the UI showing Employee email, but the actual email that is used in the backend is my email.

Summary ::

To summarize this bug, simply an admin can takeover any employee or other admin account by modifying the change settings request and adding a new email parameter and value then resetting the password by adding employee email in the reset password input and receiving the reset link to his newly added email.

As a proof of concept, I did it on an account related to the Private program and showed them how I was able to take over their account and deny them from accessing it.

Report Timeline ::

Apr 28, 2021: I recorded a video PoC and reported the issue to the private program on hackerone.
Apr 29, 2021: HackerOne Team Triaged the report and decreased the severity from Critical to Medium.
Apr 29, 2021: I asked them to reconsider the severity and to assess the bug according to the company business risk and the impact that can cause on company reputation and business.
Mar 3, 2021: Further discussion and debate about the severity between me, HackerOne team and the Program internal team.
Mar 25, 2021: Program Internal Team scored it as Medium describing that you have to be an admin/manager in order to take over the other accounts. And they asked me to wait for further investigation about the root cause of this issue before issuing a bounty.
July 9, 2021: I asked for update about the issue.
July 12, 2021: Team still investigating.
July 21, 2021: Internal Team kept the severity as Medium. And awarded me with a total of $600 ($500 bounty + $100 bonus).

To be honest, I think that this finding deserves a Critical severity taking into consideration the impact that can cause on the whole company.

Impact ::

Impact here is unlimited. Any Manager or a user with Admin privileges can takeover and access any other user found under the same Company. So you can steal information, modify data, or do some malicious activities inside user accounts.

Business Logic Bugs and Bypassing Security Configurations are my favorites. I found some similar scenarios before, but this bug specifically was unique and first time I find something like that.

I created private bug bounty course to help struggled hunters find valid bugs and earn bounties.

If you are struggling in finding valid bugs or earning enough bounties, you just need to enroll and your mindset about approaching bug bounty hunting will improve.

Check Student bounties and feedbacks and enroll now: https://ahmadhalabi.net/course

Press enter or click to view image in full size

I am also willing to publish a writeup about a bug that I found in Apple which payed me $5000 for disclosing Apple users address information and phone numbers by chaining an IDOR with Rate Limiting.

Press enter or click to view image in full size

You can follow me on:

Twitter , Instagram , and my website.

Thanks for Reading!
