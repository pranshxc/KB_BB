---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-22_an-interesting-xxe-in-sap.md
original_filename: 2018-11-22_an-interesting-xxe-in-sap.md
title: An interesting XXE in SAP.
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: d9f11e08fa91b30418ce661a0ccf9eaa3d923cad59b0c84ea6bd280ba5f097aa
text_sha256: 5f888ff4d57e192ca7791e7561d699c0eb4947c2f7f3fbd4c553955e842076d9
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# An interesting XXE in SAP.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-22_an-interesting-xxe-in-sap.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `d9f11e08fa91b30418ce661a0ccf9eaa3d923cad59b0c84ea6bd280ba5f097aa`
- Text SHA256: `5f888ff4d57e192ca7791e7561d699c0eb4947c2f7f3fbd4c553955e842076d9`


## Content

---
title: "An interesting XXE in SAP."
url: "https://medium.com/@zain.sabahat/an-interesting-xxe-in-sap-8b35fec6ef33"
authors: ["Zain Sabahat (@Zain_Sabahat)"]
programs: ["SAP"]
bugs: ["XXE"]
publication_date: "2018-11-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5570
scraped_via: "browseros"
---

# An interesting XXE in SAP.

An interesting XXE in SAP.
Zain Sabahat
Follow
2 min read
·
Nov 19, 2018

227

1

Hello Folks!

Let me introduce myself to the community. I’m Zain Sabahat, a Security Researcher and Bug Bounty Hunter from Pakistan. Since I have learned a lot of stuff from reading write-ups I have decided to play my role in giving back to the community. I will be disclosing some of my best findings in a series of write-ups.

Today I will be disclosing about an XXE — XML External Entity vulnerability I discovered in SAP’s subdomain https://store.sap.com

During my recon, I came across a store subdomain. When I opened https://store.sap.com it redirected me to the https://store.sap.com/sap/cpa/ui/resources/store/html/StoreFront.html During the loading of that page, a set of GET and POST requests were passed. One of the POST request to “/sap/cpa/api/getSolutions” endpoint caught my attention.

Press enter or click to view image in full size

I manipulated the POST data to :

<!DOCTYPE foo [<!ENTITY xxe SYSTEM “Zain Here”> ]><SolutionListRequest><Facets><FacetType><Code/><Value/></FacetType></Facets><ListingType>2</ListingType><CountryCode>US</CountryCode><RetrieveAllDetailsIndicator>1</RetrieveAllDetailsIndicator><RetrieveFacetsIndicator/><RowCount>24&xxe;</RowCount><RowIndex>1</RowIndex><SearchText/><SolutionGroup/><SolutionTypeIndicator/><CategoryID/><RecommenderPageIndicator/><ResellerID/><ShoppingCartID/><CompanyID/><EndCustomerAddressID/><UserRoleCode/></SolutionListRequest>

in order to check if it was vulnerable to XXE or not.

Verified the presence of XXE

When I saw my name printed out in response I got very happy and decided to exploit it further. I crafted the POST request in order to print out the contents of “/etc/passwd/” file.

Press enter or click to view image in full size
Successfully printed out /etc/passwd file

Timeline:

Get Zain Sabahat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Jun 26, 2017 — Reported to SAP.

Jul 17, 2017 — Triaged.

Feb 13, 2018 — Fixed.

April 10, 2018 — Added to Hall Of Fame.

It took them almost a year to fix because that bug was in their internal component which was hard to replace.

Thanks for reading! Stay tuned for more write-ups!
