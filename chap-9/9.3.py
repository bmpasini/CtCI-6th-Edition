# If you were designing a web crawler, how would you avoid getting into infinite loops?

# Marking visited pages as visited using a hashtable, where the key can be the URL. However, the
# hashtable can grow too big. Then, an alternative would be to store this data in a key-value pair
# database such as BerkeleyDB, or Cassandra, which can be scaled in a cluster. We can cache most
# recently used URLs, to speed things up.