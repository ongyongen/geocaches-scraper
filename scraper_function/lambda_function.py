"""
This file contains the lambda function to trigger
the scraping of the geocaches
"""
import os
import json
from pymongo.mongo_client import MongoClient
import certifi
from dotenv import load_dotenv
from scraper import GeocacheScraper
from constants import DB_NAME

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

def lambda_handler(event, context):
    """
    This function runs the geocaches scraper
    and outputs the result into a mongodb collection
    """

    # Start the scraper
    scraper = GeocacheScraper()
    scraper.scrape_table_data()
    scraper.clean_table_data()

    # Connect to MongoDB
    client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

    # Seed the DB with the newly scraped caches
    collection = client.geocaches
    geocaches_collection = collection[DB_NAME]
    geocaches_collection.drop()

    geocaches_collection.insert_many(scraper.json)

    print(event, context)

    return {
        'statusCode': 200,
        'body': json.dumps('All Singapore Geocaches are scraped!')
    }
