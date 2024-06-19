from typing import Dict, List
import pandas as pd
import json
import requests
import bs4
import urllib
import unicodedata
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from robots import process_robots, check_link_ok
from task2 import task2


# Task 3 - Producing a Bag Of Words for All Pages (2 Marks)
def task3(link_dictionary: Dict[str, List[str]], csv_filename: str):
    # Create lists to store the resulting columns of the dataframe
    link_url = []
    words = []
    seed_url = []

    # Iterate through the link_dictionary
    for seed, links in link_dictionary.items():
        for link in links:
            # Use the task2 function to get the words for each link_url
            words_dict = task2(link, "temp.json")

            # Extract the list of words for the current link_url
            words_list = words_dict.get(link, [])

            # Join the words_list into a single string separated by spaces
            words_string = " ".join(words_list)

            # Append the current values to the respective lists
            link_url.append(link)
            words.append(words_string)
            seed_url.append(seed)

    # Create a DataFrame from the data lists
    dataframe = pd.DataFrame({"link_url": link_url, "words": words, "seed_url": seed_url})
    # Sort the DataFrame by link_url and seed_url
    dataframe = dataframe.sort_values(by=["link_url", "seed_url"])
    # Save the DataFrame to a CSV file without the numeric index
    dataframe.to_csv(csv_filename, index=False)
    return dataframe

