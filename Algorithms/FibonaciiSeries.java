import java.util.Scanner;

public class FibonaciiSeries 
{

	public static void main(String[] args)
	{
	   Scanner s=new Scanner(System.in);
	   System.out.println("Enter Number");
	   int x=s.nextInt();
	   int fib[]=new int [x];
	   fib[0]=0;
	   fib[1]=1;
	   for(int i=2;i<x;i++)
	   {
	   fib[i]=fib[i-1]+fib[i-2];
	   }
	  for(int se:fib)
	  {
		  System.out.print(se+" ");
	  }
	}

}
