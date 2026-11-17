use dblibrary

select memberid,firstname,lastname,gender,nationalid,phonenumber,
datediff(year,birthdate,getdate())
,[address],registerdate
from members

create or alter procedure sp_addbook
    @name nvarchar(200),
    @author nvarchar(150),
    @language nvarchar(50),
    @category nvarchar(100),
    @quantity int,
    @publishyear smallint,
    @description nvarchar(500)
as
begin
    insert into books

    values
        (@name, @author, @language, @category,
         @quantity, @publishyear, @description);
end;



create or alter procedure sp_addmember
    @firstname nvarchar(100),
    @lastname nvarchar(100),
    @gender nvarchar(20),
    @nationalid varchar(10),
    @phonenumber varchar(11),
    @birthdate date,
    @address nvarchar(500)
as
begin
    insert into members
    (firstname, lastname, gender, nationalid,
     phonenumber, birthdate, [address])

    values
        (@firstname, @lastname, @gender, @nationalid,
         @phonenumber, @birthdate, @address);
end;
