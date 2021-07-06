#!/usr/bin/env ruby
# Match && repeat token "t" preciding "n" using {}

puts ARGV[0].scan(/hbt{2.5}n/).join
