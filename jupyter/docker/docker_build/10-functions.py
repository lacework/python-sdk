def query_snowflake(query):
    """Returns a Pandas DataFrame from a text based SQL query."""
    cs.execute(query)
    return cs.fetch_pandas_all()
