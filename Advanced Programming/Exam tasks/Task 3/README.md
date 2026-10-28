FilterMapAndSort --- Java Generics Exercise
Part 1: Complete the Starter Code (TODOs)
Task 1: Filtering, Transforming, and Sorting Products
Interfaces used: Predicate<E>, Function<E, E>, Comparable<E>

Implement the FilterMapAndSort class with a static generic method
named process.

The method accepts three arguments:
- A list of comparable objects (List<E>)
- A predicate (Predicate<E>) used to filter the objects
- A function (Function<E, E>) that accepts and returns an object of
  the same type
The method must keep only the elements that satisfy the predicate,
transform them using the supplied function, and return a new list
sorted in descending order.

Complete the sections marked with // TODO in the
FilterMapAndSortTest program's main method.

Test cases
Test Case 1 --- Product promotion
Input
1
4
1
P01 100 20 20 20
P02 200 10 10 10
P03 400 30 25 10
P04 50 40 30 20
Expected output
[Product PROMO_P04 (Price: 42.50) - Sold: 90, Avg: 30.00 | Popularity: 1694.12, Product PROMO_P01 (Price: 85.00) - Sold: 60, Avg: 20.00 | Popularity: 564.71, Product PROMO_P03 (Price: 340.00) - Sold: 65, Avg: 21.67 | Popularity: 152.94]

Test Case 2 --- Increase monthly sales
Input
1
4
2
P01 100 10 20 30
P02 600 5 5 5
P03 499 0 10 20
P04 250 15 15 15
Expected output
[Product P01 (Price: 100.00) - Sold: 90, Avg: 30.00 | Popularity: 720.00, Product P04 (Price: 250.00) - Sold: 75, Avg: 25.00 | Popularity: 240.00, Product P03 (Price: 499.00) - Sold: 60, Avg: 20.00 | Popularity: 96.19]

Test Case 3 --- Filter and transform words
Input
2
7
java
programming
FINKI
AI
stream
code
university
Expected output
[UNIVERSITY_MK, STREAM_MK, PROGRAMMING_MK, FINKI_MK]

Test Case 4 --- No words pass the filter
Input
2
4
java
AI
C
cat
Expected output
[]
