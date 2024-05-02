import java.util.*;

class DiffieHellmanAlgo {
    public static void main(String[] args) {
        long P, G, a, b, ka, kb;

        Scanner sc = new Scanner(System.in);

        System.out.println("Both users should agree on the public keys G and P.");
        System.out.print("Enter value for public key G: ");
        G = sc.nextLong();
        System.out.print("Enter value for public key P: ");
        P = sc.nextLong();

        System.out.print("Enter value for private key a (selected by User1): ");
        a = sc.nextLong();
        System.out.print("Enter value for private key b (selected by User2): ");
        b = sc.nextLong();

        long x = modExp(G, a, P); // Public key for User1
        long y = modExp(G, b, P); // Public key for User2

        // Compute shared secret keys
        ka = modExp(y, a, P); // Secret key for User1
        kb = modExp(x, b, P); // Secret key for User2

        System.out.println("Secret key for User1 is: " + ka);
        System.out.println("Secret key for User2 is: " + kb);

        sc.close();
    }

    // Method for modular exponentiation
    private static long modExp(long base, long exp, long mod) {
        long result = 1;
        base = base % mod;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            exp = exp >> 1;
            base = (base * base) % mod;
        }
        return result;
    }
}
