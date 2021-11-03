#!/usr/bin/env ruby
# Match repeat token "t" preciding "n" using +
# It will to match any character before "t" at least one

puts ARGV[0].scan(/hbt+n/).join
