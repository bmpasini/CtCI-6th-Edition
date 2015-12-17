# You have W billion URLs. How do you detect the duplicate documents? In this case, assume that
# "duplicate" means that the URLs are identical.

# 1 URL == 100 chars == 100 * 4 bytes
# 10 billion URLs == 10 * 2^30 * 100 * 4 == 4 * 2^40 == 4 Terabytes

# We can create a hash table to map each URL to a boolean representing whether the document has
# appeared before on the list or not.

# However, 4 TB is bigger than the main memory. Here are a few possible solutions:

# 1)
# Store these values in a key-value database that can scale in a cluster, such as Cassandra. Each time
# we add a url, we check to see if it existed before in the database.

# 2)
# Create 4000 files each of 1 GB and map the urls to each file using a hashing function, such as
# hash(url) % 4000 = x. Where the name of the file would be x.txt, for instance. Then, in a second
# we could load each of these files, one at a time, and use the hash table solution.


