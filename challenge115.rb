#challenge115.rb

answer = rand 100

loop do
  puts "guess a number"
  guess = gets.chomp
  guess = guess.to_i

  if answer > guess
    puts "too low"
  elsif answer < guess
    puts "too high"
  elsif answer == guess
    puts "got it"
    break
  else
    puts "huh?"
  end
end
