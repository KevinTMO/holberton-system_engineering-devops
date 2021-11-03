#!/usr/bin/env ruby
# Match any type of character between h and n using dot .
# Dot "." will match any character but only one.

puts ARGV[0].scan(/h.n/).join
