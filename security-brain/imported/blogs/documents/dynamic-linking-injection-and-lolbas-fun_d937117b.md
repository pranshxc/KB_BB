---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-28_dynamic-linking-injection-and-lolbas-fun.md
original_filename: 2023-03-28_dynamic-linking-injection-and-lolbas-fun.md
title: Dynamic Linking Injection and LOLBAS Fun
category: documents
detected_topics:
- command-injection
- supply-chain
- idor
- access-control
- rate-limit
- automation-abuse
tags:
- imported
- documents
- command-injection
- supply-chain
- idor
- access-control
- rate-limit
- automation-abuse
language: en
raw_sha256: d937117bb1b3f5745239289bfa15ef4a686787d8458b01dd2bf31b50afc00e2a
text_sha256: bf8ad4e65eb2d693622d51e1de7333a95bee1eddbab135e5acedcd2978d5462a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Dynamic Linking Injection and LOLBAS Fun

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-28_dynamic-linking-injection-and-lolbas-fun.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, idor, access-control, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `d937117bb1b3f5745239289bfa15ef4a686787d8458b01dd2bf31b50afc00e2a`
- Text SHA256: `bf8ad4e65eb2d693622d51e1de7333a95bee1eddbab135e5acedcd2978d5462a`


## Content

---
title: "Dynamic Linking Injection and LOLBAS Fun"
page_title: "Dynamic Linking Injection and LOLBAS Fun | Praetorian"
url: "https://www.praetorian.com/blog/dynamic-linking-injection/"
final_url: "https://www.praetorian.com/blog/dynamic-linking-injection/"
authors: ["Joseph Henry"]
bugs: ["DLL Hijacking", "Dynamic-linking injection", "Local Privilege Escalation"]
publication_date: "2023-03-28"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1334
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Product Security](https://www.praetorian.com/category/product-security/)

# Dynamic Linking Injection and LOLBAS Fun

  * [Joseph Henry](https://www.praetorian.com/author/joseph-henry/)
  * [ March 28, 2023 ](https://www.praetorian.com/blog/2023/03/28/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/Screen-Shot-2023-03-27-at-11.45.10-AM-e1722897987553.png)

### **Introduction**

LoadLibrary and LoadLibraryEx are how Windows applications load shared libraries at runtime. Praetorian recently tested a .NET web application that unsafely passed user input into LoadLibrary. In this article, we discuss this vulnerability class, dubbed dynamic-linking injection. We begin with an explanation of the vulnerability. We then walk through a simple recreation of the target web application to demonstrate how to detect and exploit dynamic-linking injection. Finally, we close by combining the vulnerability with a well-known attack technique to create a fully remote exploit.

Praetorian is unaware of other public write-ups on similar issues. As such, this may be a novel (albeit uncommon) vulnerability class.

### **What is Dynamic-Linking Injection?**

Windows libraries are typically compiled into “dynamic linked libraries” (DLLs). DLLs can be loaded at runtime and shared between processes. DLLs allow multiple processes to use the same code and reduce overall memory overhead.

DLLs can be linked statically to a binary or loaded dynamically at run-time. To load a DLL at run-time, an application must call LoadLibrary or LoadLibraryEx. These functions return a handle to the library. The calling application typically passes the handle to GetProcAddress to import specific functions from the library. See the simple example below:
  
  
  '''cpp
  
  #include <windows.h> 
  #include <stdio.h> 
  
  typedef DWORD (__cdecl *MYFUNC)(); 
  
  int main( void ) 
  { 
      HMODULE hModule; 
      MYFUNC funcPtr {}; 
      BOOL loadRes, freeRes = FALSE; 
  
      // Load DLL
      hModule = LoadLibraryA("Library.dll"); 
  
      // Import function
      if (hModule) 
      { 
          funcPtr = (MYFUNC)GetProcAddress(hModule, "MethodName"); 
  
          // Invoke the function
          if (funcPtr) 
          {
              loadRes = TRUE;
              (funcPtr)(); 
          }
          
          // Free the library module.
          freeRes = FreeLibrary(hModule); 
      
          if (!freeRes) 
              printf("Failed to free library.n"); 
      } 
  
      return 0;
  }
  '''

Dynamic-linking injection arises when the user controls the strings passed to LoadLibrary or GetProcAddress. If a user can modify these values and the application does not implement sufficient protections, the user can load arbitrary libraries and/or invoke arbitrary functions.

Because loading a DLL implies running the DLL’s DllMain function, LoadLibrary injection is likely to be more impactful than GetProcAddress injection alone. An attacker with control over the input values to both LoadLibrary and GetProcAddress can execute a variety of critical-risk attacks against the target application.

### **The Target Application**

We recreated a minimal working example of the application to avoid revealing sensitive information about our client. The example application consists of three components: a flask web server, a C++ “worker” executable, and one or more “plugin” DLLs.

#### **The Web Server:**
  
  
  '''python
  
  from flask import Flask, render_template, request
  import subprocess
  
  app = Flask(__name__)
  PLUGIN_DIR = 'Plugins'
  
  @app.route('/')
  def index():
      messages = [{'title': 'Praetorian', 'content': 'Hasher Test Application'}]
      return render_template('index.html', messages=messages)
  
  @app.route('/hash', methods=('GET', 'POST'))
  def hash():
      hashes = []
      if request.method == 'POST':
          cmd = [
                  PLUGIN_DIR + 'Worker.exe',
                  request.form['engine'],
                  request.form['method'],
                  request.form['id'],
                  request.form['title'],
                  request.form['content'],
                  request.form['operation'],
                  request.form['mode']
          ]
  
          output = subprocess.run(cmd, stdout=subprocess.PIPE)
          returnVals = output.stdout.decode("utf-8").split('rn')
          if len(returnVals) < 2:
              returnVals = ['ERROR', 'ERROR']
  
          hashes=[{'clear': returnVals[0], 'hashed': returnVals[1]}]
      return render_template('hash.html', hashes=hashes)
  
  app.run(host='0.0.0.0', port=80)
  '''

#### **The Worker Executable:**
  
  
  '''cpp

#include <windows.h>  
#include <iostream>

typedef HRESULT(WINAPI* ENGINEPROC)(DWORD, LPCTSTR, LPCTSTR, DWORD, DWORD);

size_t BUFSIZE = 256;

const wchar_t* CToW(const char* c)  
{  
size_t nChars = strlen(c) + 1;

wchar_t* ws = new wchar_t[nChars];  
char* p = (char*)ws;  
for (int i = 0; i < nChars; i++)  
{  
p[i * 2] = c[i];  
p[i * 2 + 1] =

‘\0’;  
}  
  
return ws;  
}  
  
int main(int argc, const char** argv)  
{  
HMODULE hinstLib;  
ENGINEPROC ProcessData{};  
BOOL fRunTimeLinkSuccess = FALSE;  
DWORD ID, operation, mode;  
LPCTSTR title, data;  
HRESULT res;  
  
try {  
std::string pluginsDir = “Plugins\\\”;  
std::string pluginName(argv[1]);  
std::string pluginPath = pluginsDir + pluginName;  
  
hinstLib = LoadLibraryA(pluginPath.c_str());  
  
if (NULL == hinstLib)  
{  
std::cout << “Failed to load: ” << pluginPath << std::endl;  
throw std::invalid_argument(“Failed to process.”);  
}  
  
ProcessData = (ENGINEPROC)GetProcAddress(hinstLib, argv[2]);  
if (NULL != ProcessData)  
{  
ID = atol(argv[3]);  
title = CToW(argv[4]);  
data = CToW(argv[5]);  
operation = atol(argv[6]);  
mode = atol(argv[7]);  
  
res = ProcessData(ID, title, data, operation, mode);  
fRunTimeLinkSuccess = TRUE;  
}  
  
if (!fRunTimeLinkSuccess)  
{  
std::cout << “Failed to invoke method: ” << argv[2] << std::endl;  
throw std::invalid_argument(“Failed to process.”);  
}  
}  
catch (…) {  
std::cout << “Unable to process data with those arguments.” << std::endl;  
}  
  
return 0;  
}  
“`

As seen above, the worker process accepted several command line arguments. The first two loaded a library and imported a function from that library, respectively. The remaining arguments were passed off to the function. This flexibility allowed developers to quickly write plugins and additional features for the application without edits to the primary code base.

#### **The Plugin**
  
  
  For this write-up, we wrote a single plugin to create a SHA256 hash of the input data. We compiled this plugin as a DLL named DataEngine and exported a single function  
  
  ProcessData:  
  
  '''cpp  
  
  #include "DataEngine.h"  
  #include "sha256.h"  
  #include "windows.h"  
  #include "string.h"  
  #include <string>  
  
  HRESULT ProcessData(DWORD id, LPCTSTR nodeName, LPCTSTR data, DWORD operation, DWORD mode)  
  {  
      wchar_t outputClear[256];  
      swprintf(outputClear, 256, L"%d:%s:%s:%d:%d", id, nodeName, data, operation, mode);  
      std::wcout << outputClear << std::endl;  
  
      SHA256 sha256;  
      std::wstring ws(outputClear);  
      std::string hashString(ws.begin(), ws.end());  
      std::cout << sha256(hashString) << std::endl;  
      return S_OK;  
  }  
  '''

Although contrived, these three components sufficiently recreate the vulnerable functionality of our client’s application.

We complete the remainder of this write-up from a blackbox perspective to demonstrate that source code is unnecessary to identify dynamic-linking injection.

### **Identifying Dynamic-Linking Injection**

#### **Without Local Access**

We initially discovered dynamic-linking injection without direct access to the vulnerable application. We turn to the example application to demonstrate this process.

The example application is simple. It accepts five different input fields, calculates the SHA256 hash of those fields, and returns the hash in HTML to the user (see figure 1).  
  
_Figure 1: The example application before (left) and after (right) submitting data._

In Burp Proxy, we can examine the HTTP request this submission made, as seen in figure 2.  
_  
__Figure 2: The HTTP request our example application sent._

In addition to the five parameters from the HTML form, the request includes two hidden parameters: engine and method. By modifying these parameters, the application returns interesting error messages that we can see in figure 3.  

  
_Figure 3: Two error messages we evoked by modifying two hidden fields._

The error messages indicate that a remote attacker has full control over the library and method names. It is also worth noting that the application searches for the supplied library in the Plugins\ directory.

In cases where the application does not return verbose error messages and the library and method parameters do not have obvious names, identifying dynamic-linking injection may not be feasible without direct access to the vulnerable application. Where possible, security researchers should obtain local access to the target application, where they can acquire additional information.

#### **With Local Access**

[ Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) is a collection of Windows system utilities maintained by Microsoft. This blog post uses Process Explorer and Process Monitor to identify dynamic-linking injection. We can use Process Explorer to first retrieve the PID of the web server, as in figure 4.  
  
_Figure 4: Retrieving the web server’s PID via Process Explorer._

With the PID in hand, we can use Process Monitor to search for potential dynamic-linking injections by filtering for all Load Image process events belonging to process 9928, as in figure 5.  
  
_Figure 5: Filtering for all Load Image process events belonging to process 9928, via Process Monitor._

After setting the filter and clicking “OK”, Process Monitor will capture process events. We then repeat the initial HTTP request to trigger all relevant behavior. This generates dozens of entries in Process Monitor, including the “Process Create” event in figure 6.  
  
_Figure 6: Repeating the request for all relevant behavior via Process Monitor, and finding an entry for Process Create._

Double-clicking on this entry displays additional information about the event, including the child process’s binary path and command-line arguments (see figure 7).  
  
_Figure 7: Opening the Process Create event to find the process’s binary path and command-line arguments._

We note that DataEngine and ProcessData appear as command-line arguments. We also note that the child process is named “Worker.exe”.

We can repeat this process with Worker.exe as a “Process Name” filter. To further refine our search, we can add DataEngine as a “Path” filter in figure 8.  
  
_Figure 8: Refining results by filtering with Process Name set to “Worker.exe” and Path set to “DataEngine”._

After repeating the HTTP request, we capture additional events (see figure 9).  
  
_Figure 9: Events the most recent filtered search captured, including an indication that the web server passed the user parameter to `Load Library`._

Because DataEngine is both a command-line argument and the name of the DLL in the Load Image event above, the above output indicates Worker.exe passes this argument to LoadLibrary. For additional confirmation, we could repeat this process by supplying different values for engine in the initial HTTP request and checking the Process Monitor output to determine if it reflects our changes.

The Load Image event above stands out because it references a string from a user-controlled parameter. Loading DLLs whose names appear in user input parameters is a good indicator of dynamic-linking injection.

Unfortunately, Process Monitor does not provide data on individual function calls. To confirm what functions are called from DataEngine.dll, we could use WinDBG (discussed later) or [Frida](https://frida.re/docs/installation/) (not discussed in this article).

### **Exploiting Dynamic-Linking Injection**

#### **With Write Access**

If the application runs as a privileged user, an attacker with local access to the host machine can abuse this vulnerability to elevate privileges to those of the service account. With local access, the attacker can plant a malicious DLL on the filesystem and abuse dynamic-linking injection to load the malicious library. The attacker could put code inside the library’s DllMain function to start a reverse shell, inject into another process, read or write sensitive files, or perform other malicious actions. For this writeup, we use a simple DLL that runs a single function in DllMain and exports no methods. The function prints the username and PID of the running process:
  
  
  
  dllmain.cpp:  
  
  '''cpp  
  
  #include <iostream>  
  #include <string>  
  #include <fstream>  
  
  void attackerMethod()  
  {  
      const char* outfileName = "C:\\Users\\Public\\info.txt";  
      DWORD pid = GetCurrentProcessId();  
      char username[64];  
      DWORD username_len = 64;  
      GetUserNameA((LPSTR)username, &username_len);  
  
      std::string infoMessage = "Username: " + std::string(username) + "\n";  
      infoMessage += "Process ID: " + std::to_string(pid) + "\n";  
  
      std::ofstream outfile;  
      outfile.open(outfileName);  
      outfile << infoMessage;  
      outfile.close();  
  }  
  
  BOOL APIENTRY DllMain( HMODULE hModule,  
                        DWORD  ul_reason_for_call,  
                        LPVOID lpReserved  
                      )  
  {  
      switch (ul_reason_for_call)  
      {  
      case DLL_PROCESS_ATTACH:  
      case DLL_THREAD_ATTACH:  
          //attackerMethod();  
          break;  
      case DLL_THREAD_DETACH:  
      case DLL_PROCESS_DETACH:  
          break;  
      }  
      return TRUE;  
  }  
  '''

#### _Local Privilege Escalation_

After compiling the code into a DLL, we plant the library in any world-writable location, such as C:\Users\Public (see figure 10).  
  
_Figure 10: Writing_ _EvilDll_ _to_ _C:\Users\Public_ _._

We then repeat the POST request from Burp Repeater to escape the Plugins directory and execute the malicious library, as figure 11 shows.  
  
_Figure 11: Repeating the_ _POST_ _request from Burp Repeater to escape the_ _Plugins_ _directory and execute_ _EvilDLL_ _._

The application returns an error about failing to export the Foobar method, but we expected this since the malicious DLL did not export any functions.

If we check in the C:\Users\Public directory, we see that the info.txt file was created (see figure 12).  
  
_Figure 12: An_ _info.txt_ _file now exists in_ _C:\Users\Public_ _._

The info.txt file demonstrates that the DLL code was successfully executed as SYSTEM.

#### **Without Write Access**

Depending on the application, an attacker may be able to exploit dynamic-linking injection without first planting a malicious binary on the local filesystem. This situation could arise when the vulnerability is exposed through a web application or if the vulnerable application does not perform LoadLibrary outside of a narrow set of trusted directories.

To fully develop and weaponize this type of exploit, security researchers are likely to require local access to the vulnerable binary (Worker.exe). We will use WinDBG to analyze how Worker.exe loads its engine library and invokes a method from within it. Once developed, the attack can be performed without local access.

#### _Further Investigation with WinDBG_

We first test that the command-line invocation of Worker.exe from the previous section works as expected (see figure 13).  
  
_Figure 13: Testing the command-line invocation of Worker.exe._

After launching WinDBG, we can run Worker.exe by clicking “File” > “Open Executable”, selecting Worker.exe, and providing the above command line arguments. We also must specify the working directory, which we learned from Process Monitor and which figure 14 shows.  
  
_Figure 14: Specifying the working directory and command-line arguments to Worker.exe in WinDBG._

We see in figure 15 how, upon clicking “Open”, WinDBG starts the application in a debugging environment.  
  
_Figure 15: Starting the Worker.exe application in WinDBG._

We first set an exception to break when the DataEngine library is loaded with the sxe ld command (see figure 16).  
  
_Figure 16: Setting an exception to break when Worker.exe loads the DataEngine library._

We then can examine the call stack with k to see the call to LoadLibrary, as in figure 17.  
  
_Figure 17: The call stack before LoadLibrary._

We note the relative return address from Worker!main after LoadLibraryA completes. With DataEngine.dll loaded, we can set a breakpoint at Worker!main+0x97 to return to the Worker.exe code execution context. We can then use unassemble (u) to view the assembly code responsible for importing and calling ProcessData, as figure 18 demonstrates.  
  
_Figure 18: Using_ _u_ _to disassemble Worker.exe’s main function._

The red highlights in figure 18 are the key instructions. First, the application makes a call instruction to GetProcAddress and moves the result from rax into rsi. Finally, the value in rsi is passed to call and invoked as a function pointer.

Our mission now is to determine the function signature of the method returned by GetProcAddress. We can achieve this by looking at how Worker!main passes arguments to DataEngine!ProcessData. 64-bit Windows applications typically pass the first four arguments in the rcx, rdx, r8, and r9 registers and the remaining arguments on the stack.

With this in mind, we can determine the ProcessData function signature by examining the instructions just before call rsi, which we highlighted in blue in figure 18. The application calls mov against all four argument registers and one additional stack variable.

We can set another breakpoint at the address of call rsi and run g to continue execution until the breakpoint. Having done so, we can examine each variable directly (see figure 19).  
  
_Figure 19: Hitting the breakpoint at the function pointer in rsi and examining the function parameters._

These are the same values passed in as command-line arguments. We can then use p to step over call rsi and examine rax to determine the return value (as in figure 20).  
  
_Figure 20: Determining the return value by examining_ _rax_ _._

Without source code, we can’t be certain of the exact type of each value. However, based on the above output, we can reasonably assume that the function signature of ProcessData is something akin to the following:

“`cpp

DWORD ProcessData(DWORD, LPCWSTR, LPCWSTR, DWORD, DWORD);  
“`

Or, for non-Windows code:

“`cpp

long ProcessData(long, wchar_t*, wchar_t*, long, long);  
“`

We now abuse this knowledge to complete the attack.

#### _Living Off The Land_

Recall that in this scenario, the attacker does not have the ability to plant a malicious DLL on the filesystem. However, the Windows operating system contains numerous native libraries and executables installed by default. In theory, an attacker can call any method from a native library so long as it somewhat resembles the signature in figure 20.

Employing native OS files in an attack is a technique known as “Living off the Land (with Binaries and Scripts)”, or “LOL(BAS)”. In our experience, the signatures don’t have to be an exact match, so long as the differences do not meaningfully impact the behavior of the chosen function. For example, the following signatures may prove to be “close enough” to the signature recovered in the previous section:

“`cpp

DWORD func(DWORD, LPWSTR);  
VOID func(DWORD, LPCWSTR, LPCWSTR, DWORD);  
DWORD func(DWORD, LPCWSTR);  
DWORD func(DWORD, LPWSTR, LPWSTR);  
VOID func(DWORD, BYTE);  
“`

Other, more complicated signatures may also be compatible depending on how the function uses misaligned arguments, how the application calls the function, the application’s calling convention, and other factors.

We must choose a function that meets the following criteria:

  1. It must do something useful for an attacker.
  2. It must be present in a predictable location in default installations of Windows.
  3. Its signature must be compatible with the signature recovered from WinDBG.

In this case, the [URLDownloadToFileW](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123\(v=vs.85\)) function from urlmon.dll meets each of these requirements:

“`cpp

HRESULT URLDownloadToFile(  
LPUNKNOWN pCaller,  
LPCTSTR szURL,  
LPCTSTR szFileName,  
_Reserved_ DWORD dwReserved,  
LPBINDSTATUSCALLBACK lpfnCB  
);  
“`

pCaller is an optional parameter to specify an IUnknown interface. We want this to be null. szURL is a UTF-16 string of the URL to retrieve data from. szFileName is a UTF-16 string of the file name to save the data as. dwReserved is an unused parameter and must be null. lpfnCB is a optional pointer to an IBindStatusCallback interface, which we also want to be null. These parameters map to id, title, content, operation, and node, respectively.

With this in mind, we can trigger a remote download like the one in figure 21.  
  
_Figure 21: Triggering a remote download using URLDownloadToFileW._

This triggers a GET request on the remote web server as figure 22 demonstrates.  
  
_Figure 22: Triggering a GET request to the remote web server._

This demonstrates that the above HTTP request successfully loaded urlmon.dll  
and invoked URLDownloadToFileW in Worker.exe.

An attacker could weaponize this attack by using the above technique to download a custom DLL into a predictable location and then send a second request to load and execute code from this DLL. We demonstrate this next.

#### _Remote Code Execution_

We add and export the following method in EvilDLL.dll to demonstrate this point:

“`cpp

DWORD AttackerMethod(DWORD a, LPCWSTR b, LPCWSTR c, DWORD e, DWORD f)  
{  
system(“whoami > C:\\\Users\\\Public\\\remote_info.txt”);  
return 0;  
}  
“`

We recompile EvilDLL.dll and host it on the attacker web root. We then issue the following request to the target machine to download the DLL (see figure 22).  
  
_Figure 22: Instructing the target machine to download_ _EvilDLL_ _._

After verifying the Apache logs for the download (see figure 23)…  
  
 _Figure 23: Verifying the apache logs for download._

…we trigger the DLL (see figure 24).  
  
_Figure 24: Triggering the download of_ _EvilDLL_ _._

We can check C:\Users\Public\remote_info.txt on the target machine to confirm the OS command executed successfully, as in figure 25.  
  
_Figure 25: Confirming the OS command execution was successful._

#### **Other Useful Native Windows Methods**

In the above example, we used URLDownloadToFileW to download a remote DLL onto the target file system. We chose this function because its function signature was similar to the function imported by the Worker.exe process. However, URLDownloadToFileW will not work in all situations. To exploit dynamic-linking injection in other situations, different functions may be needed.

Praetorian identified the following Win32 API methods as being of potential use to security researchers when exploiting dynamic-linking injection. Praetorian chose the following functions because they may be useful to an attacker and are in predictable locations. Recall that the function signatures do not have to match perfectly, so it is worth trying even partial matches.

This serves only as a first enumeration, as there most likely are others on Windows that perform useful features for an attacker. Note also that many Win32 APIs have both [ANSI (A) and wide-character (W) variants](https://learn.microsoft.com/en-us/windows/win32/intl/unicode-in-the-windows-api).
  
  
  [**ShellExecute**](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea) – Performs an operation (execution, read, write, and more) on a specified file.  
  Shell32.dll  
  
  '''cpp  
  
  HINSTANCE ShellExecuteA(  
    [in, optional] HWND   hwnd,  
    [in, optional] LPCSTR lpOperation,  
    [in]           LPCSTR lpFile,  
    [in, optional] LPCSTR lpParameters,  
    [in, optional] LPCSTR lpDirectory,  
    [in]           INT    nShowCmd  
  );  
  '''  
  
  [**WinExec**](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-winexec) – Runs a specified application  
  Kernel32.dll  
  
  '''cpp  
  
  UINT WinExec(  
    [in] LPCSTR lpCmdLine,  
    [in] UINT   uCmdShow  
  );  
  '''  
  
  [**CreateProcess**](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa?redirectedfrom=MSDN) – Creates a new process  
  Kernel32.dll  
  
  '''cpp  
  
  BOOL CreateProcessA(  
    [in, optional]      LPCSTR                lpApplicationName,  
    [in, out, optional] LPSTR                 lpCommandLine,  
    [in, optional]      LPSECURITY_ATTRIBUTES lpProcessAttributes,  
    [in, optional]      LPSECURITY_ATTRIBUTES lpThreadAttributes,  
    [in]                BOOL                  bInheritHandles,  
    [in]                DWORD                 dwCreationFlags,  
    [in, optional]      LPVOID                lpEnvironment,  
    [in, optional]      LPCSTR                lpCurrentDirectory,  
    [in]                LPSTARTUPINFOA        lpStartupInfo,  
    [out]               LPPROCESS_INFORMATION lpProcessInformation  
  );  
  '''  
  
  [**ReadFile**](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile) – Reads a specified file  
  Kernel32.dll  
  
  '''cpp  
  
  BOOL ReadFile(  
    [in]                HANDLE       hFile,  
    [out]               LPVOID       lpBuffer,  
    [in]                DWORD        nNumberOfBytesToRead,  
    [out, optional]     LPDWORD      lpNumberOfBytesRead,  
    [in, out, optional] LPOVERLAPPED lpOverlapped  
  );  
  '''  
  
  [**DeleteFile**](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-deletefilea) – Deletes a specified file  
  Kernel32.dll  
  
  '''cpp  
  
  BOOL DeleteFileA(  
    [in] LPCSTR lpFileName  
  );  
  '''  
  
  [**CreateDirectory**](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectorya) – Creates a new directory  
  Kernel32.dll  
  
  '''cpp  
  
  BOOL CreateDirectoryA(  
    [in]           LPCSTR                lpPathName,  
    [in, optional] LPSECURITY_ATTRIBUTES lpSecurityAttributes  
  );  
  '''  
  
  [**ExitWindowsEx**](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-exitwindowsex) – Logs off the interactive user and shuts down the system  
  User32.dll  
  
  '''cpp  
  
  BOOL ExitWindowsEx(  
    [in] UINT  uFlags,  
    [in] DWORD dwReason  
  );  
  '''

### **Remediating Dynamic-Linking Injection**

Dynamic-linking injection is fundamentally a problem with untrusted user input. Due to the highly impactful consequences, we advise preventing users from passing any input into LoadLibrary, LoadLibraryEx, or GetProcAddress.

Where this is not feasible, user input should be strictly validated, and all DLLs should be loaded from known, trusted locations. Developers should structure their application files not to require the ..\ character sequence to load different libraries. Depending on the use case, incorporating the dwFlags argument to [LoadLibraryEx](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa) may further restrict library access without impairing application functionality.

### **Concluding Thoughts**

Dynamic-linking injection offers an interesting, albeit uncommon, vulnerability class. While the prerequisites for this attack make it a difficult attack vector, the consequences can be devastating. Depending on the nature of the calling application, an attacker could abuse this for several high-impact attacks, as discussed in this article.

As with many exploits, this vulnerability is fundamentally a problem with handling untrusted user input. LoadLibrary, LoadLibraryEx, and GetProcAddress are not common destinations for user input, which may lead developers to apply less scrutiny when handling library file paths partially under the user’s control. Similar vulnerabilities may arise from untrusted user input passed to [GetModuleHandle](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea), though we did not discuss them in this article.

Furthermore, similar issues may arise on Linux and MacOS systems when loading shared libraries (.so) or dynamic libraries (.dylib) via [dlopen](https://man7.org/linux/man-pages/man3/dlopen.3.html) and [dlsym](https://man7.org/linux/man-pages/man3/dlsym.3.html). These functions are rough equivalents to LoadLibrary and GetProcAddress, respectively.

## About the Authors

![Joseph Henry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Joseph Henry](https://www.praetorian.com/author/joseph-henry/)

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
