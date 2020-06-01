#include <stdio.h>

// int main()
// {
//     printf("Hello, world");
// }

#include <stdio.h>
 /* print Fahrenheit-Celsius table
 for fahr = 0, 20, ..., 300 */
 float main()
 {
    float fahr, celsius, lower, upper, step;

    lower = 0; /* lower limit of temperature scale */
    upper = 300; /* upper limit */
    step = 20; /* step size */

    fahr = lower;
    while (fahr <= upper) {
        celsius = 5.0 * (fahr-32) / 9.0;
        printf("%6.1f\t%13.2f\n", celsius,fahr );
        fahr = fahr + step;
    }
 }