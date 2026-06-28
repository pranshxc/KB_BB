---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-12_second-bite-on-gitlab-and-some-interesting-ruby-functionsfeatures.md
original_filename: 2018-12-12_second-bite-on-gitlab-and-some-interesting-ruby-functionsfeatures.md
title: Second bite on GitLab, and some interesting Ruby functions/features
category: documents
detected_topics:
- command-injection
- file-upload
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- file-upload
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: b3273fc56a8d4c14b8e1e59fef9beaf08c0b7afffd086d96d194e546373229d3
text_sha256: 12be771cc1f5be75faf51acf58267fb94c7c814624daa5eafa18d4d68dd7edf5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Second bite on GitLab, and some interesting Ruby functions/features

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-12_second-bite-on-gitlab-and-some-interesting-ruby-functionsfeatures.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b3273fc56a8d4c14b8e1e59fef9beaf08c0b7afffd086d96d194e546373229d3`
- Text SHA256: `12be771cc1f5be75faf51acf58267fb94c7c814624daa5eafa18d4d68dd7edf5`


## Content

---
title: "Second bite on GitLab, and some interesting Ruby functions/features"
page_title: "Second bite on GitLab, and some interesting Ruby functions/features - Nyangawa"
url: "https://blog.nyangawa.me/security/CVE-2018-18649-Gitlab-RCE/"
final_url: "https://blog.nyangawa.me/security/CVE-2018-18649-Gitlab-RCE/"
authors: ["Nyangawa"]
programs: ["GitLab"]
bugs: ["RCE"]
bounty: "10,000"
publication_date: "2018-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5530
---

# Second bite on GitLab, and some interesting Ruby functions/features 

# Brief

It’s been a while since I wrote something in this blog last time. I just posted something about several bugs I found several months ago in GitHub Pages and GitHub Enterprise. Go check them out if you are interested in some more examples of incorrect path sanitizing and symbolic links in real world softwares!

But today I’m not going to talk about more of those. I’m going introduce some recent findings about Ruby and how did I a find an RCE bug in GitLab. ([CVE-2018-18649](https://about.gitlab.com/2018/10/29/security-release-gitlab-11-dot-4-dot-3-released/))

# Ruby and GitLab

I wrote Ruby a lot when I was still in university. I used Ruby almost everywhere I could use and even once submitted an assignment of my Operating System course about threads and processes. However, after graduation I didn’t have much time to continue on the cool stuff with Ruby and focused on something else. :(

Recently, the experiences during the code auditing of GitLab, GitHub and several other cool Ruby projects recalls me the best days of learning Ruby and feels me like I’m designing the software and refining the code snippets with the developers.

As many people say, Ruby is an extremely flexible language and this flexibility brings us elegant implementations, the freedom of creating DSL and etc. However the flexibility also brings unnoticeable bugs. Here I’m going to show some code snippets existed in GitLab.

## Duck Typing

> If it walks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

GitLab uses [Grape](https://github.com/ruby-grape/grape) to create their APIs, for example, the following API is used to upload attachments to the wiki of a project.
  
  
  params do
  requires :file, type: File, desc: 'The attachment file to be uploaded'
  optional :branch, type: String, desc: 'The name of the branch'
  end
  post ":id/wikis/attachments", requirements: API::PROJECT_ENDPOINT_REQUIREMENTS do
  authorize! :create_wiki, user_project
  
  result = ::Wikis::CreateAttachmentService.new(user_project,
  current_user,
  commit_params(declared_params(include_missing: false))).execute
  ...
  end
  

Normally, Rack intercepts file uploading requests and sets `params[key][:tempfile]` and `params[key][:filename]` to the temporary path of the uploaded file and the original filename. So GitLab reads the content of the temp file and saves it afterwards.
  
  
  def commit_params(attrs)
  {
  file_name: attrs[:file][:filename],
  file_content: File.read(attrs[:file][:tempfile]),
  branch_name: attrs[:branch]
  }
  end
  

At the same time, grape has a simple validation for `type: File`:
  
  
  def value_coerced?(value)
  # Rack::Request creates a Hash with filename,
  # content type and an IO object. Do a bit of basic
  # duck-typing.
  value.is_a?(::Hash) && value.key?(:tempfile)
  end
  

Well, it’s not really duck-typing here. But the comments of the developer reminds me this and it’s surely thinking about duck-typing when it was implementing this function.

Unfortunately, only duck quacking is not enough. A key named `:tempfile` exists in the `params[:file]` hash doesn’t really mean `params[:file]` is really a uploaded file as expected.

Sending a simple POST request, we can easily smuggle our duck-like bird to pass this duck typing check by setting `file[tempfile]` in the form data.
  
  
  curl -d "file[tempfile]=/etc/passwd&file[filename]=123" http://host:port
  

So, our bird can pass the inspection and tell us anything within a GitLab instance.

![2018-12-12-CVE-2018-18649-Gitlab-RCE_1](/assets/2018-12-12-CVE-2018-18649-Gitlab-RCE_1.png)

## Inheritance

Inheritance is not a Ruby only feature, inheritance exists in almost every OOP language. It is a very helpful for designing softwares. However it also brings some security risks.

In Ruby, there’s a function `Kernel#open`
  
  
  open(path [, mode [, perm]] [, opt]) → io or nil
  ...
  If path starts with a pipe character ("|"), a subprocess is created, connected to the caller by a pair of pipes. The returned IO object may be used to write to the standard input and read from the standard output of this subprocess.
  

