def chunker(input_file_name,chunksize=1048576):
	with open(input_file_name, 'r+b') as source:
		while True:
			buff = source.read(chunksize)
			if not buff:
				break
			yield buff

def unchunker(chunks, output_file_name):
	with open(output_file_name, 'w+b') as target:
		for chunk in chunks:
			target.write(chunk)

import os
			
def file_split(input_file_name, count):
	input_file_name_size = os.lstat(input_file_name).st_size
	prefix, ftype = input_file_name.split('.')
	chunksize = input_file_name_size / count
	chunksize_remainder = input_file_name_size % count
	read_list = [chunksize]*count
	read_list[0] += chunksize_remainder
	with open(input_file_name, 'r+b') as source:
		read_index = 0
		for read_size in read_list:
			data = source.read(read_size)
			with open(prefix + '.part.' + str(read_index), 'w+b') as target:
				target.write(data)
			read_index += 1
# identical read sizes in the read list cause an issue with target nameing using the read_list.index.
