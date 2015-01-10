-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

select "States adjacent to California:";
select s1, s2
	from adjacencies as a
	where s1 = "CA"
-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
    select s1, s2, 1 
    	from adjacencies union
	select d.start, a.s2, d.hops + 1
		from distance as d, adjacencies as a
		where d.end = a.s1 and d.hops < 15
    )
  select * from distances;

select "Lengths of paths between CA and WI:";
select * from distances where start = "CA" and end = "WI" order by hops;

select "States 3 hops from CA:";
select * from distances where start = "CA" and hops = 3;
select "Long alphabetical paths:";
with
  paths(s, n, last) as (
    select "Your", "Code", "Here"
  )
select s from paths where n > 6 order by -n;
