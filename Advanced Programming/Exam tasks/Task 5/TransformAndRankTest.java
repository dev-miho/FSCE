
import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

class Developer {
    String username;
    int yearsExperience;
    List<Integer> commitsPerProject;

    public Developer(String username, int yearsExperience, List<Integer> commitsPerProject) {
        this.username = username;
        this.yearsExperience = yearsExperience;
        this.commitsPerProject = commitsPerProject;
    }

    public int totalCommits() {
        return commitsPerProject.stream().mapToInt(i -> i).sum();
    }
}

class DeveloperSummary implements Comparable<DeveloperSummary> {
    String badgeId;
    double productivityScore;

    public DeveloperSummary(String badgeId, double productivityScore) {
        this.badgeId = badgeId;
        this.productivityScore = productivityScore;
    }

    @Override
    public int compareTo(DeveloperSummary o) {
        return Comparator.comparingDouble((DeveloperSummary s) -> s.productivityScore)
                .thenComparing(s -> s.badgeId)
                .compare(this, o);
    }

    @Override
    public String toString() {
        return String.format("[%s] Score: %.2f", badgeId, productivityScore);
    }
}

class TransformAndRank {
    // TODO 1: Имплементирајте го генеричкиот метод со два типски параметри <T, R extends Comparable<R>>:
    // public static <T, R extends Comparable<R>> List<R> transform(
    //         List<T> source, Predicate<T> validator, Function<T, R> mapper, Supplier<R> fallback)
    public static <T,R extends Comparable <R>> List<R> transform(List<T> source,Predicate<T> validator,Function<T,R> mapper,Supplier<R> fallback){
        List<R> result = new ArrayList<>();
        for (T item:source){
            if(validator.test(item)){
                result.add(mapper.apply(item));
            }else{
                result.add(fallback.get());
            }
        }
        result.sort(Collections.reverseOrder());
        return result;
    }
}

public class TransformAndRankTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = Integer.parseInt(sc.nextLine());
        int n = Integer.parseInt(sc.nextLine());

        if (testCase == 1) {
            List<Developer> devs = new ArrayList<>();
            while (n > 0) {
                String[] parts = sc.nextLine().split("\\s+");
                String user = parts[0];
                int exp = Integer.parseInt(parts[1]);
                List<Integer> commits = Arrays.stream(parts).skip(2)
                        .map(Integer::parseInt)
                        .collect(Collectors.toList());
                devs.add(new Developer(user, exp, commits));
                --n;
            }
            // TODO 2: Трансформирајте ја листата List<Developer> во List<DeveloperSummary>:
            // - Валидни се програмери со yearsExperience >= 2 и totalCommits() >= 30
            // - За валидните се креира DeveloperSummary со badgeId = "SR_" + username и
            //   productivityScore = totalCommits() * 1.5 + yearsExperience * 10.0
            // - За невалидните преку Supplier се враќа DeveloperSummary("JR_INTERN", 10.0)
            List<DeveloperSummary> summaries = TransformAndRank.transform(devs, p -> p.yearsExperience >=2 && p.totalCommits()>=30, d -> new DeveloperSummary(
                "SR_" + d.username,d.totalCommits() * 1.5 + d.yearsExperience * 10.0 ), () -> new DeveloperSummary("JR_INTERN", 10.0));
            System.out.println(summaries);
        } else {
            List<String> rawNumbers = new ArrayList<>();
            while (n > 0) {
                rawNumbers.add(sc.nextLine());
                --n;
            }
            // TODO 3: Трансформирајте ја List<String> во List<Integer>:
            // - Валидни се стринговите кои содржат само цифри (s.matches("\\d+"))
            // - Валидните се парсираат во Integer помножен со 2
            // - Невалидните се заменуваат со -1 преку Supplier
            List<Integer> parsed = TransformAndRank.transform(rawNumbers,s -> s.matches("\\d+"),s -> Integer.parseInt(s)*2,()-> -1);
            System.out.println(parsed);
        }
    }
}
