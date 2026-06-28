---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_default-credentials-on-sony-swag-time.md
original_filename: 2023-03-10_default-credentials-on-sony-swag-time.md
title: Default Credentials on Sony- Swag Time
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: d831698bcb38b2f02258ab211f491a55fe57a43cbd8debb07c503c158d3dc7f5
text_sha256: ae78d550a66fa00c91b7bb8036824763ecb63db42025f7d77ef12141423f9d3a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Default Credentials on Sony- Swag Time

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_default-credentials-on-sony-swag-time.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `d831698bcb38b2f02258ab211f491a55fe57a43cbd8debb07c503c158d3dc7f5`
- Text SHA256: `ae78d550a66fa00c91b7bb8036824763ecb63db42025f7d77ef12141423f9d3a`


## Content

---
title: "Default Credentials on Sony- Swag Time"
url: "https://m7arm4n.medium.com/default-credentials-on-sony-swag-time-8e35681ad39e"
authors: ["Arman (@M7arm4n)"]
programs: ["Sony"]
bugs: ["Hardcoded credentials", "Information disclosure"]
publication_date: "2023-03-10"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1396
scraped_via: "browseros"
---

# Default Credentials on Sony- Swag Time

Default Credentials on Sony- Swag Time
M7arm4n
Follow
3 min read
·
Mar 11, 2023

116

2

Hi Guys, Again I'm here to review another of my finding on the Sony program, This write-up is about how to automate process helps you find High or even critical vulnerability easier.

https://hackerone.com/sony

What’s the default credential vulnerability !?

The term “default credentials vulnerability” describes a security problem where software, hardware, or systems that are supplied to users do not require them to create their own unique credentials but instead use default usernames and passwords. Attackers can acquire unauthorized access to the system or application by utilizing default credentials that are publicly known, which can lead to data loss, theft, or other negative repercussions.

How to find the default credential vulnerability !?

Finding this vulnerability is unique to your target and you can create infinity flows to find an IP, a subdomain, a virtual host, or a special open port. I decided to put my focus on this vulnerability, and after 3/2 weeks, I found up to 20 login pages that are vulnerable to default credentials. So here I want to share how I found 2 default credentials on Sony and what was my methodology …

The Sony bug bounty program launched on the HackerOne platform, The scope of this program includes all Sony products which means you can start your recon process from anywhere or anything :D

I decided to start by discovering CIDRs and ASNs with bgpview.io and bgp.he.net, these websites provide tools and information related to internet routing, particularly BGP routing. BGP routing is a protocol used to exchange routing information between different networks on the internet. The website offers tools to help network administrators and other users analyze BGP routing, such as visualizing routes and checking routing information. It also provides information on internet service providers and IP addresses. After some while, I had a long list of CIDRs and ASNs that belongs to Sony.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now time to Convert CIDRs and ASNs to IP range with mapcidr

for i in $(cat cidr-asn.txt) ; do echo "$i" | mapcidr -silent >> ip_list.txt ; done

After sorting results, Now time to check the validity of the DNS of IP addresses with My Privet Tools.

python iptracker.py -l ip_list.txt -o valid_ips.txt -silent -stats -t 50

Port Scan with naabu is my favorite part as most hunters skip this part because takes too much process, But I use multi-tread with python to make it really fast (I will explain this process in another write-up). This is a simple command for port scan, I used:

