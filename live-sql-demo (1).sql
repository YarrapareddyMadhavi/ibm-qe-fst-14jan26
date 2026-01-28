select * from salesman;
select * from scott.emp;
select * from scott.dept;
-- traditional join syntax
select emp.ename,dept.dname from scott.emp emp, scott.dept dept where emp.deptno=dept.deptno;
-- ANSI inner join syntax
select emp.ename,dept.dname from scott.emp emp inner join scott.dept dept on emp.deptno=dept.deptno;
-- ANSI right join syntax
select emp.ename,dept.dname from scott.emp emp right join scott.dept dept on emp.deptno=dept.deptno;
-- ANSI left join syntax
select emp.ename,dept.dname from scott.emp emp left join scott.dept dept on emp.deptno=dept.deptno;
-- ANSI outer join  syntax
select emp.ename,dept.dname from scott.emp emp full outer join scott.dept dept on emp.deptno=dept.deptno;


-- challenge activity 1


-- retrive data from scott.emp to print follwing data
-- emp name,dept name,manager name
select * from scott.emp;
SELECT
    e.ename   AS emp_name,
    d.dname   AS dept_name,
    m.ename   AS manager_name
FROM scott.emp e
INNER JOIN scott.dept d
    ON e.deptno = d.deptno
LEFT JOIN scott.emp m
    ON e.mgr = m.empno;

SELECT
    e.ename   AS emp_name,
    d.dname   AS dept_name,
    m.ename   AS manager_name
FROM scott.emp e
INNER JOIN scott.dept d
    ON e.deptno = d.deptno
inner JOIN scott.emp m
    ON e.mgr = m.empno;

SELECT
    e.ename   AS emp_name,
    d.dname   AS dept_name,
    m.ename   AS manager_name
FROM scott.emp e
INNER JOIN scott.dept d
    ON e.deptno = d.deptno
LEFT JOIN scott.emp m
    ON e.mgr = m.empno;

SELECT
    e.ename   AS emp_name,
    d.dname   AS dept_name,
    m.ename   AS manager_name
FROM scott.emp e
INNER JOIN scott.dept d
    ON e.deptno = d.deptno
right JOIN scott.emp m
    ON e.mgr = m.empno;

--challenge Activity  2

-- retrive and  display information about all managers
-- in scott.emp and their location 

SELECT m.ename, dept.loc FROM scott.emp emp JOIN scott.emp m ON emp.mgr = m.empno JOIN scott.dept dept ON emp.deptno = dept.deptno;

select * from scott.dept;
select deptno from scott.dept where loc='CHICAGO';
select count(*) from hr.employees where department_id=60;
select * from hr.departments;
select * from hr.locations;
 
--challenge activity 3
-- retrive employee name, department name and city
--for all employees working in the 'IT' department

select e.first_name || ' ' || e.last_name as employee_name,
       d.department_name,
       l.city
from hr.employees e
inner join hr.departments d
    on e.department_id = d.department_id
inner join hr.locations l
    on d.location_id = l.location_id
where d.department_name = 'IT';
  
---Activity 4
--- using scott schemas
---list out all the managers along with their empno, name and no,of reporters

select m.empno,
       m.ename as manager_name,
       count(e.empno) as number_of_reporters
from scott.emp m
left join scott.emp e
    on e.mgr = m.empno
group by m.empno, m.ename
having count(e.empno) > 0;