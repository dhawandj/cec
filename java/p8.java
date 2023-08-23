//PROGRAMME – Floyd.java
import java.util.Scanner;
public class p8 {
void flyd(int[][] w,int n)
{
int i,j,k;
for(k=1;k<=n;k++)
for(i=1;i<=n;i++)
for(j=1;j<=n;j++)
w[i][j]=Math.min(w[i][j], w[i][k]+w[k][j]);
}
public static void main(String[] args)
{
int a[][]=new int[10][10];
int n,i,j;
System.out.println("enter the number of vertices");
Scanner sc=new Scanner(System.in);
n=sc.nextInt();
System.out.println("Enter the weighted matrix");
for(i=1;i<=n;i++)
for(j=1;j<=n;j++)
a[i][j]=sc.nextInt();
p8 f=new p8();
f.flyd(a, n);
System.out.println("The shortest path matrix is");
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
{
System.out.print(a[i][j]+" ");
}
System.out.println();
}
sc.close();
}
}
// SAMPLE OUTPUT -
// enter the number of vertices
// 3
// Enter the weighted matrix
// 0 3 99
// 3 0 1
// 99 1 0
// The shortest path matrix is
// 0 3 4
// 3 0 1
// 4 1 0

