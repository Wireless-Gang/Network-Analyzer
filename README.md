# Network-Analyzer

Wednesday, September 16, 2020
10:25 AM

Minimum Viable Product (MVP):
Create a command line tool that indicates how busy a network is by logging the number of MAC addresses in a given time.

Reason: 
We all have shared the frustration of waiting 20 minutes to download a video at the library or simply cannot view a document at your local coffee shop. We want to communicate this information to the user before they waste their time trying to stream or download.

Extensions:
	- In addition to the command line tool, have this script run on a rasp-pi in a remote location, then communicate this information to a server. The user can access this information BEFORE going to join the network. This information can be hosted on an app, email, etc.
	- Not only log the MAC addresses, but also the AMOUNT of network traffic at any given time
	- Examine the average Total Travel Time for each packet, to determine the SPEED of the network traffic.  


Helpful links: 
	- Mac address Tracker: https://www.netfort.com/blog/mac-address-tracker-using-network-traffic-analysis/
	- Nslookup: linux command line tool that will shwo you the IP addresses of the network, CON: slow as heck
	- Tshark!! -- command line version of wireshark that captures the bytes over the computer network and saves them into a file.
	
Requirements:
	- A UNIX operating system
	- Git to download the code
	- Docker? To make this easier to download
	- Python? Possibly on how we implement
	- Database, and possibly Pandas python library to analyze the data
	
Implementation: 

Jobs for this project: (7 undergraduate students)
	1) Group leader: make sure all of the allocated jobs are completed by their allocated deadlines. Help with miscellaneous jobs
	2) Research and coordinator: understand how all of the various parts actually talk to each other, and how this relates to our final goal
	3) GIT coordinator: set up a git location, and allocate the different folders for either the data analytics files, python files, and bash scripts. Make sure everyone has a git token and can go to you for help for push/pull to/from git
	4) TSHARK: either 1 or 2 people. Understand the tool and how to put the information we want into a file that we can parse 
	5) DATA PARSER: 1/2 people that will take the information from the out files in tshark in the programming language of your choice. When this file is run, it will output on the command line how busy the network is.
	6) NSLOOKUP:  1 person. very simple job of simply finding out the default gateway of the network. Then person can run a network scan and put input into out file for the data parsers
	7) User experience person: make sure that the experience is user friendly, i.e, the user can run ONE file and then have an output in a form that is easy to read and comprehend
	8) Formula person: come up with a simple formula for average packet time  
