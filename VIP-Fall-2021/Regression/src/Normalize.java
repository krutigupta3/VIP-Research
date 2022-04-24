import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Normalize {

    /**
     * main method.
     *
     * @param args string array
     * @throws FileNotFoundException for reading file
     */
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new File("input_parameters.csv"));
        sc.useDelimiter(",");   //sets the delimiter pattern
        double[] density = new double[1000];
        double[] E = new double[1000];
        double[] v = new double[1000];
        double[] phi = new double[1000];
        double[] psi = new double[1000];
        double[] c = new double[1000];
        double[] areaReduced = new double[1000];
        double[] plasticZone = new double[1000];
        double[] maxPeeq = new double[1000];
        double[] minPeeq = new double[1000];
        //double[] simNum = new double[1000];

        int count = -1;
        while (sc.hasNext()) {
            String temp = sc.nextLine();
            Scanner data = new Scanner(temp);
            data.useDelimiter(",");
            if (count >= 0) {
                density[count] = Double.parseDouble(data.next());
                E[count] = Double.parseDouble(data.next());
                v[count] = Double.parseDouble(data.next());
                phi[count] = Double.parseDouble(data.next());
                psi[count] = Double.parseDouble(data.next());
                c[count] = Double.parseDouble(data.next());
                areaReduced[count] = Double.parseDouble(data.next());

                plasticZone[count] = Double.parseDouble(data.next());
                maxPeeq[count] = Double.parseDouble(data.next());
                minPeeq[count] = Double.parseDouble(data.next());
                data.next();

                //System.out.println(minPeeq[count]);
            } else {
                data.next();
            }

            count++;
            //System.out.println(count);


        }

        sc.close();

        FileWriter csvWriter = new FileWriter("output.csv");

        for (int i = 0; i < 1001; i++) {
            csvWriter.append(Integer.toString(i) + ", ");

        }
        csvWriter.append("\n");


        normalize("density(tonne/mm3)", density, csvWriter);
        System.out.println();
        normalize("E(MPa)", E, csvWriter);
        System.out.println();
        normalize("v(-)", v, csvWriter);
        System.out.println();
        normalize("phi(deg)", phi, csvWriter);
        System.out.println();
        normalize("psi(deg)", psi, csvWriter);
        System.out.println();
        normalize("c(MPa)", c, csvWriter);
        System.out.println();
        normalize("area_reduced(%)", areaReduced, csvWriter);
        System.out.println();
        normalize("plastic_zone(%)", plasticZone, csvWriter);
        System.out.println();
        normalize("max_PEEQ(-)", maxPeeq, csvWriter);
        System.out.println();
        normalize("min_PEEQ(-)", minPeeq, csvWriter);

        csvWriter.flush();
        csvWriter.close();

    }

    // Method to find minimum value from the data set
    static double minValue(double[] arr) {
        double min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }

    // Method to find maximum value from the data set
    static double maxValue(double arr[]) {
        double max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    // Method to find the normalized values of the data set
    static void normalize(String label, double arr[], FileWriter csv) throws IOException {
        List<Double> res = new ArrayList<>();
        //System.out.println("The Data Set after Normalization: ");
        for (int i = 0; i < arr.length; i++) {
            double v = ((arr[i] - minValue(arr)) / (maxValue(arr) - minValue(arr)));
            res.add(v);
        }

        csv.append(label + ", ");
        for (double normalizedData : res) {
            csv.append(String.valueOf(normalizedData) + ", ");
        }
        csv.append("\n");

    }
}
