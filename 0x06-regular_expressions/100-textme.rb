#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+?[a-zA-Z0-9]*)\] \[to:(\+?\d{11})\] \[flags:(\-?\d:\-?\d:\-?\d:\-?\d:\-?\d)/).join(',')

