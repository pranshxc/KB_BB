---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-28_irctc-millions-of-passenger-details-left-at-huge-risk.md
original_filename: 2018-11-28_irctc-millions-of-passenger-details-left-at-huge-risk.md
title: IRCTC — Millions of Passenger Details left at huge risk!
category: documents
detected_topics:
- rate-limit
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- rate-limit
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 4dd528fdb7d4e9486821790554bc2eb38085d4bf1d658850b1c97029daa7fe9a
text_sha256: 484863238e0ba82207bf5a2639d3b4ba046ee2484e38cfce2bd4f4be936ae86b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# IRCTC — Millions of Passenger Details left at huge risk!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-28_irctc-millions-of-passenger-details-left-at-huge-risk.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4dd528fdb7d4e9486821790554bc2eb38085d4bf1d658850b1c97029daa7fe9a`
- Text SHA256: `484863238e0ba82207bf5a2639d3b4ba046ee2484e38cfce2bd4f4be936ae86b`


## Content

---
title: "IRCTC — Millions of Passenger Details left at huge risk!"
url: "https://medium.com/@logicbomb_1/irctc-millions-of-passenger-details-left-at-huge-risk-18c5ecc09d7f"
authors: ["Avinash Jain (@logicbomb_1)"]
programs: ["IRCTC"]
bugs: ["Information disclosure", "Lack of rate limiting"]
publication_date: "2018-11-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5558
scraped_via: "browseros"
---

# IRCTC — Millions of Passenger Details left at huge risk!

IRCTC — Millions of Passenger Details left at huge risk!
Avinash Jain (@logicbomb)
Follow
6 min read
·
Nov 28, 2018

211

2

Press enter or click to view image in full size

I
RCTC , India’s largest online ticketing operations site which runs one of the largest e-commerce sites, has around 3 crores registered users with around 5,50,000 to 6,00,000 bookings every day makes it world’s second busiest travelling portal generating revenue of Rs 1,506 crore on yearly basis (Source: Wiki)

Indian hackers have been playing a vital role in helping companies securing their infrastructure by finding and ethically reporting security vulnerabilities to them. Along with Gurunath , we decided to move the focus and attention towards Government sites for the sole reason of helping them to be securer and creating security awareness which is big time missing in government sectors. This blog post aims at such step we have taken in protecting information of IRCTC passengers. Let’s begin —

Technical Details

In 2016, IRCTC has introduced free accidental Insurance cover for all the tickets booked online. So when a passenger books a ticket through IRCTC portal, IRCTC shares information regarding passenger and journey details with third party insurer. Once the ticket is confirmed, IRCTC generates a premium number with one of three insurance vendors. When passengers click on the premium link, they are redirected to the third party Insurer web portal where they can view and update nominee details.

When a user clicks on the link, he is redirected to https://www.shriramgi.com/irctc-nominee.html?TXNId=10000139XX​XXX. So, basing on the transaction number (TXNId), all the passenger information is being retrieved.
This transaction number is hard to guess. By further inspection, we were able to modify the request to supply PNR number as input and receive transaction number as response :)
API response showing transaction ID of passenger from PNR number
This PNR number is a 10 digit number which follows a sequence of first 3 digits being constant for a given zone. So all it requires is to brute force (change) remaining seven digits to get all valid transaction numbers.
After getting access to valid combination of PNR number and transaction numbers, all it took is to send this information to another API which is also not protected by any rate limiting (hit as many times with no blocking).
And below show that we are able to fetch detail of any passenger.
Passenger Information received as response
Press enter or click to view image in full size
Passenger Detail
IMPACT — All Passenger Details can be accessed!

Since both API are not protected by any rate limiting, Information of passengers including Passenger full name, his age, gender, journey details and even his Insurance nominee details — Name, Mobile Number, Age are accessible without any proper protection mechanism. Within 10 min, we were able to read almost 1000 passenger information​.

Press enter or click to view image in full size
1000 Passenger details in less than 10mins
Press enter or click to view image in full size
Passenger Detail
Press enter or click to view image in full size
Another Passenger Detail
Press enter or click to view image in full size
Some list of Passenger Details

More than half a million tickets ( 5,00,000 - 6,00,000) are booked through IRCTC on a daily basis, an attacker can exploit this vulnerability to access about 1/3 of all the passenger details as a daily target.

It is to note that IRCTC has introduced free accidental Insurance in 2016 so this vulnerability/hack might be lying since then and passenger details were getting leaked for past 2 years.

Conclusion

The bug was reported to the CERT-In team and they were quick to respond.

But the sad part is that Indian Government don’t appreciate such efforts which can be a demotivating factor for security researchers and skillful bug hunters to actually not report such bugs. It’s important that independent security researchers and governments should work together to improve our collective security and help government site to be more secure.

India, being a country with millions of active internet users has valuable information being shared with different portals like IRCTC. These vendors must ensure that user data is secure and there should be no compromise made on user data privacy. It is good to see organisations like CERT In are taking steps towards making internet a safe place for all Indian users.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Some steps that are required to take to protect user data and massive data breaches —

Every government website which is storing user data should have a dedicated security team.
Regular testing of such application is needed to be done either by outsourcing to external vendors or from inside.
BugBounty programme or responsible disclosure policy should be implemented asap to help hackers to ethically report such loopholes.
A Myth — Having a firewall doesn't mean it protect the application completely. Security team needs to be built for maintaining and reviewing security of the applications.
Appropriate reward and appreciation should be given to ethical hackers who reports vulnerabilities and protect user data from breaches

It is no surprise that India is ranked third after US and China in terms of cyber crime incidents . Over 22,000 Indian websites hacked between Apr 2017-Jan 2018 as confirmed by IT Ministry which includes 114 government portals.The stats can get even worse if proper security awareness and serious steps are not taken. There is no doubt in the talent and skillset that India has in terms of information security. India has already produced some great security researchers but the problem lies when such talents are not recognized in Indian market by Indian government which leaves government sites to be exploited, attacked, exposed by outside malicious hackers and we all know what’s going on with our Aadhar breaches. This is where government should realise what is required and what is lacking in the field of Information Security and take the right steps in the right direction!

Hope this post will be a wake up call for the government to improve and strengthen its commitment towards responsible data practices and helps to highlight the below par security standards in the IT industry and bring to the attention, the importance of security and spread awareness among companies and government to take information security as importantly as any other branch.

Timeline

We reported the vulnerability to Cert-In and IRCTC team and they patched it within some days.

Discovered Issue — Aug 13 11:30 PM
Reported to CERT In and IRCTC — Aug 14 12:30 AM
Press enter or click to view image in full size
First reach out to IRCTC and CERT team
Acknowledgment from CERT — Aug 14 4:30 AM
Response Received as issue fixed — Aug 29 11:02 AM
Verified and Notified CERT about public disclosure Aug 29 9:58 PM
Notified CERT team for public disclosure

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
