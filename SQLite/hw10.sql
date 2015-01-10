create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------


-- The names of all "toy" and "mini" dogs
select name
  from dogs as d, sizes as toySize
  where d.height > toySize.min and d.height <= toySize.max and (toySize.size = "toy" or toySize.size = "mini")
  order by name;

-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- All dogs with parents ordered by decreasing height of their parent
select p.child
  from parents as p, dogs as pdog
  where p.parent = pdog.name
  order by -pdog.height;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size
select sib1.child || " and " || sib2.child || " are " || size1.size || " siblings"
  from parents as sib1, parents as sib2, dogs as s1, dogs as s2, sizes as size1
  where sib1.parent = sib2.parent and
  s1.name = sib1.child and s2.name = sib2.child and
  size1.min < s1.height and size1.max >= s1.height and
  size1.min < s2.height and size1.max >= s2.height and
  sib1.child < sib2.child and
  sib1.child != sib2.child;
-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
with
  sums(names, total, n, max) as (
    select name, height, 1, height from dogs union
    select names || ", " || name, total + height, n + 1, height
      from sums, dogs
      where n < 4 and max < height )
select names, total
  from sums
  where sums.total >= 170 and sums.n = 4
  order by total
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference
select "REPLACE THIS LINE WITH YOUR SOLUTION";
-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


