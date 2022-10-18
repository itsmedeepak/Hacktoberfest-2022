#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double a, b, c, discriminant, root1, root2, realPart, imaginaryPart;

    cout << "Enter coefficients a, b and c : ";
    cin >> a >> b >> c;

    discriminant = b * b - 4 * a * c;
 
    if (discriminant > 0)
    {
        
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        cout << "root1 = " << root1 << "  and root2 = "  << root2;
    }

    
    else if (discriminant == 0)
    {
        root1 = root2 = -b / (2 * a);

        cout << "root1 = root2 = " << root1;
    }
 
    else
    {
        realPart = -b / (2 * a);
        imaginaryPart = sqrt(-discriminant) / (2 * a);
        cout << "root1 = "<< realPart << "+"<< imaginaryPart <<" and root2 = "<< realPart << "+"<< imaginaryPart;
    }

    return 0;
}
