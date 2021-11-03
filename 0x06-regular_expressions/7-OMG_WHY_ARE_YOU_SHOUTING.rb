#!/usr/bin/env ruby
# Make a set of A-Z characters uppercase
# And match all of them from 0 to infinite preciding token *

puts ARGV[0].scan(/[A-Z]*/).join
