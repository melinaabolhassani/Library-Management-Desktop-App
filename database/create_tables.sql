--drop database dblibrary
use dblibrary


--books table
create table books
(	bookid int primary key identity(1,1),
	[name] nvarchar (200) not null,
	author nvarchar (150),
	[language] nvarchar (50),
	category nvarchar (100) ,
	quantity smallint ,
	publishyear smallint ,
	[description] nvarchar(500),
	constraint chk_books_publishyear check (publishyear between 1000 and 2100),
	constraint chk_book_language check ([language] in ('persian','english','arabic','french','german'))
	)

--members table
create table members
(	memberid int primary key identity(101,1),
	firstname nvarchar (100) not null,
	lastname nvarchar (100) not null,
	Gender nvarchar(20),
	nationalid varchar (10) not null unique,
	phonenumber varchar(11) ,
	birthdate date not null, 
	[address] nvarchar(500),
	registerdate date not null default getdate(),
	constraint chk_members_birthdate check (birthdate <= dateadd(year,-7,getdate())),
	constraint chk_memeber_gender check (gender in ('male','female'))

)

--borrowing table
create table borrowings
(	borrowingid int primary key identity(1001,1),
	bookid int not null,
	memberid int not null,
	borrowingdate date not null default getdate(),
	returndate date ,
	constraint fk_borrowings_books foreign key (bookid) references books(bookid),
	constraint fk_borrowings_members foreign key (memberid) references members(memberid),
	constraint chk_borrowings_returndate check (returndate is null or returndate >= borrowingdate)
)

DROP TABLE IF EXISTS borrowings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;
