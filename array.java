
import java.util.Arrays;


public class array {

    public static void main(String[] args) {
        int[] arr = new int[4];
        int[] coppid = Arrays.copyOf(arr, arr.length);

        String[] names = {"Tharun","Jeevith","Suresh"};
        for(String name:names){
            System.out.println(name);
        }
        String[] copidarray = Arrays.copyOf(names,names.length);
        for(String hesaru:copidarray){
            System.out.println(hesaru);
        }

    }
}
