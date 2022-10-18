import java.util.Scanner;

public class Factorail 
{
	public int factorail(int number)
	{
		int res=1;
		for(int n=1;n<=number;n++)
		{
			res=res*n;
		}
		return res;
	}

	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number ");
		int num=sc.nextInt();
		Factorail f=new Factorail();
		int fact=f.factorail(num);
		System.out.println("Factorail is "+fact);
	}

}
