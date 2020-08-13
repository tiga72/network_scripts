## Introduction

When network engineers work on complex changes that could possibly impact critical network device. It is good to be able to monitor these devices with ping. If the network change coincides with the monitored device downtime is an indication of network impact due to the changes and we could take appropriate steps (ie back out from the change)



## General info
This project is simple ping script that pings a list of ips(from ping-host.txt) every 5 secs
Each time the script runs, a list of pings are pinged and timestamp is logged(shown on screen)



## Setup
```
Use 'ctrl-C' to manually stop script
ping-host.txt format: ip-host, host-name
```



## Sample screen shots

root@eve-ng:~# cd py_script
root@eve-ng:~/py_script# ls
ping-host.txt  ping.py
root@eve-ng:~/py_script# ^C
root@eve-ng:~/py_script# cat ping-host.txt
74.6.143.26, yahoo
142.250.4.113, google
root@eve-ng:~/py_script# python ping.py

=================================
Thu Aug 13 06:59:53 2020

 yahoo is alive
 google is alive

=================================
Thu Aug 13 06:59:58 2020

 yahoo is alive
 google is alive

=================================
Thu Aug 13 07:00:03 2020

 yahoo is alive
 google is alive
^CTraceback (most recent call last):
  File "ping.py", line 34, in <module>
    main()
  File "ping.py", line 33, in main
    time.sleep(5)
KeyboardInterrupt
root@eve-ng:~/py_script# 