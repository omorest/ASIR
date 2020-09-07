#!/usr/bin/ruby

# Funciones

def operations(n1,op,n2)

  oper = ("#{n1} #{op} #{n2} =")

  if op == "+"
	  result = n1 + n2
	  puts ("#{oper} #{result}")		
  elsif op == "-"
	  result = n1 - n2		
	  puts ("#{oper} #{result}")
  elsif op == "/"
	  result = n1 / n2
	  puts ("#{oper} #{result}")		
  elsif op == "x"
	  result = n1 * n2	
	  puts ("#{oper} #{result}")	
  else
	  puts ("#{oper} --> Símbolo (#{op}) incorrecto, solo se aceptan (+, -, /, x) ")
  end

end

# Programa 

if ARGV.size !=1
  puts ("Falta un argumento\nIntroducir nombre del fichero")
  exit 1
end


argument = ARGV[0]
file     = `cat #{argument}`
line     = file.split("\n")

line.each do |j|
  camp_line = j.split(" ")
  num1 = camp_line[0].to_i
  op   = camp_line[1]
  num2 = camp_line[2].to_i
  
  operations(num1,op,num2)
end
