lwords = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged', 'bijoux', 'abhors', 'fiddle', 'begins', 'chimps', 'wronged'] 

(0...(lwords.length)).each do |word|
	bInOrder = true
	bRInOrder = true 
	(0...(lwords[word].length)-1).each do |char|
		if (lwords[word][char] <=> lwords[word][char+1]) == 1
			bInOrder = false
		elsif (lwords[word][char] <=> lwords[word][char+1]) == -1
			bRInOrder = false
		end #if statements 
	end #inner for loop
			
	if bInOrder
		puts "#{lwords[word]} IN ORDER"
	elsif bRInOrder
		puts "#{lwords[word]} REVERSE IN ORDER"
	else
		puts "#{lwords[word]} NOT IN ORDER"
	end #if statements
end #outer for loop