#!/usr/bin/ruby

num1 = ARGV[0].to_i
op = ARGV[1]
num2 = ARGV[2].to_i


if ARGV.size == 3
	if op == "+"
		result = num1 + num2
		puts (result)
	elsif op == "-"
		result = num1 - num2
		puts (result)
	elsif op == "/"
		result = num1 / num2
		puts (result)
	elsif op == "x"
		result = num1 * num2
		puts (result)
	else
		puts ("Símbolo op incorrecto")
	end

else
	puts ("La estructura debe ser:\n num1 = número entero\n op = +,-,/ o x\n num2= número entero")

end