Which means, this function could be used to spawn sub-processes as long as the first char of `path` is the pipe symbol.
  
  
  irb(main):001:0> Kernel.open('|id').read
  => "uid=0(root) gid=0(root) groups=0(root)\n"
  irb(main):002:0> open('|id').read
  => "uid=0(root) gid=0(root) groups=0(root)\n"
  

And, there are also some other functions having similar behavior, `IO::read` for example:
  
  
  read(name, [length [, offset]] [, opt] ) → string
  Opens the file, optionally seeks to the given offset, then returns length bytes (defaulting to the rest of the file). read ensures the file is closed before returning.
  
  If name starts with a pipe character ("|"), a subprocess is created in the same way as Kernel#open, and its output is returned.
  

Which means:
  
  
  irb(main):003:0> path = '|id'
  => "|id"
  irb(main):004:0> IO.read path
  => "uid=0(root) gid=0(root) groups=0(root)\n"
  

Well, so what’s the business with inheritance here? A very very important point of inheritance is that, the public methods of a parent class is inherited by a child class, we can directly use those inherited methods in child classes as long as we didn’t override them. In Ruby, `File` is a child class of `IO`
  
  
  irb(main):005:0> File.ancestors
  => [File, IO, File::Constants, Enumerable, Object, Kernel, BasicObject]
  

So,
  
  
  irb(main):006:0> path = '|id'
  => "|id"
  irb(main):007:0> File.read path
  (irb):7: warning: IO.read called on File to invoke external command
  => "uid=0(root) gid=0(root) groups=0(root)\n"
  

easy huh? Till now, the arbitrary file read bug can be directly used to execute system commands remotely.

![2018-12-12-CVE-2018-18649-Gitlab-RCE_2](/assets/2018-12-12-CVE-2018-18649-Gitlab-RCE_2.png)

# Some thoughts

I was quite shocked when I first discovered this `File.read` surprise. No matter how to explain, I still can’t accept the fact that calling `File.read` method on a `|` started string spawns a sub-process instead of opening a file with that name.

The fact is, not only method `read`:
  
  
  pry(main)> (File.methods - File.methods(false)) & IO.methods(false)
  => [:console,
  :read,
  :sysopen,
  :for_fd,
  :popen,
  :foreach,
  :binread,
  :new,
  :binwrite,
  :write,
  :copy_stream,
  :select,
  :pipe,
  :open,
  :try_convert,
  :readlines]
  

All of these functions are inherited by `File` directly from `IO`, and some of them have similar behavior with `File.read`.

According to the warning message printed in irb, I believe that Ruby-lang developers already know this and are trying to rise notice of the users. It’s a good signal but I think it might be better to totally avoid this kind of unexpected behavior from the language implementation layer, such as override them in `File`.

# Timeline

[GitLab’s bug bounty program](https://hackerone.com/gitlab) is very responsive and regularly updated to keep reporters in the loop.

  * Oct 24th, Reported to GitLab
  * Oct 29th, Patch released https://about.gitlab.com/2018/10/29/security-release-gitlab-11-dot-4-dot-3-released/
  * Oct 29th, $10000 bounty was rewarded for this report

**__Categories:** [security](/categories/#security)

**__Updated:** December 12, 2018

[__Twitter](https://twitter.com/intent/tweet?text=Second+bite+on+GitLab%2C+and+some+interesting+Ruby+functions%2Ffeatures%20https%3A%2F%2Fblog.nyangawa.me%2Fsecurity%2FCVE-2018-18649-Gitlab-RCE%2F "Share on Twitter") [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.nyangawa.me%2Fsecurity%2FCVE-2018-18649-Gitlab-RCE%2F "Share on Facebook") [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fblog.nyangawa.me%2Fsecurity%2FCVE-2018-18649-Gitlab-RCE%2F "Share on LinkedIn") [Previous](/security/Github-Path-Traversal-To-RCE/ "Path Traversal in GitHub pages, and more for GitHub Enterprise
") [Next](/security/GitLab-Local-File-Read/ "Chaining multiple low-impact bugs to arbitrary file read in GitLab
")
