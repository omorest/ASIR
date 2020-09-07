#!/usr/bin/ruby

subjects = ['add', 'ade', 'imw', 'srd']

subjects.each do |subject|
  system("mkdir #{subject}")
end
system("ls")
