"""
ddd
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
    dddd
    """

    # Start the scraper
    scraper = GeocacheScraper()
    scraper.scrape_table_data()
    scraper.clean_table_data()

    # Connect to MongoDB
    client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

    # Seed the DB with the newly scraped caches
    doc = client.geocaches
    geocaches_collection = doc[DB_NAME]
    geocaches_collection.drop()

    geocaches_collection.insert_many(scraper.json)

    print(event, context)

    return {
        'statusCode': 200,
        'body': json.dumps('All Singapore Geocaches are scraped!')
    }
