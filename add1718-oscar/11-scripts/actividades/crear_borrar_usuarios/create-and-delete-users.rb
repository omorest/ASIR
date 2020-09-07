#!/usr/bin/ruby
# Funciones
def create_user(camp)
  user_exist = system("id #{camp[0]} 2> /dev/null 1>/dev/null")

  case user_exist
  when true
    if camp[4] == "delete"
      if camp[2] == ""
        puts("El campo de correo del usuario #{camp[0]} necesita ser rellenado")
      else
        puts("Borrando usuario #{camp[0]}")
        system("userdel -rf #{camp[0]} 2> /dev/null 1>/dev/null")

      end
    elsif camp[4] == "add"
      puts("El usuario #{camp[0]} que intenta crear ya existe")
    end

  when false
    if camp[4] == "add"
      if camp[2] == ""
        puts("El campo de correo del usuario #{camp[0]} necesita ser rellenado")
      else
        puts("Creando usuario #{camp[0]}")
        system("useradd -m #{camp[0]} 2> /dev/null 1>/dev/null")
      end
    elsif camp[4] == "delete"
      puts("El usuario #{camp[0]} que intenta borrar no existe")
    end
  end
end


user       = `whoami`.rstrip
filename   = ARGV[0]
file_exist = File.exist?("#{filename}")

if user != "root" or ARGV.size != 1 or file_exist == false
  puts ("No es el usuario ROOT o no ha puesto el argumento de forma correcta o no existe el fichero #{filename}!!!")
  puts ("\nNecesario ser usuario ROOT y poner solo un argumento con el nombre del fichero y que exista.")
  exit 1
end

file       = `cat #{filename}`
lines    = file.split("\n")
lines.each do |camps|
  camp = camps.split(":")
  create_user(camp)
end