for sub in $(cat valid_ips.txt) ; do naabu -host $sub -p "1,3-4,6-7,9,13,17,19-26,30,32-33,37,42-43,49,53,70,79-85,88-90,99-100,106,109-111,113,119,125,135,139,143-144,146,161,163,179,199,211-212,222,254-256,259,264,280,301,306,311,340,366,389,406-407,416-417,425,427,443-445,458,464-465,481,497,500,512-515,524,541,543-545,548,554-555,563,587,593,616-617,625,631,636,646,648,666-668,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800-801,808,843,873,880,888,898,900-903,911-912,981,987,990,992-993,995,999-1002,1007,1009-1011,1021-1100,1102,1104-1108,1110-1114,1117,1119,1121-1124,1126,1130-1132,1137-1138,1141,1145,1147-1149,1151-1152,1154,1163-1166,1169,1174-1175,1183,1185-1187,1192,1198-1199,1201,1213,1216-1218,1233-1234,1236,1244,1247-1248,1259,1271-1272,1277,1287,1296,1300-1301,1309-1311,1322,1328,1334,1352,1417,1433-1434,1443,1455,1461,1494,1500-1501,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687-1688,1700,1717-1721,1723,1755,1761,1782-1783,1801,1805,1812,1839-1840,1862-1864,1875,1900,1914,1935,1947,1971-1972,1974,1984,1998-2010,2013,2020-2022,2030,2033-2035,2038,2040-2043,2045-2049,2065,2068,2099-2100,2103,2105-2107,2111,2119,2121,2126,2135,2144,2160-2161,2170,2179,2190-2191,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381-2383,2393-2394,2399,2401,2492,2500,2522,2525,2557,2601-2602,2604-2605,2607-2608,2638,2701-2702,2710,2717-2718,2725,2800,2809,2811,2869,2875,2909-2910,2920,2967-2968,2998,3000-3001,3003,3005-3007,3011,3013,3017,3030-3031,3052,3071,3077,3128,3168,3211,3221,3260-3261,3268-3269,3283,3300-3301,3306,3322-3325,3333,3351,3367,3369-3372,3389-3390,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689-3690,3703,3737,3766,3784,3800-3801,3809,3814,3826-3828,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000-4006,4045,4111,4125-4126,4129,4224,4242,4279,4321,4343,4443-4446,4449,4550,4567,4662,4848,4899-4900,4998,5000-5004,5009,5030,5033,5050-5051,5054,5060-5061,5080,5087,5100-5102,5120,5190,5200,5214,5221-5222,5225-5226,5269,5280,5298,5357,5405,5414,5431-5432,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678-5679,5718,5730,5800-5802,5810-5811,5815,5822,5825,5850,5859,5862,5877,5900-5904,5906-5907,5910-5911,5915,5922,5925,5950,5952,5959-5963,5987-5989,5998-6007,6009,6025,6059,6100-6101,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565-6567,6580,6646,6666-6669,6689,6692,6699,6779,6788-6789,6792,6839,6881,6901,6969,7000-7002,7004,7007,7019,7025,7070,7100,7103,7106,7200-7201,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777-7778,7800,7911,7920-7921,7937-7938,7999-8002,8007-8011,8021-8022,8031,8042,8045,8080-8090,8093,8099-8100,8180-8181,8192-8194,8200,8222,8254,8290-8292,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651-8652,8654,8701,8800,8873,8888,8899,8994,9000-9003,9009-9011,9040,9050,9071,9080-9081,9090-9091,9099-9103,9110-9111,9200,9207,9220,9290,9415,9418,9485,9500,9502-9503,9535,9575,9593-9595,9618,9666,9876-9878,9898,9900,9917,9929,9943-9944,9968,9998-10004,10009-10010,10012,10024-10025,10082,10180,10215,10243,10566,10616-10617,10621,10626,10628-10629,10778,11110-11111,11967,12000,12174,12265,12345,13456,13722,13782-13783,14000,14238,14441-14442,15000,15002-15004,15660,15742,16000-16001,16012,16016,16018,16080,16113,16992-16993,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221-20222,20828,21571,22939,23502,24444,24800,25734-25735,26214,27000,27352-27353,27355-27356,27715,28201,30000,30718,30951,31038,31337,32768-32785,33354,33899,34571-34573,35500,38292,40193,40911,41511,42510,44176,44442-44443,44501,45100,48080,49152-49161,49163,49165,49167,49175-49176,49400,49999-50003,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055-55056,55555,55600,56737-56738,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389" -exclude-ports 80,443,8443,21,25,22 -silent >> Portscan_result ; done

After completing the port scan, now time to service discovery with httpx

httpx -l Finall_result -nc  -sc -cl -title -random-agent -silent -tech-detect -follow-redirects >> httpx_new.txt

You can make all these steps automatically (except step 1, I recommend doing it manually). I grep Grafana from the httpx_new.txt file and got around 3~4 results, Open them in the browser and tested admin:admin Credential, and spuriously 2 of them logged successfully :D. I submitted reports immediately, and after 2 days both triggered and around 1 week Sony resolved the vulnerabilities and gives me swags.

Thank you for following me here, Don’t forget to follow me for more write-ups.

Twitter
