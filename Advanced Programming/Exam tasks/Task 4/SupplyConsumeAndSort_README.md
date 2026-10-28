# SupplyConsumeAndSort --- Java Generics Exercise

## Task Description

Implement the `SupplyConsumeAndSort` class with a static generic method
named `fillAndExecute`.

The method receives: - An input list, `List<E> list` - A target minimum
size, `int targetSize` - A supplier, `Supplier<E> defaultSupplier`, used
to generate and add new elements until the list reaches `targetSize` - A
predicate, `Predicate<E> condition` - A consumer, `Consumer<E> action`

All elements in the filled list that satisfy the predicate must be
processed by the consumer **before sorting**. After processing, return
the entire list sorted in **ascending order**.

The method signature is:

``` java
public static <E extends Comparable<E>> List<E> fillAndExecute(
        List<E> list,
        int targetSize,
        Supplier<E> defaultSupplier,
        Predicate<E> condition,
        Consumer<E> action)
```

## Test Cases

The test cases below assume the program's input format is:

-   First line: `testCase` (`1` for bank accounts, `2` for measurements)
-   Second line: number of input elements, `n`
-   Third line: target minimum list size, `targetSize`
-   For test case `1`, each remaining line contains an account number,
    balance, and zero or more transaction amounts.
-   For test case `2`, each remaining line contains one measurement.

### Test Case 1 --- Bank Accounts Without Filling

**Purpose:** Check that the list is sorted in ascending order by
`creditScore`, and that accounts with a balance greater than `5000.0`
receive 5% interest and an additional transaction of `250.0`.

**Input**

``` text
1
3
3
ACC03 6000 100 200
ACC01 4000 300
ACC02 7000 1000 2000
```

**Expected output**

``` text
[Account ACC01 | Balance: 4000.00 | TxCount: 1 | Score: 2520.00, Account ACC03 | Balance: 6300.00 | TxCount: 3 | Score: 4080.00, Account ACC02 | Balance: 7350.00 | TxCount: 3 | Score: 6810.00]
```

### Test Case 2 --- Bank Accounts With Default Accounts

**Purpose:** Check that default accounts are added until the list
reaches the target size of four, and that the consumer processes only
accounts with a balance greater than `5000.0`.

**Input**

``` text
1
2
4
ACC01 4500 500
ACC02 8000 50
```

**Expected output**

``` text
[Account DEFAULT_000 | Balance: 1000.00 | TxCount: 1 | Score: 640.00, Account DEFAULT_000 | Balance: 1000.00 | TxCount: 1 | Score: 640.00, Account ACC01 | Balance: 4500.00 | TxCount: 1 | Score: 2900.00, Account ACC02 | Balance: 8400.00 | TxCount: 2 | Score: 5240.00]
```

### Test Case 3 --- Measurements With High Values

**Purpose:** Check that `50.0` is added until the target size is
reached, values greater than or equal to `100.0` are logged, and the
measurements are sorted in ascending order.

**Input**

``` text
2
5
7
150
40
100
250
75
```

**Expected output**

``` text
[40.0, 50.0, 50.0, 75.0, 100.0, 150.0, 250.0]
Logged high values: [150.0, 100.0, 250.0]
```

The log preserves the order in which qualifying values are processed,
before the measurements list is sorted.

### Test Case 4 --- Measurements With No High Values

**Purpose:** Check filling to the target size and verify that values
below `100.0` are not added to the log.

**Input**

``` text
2
3
5
-5
0
99.9
```

**Expected output**

``` text
[-5.0, 0.0, 50.0, 50.0, 99.9]
Logged high values: []
```

## Implementation Checklist

-   Use `defaultSupplier.get()` to generate each missing element.
-   Continue adding elements while `list.size() < targetSize`.
-   Use `condition.test(element)` to check each element.
-   Call `action.accept(element)` for every element that satisfies the
    predicate.
-   Process qualifying elements before sorting.
-   Sort the complete list in ascending natural order.
-   Return the filled, processed, and sorted list.
