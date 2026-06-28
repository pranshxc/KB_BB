---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-19_a-twist-in-the-code-openmeetings-vulnerabilities-through-unexpected-application-.md
original_filename: 2023-07-19_a-twist-in-the-code-openmeetings-vulnerabilities-through-unexpected-application-.md
title: 'A Twist in the Code: OpenMeetings Vulnerabilities through Unexpected Application
  State'
category: documents
detected_topics:
- sso
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- sso
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: 1aaeb65138b26937c706b0903d9eee50a3e3b9a872529d519c3b6962d766e46c
text_sha256: 2cea849497fec9ab9b3a11dd5f807d832c3a5c626b96f679a4975be900e459e3
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# A Twist in the Code: OpenMeetings Vulnerabilities through Unexpected Application State

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-19_a-twist-in-the-code-openmeetings-vulnerabilities-through-unexpected-application-.md
- Source Type: markdown
- Detected Topics: sso, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `1aaeb65138b26937c706b0903d9eee50a3e3b9a872529d519c3b6962d766e46c`
- Text SHA256: `2cea849497fec9ab9b3a11dd5f807d832c3a5c626b96f679a4975be900e459e3`


## Content

---
title: "A Twist in the Code: OpenMeetings Vulnerabilities through Unexpected Application State"
page_title: "A Twist in the Code: OpenMeetings Vulnerabilities through Unexpected Application State | Sonar"
url: "https://www.sonarsource.com/blog/a-twist-in-the-code-openmeetings-vulnerabilities-through-unexpected-application-state/"
final_url: "https://www.sonarsource.com/blog/a-twist-in-the-code-openmeetings-vulnerabilities-through-unexpected-application-state/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Apache OpenMeetings"]
bugs: ["Account takeover", "RCE", "Null-Byte injection", "Security code review"]
publication_date: "2023-07-19"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 917
---

## TL;DR overview

  * This security research post analyzes vulnerabilities discovered in Apache OpenMeetings, a web conferencing application, that arise from unexpected application state—situations where the application behaves insecurely due to assumptions about state that can be violated by an attacker.
  * The research demonstrates how complex application state management, especially in multi-user collaborative software, creates subtle attack surfaces that are difficult to detect through standard testing but visible through deep static analysis.
  * Findings highlight the value of taint analysis and data-flow tracking in identifying security vulnerabilities that depend on specific sequences of application state transitions rather than simple, isolated code patterns.
  * Sonar's security research work informs the development of new static analysis rules, contributing to SonarQube's ability to detect novel vulnerability classes in real-world open source and enterprise codebases.

OpenMeetings is a web conferencing application that can be used for video calls, presentations, and collaborative work. Its official [docker image](https://hub.docker.com/r/apache/openmeetings) has been downloaded more than 50.000 times, and OpenMeetings can also be deployed as a plugin for applications such as Jira, Confluence, or Drupal. Its widespread adoption and the fact that it might be used for sensitive discussions, meetings, and collaborations make it an attractive target for attackers.

In this article, we will show you an interesting issue we discovered in Apache OpenMeetings, which is caused by an unexpected application state. Attackers can combine this issue with additional code vulnerabilities we found to hijack an OpenMeetings instance and execute commands on the underlying server. All they need is an account that they can create themselves in the default configuration.

## OpenMeetings Vulnerabilities - Impact

We discovered the following vulnerabilities in Apache OpenMeetings:

  * CVE-2023-28936: Weak Hash Comparison
  * CVE-2023-29032: Unrestricted Access via Invitation Hash
  * CVE-2023-29246: Null-Byte Injection

These Apache OpenMeetings vulnerabilities allow a self-registered user (enabled by default) to **take over an admin account** and gain **remote code execution** :

The account takeover is possible due to the combination of a **logical flaw** and a **weak hash comparison**. Attackers can trigger certain actions in an unexpected order to create a room invitation without a room assigned to it. This results in an **unrestricted invitation** to access any user account. By using a **wildcard character** , attackers can redeem this invitation themselves and **gain admin privileges**.

Due to **insufficient validation** of configurable items, attackers can use the acquired admin privileges to **inject a null-byte** in one of the binary paths. This can be leveraged to **run an arbitrary binary** and thus results in remote code execution.

All vulnerabilities were fixed with Apache OpenMeetings **7.1.0**.

## OpenMeetings Vulnerabilities - Technical Details

In this section, we explain how the room invitation of OpenMeetings works and dive into the technical details of the account takeover and the null-byte injection.

### Room Invitation

OpenMeetings allows users to add events to their calendars. When a new event is added, an individual room is created, which can be used during the event:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3d15f97e-95d5-4450-b90e-2cca523a6877/openmeetings_room-invite-01.png)

