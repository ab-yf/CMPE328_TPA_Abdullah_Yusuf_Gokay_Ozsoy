# Twitter Sentiment Analysis Tool

This repository contains a Twitter sentiment analysis tool built using AWS EC2, Python, and various libraries and technologies. The tool provides sentiment analysis of tweets, categorizing them as positive, negative, or neutral. Below are the key components and features of this tool:

## Features

- **Sentiment Analysis**: Utilized TextBlob for sentiment analysis of tweets, categorizing them as positive, negative, or neutral.

- **Twitter API Integration**: Implemented Tweepy to import tweets by establishing a connection with the Twitter API.

- **Sentiment Visualization**: Employed Matplotlib to generate a sentiment pie chart based on the analyzed tweets.

- **AWS EC2 Integration**: Integrated AWS EC2 for seamless deployment and hosting of the application.

- **Docker Containerization**: Set up a Docker container to ensure portability and efficient deployment of the application.

## How to Use

To use the Twitter sentiment analysis tool, follow the steps below:

1. Open the Putty App.
2. Enter the host name or IP address of the AWS Instance (Public IPv4 DNS address).
3. Click on the connection tab on the side of the window. Select SSH(+) and click on Auth. Then browse for your private key file that you generated with PuttyGen (.ppk).
4. Click on "open" in the main tab.
5. Write the following commands in order:

    ```
    cd testing_python/
    dir
    sudo pip3 install tweepy
    sudo pip3 install TextBlob
    python3 TSA2.py
    ```

6. Write the desired inputs and press Enter.

Please note that this tool requires the installation of the necessary dependencies (`tweepy` and `TextBlob`) before running the Python script (`TSA2.py`).

## Disclaimer

Please note that with the recent changes in Twitter's ownership, securing an API from Twitter has become a bit difficult. This may affect the availability and functionality of the Twitter sentiment analysis tool. We recommend checking the current status of Twitter's API access and ensuring compliance with any requirements or limitations imposed by Twitter.

I hope you find this Twitter sentiment analysis tool useful and insightful. If you have any questions or suggestions, please feel free to reach out. Happy analyzing!
