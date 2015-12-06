# Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

# Assuming 1 GB of Main memory

# (1)
# Read 1 GB of the data in main memory and sort by some conventional method, like quicksort.

# (2)
# Write the sorted data to disk.

# (3)
# Repeat steps 1 and 2 until all of the data is in sorted 1 GB chunks (there are 20 chunks),
# which now need to be merged into one single output file.

# (4)
# Read the first 40 MB (= 1000MB / (20 chunks + 5)) of each sorted chunk into input buffers
# in main memory and allocate the remaining 200 MB for an output buffer.

# (5)
# Perform a 20-way merge and store the result in the output buffer. Whenever the output buffer fills,
# write it to the final sorted file and empty it. Whenever any of the 20 input buffers empties, fill
# it with the next 40 MB of its associated 1 GB sorted chunk until no more data from the chunk is
# available. This is the key step that makes external merge sort work externally -- because the merge
# algorithm only makes one pass sequentially through each of the chunks, each chunk does not have to
# be loaded completely; rather, sequential parts of the chunk can be loaded as needed.

