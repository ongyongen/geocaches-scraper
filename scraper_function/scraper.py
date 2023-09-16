"""
This file contains the geocaches scraper class
"""
from json import loads
import requests
import pandas as pd

from config import table_headers, table_params, table_cookies


class GeocacheScraper:
    """
    This class encapsulates methods to scrape the
    geocaches from the geocaching website
    """

    def __init__(self):

        # url for the table of all caches
        self.table_url = 'https://www.geocaching.com/api/proxy/web/search/v2'

        # url for the individual cache listing pages
        self.cache_url = 'https://www.geocaching.com/geocache/'

        # dataframe to copy over the scraped data
        self.gc_df = pd.DataFrame(columns=[
            'cache_id', 'cache_code', 'name', 'favorite_points',
            'geocache_type', 'container_type', 'difficulty', 'terrain',
            'latitude', 'longitude', 'details_url', 'placed_date',
            'last_found_date', 'owner_name', 'owner_id', 'trackable_count'
        ])

        # json format to return the scraped data for seeding the MongoDB
        self.json = {}

        # dictionary for decrypting the hints (at the individual cache listing pages)
        self.hint_decryption_keys = {
            "a": "n", "n": "a", "b": "o", "o": "b", "c": "p", "p": "c",
            "d": "q", "q": "d", "e": "r", "r": "e", "f": "s", "s": "f",
            "g": "t", "t": "g", "h": "u", "u": "h", "i": "v", "v": "i",
            "j": "w", "w": "j", "k": "x", "x": "k", "l": "y", "y": "l",
            "m": "z", "z": "m"
        }

        # dictionary for mapping int values to cache types
        self.cache_types = {
            2: "traditional",
            3: "multi-cache",
            4: "virtual",
            5: "letterbox",
            6: "event",
            8: "mystery",
            137: "earth",
            1858: "whereigo"
        }

        # dictionary for mapping int values to container types
        self.container_types = {
            1: "not specified",
            2: "micro",
            3: "regular",
            4: "large",
            5: "virtual",
            6: "other",
            8: "small"
        }

    def __extract_geocaches_data(self):
        """
        GET geocaches data from the url link provided
        """

        try:
            response = requests.get(
                self.table_url,
                params=table_params,
                cookies=table_cookies,
                headers=table_headers,
                timeout=100
            )

            # Successfully retrieved data
            if response.status_code == 200:
                return response.json()['results']

            # Did not successfully retrieve data
            print(f"API failed with status code {response.status_code}")
            print(f"Error: {response.text}")
            return None
        # Connection timeout
        except requests.exceptions.Timeout:
            print("Error: request to API timed out")
            return None

    def scrape_table_data(self):
        """
        Scrape geocaches data and output them into a 
        pandas dataframe
        """
        res = self.__extract_geocaches_data()
        # Obtain all relevant data for non-premium caches and copy it over to the dataframe
        for i, record in enumerate(res):
            if res[i]['premiumOnly'] is False:
                self.gc_df.loc[i, 'cache_id'] = record['id']
                self.gc_df.loc[i, 'cache_code'] = record['code']
                self.gc_df.loc[i, 'name'] = record['name']
                self.gc_df.loc[i, 'favorite_points'] = record['favoritePoints']
                self.gc_df.loc[i, 'difficulty'] = record['difficulty']
                self.gc_df.loc[i, 'terrain'] = record['terrain']
                self.gc_df.loc[i, 'latitude'] = \
                    record['postedCoordinates']['latitude']
                self.gc_df.loc[i, 'longitude'] = \
                    record['postedCoordinates']['longitude']
                self.gc_df.loc[i, 'details_url'] = record['detailsUrl']
                self.gc_df.loc[i, 'placed_date'] = record['placedDate']
                self.gc_df.loc[i, 'last_found_date'] = record['lastFoundDate']
                self.gc_df.loc[i, 'owner_name'] = record['owner']['username']
                self.gc_df.loc[i, 'owner_id'] = record['owner']['code']
                self.gc_df.loc[i, 'trackable_count'] = record['trackableCount']

                # Map int representation to cache and container type
                geocache_type = record['geocacheType']
                if geocache_type not in self.cache_types:
                    self.gc_df.loc[i, 'geocache_type'] = "other"
                else:
                    self.gc_df.loc[i, 'geocache_type'] = [
                        self.cache_types[geocache_type]]

                container_type = record['containerType']
                if container_type not in self.container_types:
                    self.gc_df.loc[i, 'container_type'] = "other"
                else:
                    self.gc_df.loc[i, 'container_type'] = [
                        self.container_types[container_type]]

    def __extract_integer_values_from_cell(self):
        """
        Helper function to obtain geocaches and container type
        """
        self.gc_df['geocache_type'] = list(
            map(lambda x: x[0], list(self.gc_df['geocache_type'])))
        self.gc_df['container_type'] = list(
            map(lambda x: x[0], list(self.gc_df['container_type'])))

    def __format_url_links(self):
        """
        Helper function to format URL link to geocaches page
        """
        # Format URL link to individual caches
        self.gc_df['details_url'] = list(map(
            lambda x: "www.geocaching.com" + str(x), list(self.gc_df['details_url'])
    ))

    def __format_datetime(self):
        """
        Helper function to format datetime string
        """
        self.gc_df['placed_date'] = list(map(lambda x: str(x).split(
            "T", maxsplit=1)[0] if len(str(x)) > 0 else x, list(self.gc_df['placed_date'])))
        found_date = [str(x).split("T", maxsplit=1)[0] if len(str(x)) >
                      0 else x for x in list(self.gc_df['last_found_date'])]
        self.gc_df['last_found_date'] = found_date

    def clean_table_data(self):
        """
        Cleans and processes geocaches data into a suitable format
        for export
        """
        self.__extract_integer_values_from_cell()
        self.__format_url_links()
        self.__format_datetime()

        # Rearrange columns
        self.gc_df = self.gc_df.reset_index()
        self.gc_df = self.gc_df.drop(columns=["index"])
        self.gc_df = self.gc_df.reindex(columns=[
            "cache_id", "cache_code", "name", "geocache_type", "container_type",
            "difficulty", "terrain",
            "favorite_points", "trackable_count", "latitude", "longitude",
            "owner_id", "owner_name", "placed_date", "last_found_date", "details_url"
        ])

        result = loads(self.gc_df.to_json(orient='records'))
        self.json = result

        print("Done scraping from table")
