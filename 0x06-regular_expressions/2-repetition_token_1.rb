#!/usr/bin/env ruby
# Matches 0 or 1 time preciding token using ?
# It will make the preciding character of "?" optional

puts ARGV[0].scan(/hb?tn/).join
