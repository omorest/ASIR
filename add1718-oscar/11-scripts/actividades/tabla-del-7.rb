#!/usr/bin/ruby

number = 7
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

puts("Tabla de multiplicar del #{number}\n ")

list_numbers.each do |i|
  mult = number * i
  puts "#{number} x #{i} = #{mult}"
end
