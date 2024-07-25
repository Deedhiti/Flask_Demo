create database employees;
show databases;
use employees;
create table admins(id int primary key auto_increment, employee_name varchar(255), employee_contact bigint,employee_age int);
show tables;
describe admins;
insert into admins(employee_name,employee_contact,employee_age) values('Jack',9876543210,28);
select * from admins;
insert into admins (employee_name,employee_contact,employee_age)
values
('Joe',9875612340,32),
('John',8765147820, 33);
select * from admins;