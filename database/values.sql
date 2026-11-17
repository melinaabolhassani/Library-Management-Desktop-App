 --use dblibrary

select* from books
select* from members
select * from borrowings


insert into books
values('clean code','neda akbari','english','programming',5,1398,'How to write clean code so that it becomes a good resource later'),
('matrix','tina rad','german','math',3,1399,'Comprehensive Mathematics Tutorial: Matrices'),
('web design','neda akbari','english','css',4,1389,'Comprehensive Web Page Design Training for Beginners'),
('red plants','poone moghimi','english','siences',1,1344,'A comprehensive resource for laboratory use concerning plants and their living cells.'),
('dark lamp','ali maleki','persian','psychology',3,1401,'In this book, you will learn how to recognize the dark shadows within yourself.'),
('hug me','asra miri','french','novel',1,1405,'A novel about a lonely girl whose lover leaves her.')

insert into members
values ('ava','nazari','female','0159190988','09121186545','19800207','tehran',getdate()),
('roya', 'mahbin','female','0199599998','09139877895','19700919','tabriz', getdate()),
('ali', 'razi','male','0135693478','09121189090','20000212','shiraz', getdate()),
('asal','shahi','female','0016772898','09123300545','20011214','mashhad',getdate())


insert into borrowings
values(2,101,getdate(),null)

delete from members
dbcc checkident ('members',reseed,100)