A user within a room can send an invitation to another user:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/86b14d0b-300f-4029-9f17-8d46411954c8/openmeetings_room-invite-02.png)

Such an invitation is represented as an `Invitation` class. When an object of this class is created, the invitee is set, and a random UUID is used as the hash:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/common/InvitationForm.java**

Copy to clipboard
  
  
  protected Invitation create(User u) {
  Invitation i = new Invitation(getModelObject());
  // ...
  i.setInvitee(u);
  i.setHash(randomUUID().toString());

Also, the `Invitation` object is bound to the specific room by calling `setRoom`:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/room/menu/RoomInvitationForm.java**

Copy to clipboard
  
  
  public void updateModel(AjaxRequestTarget target) {
  super.updateModel(target);
  Invitation i = getModelObject();
  i.setRoom(roomDao.get(roomId));

Once the user submits the invitation, the invitee receives an email with an invitation link. This link points to `/openmeetings/hash` and contains the generated hash in the `invitation` query parameter, e.g.:

`https://example.com/openmeetings/hash?invitation=52e2f294-cc34-13...`

This invitation hash is then used to retrieve the corresponding `Invitation` object by calling `getByHash`:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/app/WebSession.java**

Copy to clipboard
  
  
  public void checkHashes(StringValue secure, StringValue inviteStr) {
  // ...
  invitation = inviteDao.getByHash(inviteStr.toString(), false);
  // ...

To summarize: an invitation is **bound to a specific room and user**. It can be redeemed with a **randomly generated hash**.

## Weak Hash Comparison (CVE-2023-28936)

The first vulnerability resides within the `getByHash` method. This method uses the following named query to retrieve the `Invitation` object from the database identified by the user-provided hash:

**openmeetings-db/src/main/java/org/apache/openmeetings/db/entity/room/Invitation.java**

Copy to clipboard
  
  
  @NamedQuery(name = "getInvitationByHashCode", query = "SELECT i FROM Invitation i where i.hash LIKE :hashCode AND i.deleted = false")

The hash value is compared using the `LIKE` operator. In contrast to a strict comparison using the equals sign (`=`), the `LIKE` operator allows wildcards to be used. The default database, H2, requires at least one character before a wildcard. Thus, when, e.g., passing the hash value `"5%"`, all `Invitation` objects with a hash value beginning with five are returned. This way, an attacker can easily enumerate valid invitation hashes and redeem them (the charset of a UUID is limited to `[0-9a-f]`).

Since an invitation is bound to a specific room, this only allows an attacker to access this room on behalf of the invited user. No other interactions with the applications are possible. But let’s see how an invitation is redeemed.

## Unrestricted Access via Invitation Hash (CVE-2023-29032)

After the `checkHashes` method retrieved an invitation, the method continues by declaring a set called `hrights` and tries to determine the room for the invitation:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/app/WebSession.java**

Copy to clipboard
  
  
  // ...
  Room r = null;
  if (invitation != null && invitation.isAllowEntry()) {
  // initialize hrights set
  Set<Right> hrights = new HashSet<>();
  // try to determine room associated to invitation
  if (invitation.getRoom() != null) {
  r = invitation.getRoom();
  } else if (invitation.getAppointment() != null && invitation.getAppointment().getRoom() != null) {
  r = invitation.getAppointment().getRoom();
  }
  // ...

If the room was successfully identified, the constant `Right.ROOM` is added to the `hrights` set. At last, `setUser` is called, passing the invitee and `hrights` as parameters:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/app/WebSession.java**

Copy to clipboard
  
  
  if (r != null) {
  // room was identified
  redirectHash(r, () -> inviteDao.markUsed(invitation));
  hrights.add(Right.ROOM);
  roomId = r.getId();
  }
  // set session user to invited user
  setUser(invitation.getInvitee(), hrights);

Please note that if no room could be identified, the `hrights` set is empty when being passed to `setUser`. In this case, the rights for the newly set user are not restricted but derived from the user itself:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/app/WebSession.java**

Copy to clipboard
  
  
  private void setUser(User u, Set<Right> rights) {
  userId = u.getId();
  if (rights == null || rights.isEmpty()) {
  // rights empty? derive rights from user
  Set<Right> r = new HashSet<>(u.getRights());
  // ...
  this.rights = Collections.unmodifiableSet(r);
  } else {
  // rights not empty? only apply these
  this.rights = Collections.unmodifiableSet(rights);
  }
  }

This means that redeeming an invitation with no room attached to it results in an unrestricted session in the context of the _invited_ user.

Although the usual sequence of actions prevents this, attackers can circumvent this by bringing the application to an unexpected state. At first, an attacker could create an event (`1`) and join the associated room (`2`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3ba38c28-1ab2-405c-853c-6d49d962e05f/openmeetings_flow-01.png)

Now, the attacker deletes the event (`3`) while still being present in the room. Although the room is also deleted when its associated event is deleted, the presence of the attacker in the room makes this a _zombie room_. Next, the attacker creates an invitation for the admin user to this room (`4`). This results in an invitation with no room attached to it:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f7daff54-1ead-4f58-81eb-dd14a1b7c9d8/openmeetings_flow-02.png)

At last, the attacker could leverage the weak hash comparison to redeem the invitation by using a wildcard character (`5`). Although an error is raised when redeeming the hash for such an invitation, a valid web session for the invitee with full permissions of this user is created. This web session can be accessed by using the session cookie in the server’s response (`6`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/bbbe726d-8ad3-4f09-b589-ac5210c754ed/openmeetings_flow-03.png)

The acquired admin privileges allow attackers to change the configuration of the OpenMeetings instance. This includes adding and removing users and groups, changing room settings, and terminating sessions of connected users. Although this is already quite powerful, we were looking for a way to gain code execution to control not only OpenMeetings but also the underlying server.

### Null-Byte Injection (CVE-2023-29246)

OpenMeetings allows an administrator to configure the path for the executables of ImageMagick, FFMPEG, etc. For example, the path for the `convert` binary is retrieved by calling `getPath` with the configuration key `CONFIG_PATH_IMAGEMAGIC` and the name of the binary (`convert`):

**openmeetings-core/src/main/java/org/apache/openmeetings/core/converter/BaseConverter.java**

Copy to clipboard
  
  
  protected String getPathToConvert() {
  return getPath(CONFIG_PATH_IMAGEMAGIC, "convert");
  }

The `getPath` method adds a file separator to the configured path if not already present and appends the name of the binary:

**openmeetings-core/src/main/java/org/apache/openmeetings/core/converter/BaseConverter.java**

Copy to clipboard
  
  
  public abstract class BaseConverter {
  // ...
  private String getPath(String key, String app) {
  final String cfg = cfgDao.getString(key, "");
  StringBuilder path = new StringBuilder(cfg);
  if (!Strings.isEmpty(path) && !cfg.endsWith(File.separator)) {
  path.append(File.separator);
  }
  path.append(app).append(EXEC_EXT);
  return path.toString();
  }

Due to the fact that the configured path does always end with a file separator (e.g., slash) and the executable name is fixed (e.g., `convert`), it seems not possible to run executables with different names. Though, when injecting a null-byte in the configured path, every character following the null-byte will be ignored. Although the `ProcessBuilder` class used to execute the command carries on the null-byte in the Java realm, the implementation of the actual execution of the command is OS-specific and implemented in native C. While in Java the length of a string is stored separately allowing it to contain null-bytes, in C a single null-byte designates the end of the string effectively ignoring every character that was appended after the null-byte.

This allows an attacker with admin privileges to gain code execution by changing the ImageMagic path to `"/bin/sh%00x"` (a single character after the null-byte is required to prevent it from being ignored in the first place). When now uploading a fake image containing a valid image header followed by arbitrary shell commands, the conversion spawns `/bin/sh` with the first argument being the fake image, effectively executing every command in it. [**Update** : _The possibility of injecting a null-byte in the binary path provided to`ProcessBuilder` has been [fixed in OpenJDK](https://github.com/openjdk/jdk/commit/3656939a6a5d2d308ea57dd4238cfd7296950893) by now. The issue is tracked as [CVE-2023-21938](https://bugzilla.redhat.com/show_bug.cgi?id=2187758)._]

In combination with the account takeover, this vulnerability allows a self-registered attacker to gain remote code execution on the underlying server.

## Patch

In this section, we briefly look at the applied patches to fix the vulnerabilities. All vulnerabilities were fixed in OpenMeetings version 7.1.0.

### Issue 1 - Weak Hash Comparison (CVE-2023-28936)

Interestingly, the weak hash comparison vulnerability was not fixed by changing the underlying SQL statement, but by adding an additional check whether the retrieved hash value completely matches the provided value:

**openmeetings-db/src/main/java/org/apache/openmeetings/db/dao/room/InvitationDao.java**

Copy to clipboard
  
  
  private Invitation get(String hash) {
  Invitation i = only(em.createNamedQuery("getInvitationByHashCode", Invitation.class).setParameter("hashCode", hash).getResultList());
  return i != null && i.getHash().equals(hash) ? i : null;
  }

This prevents an attacker from redeeming an invitation hash using a wildcard character.

### Issue 2 - Unrestricted Access via Invitation Hash (CVE-2023-29032)

The second issue was mitigated by adjusting the `setUser` method. The applied permissions are not derived from the given user anymore if the `rights` set is empty:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/app/WebSession.java**

Copy to clipboard
  
  
  private void setUser(User u, Set<Right> rights) {
  // ...
  userId = u.getId();
  if (rights == null) { // || rights.isEmpty() removed
  Set<Right> r = new HashSet<>(u.getRights());
  // ...
  this.rights = Collections.unmodifiableSet(r);
  }
  // ...
  }

This prevents an invitation without a room assigned to it resulting in unrestricted access to the invited user.

### Issue 3 - Null-Byte Injection (CVE-2023-29246)

At last, the null-byte injection was fixed by validating the configured path via the `Path.of` method:

**openmeetings-web/src/main/java/org/apache/openmeetings/web/admin/configurations/ConfigForm.java**

Copy to clipboard
  
  
  public void validate(IValidatable<String> validatable) {
  Configuration c = getModelFixType();
  if (Type.PATH == c.getType()) {
  try {
  Path.of(validatable.getValue());
  } catch (InvalidPathException e) {
  validatable.error(new ValidationError(e.getMessage()));
  }
  }
  }

If the configured path contains a null-byte, `Path.of` throws an `InvalidPathException` and the validation fails. This prevents the possible truncation of the applied file separator and binary name.

## Timeline

**Date**| **Action**  
---|---  
2023-03-20| We report all issues to maintainers.  
2023-03-20| Initial response from maintainers;  
findings will be checked.  
2023-03-28| Maintainers confirm issue 1.  
(Weak Hash Comparison, CVE-2023-28936)  
2023-03-30| Maintainers confirm issue 2.  
(Unrestricted Access via Invitation Hash, CVE-2023-29032)  
2023-04-04| Maintainers confirm issue 3.  
(Null-Byte Injection, CVE-2023-29246)  
2023-05-09| Version 7.1.0 is released, which fixes all three issues.  
  
## OpenMeetings Vulnerabilities - Summary

In this article, we looked at an interesting issue in the web conferencing application Apache OpenMeetings, which was caused by an unexpected application state. While developers typically anticipate and account for expected states during the design and development of an application, unexpected states can arise due to unintentional misusage or intentionally triggered attacks. As we have seen, these unexpected states can inadvertently introduce security vulnerabilities that attackers can exploit.

By following Code Quality principles, developers can reduce the risk of introducing these code vulnerabilities, ensuring that the application behaves as expected under various conditions. These principles promote security, maintainability, and reliability, enabling developers to anticipate and handle unexpected states more effectively.

We additionally pointed out the importance of this by demonstrating how attackers could combine the issue with a weak hash comparison to take over any user account. Furthermore, we looked at a null-byte injection caused by insufficient validation of user input, which results in remote code execution. At last, we looked at the applied patches and determined how the vulnerabilities were addressed.

Finally, we would like to thank the maintainers of Apache OpenMeetings for quickly responding to our report and providing a patch for all reported issues.

## Related Blog Posts

  * [Securing Developer Tools: OneDev Remote Code Execution](https://www.sonarsource.com/blog/onedev-remote-code-execution/)
  * [Zimbra Email - Stealing Clear-Text Credentials via Memcache injection](https://www.sonarsource.com/blog/zimbra-mail-stealing-clear-text-credentials-via-memcache-injection/)
  * [Agent 008: Chaining Vulnerabilities to Compromise GoCD](https://www.sonarsource.com/blog/gocd-vulnerability-chain/)
