public class Java {
    public static void main(String[] args) {

        int nb_simulation = (int) Math.pow(10, 6);
        int nb_correct = 0;

        for (int i = 1;i < nb_simulation;i++) {
            double x = Math.random()*10;
            double y = Math.random()*10;
            double z = Math.random()*10;
            if ((x + y) + z == x + (y + z)) {
                nb_correct++;
            }
        }

        System.out.printf("%.2f%% accuracy for java\n", (double) nb_correct / nb_simulation * 100);

    }
}