def inputtt():

   intake=[int(input(f"Enter number {i+1}: ")) for i in range(5)]
   return intake
def small_big(arr):
   smallest_v=biggest_v=arr[0]
   for j in range(5):
      if(arr[j]<smallest_v):
         smallest_v=arr[j]
      if(arr[j]>biggest_v):
         biggest_v=arr[j]
   return smallest_v,biggest_v
def main():
   ans=inputtt()
   min,max=small_big(ans)
   print(min)
   print(max)
main()

