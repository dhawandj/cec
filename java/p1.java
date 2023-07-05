// Source code is decompiled from a .class file using FernFlower decompiler.
import java.util.Random;

public class p1 {
   

   public static void main(String[] var0) {
      byte var1 = 10;
      int[] var2 = generateRandomArray(var1);
      System.out.println("Original array:");
      printArray(var2);
      long var3 = System.nanoTime();
      selectionSort(var2);
      long var5 = System.nanoTime();
      System.out.println("Sorted array:");
      printArray(var2);
      System.out.println("\nThe time taken to sort is " + (var5 - var3) + "ns");
   }

   public static void selectionSort(int[] var0) {
      int var1 = var0.length;

      for(int var2 = 0; var2 < var1 - 1; ++var2) {
         int var3 = var2;

         int var4;
         for(var4 = var2 + 1; var4 < var1; ++var4) {
            if (var0[var4] < var0[var3]) {
               var3 = var4;
            }
         }

         var4 = var0[var3];
         var0[var3] = var0[var2];
         var0[var2] = var4;
      }

   }

   public static int[] generateRandomArray(int var0) {
      int[] var1 = new int[var0];
      Random var2 = new Random();

      for(int var3 = 0; var3 < var0; ++var3) {
         var1[var3] = var2.nextInt(100);
      }

      return var1;
   }

   public static void printArray(int[] var0) {
      for(int var1 = 0; var1 < var0.length; ++var1) {
         System.out.print(var0[var1] + " ");
      }

      System.out.println();
   }
}

// Sample Output:
// Original array:
// 67 18 91 82 94 46 11 4 17 2 Sorted array:
// 2 4 11 17 18 46 67 82 91 94
// The time taken to sort is 3071ns