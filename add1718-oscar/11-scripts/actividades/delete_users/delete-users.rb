#!/usr/bin/ruby

# Funciones

def delete_user(user,command_user)
	if command_user != ""
		puts ("El usuario (#{user}) si existe")
		puts ("Eliminamos el usuario (#{user})")
		system("sudo userdel -r #{user}")
	else
		puts ("El usuario (#{user}) no existe")
	end
end


if ARGV.size != 1
  puts ("\nFalta un argumento.\nDebe poner el nombre del fichero con el nombre de los usuarios\n ")
  exit 1
end

filename = ARGV[0]
file     = `cat #{filename}`
line     = file.split("\n")

line.each do |n|


  puts command
end


=======
names    = file.split("\n")
>>>>>>> c7555e2ccc6a87737068559f94d04d96a2d3af2f

names.each do |n|
	command = `id #{n}`
	delete_user(n,command)

end
