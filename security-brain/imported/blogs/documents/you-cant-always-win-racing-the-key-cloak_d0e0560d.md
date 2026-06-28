---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-01_you-cant-always-win-racing-the-keycloak.md
original_filename: 2024-07-01_you-cant-always-win-racing-the-keycloak.md
title: You Can’t Always Win Racing the (Key)cloak
category: documents
detected_topics:
- sso
- password-reset
- oauth
- access-control
- xss
- command-injection
tags:
- imported
- documents
- sso
- password-reset
- oauth
- access-control
- xss
- command-injection
language: en
raw_sha256: d0e0560dd7960d5fd0f8619c25296f5155ad25f323ba0ddd2f3ae81782209b4d
text_sha256: 646cfb295420d130dff7d7f6080dfae1f362742171a8acaf4743b9d3f0a136e3
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# You Can’t Always Win Racing the (Key)cloak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-01_you-cant-always-win-racing-the-keycloak.md
- Source Type: markdown
- Detected Topics: sso, password-reset, oauth, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `d0e0560dd7960d5fd0f8619c25296f5155ad25f323ba0ddd2f3ae81782209b4d`
- Text SHA256: `646cfb295420d130dff7d7f6080dfae1f362742171a8acaf4743b9d3f0a136e3`


## Content

---
title: "You Can’t Always Win Racing the (Key)cloak"
page_title: "You can’t always win racing the (key)cloak"
url: "https://www.cyberark.com/resources/threat-research-blog/you-cant-always-win-racing-the-keycloak"
final_url: "https://www.cyberark.com/resources/threat-research-blog/you-cant-always-win-racing-the-keycloak"
authors: ["Maor Abutbul"]
programs: ["Keycloak"]
bugs: ["Race condition", "LDAP", "Application-level DoS"]
publication_date: "2024-07-01"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 207
---

# You Can’t Always Win Racing the (Key)cloak

