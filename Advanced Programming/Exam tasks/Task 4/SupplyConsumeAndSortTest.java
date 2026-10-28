import java.util.*;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

class BankAccount implements Comparable<BankAccount> {
    String accountNumber;
    double balance;
    List<Double> transactions;

    public BankAccount(String accountNumber, double balance, List<Double> transactions) {
        this.accountNumber = accountNumber;
        this.balance = balance;
        this.transactions = transactions;
    }

    public double maxTransaction() {
        return transactions.stream().mapToDouble(d -> Math.abs(d)).max().orElse(0.0);
    }

    public double creditScore() {
        return balance * 0.6 + maxTransaction() * 0.4 * transactions.size();
    }

    @Override
    public int compareTo(BankAccount o) {
        return Comparator.comparingDouble(BankAccount::creditScore)
                .thenComparing(a -> a.accountNumber)
                .compare(this, o);
    }

    @Override
    public String toString() {
        return String.format("Account %s | Balance: %.2f | TxCount: %d | Score: %.2f",
                accountNumber, balance, transactions.size(), creditScore());
    }
}

class SupplyConsumeAndSort {
    // TODO 1: Имплементирајте го статичкиот генерички метод fillAndExecute:
    // public static <E extends Comparable<E>> List<E> fillAndExecute(
    //         List<E> list, int targetSize, Supplier<E> defaultSupplier,
    //         Predicate<E> condition, Consumer<E> action)
    public static <E extends Comparable <E>> List<E> fillAndExecute(List<E> list,int targetSize,Supplier<E> defaultSupplier,Predicate<E> condition,Consumer<E> action){
        List<E> result = new ArrayList<>();
        while(list.size()<targetSize){
            list.add(defaultSupplier.get());
        }
        for (E element : list){
            if(condition.test(element)){
                action.accept(element);
            }
        }
        Collections.sort(list);
        return list;

    }
}

public class SupplyConsumeAndSortTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = Integer.parseInt(sc.nextLine());
        int n = Integer.parseInt(sc.nextLine());
        int targetSize = Integer.parseInt(sc.nextLine());

        if (testCase == 1) {
            List<BankAccount> accounts = new ArrayList<>();
            while (n > 0) {
                String[] parts = sc.nextLine().split("\\s+");
                String accNum = parts[0];
                double balance = Double.parseDouble(parts[1]);
                List<Double> tx = Arrays.stream(parts).skip(2)
                        .map(Double::parseDouble)
                        .collect(Collectors.toList());
                accounts.add(new BankAccount(accNum, balance, tx));
                --n;
            }
            // TODO 2: Повикајте SupplyConsumeAndSort.fillAndExecute така што:
            // - ако фалат сметки до targetSize, се генерираат резервни сметки со број "DEFAULT_000", салдо 1000.0 и една трансакција [100.0]
            // - за сите сметки со салдо поголемо од 5000.0, преку Consumer се додава камата од 5% на салдото и се додава трансакција од 250.0
            accounts = SupplyConsumeAndSort.fillAndExecute(accounts, targetSize, () -> new BankAccount("DEFAULT_000", 1000.0, new ArrayList<>(List.of(100.0))), acc ->acc.balance > 5000.0, acc ->{
                acc.balance = acc.balance * 1.05;
                acc.transactions.add(250.0);
            });
            System.out.println(accounts);
        } else {
            List<Double> measurements = new ArrayList<>();
            while (n > 0) {
                measurements.add(Double.parseDouble(sc.nextLine()));
                --n;
            }
            List<Double> highValuesLog = new ArrayList<>();
            // TODO 3: Повикајте fillAndExecute со Supplier кој враќа 50.0,
            // Predicate за вредности >= 100.0, и Consumer кој ги додава тие вредности во highValuesLog
            measurements = SupplyConsumeAndSort.fillAndExecute(
                    measurements,
                    targetSize,
                    () -> 50.0,
                    val -> val >= 100.0,
                    val -> highValuesLog.add(val)
            );

            System.out.println(measurements);
            System.out.println("Logged high values: " + highValuesLog);
        }
    }
}
