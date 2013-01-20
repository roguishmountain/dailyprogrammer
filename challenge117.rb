#challenge117.rb
i = 0
r = 0
File.open(ARGV[0], 'r') do |f|  
  while c = f.getc  
  	if i%16 == 0
  	  print "\n#{r.to_s(16).rjust(8, '0')}	"
  	  r += 1
  	end
   	  print "#{c.to_s(16).rjust(2, '0')} "
      i += 1
  end  
  puts 
end 
