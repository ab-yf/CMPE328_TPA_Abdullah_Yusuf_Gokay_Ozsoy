We chose the AWS EC2 cloud service. The reasons are:
1) Reliability:Amazon EC2 offers 99.9% availability for each Amazon EC2 region. 
The services are highly reliable where replacement of instances can be done easily and rapidly.
2) Security:Amazon works with Amazon VPC to provide robust networking and security for the compute resources. 
The compute instances are located in a VPC (Virtual Private Cloud) in a specific IP range.
This specific function helps the user in deciding which instances are exposed to the internet and which remains private.

We chose python as the programming language. The reasons are:
1) flexibility
2) Python is a great language for building RESTFUL APIs.The simplicity in the language, makes complex functions easier to
understand when a developer reads them.

-HOW OUR PROGRAM WORKS-
step1- open Putty App.
step2- Enter host name or IP adress of the AWS Instance (Public IPv4 DNS adress)
step3- Click to the connection tab on the side of the window. Select SSH(+). Click on Auth. Then browse your private key
file that you have generated with PuttyGen (.ppk).
step4-Click to "open" in the main tab.
step5-Write the following commands in-order:
	-cd testing_python/
	-dir
	-sudo pip3 install tweepy
	-sudo pip3 install TextBlob
	-python3 TSA2.py
step6-Write the desired inputs and push enter.
