# Saving-Database-Space

A talk I listened to recently discussed the efficacy of saving a table of names for users and then pointing to those names 
from a user table to save space.

Boy was I surprised that you'd do such a thing! But it makes sense. I think... right? How can I calculate something like that? 
So how much space would it save to store the 200 most common male/female names in a single table and have user names point at that?

Turns out, for the 200 most common names in America according to the [SSA](https://www.ssa.gov/oact/babynames/decades/century.html), quite a lot.

I calculated the space it would take to store 158,649,724 peoples names with the weighting from the SSA and compared it to saving a reference to the some peoples names in another table.

83.31% space savings. The savings slowly cuts off as you start to get in to having millions of unique names. But by that time, you've already saved plenty of space.

## Bits required to save x number of names

### The first 255 names requires 1 byte [^1]
```
>>> 0b11111111
255
```

### The next 65280 names require 2 bytes
```
>>> 0b1111111111111111
65535
```

### The next 1611680 names require 3 bytes
```
>>> 0b111111111111111111111111
16777215
```

### The next 4293355615 names require 4 bytes
```
>>> 0b11111111111111111111111111111111
4294967295
```

[^1]: Our data here doesn't even leave this range.