July 1, 2024 Maor Abutbul

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fyou-cant-always-win-racing-the-keycloak)
  * [Twitter](https://twitter.com/share?text=You%20Can%E2%80%99t%20Always%20Win%20Racing%20the%20%28Key%29cloak&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fyou-cant-always-win-racing-the-keycloak&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#7b44080e19111e180f463814150f1e150f5e494b1d0914165e494b16025e494b330e195e494a5d1a160b4019141f024638131e18105e494b140e0f5e494b0c131a0f5e494c085e494b131a0b0b1e1512151c5e494b1a0f5e494b3802191e093a09105e494a5e4b3a5e4b3a22140e5e494b381a155e3e495e434b5e42420f5e494b3a170c1a02085e494b2c12155e494b291a1812151c5e494b0f131e5e494b5e4943301e025e49421817141a105e4b3a2c1e195e494b291a181e5e494b3814151f120f121415085e494b5e3e495e434b5e42485e494b280e18181e08085e494b1a151f5e494b3d1a12170e091e5e494b5e3e495e434b5e42485e494b1a5e494b301e021817141a105e494b381a081e5e494b280f0e1f025e494b32155e494b0f141f1a025e3e495e434b5e4242085e494b181415151e180f1e1f5e494b0c1409171f5e49385e494b161a15025e494b14091c1a1512011a0f121415085e3e495e434b5e42425e494b5e3e495e434b5e4238101e02085e494b0f145e494b0f131e5e494b1012151c1f14165e3e495e434b5e423f5e494b1a091e5e494b131e171f5e494b12155e494b121f1e150f120f025e494b1a151f5e494b1a18181e08085e494b161a151a1c1e161e150f5e494b5e4943323a365e49425e494b0814170e0f121415085e48395555555e4b3a5e4b3a130f0f0b085e483a5e493d5e493d0c0c0c551802191e091a0910551814165e493d091e08140e09181e085e493d0f13091e1a0f56091e081e1a091813561917141c5e493d02140e56181a150f561a170c1a0208560c121556091a1812151c560f131e56101e021817141a10)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fyou-cant-always-win-racing-the-keycloak&title=You%20Can%E2%80%99t%20Always%20Win%20Racing%20the%20%28Key%29cloak&summary=Web%20Race%20Conditions%20%E2%80%93%20Success%20and%20Failure%20%E2%80%93%20a%20Keycloak%20Case%20Study%20In%20today%E2%80%99s%20connected%20world%2C%20many%20organizations%E2%80%99%20%E2%80%9Ckeys%20to%20the%20kingdom%E2%80%9D%20are%20held%20in%20identity%20and%20access%20management%20%28IAM%29%20solutions%3B...)

![Cartoon of minion racing](https://www.cyberark.com/wp-content/uploads/2024/06/keycloak-blog-hero.jpg)

## Web Race Conditions – Success and Failure – a Keycloak Case Study

In today’s connected world, many organizations’ “keys to the kingdom” are held in identity and access management (IAM) solutions; these play a crucial role in protecting organizations’ assets.

In this post, we delve into the world of [Keycloak](https://www.keycloak.org/), a popular open-source IAM solution.

As part of our work at CyberArk Labs, we research open-source projects and look for security issues so we can share our findings with the open-source and security communities.

Our research focuses on dissecting Keycloak’s security mechanisms. We will delve into a straightforward yet powerful technique for fuzzing LDAP servers. Then, we will deep dive into web race conditions, showcasing two distinct scenarios: (1) one where concurrency appears to be effectively managed and (2) another scenario where we discovered a race condition within the application.

But that’s not all; brace yourself for the finale: presenting and analyzing the root cause of a security issue we found ([CVE-2024-1722](https://nvd.nist.gov/vuln/detail/CVE-2024-1722)).

This research, with the [second](https://www.cyberark.com/resources/threat-research-blog/lets-be-authentik-you-cant-always-leak-orms) part of this series, has been presented at: Insomnihack, Nullcon (Goa), and [BlueHatIL2025](https://www.youtube.com/watch?v=_-SHa7LaAvA); the presentation slides are available [here](https://github.com/m2a2/Research/blob/main/presentations/2025/BlueHatIL_2025_Lets_Be_Authentik_v39_Final_FullPage.pdf)

## The Target System: Keycloak

Keycloak, the open-source identity and access management solution, simplifies securing your applications by seamlessly managing user authentication, authorization and single sign-on (SSO).

According to our Shodan search, there are ~27,000 internet-facing Keycloak systems; additionally, Keycloak boasts an extensive library of extensions, including specialized support for the French administration identity provider, France-connect.

Keycloak is the upstream of [Red Hat Single Sign-On (RH-SSO) ](https://access.redhat.com/products/red-hat-single-sign-on/)and is actively maintained by Red Hat.

So, with our target set, let’s start researching.

## Our Keycloak Security Research

We start at the Keycloak website and documentation. While reading the documentation, we focus on identifying the system’s interfaces, looking for potential attack vectors, and defining a scope for our security review.  
![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-1.png)

**Figure 1: Keycloak interfacese**

As can be seen in Figure 1, Keycloak has many interfaces.

Our scope included the following areas:

  * Web UI + web API – authorization tests
  * LDAP integrations
  * User self-registration flow
  * Client (applications) registration
  * Integrations with identity providers
  * OpenID connect flow

Although the original scope is vast, in this post, we will only dive into areas we think are worth detailing.

The first Keycloak feature we will look at is [LDAP integrations](https://www.keycloak.org/docs/latest/server_admin/index.html#_ldap).

## LDAP

This functionality enables Keycloak to link with a pre-existing LDAP server; this allows users to authenticate using their LDAP credentials, such as Active Directory, and gain access to an application that trusts Keycloak.

### LDAP Injections

When encountering an LDAP interface, the first attack method that comes to mind is [LDAP injection](https://owasp.org/www-community/attacks/LDAP_Injection); if susceptible, this could enable an attacker to gain unauthorized access to the LDAP directory, potentially bypassing access restrictions or even viewing or modifying usernames and passwords.

We tried to use some known LDAP (injection) payloads; during that process, we inspected the traffic flowing between our Keycloak and LDAP servers, and based on our inspections, none of the payloads seemed to “escape” from the LDAP query; hence the server is not vulnerable to a common LDAP injection.

### LDAP Fuzzing

While in the Keycloak context, LDAP injections are straightforward (attacks are performed directly on the user-facing login page), and since LDAP servers are considered closed/internal systems, we speculated that the data from the LDAP server might be overlooked.

#### LDAP Server as an Attack Vector

Assuming an internal user can update some fields in their LDAP profile (maybe via an internal portal or by other means), and when taking into account previous [Keycloak XSS CVEs](https://www.cvedetails.com/product/46161/Redhat-Keycloak.html?vendor_id=25), there may be some payloads (or special characters) that are acceptable in the LDAP context but, for some reason, “break” the Keycloak LDAP parser – and may cause harm to the system.

Using this attack vector, we are primarily seeking to determine the following:

  1. Is it possible for us to disrupt other users, potentially denying their login attempts?
  2. Can we inject a payload that will be executed on the admin web interface (XSS) with their permission?
  3. While less likely, could we cause the system to crash, lock or uncover a memory issue?

Now that we’ve established our theory, let’s go bug hunting!

#### Fuzzing LDAP – Methodology

To execute our tests, we developed the following process: our lab environment included setting up an [OpenLDAP](https://www.openldap.org/project/) docker container and configuring a Keycloak realm to use our OpenLDAP server; furthermore, we used [LDAP Data Interchange Format (LDIF)](https://en.wikipedia.org/wiki/LDAP_Data_Interchange_Format) files and the [ldapadd](https://linux.die.net/man/1/ldapadd) command.

Our fuzzing process is based on the following steps:

  1. Create an LDAP user template.
  2. Create a script to produce a single LDAP-user file.
  3. Execute the script, creating LDIF files.
  4. Populate the users from the LDIF files to our OpenLDAP server. 
  1. Note: Here, we used the [ldapadd](https://linux.die.net/man/1/ldapadd)

Our verification process included the following steps:

  1. Configure the Keycloak to use the relevant OpenLDAP server.
  2. Inspect the “imported” users in the Keycloak UI. 
  1. Pray for profit.

This method allowed us to inject special characters (which the LDAP server accepts) and create many users faster than the manual process (see Figure 2 below).

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-2.png)

**Figure 2: Snippet of the users’ list while fuzzing the first-name parameter**

We tested a long list of payloads, including special characters and some [known XSS payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection); not all payloads are accepted by the OpenLDAP Server, so these are filtered “natively.”

#### Fuzzing LDAP – Issue Found and Further Research

Using the above fuzzing process, we discovered the following issue:

If the same email address is used for two different users (this is acceptable in OpenLDAP and Active Directory) while listing the realm users, the Keycloak admin UI and API malfunction (see Figure 3 below).

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-3.png)

**Figure 3: LDAP email issue**

As shown in Figure 3 above, while listing the modified user, the UI displays an error and does not present the user’s list; nevertheless, other users (except the modified user) are unaffected by this issue and can log in normally.

We reported this issue to the vendor, who informed us that it was [reported before we did](https://github.com/keycloak/keycloak/issues/25778).

Even though our fuzzing session did not discover a security issue, this area can be further explored on other systems (supporting LDAP protocol).

## Web Race Conditions – Success and Failure

While considering our potential attack vectors, one area that caught our attention is User Self-Registration; when enabled, the login page displays a registration link so that a user can create a Keycloak account.

One topic that came up here is race conditions and the question of whether the system handles concurrency-related problems.

While looking for techniques that could be useful for our research, we encountered the great James-kettle (portswigger) [blogpost](https://portswigger.net/research/smashing-the-state-machine). The author’s article introduces “new classes of race conditions that go far beyond the limit-overrun exploits.”

A recurring theme in the [article](https://portswigger.net/research/smashing-the-state-machine) is “with race conditions, everything is multi-step.” In essence, this means that “Every HTTP request may transition an application through multiple, hidden states; if you time it right, you can abuse these sub-states for unintended transitions, break business logic and achieve high–impact exploits.”

With that in mind, let’s try the learned techniques on our target system.

### Everything is Multi-step (Well, Sometimes)

While inspecting the Keycloak database, we noticed that the User Entity table is separated from the Required Action table (see Figure 4 below).

In the Keycloak context, Required Action means what actions a user needs to do/set upon the next login. An example entry can be a _verify email_ , so the user must verify his email upon the next login.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-4.png)

**Figure 4: Keycloak user required_action table**

Here, our attack theory was: “Creating an internal user and setting his email-verified flag (database row) might be a multi-step process,” and if so, by using race-condition techniques, we will be able to log in without email verification (and by that gain access to an application trusting Keycloak using an arbitrary email address).

### Racing Self-Registration

This test required us to create some [burp macros](https://portswigger.net/burp/documentation/desktop/settings/sessions/macros), which allowed us to issue login requests at the same time as user registration requests.

According to our tests, the registration process is not vulnerable to this race condition; let’s find out why in the next section.

### Digging Deeper – Race (Condition) Avoidance

While this attack was unsuccessful for us, as researchers, we thought this was an excellent opportunity to inspect the code and see an exemplary implementation to avoid race conditions.

Let’s dive into the code responsible for creating a user in the system.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-5.png)

**Figure 5: Add user code snippet (modified for visualization)**

In Figure 5, in the addUser function, our theoretical race window starts around line 113 (new user is created) and ends at line 129 (after this line, the required_action seems to be affected), so our attack might be successful at this time window.

Next, let’s look at the model of the user-entity.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-6.png)

**Figure 6: Keycloak user-entity model**

In Figure 6, we found our first clue: the model uses the ([Jakarta.persistence](https://jakarta.ee/learn/docs/jakartaee-tutorial/current/persist/persistence-intro/persistence-intro.html)) Entity annotation (line 60).

Jakarta.persistence is a Java specification that enables developers to manage relational data in Java Enterprise applications.

While glancing at the Jakarta.persistence documentation, we see that this specification can utilize transactions.

#### Database Transactions

One of the mitigation strategies for concurrency issues (race conditions) in the context of web applications is using [database transactions](https://en.wikipedia.org/wiki/Database_transaction).

Keycloak uses Jakarta.persistence and [Hibernate](https://docs.jboss.org/hibernate/orm/3.5/reference/en/html/transactions.html) as its [object relational mapper (ORM)](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) provider.

With that in mind, let’s inspect the database operations while creating the user and see if they indeed use transactions while updating the database. To do that, we enabled logging on to the ORM (org.hibernate:debug).

Using a debugger, setting a breakpoint at line 129 (just before the required_action table is updated), at this timeframe (the race window – between lines 113 to 129), we should see the new user added to the database without the email-verification requirement.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-7.png)

**Figure 7: Inspecting hibernate log while debugging user creation**

The figure above shows the Hibernate logs indicating a new user-entity and an SQL Insert statement.

Querying the database at this moment reveals to us that the new user has not yet been created in the database.

After a few debugging trials, we found other hints; when releasing the breakpoint (and letting the user creation flow finish executing), we encountered the following Hibernate log:

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-8.png)

**Figure 8: Hibernate log indicating the use of transaction**

As seen in Figure 8, the Hibernate log indicates the use of transactions, so we conclude that the user creation flow uses transactions.

While considering the database state at runtime and the conclusion above, this explanation is acceptable; nevertheless, we were looking for more ‘solid’ proof.

After a few more debugging sessions and adding [tracing](https://www.h2database.com/html/features.html#trace_options) to our database, we finally found a sufficient answer.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-9.png)

**Figure 9: Hibernate log and database (H2) trace**

As seen in the above image (Figure 9), the Hibernate log indicates the use of transaction ([auto-commit](https://www.baeldung.com/java-jdbc-auto-commit) disabled), and the database (H2) trace indicates a COMMIT statement.

This means that the database state is updated in “one shot” (transaction), so from the db (and users) perspective, the user does not exist or exists with the email-verification-required (set).

Therefore, this code is not vulnerable to our theoretical race condition.

## Limit Overrun Race Conditions

Another Keycloak feature that caught our attention is Client-Registrations, specifically Dynamic-Client-Registration; when enabled, clients can register themselves through the Keycloak client registration service; this requires an admin-created [access-token](https://www.keycloak.org/docs/23.0.7/securing_apps/#authentication) (or other configuration).

Here, we speculated, _can we override the_ initial-access-token _count limit?_

We will look into it in the next section.

### Keycloak Initial-Access-Token – Limit Overrun Race Condition

Keycloak client-registration initial-access-token (IAT) count limit (set by admin on token creation) can be bypassed when used multiple times in parallel (race condition).  
Exploiting this issue is trivial; use a provided initial-access-token in multiple requests and issue the requests in parallel.

#### Keycloak IAT Race Condition – Demo

![](https://fast.wistia.com/embed/medias/1izpbn7huf/swatch)

**Demo video 1: Keycloak IAT race condition demo**

We reported this issue to the vendor, and from their perspective, the [issue](https://github.com/keycloak/keycloak/issues/27294) is evaluated as low severity, classifying it as a weakness so that no CVE will be assigned.

As seen by the above sections, on the same system, even if some parts of the application are considered for concurrency, there may be overlooked areas, such as web API in our case, where race conditions are still feasible.

## CVE-2024-1722 – A Rare but Painful Denial-of-Service (DoS)

Keycloak can be configured to enable (User) [self-registration](https://www.keycloak.org/docs/23.0.7/server_admin/#con-user-registration_server_administration_guide) (see Figure 10 below); as an additional security feature, the system can also be configured to verify the user’s email pre-login.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-10.png)

**Figure 10: Keycloak configured to enable self-registration**

While testing this feature, we found the following issue:

In any realm set with “User self-registration”, a user registered using a username in an email format and the username is not the same as the email, can be denied from logging in (“locked out”) using their username; nevertheless, the victim can log in using their (registered) email.

### Impact:

A successful exploit of the issue will prevent the specific user from logging in to their account using their username; see the demo in the next section.

### Potential Attack Scenario – UserMail Conflict

Assumption 1: A realm is configured for user-registration.

Note: The “verify email” and “forgot password” settings can be activated.

Assumption 2: The attacker obtained the victim’s username.

Let’s dive into the scenario.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-11.png)

**Figure 11: CVE-2024-1722 – potential attack scenario (icons source:[Flaticon](https://www.flaticon.com/free-icons/))**

1\. A user registers to the realm using a username in an email format. (step (1) in Figure 11).

1\. 1. We will refer to this user as the victim (Alice in Figure 11 above).  
1.2. The user can verify her email using the received email; this can be seen in the demo below (not in the figure)

2\. The user (Alice) normally logs in using the username and password (step (2) in Figure 11); at this point, the username and email can be the same.

3\. Alice updates her email (to her parent Corp in this case – step (3) in Figure 11); now, the username and email are not the same address.

4\. Alice logs in using her username (old email) and password (step (4) in Figure 11) (user credentials can be saved in the user’s browser or password manager).

4.1 Note: At this point, the database lookup matched the username (not the email).

From the user’s perspective, the login is the same.

Time goes by…

Alice logs in using her username and, so far, all is good…

Time goes by…

An attacker obtained the victim’s username (her previous email address).

5\. The attacker registers a new user (step (5) in Figure 11).

5.1. The attacker registers and sets his email address as Alice’s old email (now her username); he can use any username.  
5.2. The attacker does not need access to the email, even when the “verify email” option is set (seen in the demo below).

6\. At this point, the victim cannot access her account using her username (step (6) in Figure 11).

6.1. The victim cannot log in using her username, even after a password reset.  
6.2. The victim can log in using her (registered) email.  
6.3. In the case where the “forgot password” flow is set, the user can “log in” only once using that flow (see demo).

Alice can no longer log in using her username (old email).  

![](https://fast.wistia.com/embed/medias/w43eixgou3/swatch)

**Demo video 2: Keycloak email conflict DOS**

We reported this issue to the vendor, who assigned it the following CVE number: [CVE-2024-1722](https://access.redhat.com/security/cve/CVE-2024-1722).

While feasibility might be rare, the impact on the affected user requires an admin to revert.

### CVE-2024-1722 Root Cause Analysis

So, we found a problem; let’s find the root cause.

When inspecting the login-flow logic, we can see our suspected source.

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-12.png)

**Figure 12: Login flow user lookup code snippet**

![](https://www.cyberark.com/wp-content/uploads/2024/06/Figure-13.png)

**Figure 13: Login flow user lookup code snippet**

As shown in the figures above (Figures 12 and 13), upon login, the user-entity is looked up in the database, first searching by email and then by username.

This process, in combination with the ability to create a user where the email exists in the database in the username field, causes the issue.

## Key Insights from the Keycloak Case Study

Even though our LDAP fuzzing session discovered a non-security issue, we believe this area can be further explored on other systems.

When auditing a system, even if some parts of an application are considered for concurrency, there may be overlooked areas where race conditions are still feasible.

When inspecting a system in a white-box setup, some hints can tell us concurrency has been considered; additionally, debugging can be helpful when searching for these issues.

Although rare, the username-email conflict can cause a “user lockout” scenario; we suggest looking for this pattern in other user-management systems.

## Wrapping up

In this post, we delved into the world of the widely used Keycloak system; our research journey led us through exploring attack vectors and uncovering vulnerabilities from LDAP injections and fuzzing to web race conditions.

Moreover, we shed light on the security issue we found, CVE-2024-1722, an impactful denial-of-service vulnerability.

Whether you’re a developer, system administrator or security enthusiast, understanding these intricacies is vital for safeguarding your systems against potential threats.

_Maor Abutbul is a vulnerability researcher at CyberArk Labs._
