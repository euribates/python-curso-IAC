
public class IEEE754 {
    public static void main(String args[]) {
        double i = 0.1;
        if (0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1 == 1.0) {
            System.out.print("OK\n");
            }
        else {
            System.out.print("WTF?\n");
        }
        System.out.print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1 - 1.0);
    }
}
