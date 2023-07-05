
// IMPLEMENTATION/ PROGRAMME: 2. QuickSort.java
/* QUICK SORT- for random numbers */

 import java.util.Random; import java.util.Scanner;
  public class p2 {
public static void main(String[] args) {
int a[]= new int[100000];
Scanner in = new Scanner(System.in);
long start, end;
System.out.println("QUICK SORT PROGRAM"); System.out.println("Enter the number of elements to be sorted"); int n = in.nextInt();
Random rand= new Random();
for(int i=0;i<n;i++)
a[i]=rand.nextInt(100);
System.out.println("Array elements to be sorted are"); for(int i=0; i<n; i++)
System.out.print(a[i]+" "); a[n]=999;
start=System.nanoTime(); quick(a,0,n-1); end=System.nanoTime();
System.out.println("\nThe sorted elements are"); for(int i=0; i<n; i++)
System.out.print(a[i]+" ");
System.out.println("\nThe time taken to sort is "+(end-start)+"ns"); }
static void quick(int a[],int p, int q) {
int j; if(p < q) {
j=partition(a,p,q); quick(a,p,j-1); quick(a,j+1,q);
} }
static int partition(int a[],int m, int p) {
int v, i=0, j;
v=a[m]; // first element is pivot element i=m;
j=p;
        while(i <= j)
        {
        while(a[i] <= v) 
        i++;
        while(a[j] > v)
                j--;
                if(i < j)
        interchange(a,i,j); }
        a[m] = a[j]; a[j] = v; return j;
        }
        static void interchange(int a[], int i, int j) {
        int p;
        p = a[i]; a[i] = a[j]; a[j] = p;
        } }


// Sample Output 1:
// QUICK SORT PROGRAM
// Enter the number of elements to be sorted
// 15
// Array elements to be sorted are
// 64 34 37 92 11 65 50 49 49 24 59 16 90 80 16 
// The sorted elements are
// 11 16 16 24 34 37 49 49 50 59 64 65 80 90 92 
// The time taken to sort is 25722ns