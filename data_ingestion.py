###
# data_ingestion.py

# This module handles data ingestion for solar power forecasting.
# Polling mechanism to fetch RTE data from RTE-API at regular intervals.

# Author : Simon Senegas
# Created : 2025-05-21
###
#%% Librairies
import requests
import pandas as pd
import logging  
import time