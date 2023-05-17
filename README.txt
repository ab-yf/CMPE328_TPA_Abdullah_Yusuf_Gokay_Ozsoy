Twitter Sentiment Analysis Tool
This repository contains a Twitter sentiment analysis tool built using AWS EC2, Python, and various libraries and technologies. The tool provides sentiment analysis of tweets, categorizing them as positive, negative, or neutral. Below are the key components and features of this tool:

Features
Sentiment Analysis: Utilized TextBlob, a Python library, for sentiment analysis of tweets. The tool categorizes the sentiment of each tweet as positive, negative, or neutral.

Twitter API Integration: Implemented Tweepy, a Python library, to import tweets by establishing a connection with the Twitter API. This allows the tool to fetch real-time tweets for sentiment analysis.

Sentiment Visualization: Employed Matplotlib, a Python plotting library, to generate a sentiment pie chart based on the analyzed tweets. The pie chart provides a visual representation of the distribution of positive, negative, and neutral sentiments.

AWS EC2 Integration: Integrated AWS EC2, a cloud computing service, for seamless deployment and hosting of the application. This ensures that the sentiment analysis tool is easily accessible and scalable.

Docker Containerization: Set up a Docker container to ensure portability and efficient deployment of the application. Docker allows for easy packaging of the tool and its dependencies, making it straightforward to deploy and run the application in various environments.

How to Use
To use the Twitter sentiment analysis tool, follow the steps below:

Open the Putty App.

Enter the host name or IP address of the AWS Instance (Public IPv4 DNS address).

Click on the connection tab on the side of the window. Select SSH(+) and click on Auth. Then browse for your private key file that you generated with PuttyGen (.ppk).

Click on "open" in the main tab.

Write the following commands in order:

bash
Copy code
cd testing_python/
dir
sudo pip3 install tweepy
sudo pip3 install TextBlob
python3 TSA2.py
Write the desired inputs and press Enter.

Please note that this tool requires the installation of the necessary dependencies (tweepy and TextBlob) before running the Python script (TSA2.py).

Disclaimer
Please note that with the recent changes in Twitter's ownership, securing an API from Twitter has become a bit difficult. This may affect the availability and functionality of the Twitter sentiment analysis tool. We recommend checking the current status of Twitter's API access and ensuring compliance with any requirements or limitations imposed by Twitter.

Feel free to modify and enhance this tool according to your specific needs.

License
This project is licensed under the MIT License.

We hope you find this Twitter sentiment analysis tool useful and insightful. If you have any questions or suggestions, please feel free to reach out. Happy analyzing!
