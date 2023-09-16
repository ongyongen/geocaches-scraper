"""
ddd
"""

from scraper import GeocacheScraper

def test_extract_data():
    """
    Test that restaurant data (from a list) is collected
    into a dataframe for subsequent data processing steps
    """
    scraper = GeocacheScraper()
    scraper.scrape_table_data()

    assert len(scraper.gc_df) != 0

    cols = [
        'cache_id', 'cache_code', 'name', 'favorite_points',
        'geocache_type', 'container_type', 'difficulty', 'terrain',
        'latitude', 'longitude', 'details_url', 'placed_date',
        'last_found_date', 'owner_name', 'owner_id', 'trackable_count'
    ]

    for col in cols:
        assert col in scraper.gc_df.columns

def test_clean_data():
    """
    ddd
    """

    scraper = GeocacheScraper()
    scraper.scrape_table_data()
    scraper.clean_table_data()

    assert isinstance(scraper.gc_df.loc[0,'favorite_points'], int)
    assert isinstance(scraper.gc_df.loc[0,'geocache_type'], str)
    assert isinstance(scraper.gc_df.loc[0,'container_type'], str)
    assert isinstance(scraper.gc_df.loc[0,'difficulty'], float)
    assert isinstance(scraper.gc_df.loc[0,'terrain'], float)

    assert 'www.geocaching.com' in scraper.gc_df.loc[0,'details_url']

    cleaned_cols = [
        "cache_id", "cache_code", "name", "geocache_type", "container_type",
        "difficulty", "terrain",
        "favorite_points", "trackable_count", "latitude", "longitude",
        "owner_id", "owner_name", "placed_date", "last_found_date", "details_url"
    ]

    for col in cleaned_cols:
        assert col in scraper.gc_df.columns

