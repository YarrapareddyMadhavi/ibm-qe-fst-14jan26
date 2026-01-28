create table salesman(
    salesman_id int null,
    salesman_name varchar2(20),
    salesman_city VARCHAR2(20),
    commission int
);
describe salesman;
insert into salesman values (1,'james hoog','new york',15);
insert into salesman values(2,'nail','paris',13);
insert into salesman values(3,'pit','london',11);
insert into salesman values(4,'mslyon','rome',13);
insert into salesman values(5,'paul','san',12);
select * from salesman;
select salesman_id ,salesman_city from salesman;
select *from salesman where salesman_city='paris';
SELECT salesman_id, commission FROM salesman WHERE salesman_name='paul';
alter table salesman add dob date;
select * from salesman;
delete from salesman where salesman_id=4;
select * from scott.emp;
select * from scott.emp where sal>2000 and sal <4000;
select deptno,empno from scott.emp order by 1,2 desc;
select * from scott.emp where sal between 2500 and 3000;
select * from scott.emp where sal <2450;
select * from scott.emp where sal >=2450;
select * from scott.emp where sal <=1000;
savepoint sp1;
delete from salesman where salesman_id=5;
savepoint sp2;
delete from salesman where salesman_id=2;
savepoint sp3;
rollback to sp2;
select * from salesman;
select count(*) as "num of salesman" from salesman;
select count (*) from scott.emp;
select sum(sal) from scott.emp;
select min(sal) from scott.emp;
select max(sal) from scott.emp;
select avg(sal) from scott.emp;
select round(avg(sal)) from scott.emp;
select deptno,sum(sal) from scott.emp group by deptno;
select deptno,sum(sal) from scott.emp group by deptno having sum(sal) > 9000 order by deptno;
select * from salesman;
SELECT deptno, SUM(sal) AS total_salary FROM scott.emp GROUP BY deptno;
SELECT deptno, SUM(sal) AS total_salary FROM scott.emp GROUP BY deptno HAVING AVG(sal) > (SELECT AVG(sal) FROM scott.emp);