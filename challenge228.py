lwords = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged', 'bijoux', 'abhors', 'fiddle', 'begins', 'chimps', 'wronged'] 

for word in range(len(lwords)):
	bInOrder = True
	bRInOrder = True 
	for char in range(len(lwords[word])-1):
		if lwords[word][char] > lwords[word][char+1]:
			bInOrder = False
		elif lwords[word][char] < lwords[word][char+1]:
			bRInOrder = False
			
	if bInOrder:
		print lwords[word], 'IN ORDER'
	elif bRInOrder:
		print lwords[word], 'REVERSE IN ORDER'
	else:
		print lwords[word], 'NOT IN ORDER'