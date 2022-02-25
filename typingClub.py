import random
alphabet="azertyuiopqsdfghjklm "
l=len(alphabet)
visible=""
for item in range(100):
	word=random.randrange(l)
	visible+=alphabet[word]

print(visible)
user=input("taper ce texte\n")
print(user)
"""
void miniMaxSum(int arr_count, int* arr) {
    long long int max, min, iMin, iMax, cmp, sommeMin=0, sommeMax=0;
    //en va chercher le maximum
    max=arr[0];iMax=0;
    for(cmp=1; cmp<arr_count;cmp++)
        if(arr[cmp]>max){
            max=arr[cmp];iMax=cmp;
        }
    //chercher le minimum
    min=arr[0];iMin=0;
    for(cmp=1;cmp<arr_count;cmp++)
        if(arr[cmp]<min){
            min=arr[cmp];iMin=cmp;
        }
    //calculer le valeur possible
    for(cmp=0;cmp<arr_count;cmp++){
        if(cmp != iMax)
            sommeMin+=arr[cmp];
        if(cmp != iMin)
            sommeMax+=arr[cmp];
    }
    printf("%lld %lld ",sommeMin, sommeMax);
}"""
_________________________
"""int birthdayCakeCandles(int candles_count, int* candles) {
    long int cmp, grand, max;
    max=candles[0];
    for(cmp=1;cmp<candles_count; cmp++){
        if(candles[cmp] > max){
            max=candles[cmp];
        }
    }
    //chercher le nombre de repetition de max
    grand=0;
    for(cmp=0; cmp<candles_count; cmp++){
        if(candles[cmp] == max){
            grand+=1; 
        }
    }
    return grand;
}"""