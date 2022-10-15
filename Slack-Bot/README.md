# Slack-Bot
A bot is a nifty way to run code and automate tasks. In Slack, a bot is controlled programmatically via a bot user token that can access one or more of Slack's APIs. Read on to learn more about creating a bot for your workspace.
# Module Used

- import slack
- import os
- from pathlib import Path
- from dotenv import load_dotenv
- from flask import Flask, request, Response
- from slackeventsapi import SlackEventAdapter
- import string
- from datetime import datetime, timedelta
- import time

