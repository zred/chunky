import os,re,glob

def chunker(ifn,cs=1048576):
	with open(ifn, 'r+b') as src:
		while True:
			buff = src.read(cs)
			if not buff:
				break
			yield buff

def unchunker(chunks, ofn):
	with open(ofn, 'w+b') as tgt:
		for chunk in chunks:
			tgt.write(chunk)

			
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
			with open(prefix + '-' + ftype + '-part' + str(read_index), 'w+b') as target:
				target.write(data)
			read_index += 1
			
def tryint(s):
	try: return int(s)
	except: return s

def alnumkey(s):
	return [ tryint(c) for c in re.split('([0-9]+)', s) ]
	
def hsort(l):
	l.sort(key=alnumkey)

def file_paste(prefix):
	parts = glob.glob(prefix + '*' + '-part' + '*')
	suffix = glob.glob(prefix + '*' + '-part' + '*')[0].split('-')[1]
	hsort(parts)
	for part in parts:
		with open(part, 'r+b') as source:
			data = source.read()
			with open(prefix + '.' + suffix, 'a+b') as target:
				target.write(data)