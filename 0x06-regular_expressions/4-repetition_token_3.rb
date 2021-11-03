#!/usr/bin/env ruby
# Match && repeat token "t" preciding "n" using *
# It will match any other character preciding "t" at least one

puts ARGV[0].scan(/hbt*n/).join
