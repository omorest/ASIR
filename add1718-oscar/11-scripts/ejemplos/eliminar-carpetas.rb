#!/usr/bin/ruby

subjects = ['add', 'ade', 'imw', 'srd']

subjects.each do |subject|
  system("rmdir #{subject}")
end
system("ls")
