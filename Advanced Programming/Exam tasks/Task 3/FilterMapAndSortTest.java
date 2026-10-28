import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

class Product implements Comparable<Product> {

    String code;
    double basePrice;
    List<Integer> monthlySales;

    public Product(String code, double basePrice, List<Integer> monthlySales) {
        this.code = code;
        this.basePrice = basePrice;
        this.monthlySales = monthlySales;
    }

    public int totalSold() {
        return monthlySales.stream()
                .mapToInt(i -> i)
                .sum();
    }

    public double averageSales() {
        return monthlySales.stream()
                .mapToDouble(i -> i)
                .average()
                .orElse(0.0);
    }

    public double popularityIndex() {
        return (totalSold() * 0.7 + averageSales() * 0.3)
                * (1000.0 / Math.max(basePrice, 1.0));
    }

   // TODO 1: Implement a static method that increases each month's sales by a given bonus.
    public static List<Integer> boostSales(List<Integer> sales, int bonus) {
        List<Integer> result = new ArrayList<>();

        for (Integer item : sales) {
            result.add(item + bonus);
        }

        return result;
    }

    @Override
    public int compareTo(Product o) {
        return Comparator.comparingDouble(Product::popularityIndex)
                .thenComparingDouble(p -> p.basePrice)
                .compare(this, o);
    }

    @Override
    public String toString() {
        return String.format(
                "Product %s (Price: %.2f) - Sold: %d, Avg: %.2f | Popularity: %.2f",
                code,
                basePrice,
                totalSold(),
                averageSales(),
                popularityIndex()
        );
    }
}

class FilterMapAndSort {

    // TODO 2: Implement the static generic method process(List<E> elements,
       //         Predicate<E> filter, Function<E, E> mapper).
    public static <E extends Comparable<E>> List<E> process(
            List<E> elements,
            Predicate<E> filter,
            Function<E, E> mapper) {

        List<E> result = new ArrayList<>();

        for (E element : elements) {
            if (filter.test(element)) {
                result.add(mapper.apply(element));
            }
        }

        result.sort(Collections.reverseOrder());

        return result;
    }
}

public class FilterMapAndSortTest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int testCase = Integer.parseInt(sc.nextLine());
        int n = Integer.parseInt(sc.nextLine());

        if (testCase == 1) {

            // Products
            int scenario = Integer.parseInt(sc.nextLine());
            List<Product> products = new ArrayList<>();

            while (n > 0) {
                String[] parts = sc.nextLine().split("\\s+");

                String code = parts[0];
                double price = Double.parseDouble(parts[1]);

                List<Integer> sales = Arrays.stream(parts)
                        .skip(2)
                        .map(Integer::parseInt)
                        .collect(Collectors.toList());

                products.add(new Product(code, price, sales));

                --n;
            }

            if (scenario == 1) {

                // TODO 3: Use FilterMapAndSort.process for products with total sales > 50.
                                //         Add the prefix "PROMO_" to each product code and reduce its price by 15%.
                products = FilterMapAndSort.process(
                        products,
                        p -> p.totalSold() > 50,
                        p -> {
                            Product updated = new Product(
                                    "PROMO_" + p.code,
                                    p.basePrice * 0.85,
                                    new ArrayList<>(p.monthlySales)
                            );

                            return updated;
                        }
                );

            } else {


                // TODO 4: Use FilterMapAndSort.process for products with basePrice < 500.
                                //         Increase each month's sales by 10 using Product.boostSales.
                products = FilterMapAndSort.process(
                        products,
                        p -> p.basePrice < 500.0,
                        p -> new Product(
                                p.code,
                                p.basePrice,
                                Product.boostSales(p.monthlySales, 10)
                        )
                );
            }

            System.out.println(products);

        } else {

            // Strings
            List<String> words = new ArrayList<>();

            while (n > 0) {
                words.add(sc.nextLine());
                --n;
            }

            // TODO 5: Keep words longer than 4 characters, convert them to uppercase,
                        //         and append the suffix "_MK".

            words = FilterMapAndSort.process(
                    words,
                    p -> p.length() > 4,
                    p -> p.toUpperCase() + "_MK"
            );

            System.out.println(words);
        }

        sc.close();
    }
}
