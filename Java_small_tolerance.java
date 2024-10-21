public class Java_small_tolerance{
    public static void main(String[] args) {

        int nb_simulation = (int) Math.pow(10, 6);
        int[] nb_correct = new int[11];  // Array to store results for each tolerance level (10 to 20)

        for (int sim = 1; sim < nb_simulation; sim++) {
            double x = Math.random();
            double y = Math.random();
            double z = Math.random();
            
            for (int t = 10; t <= 20; t++) {  // Iterate over tolerance levels from 10 to 20
                double tolerance = Math.pow(10, -t);  // 1e-10, 1e-11, ..., 1e-20
                
                // Check if the expression is within the tolerance range
                if (Math.abs((x + y) + z - (x + (y + z))) < tolerance) {
                    nb_correct[t - 10]++;  // Store results in array (offset by 10)
                }
            }
        }

        // Print the accuracy for each tolerance level
        for (int t = 10; t <= 20; t++) {
            double tolerance = Math.pow(10, -t);
            System.out.printf("Accuracy with tolerance 1e-%d: %.2f%%\n", t, (double) nb_correct[t - 10] / nb_simulation * 100);
        }

    }
}
