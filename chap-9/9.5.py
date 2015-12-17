# Imagine a web server for a simplified search engine. This system has 100 machines to respond to 
# search queries, which may then call out using processSearch(string query) to another cluster of
# machines to actually get the result. The machine which responds to a given query is chosen at
# random, so you can not guarantee that the same machine will always respond to the same request.
# The method processSearch is very expensive. Design a caching mechanism to cache the results of
# the most recent queries. Be sure to explain how you would update the cache when data changes.


# Create a cache for the queries, where each cached query can be stored in a single machine, the
# query can be mapped to a machine using hash(query) % 100. When the server receives a query, it
# finds the corresponding machine and send a request for the query. The machine looks it up on its
# own cache, if it doesn't find it, it calls processSearch(string query), stores the result in
# its own cache and sends it back to the first machine, that will forward the response to the client.

# The cache can be a combination of a doubly linked list with a hash, so operations such as
# get, update (set), delete can always be O(1). Here's a sample code:

def processSearch(query):
    pass # return response object

class Node(object):

    def __init__(self, query, response=None):
        self.query = query
        self.response = response
        self.next = None
        self.prev = None

class DoublyLinkedList(object):

    head = None
    tail = None

    def add_first(self, node):
        pass

    def remove_last(self):
        pass # return tail

    def remove_node(self, node):
        pass

class Cache(object):

    hash_map = dict() # query -> node
    linked_list = DoublyLinkedList()

    def __init__(self, size):
        self.max_size = size

    def size(self):
        return len(hash_map)

    # also serve as set_query
    def update_query(self, query):
        if hash_map.get(query) is not None:
            node = hash_map[query]
            linked_list.remove_node(node)
        else:
            response = processSearch(query)
            node = Node(query, response)
        linked_list.add_first(node)
        if len(linked_list) > self.max_size:
            self.remove_last()

    def remove_last(self):
        stale_node = linked_list.remove_last()
        stale_query = stale_node.query
        del hash_map[stale_query]

    def get_query(self, query):
        if hash_map.get(query) is None:
            return None
        node = hash_map[query]
        return node.response


# When the data changes, the crawler has to crawl the new page, then compare to previous crawls and
# let the cache know somehow that the data have changed. It can happen in real time, or in
# pre-defined times, let's say after a fixed number of minutes. I think the process of making this
# happening in real time would be too hard to accomplish (a lot of resource is needed) and probably
# not worth it. It might be easier to just give an expire date to all queries, maybe the expire date
# can be a function of the change rate of the page over the time. The more the page changes, shorter
# must be the expire date.





