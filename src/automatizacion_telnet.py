NetworkAutomation-1 console is now available... Press RETURN to get started.
chmod: /usr/lib/systemd/system/system-systemdx2dcryptsetup.slice: No such file o                                   r directory
chown: /usr/lib/systemd/system/system-systemdx2dcryptsetup.slice: No such file o                                   r directory
udhcpc: started, v1.37.0
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting select for 192.168.42.235, server 192.168.42.1
udhcpc: lease of 192.168.42.235 obtained from 192.168.42.1, lease time 3600
root@NetworkAutomation-1:~# ipconfig
bash: ipconfig: command not found
root@NetworkAutomation-1:~# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.42.235  netmask 255.255.255.0  broadcast 192.168.42.255
        ether 02:42:96:fd:b5:00  txqueuelen 1000  (Ethernet)
        RX packets 23  bytes 2082 (2.0 KB)
        RX errors 0  dropped 4  overruns 0  frame 0
        TX packets 7  bytes 1338 (1.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

root@NetworkAutomation-1:~# apt-get update
Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal-updates InRelease [128 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal-backports InRelease [128 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1275 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]
Get:6 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]
Get:7 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
Get:8 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [4850 kB]
Get:9 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [36.2 kB]
Get:10 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [4904 kB]
Get:11 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1588 kB]
Get:12 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [54.7 kB]
Get:13 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.4 kB]
Get:14 http://security.ubuntu.com/ubuntu focal-security InRelease [128 kB]
Get:15 https://apt.releases.hashicorp.com focal InRelease [4429 B]
Err:15 https://apt.releases.hashicorp.com focal InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY AA16FCBCA621E701
Get:16 http://ppa.launchpad.net/ansible/ansible/ubuntu focal InRelease [18.0 kB]
Get:17 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [32.5 kB]
Get:18 http://ppa.launchpad.net/ansible/ansible/ubuntu focal/main amd64 Packages [1086 B]
Get:19 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [4368 kB]
Get:20 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [4710 kB]
Get:21 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [1300 kB]
Reading package lists... Done
W: GPG error: https://apt.releases.hashicorp.com focal InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY AA16FCBCA621E701
E: The repository 'https://apt.releases.hashicorp.com focal InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
root@NetworkAutomation-1:~# ping www.google.com
PING www.google.com (142.251.152.119) 56(84) bytes of data.
64 bytes from 142.251.152.119: icmp_seq=1 ttl=127 time=23.7 ms
64 bytes from 142.251.152.119: icmp_seq=2 ttl=127 time=21.7 ms
64 bytes from 142.251.152.119: icmp_seq=3 ttl=127 time=23.5 ms
64 bytes from 142.251.152.119: icmp_seq=4 ttl=127 time=17.5 ms
64 bytes from 142.251.152.119: icmp_seq=5 ttl=127 time=19.3 ms
64 bytes from 142.251.152.119: icmp_seq=6 ttl=127 time=19.5 ms
64 bytes from 142.251.152.119: icmp_seq=7 ttl=127 time=20.6 ms
64 bytes from 142.251.152.119: icmp_seq=8 ttl=127 time=18.8 ms
64 bytes from 142.251.152.119: icmp_seq=9 ttl=127 time=20.5 ms
64 bytes from 142.251.152.119: icmp_seq=10 ttl=127 time=21.0 ms
64 bytes from 142.251.152.119: icmp_seq=11 ttl=127 time=25.4 ms
64 bytes from 142.251.152.119: icmp_seq=12 ttl=127 time=22.7 ms
64 bytes from 142.251.152.119: icmp_seq=13 ttl=127 time=22.2 ms
64 bytes from 142.251.152.119: icmp_seq=14 ttl=127 time=17.6 ms
64 bytes from 142.251.152.119: icmp_seq=15 ttl=127 time=18.2 ms
64 bytes from 142.251.152.119: icmp_seq=16 ttl=127 time=24.5 ms
64 bytes from 142.251.152.119: icmp_seq=17 ttl=127 time=22.7 ms
64 bytes from 142.251.152.119: icmp_seq=18 ttl=127 time=25.7 ms
64 bytes from 142.251.152.119: icmp_seq=19 ttl=127 time=20.0 ms
64 bytes from 142.251.152.119: icmp_seq=20 ttl=127 time=23.3 ms
^Z
[1]+  Stopped                 ping www.google.com
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# y
bash: y: command not found
root@NetworkAutomation-1:~# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.42.235  netmask 255.255.255.0  broadcast 192.168.42.255
        ether 02:42:96:fd:b5:00  txqueuelen 1000  (Ethernet)
        RX packets 25442  bytes 36770141 (36.7 MB)
        RX errors 0  dropped 4  overruns 0  frame 0
        TX packets 5161  bytes 286289 (286.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

root@NetworkAutomation-1:~# ping 192.168.42.70
PING 192.168.42.70 (192.168.42.70) 56(84) bytes of data.
From 192.168.42.235 icmp_seq=1 Destination Host Unreachable
From 192.168.42.235 icmp_seq=2 Destination Host Unreachable
From 192.168.42.235 icmp_seq=3 Destination Host Unreachable
From 192.168.42.235 icmp_seq=4 Destination Host Unreachable
From 192.168.42.235 icmp_seq=5 Destination Host Unreachable
From 192.168.42.235 icmp_seq=6 Destination Host Unreachable
From 192.168.42.235 icmp_seq=7 Destination Host Unreachable
From 192.168.42.235 icmp_seq=8 Destination Host Unreachable
From 192.168.42.235 icmp_seq=9 Destination Host Unreachable
^Z
[2]+  Stopped                 ping 192.168.42.70
root@NetworkAutomation-1:~# ping 192.168.122.70
PING 192.168.122.70 (192.168.122.70) 56(84) bytes of data.
^Z
[3]+  Stopped                 ping 192.168.122.70
root@NetworkAutomation-1:~# ping 192.168.122.70
PING 192.168.122.70 (192.168.122.70) 56(84) bytes of data.
^Z
[4]+  Stopped                 ping 192.168.122.70
root@NetworkAutomation-1:~# ping 192.168.42.70
PING 192.168.42.70 (192.168.42.70) 56(84) bytes of data.
64 bytes from 192.168.42.70: icmp_seq=2 ttl=255 time=7.70 ms
64 bytes from 192.168.42.70: icmp_seq=3 ttl=255 time=3.81 ms
64 bytes from 192.168.42.70: icmp_seq=4 ttl=255 time=4.18 ms
64 bytes from 192.168.42.70: icmp_seq=5 ttl=255 time=4.47 ms
64 bytes from 192.168.42.70: icmp_seq=6 ttl=255 time=3.63 ms
64 bytes from 192.168.42.70: icmp_seq=7 ttl=255 time=2.51 ms
64 bytes from 192.168.42.70: icmp_seq=8 ttl=255 time=6.13 ms
64 bytes from 192.168.42.70: icmp_seq=9 ttl=255 time=3.50 ms
64 bytes from 192.168.42.70: icmp_seq=10 ttl=255 time=3.59 ms
64 bytes from 192.168.42.70: icmp_seq=11 ttl=255 time=3.74 ms
64 bytes from 192.168.42.70: icmp_seq=12 ttl=255 time=5.42 ms
64 bytes from 192.168.42.70: icmp_seq=13 ttl=255 time=4.98 ms
64 bytes from 192.168.42.70: icmp_seq=14 ttl=255 time=3.13 ms
64 bytes from 192.168.42.70: icmp_seq=15 ttl=255 time=3.56 ms
64 bytes from 192.168.42.70: icmp_seq=16 ttl=255 time=4.13 ms
64 bytes from 192.168.42.70: icmp_seq=17 ttl=255 time=4.60 ms
64 bytes from 192.168.42.70: icmp_seq=18 ttl=255 time=3.53 ms
64 bytes from 192.168.42.70: icmp_seq=19 ttl=255 time=3.99 ms
^X64 bytes from 192.168.42.70: icmp_seq=20 ttl=255 time=4.89 ms
^Z
[5]+  Stopped                 ping 192.168.42.70
root@NetworkAutomation-1:~# telnet 192.168.122.70
Trying 192.168.122.70...
^Z
^X
^Xtelnet: Unable to connect to remote host: Connection refused
root@NetworkAutomation-1:~#
root@NetworkAutomation-1:~# telnet 192.168.42.70
Trying 192.168.42.70...
Connected to 192.168.42.70.
Escape character is '^]'.

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************

User Access Verification

Username: monica
Password:
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
Router>enable
% No password set
Router>
Router>enable
% No password set
Router>exit
Connection closed by foreign host.
root@NetworkAutomation-1:~# telnet 192.168.42.70
Trying 192.168.42.70...
Connected to 192.168.42.70.
Escape character is '^]'.

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************

User Access Verification

Username: monica
Password:
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
Router>enable
Password:
Router#wr
Building configuration...
[OK]
Router#exit
Connection closed by foreign host.
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~#
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# python3 python31.py
Enter your Telnet username: monica
Password:

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
Router>enable
Password:
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface loopback 0
Router(config-if)#ip address 1.1.1.1 255.255.255
% Incomplete command.

Router(config-if)#end
Router#exit

root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# python3 python31.py
Enter your Telnet username: monica
Password:

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
Router>enable
Password:
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface loopback 0
Router(config-if)#ip address 1.1.1.1 255.255.255.255
Router(config-if)#end
Router#exit

root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# nano python31.py
root@NetworkAutomation-1:~# python3 python31.py
Enter your Telnet username: monica
Password:

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************
Router>enable
Password:
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface loopback 0
Router(config-if)#ip address 1.1.1.1 255.255.255.255
Router(config-if)#exit
Router(config)#interface loopback 1
Router(config-if)#ip address 2.2.2.2 255.255.255.255
Router(config-if)#exit
Router(config)#router ospf 1
Router(config-router)#network 0.0.0.0 255.255.255.255 area 0
Router(config-router)#end
Router#exit

root@NetworkAutomation-1:~# cat python31.py
import getpass
import telnetlib

HOST = "192.168.42.70"
user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"configure terminal\n")
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
