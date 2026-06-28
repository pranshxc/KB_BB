---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-12_exposing-millions-of-irctc-passengers-ticket-details.md
original_filename: 2021-09-12_exposing-millions-of-irctc-passengers-ticket-details.md
title: Exposing Millions of IRCTC Passengers' ticket details.
category: documents
detected_topics:
- idor
- command-injection
- cloud-security
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- cloud-security
- supply-chain
language: en
raw_sha256: aae0d6d93bfbcec8e98365fef9d7df0f5fc2a6f12008cbbdb268b6846bb1ceb0
text_sha256: 1227cf3465a54a5299a01ab99b1fb9dab0c096cfd75dc8640d1e04c25f567521
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Exposing Millions of IRCTC Passengers' ticket details.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-12_exposing-millions-of-irctc-passengers-ticket-details.md
- Source Type: markdown
- Detected Topics: idor, command-injection, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `aae0d6d93bfbcec8e98365fef9d7df0f5fc2a6f12008cbbdb268b6846bb1ceb0`
- Text SHA256: `1227cf3465a54a5299a01ab99b1fb9dab0c096cfd75dc8640d1e04c25f567521`


## Content

---
title: "Exposing Millions of IRCTC Passengers' ticket details."
url: "https://infosecwriteups.com/exposing-millions-of-irctc-passengers-ticket-details-53338280fb9e"
authors: ["Renganathan (@IamRenganathan)"]
programs: ["IRCTC"]
bugs: ["IDOR"]
publication_date: "2021-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3323
scraped_via: "browseros"
---

# Exposing Millions of IRCTC Passengers' ticket details.

Exposing Millions of IRCTC Passengers' ticket details.
Renganathan
Follow
3 min read
·
Sep 12, 2021

474

1

Hi There,

Renganathan Here, I’m an Ethical Hacker & a Security researcher.

I’ve been acknowledged by LinkedIn, United Nations, BYJU’s, Nike, Lenovo, Upstox for reporting security vulnerabilities in their web applications.

What’s IRCTC?

IRCTC, India’s largest online ticketing operations site which runs one of the largest e-commerce sites, has around 30 million registered users with around 550,000 to 600,000 bookings every day makes it the world’s second-busiest traveling portal generating revenue of $20 million every year (Source: Wiki)

While I was booking a ticket as a normal human I suddenly got an idea to test for vulnerabilities.

Hacker Mode!

So the first vulnerability that came to my mind was IDOR. Here are the steps to reproduce.

Login to your IRCTC account
Go to My account > My Transactions > Booked Ticket History.
Press enter or click to view image in full size

3. So there were below tickets that gets expanded on click

Press enter or click to view image in full size

I used burp suite, turned on the interception, and saw a below-get request.

GET /eticketing/protected/mapps1/historySearchByTxnId/XXXXXXXXXX48?currentStatus=N HTTP/1.1
Host: www.irctc.co.in
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.irctc.co.in/nget/txn/my-transactions?page=Booked%20Ticket%20History&eWallet=false

I tried for IDOR and decreased the number of the transaction ID and forwarded the packet.

Get Renganathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And Yeah! I got a random user’s transaction and ticket details like Train Number, Departure time, Duration of the journey, PNR number, Status of the ticket, Boarding station, Passenger's information like their names, seat details, gender & age.

Since the backend code is the same so It’s also vulnerable to Cancelling the ticket, Changing the boarding point, Ordering food, booking a hotel, tourist package, and even Booking a bus.

I immediately recorded a POC & reported it to incident@cert-in.org.in

POC:

Press enter or click to view image in full size

TimeLine:

Aug 30, 2021, 12:45pm: Reported

Aug 30, 2021, 1:30 pm: A ticket was assigned.

Sept 4, 2021: The issue was resolved (retested)

Sept 11, 2021: Acknowledged by IRCTC.

Acknowledgment from IRCTC

Thanks for reading :)
Stay Safe.

https://www.instagram.com/renganathanofficial

https://twitter.com/IamRenganathan
