#!/usr/bin/env ruby
# Fix the beggining with ^ and the end with $ so every match is in between
# [0-9] will match digits inside between 0 to 9 and set to 10 digits with {10}

puts ARGV[0].scan(/^[0-9]{10}$/).join
