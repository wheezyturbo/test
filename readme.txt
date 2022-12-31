1. install xamp with mysql or mysql server

        https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.2.0/xampp-windows-x64-8.2.0-0-VS16-installer.exe

2. start the server

3. do the following mysql operations

    create database project;

    use project;

    create table user(username varchar(20) primary key,password text not null,address text,age int,ph_no varchar(15));

    create table trains(tr_id int primary key not null,tr_destination text);

4. then insert values

    insert into trains values(1,'mars',4);

5. create table bookings(transaction_id int primary key auto_increment not null,tr_id int not null,username text not null,order_time timestamp default current_timestamp);

6. move on to python 
    python should be installed in the system
    in the command prompt enter 
        pip install -r requirements.txt
        then python train.py
