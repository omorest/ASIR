# Práctica para examen Triggers

Preparar un disparador para que calcule el valor de venta antes de la inserción.

~~~mysql

create trigger calc_valor2 before insert on productos
for each row
set new.valorventa = new.costo + (new.costo * new.porgan/100);

insert into productos (codigo, nombre, porgan, costo, valorventa, cantidad) values ('1', 'arroz 1 kg', 15, 1.0, 0, 45);

select valorventa from productos;

~~~


~~~mysql

delimiter //

create trigger calc_valor3 before insert on productos
for each row
begin
if new.valorventa = 0 or new.porgan is null
then set new.porgan = 20;
end if;
set new.valorventa = new.costo + (new.costo * new.porgan/100);
END //

insert into productos (codigo, nombre, porgan, costo, valorventa, cantidad) values ('2', 'arroz 1 kg', 0, 1.0, 0, 45);

select * from productos;

insert into productos (codigo, nombre, porgan, costo, valorventa, cantidad) values ('3', 'arroz 1 kg', null , 1.0, 0, 45);

select * from productos;

~~~

Preparar un disparador para que antes de actualizar un producto vuelva a calcular el valor de venta

~~~mysql

create trigger update_valor before update on productos
for each row
set new.valorventa = new.costo + (new.costo * new.porgan/100);

update productos set costo=0.9 where codigo='1';

select * from productos;

~~~