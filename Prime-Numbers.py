import math
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.style.use("fivethirtyeight");
plt.rcParams["figure.figsize"] = (10.0, 10.0)

def menu():
    print('Sarah and Sophia\'s Python Extravaganza Menu!!!!!')
    print('Select option by entering corresponding number (Ex \'5.3a\')')

    choice = input("""
                1.1: Implement Euclid's Algorithm
                1.3: Report Results of Scaling Euclid's Algorithm In a Table
                2.1: Generate Primes Using Seive
                3.1: Primality Test Using Trial Division
                3.2: Primality Test Using Seive of Erastosthenes
                3.3: Primality Test Using Fermat's Little Theorem
                4.1: Prime Factorization Using Trial Division
                4.3: Report Results Showing How Each Method Scales
                5.1: Prime Set Collection
                5.2: Calculate Proportions Ending With __ Digit
                5.3a: Calculate prop. of primes ending with 1, followed by __:
                5.3b: Calculate prop. of primes ending with 3, followed by __:
                5.3c: Calculate prop. of primes ending with 7, followed by __:
                5.3d: Calculate prop. of primes ending with 9, followed by __:
                5.4: Calculate number of Twin Primes in Set
                5.5: Plot relationship between x and the # of primes less than x
                6: Prime Visualization
                7: Quit

                Enter your choice: """)

    if choice == "1.1":
        print ("GCD is: ", gcd())
    elif choice == "1.3":
        print (make_table())
    elif choice == "2.1":
        first = input("Enter the limit for the generation of primes by Seive")
        print (SieveOfEratosthenes(int(first)))
    elif choice == "3.1":
        first=input("Enter the number to test by Trial Division: ")
        print ("Is Prime? :",PrimalityTestTrialDiv(int(first)))
    elif choice == "3.2":
        first=input("Enter the number to test by Sieve: ")
        print ("Is Prime?: ",PrimalityTestSieve(int(first)))
    elif choice == "3.3":
        first=input("Enter the number to test by Fermat: ")
        print ("Is Prime?: ",PrimalityTestFLT(int(first)))
    elif choice == "4.1":
        first=input("Enter number to find Prime Factorization by Trial Division for: ")
        print (trial(int(first)))
    elif choice == "4.3":
        print (make_table_4())
    elif choice == "5.1":
        first=input("Make Prime Sets! ")
        print ("Prime Set Created!",create_primes())
    elif choice == "5.2":
        first=input("Find the prop. of primes that end in ___(enter digit 0-9): ")
        primes = create_primes()
        lengthy = len(prime_2(primes, int(first)))
        lengthy2 = len(primes)
        print ("This property is possessed by: ",lengthy, "out of ",lengthy2, "total primes,")
        print ("That is about ",int((lengthy/lengthy2)*100),"%")
    elif choice == "5.3a":
        first=input("Calculate prop. of primes ending in 1 followed by a prime ending in ___(Enter 1, 3, 7, or 9): ")
        primes = create_primes()
        print (prime_a(primes, int(first)))
        lengthy = len(prime_a(primes, int(first)))
        lengthy2 = len(primes)
        print ("This property is possessed by: ",lengthy,"out of ",lengthy2,"total primes.")
        print ("That is about ",int((lengthy/lengthy2)*100),"%")
    elif choice == "5.3b":
        first=input("Calculate prop. of primes ending in 3 followed by a prime ending in ___(Enter 1, 3, 7, or 9): ")
        primes = create_primes()
        print (prime_b(primes, int(first)))
        lengthy = len(prime_b(primes, int(first)))
        lengthy2 = len(primes)
        print ("This property is possessed by: ",lengthy,"out of ",lengthy2,"total primes.")
        print ("That is about ",int((lengthy/lengthy2)*100),"%")
    elif choice == "5.3c":
        first=input("Calculate prop. of primes ending in 7 followed by a prime ending in ___(Enter 1, 3, 7, or 9): ")
        primes = create_primes()
        print (prime_c(primes, int(first)))
        lengthy = len(prime_c(primes, int(first)))
        lengthy2 = len(primes)
        print ("This property is possessed by: ",lengthy,"out of ",lengthy2,"total primes.")
        print ("That is about ",int((lengthy/lengthy2)*100),"%")
    elif choice == "5.3d":
        first=input("Calculate prop. of primes ending in 9 followed by a prime ending in ___(Enter 1, 3, 7, or 9): ")
        primes = create_primes()
        #print (prime_d(primes, int(first)))
        lengthy = len(prime_d(primes, int(first)))
        lengthy2 = len(primes)
        print ("This property is possessed by: ",lengthy,"out of ",lengthy2,"total primes.")
    elif choice == "5.4":
        print("Calculating number of twin primes in the given data set (of first 1,000,000 primes)")
        primes = create_primes()
        print ("The number of twin primes is: ",twin(primes))
    elif choice == "5.5":
        first=input("Enter max value for x to plot relationship with number of primes less than x:")
        print (plot_it(int(first)))
    elif choice == "6":
        first = input("Enter max number for graph")
        print (makeColorMatrix(int(first)))
    elif choice=="7":
        exit()
    else:
        print("You must only select an option above")
        menu()


#1.1
def gcd():
    first=input("Enter the first number: ")
    second=input("Enter the second number: ")
    first=int(first)
    second=int(second)
    return gcd_helper(first, second)

def gcd_helper(first, second):
    if first>second:
        #if a divides b
        if first % second == 0:
            return second;
        else: return gcd_helper(first%second, second)
    else:
        if second % first == 0:
            return first
        else:
            return gcd_helper(first, second%first)

#1.3
def make_table():
  #run1
  num1_1=int(542)
  snum1_1=str(num1_1)
  num1_2=int(172)
  snum1_2=str(num1_2)
  total_runs = 1
  runs1 = gcd_time(num1_1, num1_2, total_runs)
  answer1 = gcd_helper(num1_1, num1_2)
  set1 = '('+snum1_1+','+snum1_2+')'
  #run2
  num2_1=int(789)
  snum2_1=str(num2_1)
  num2_2=int(256)
  snum2_2=str(num2_2)
  total_runs = 1
  runs2 = gcd_time(num2_1, num2_2, total_runs)
  answer2 = gcd_helper(num2_1, num2_2)
  set2 = '('+snum2_1+','+snum2_2+')'
  #run3
  num3_1=int(9993)
  snum3_1=str(num1_1)
  num3_2=int(8262)
  snum3_2=str(num3_2)
  total_runs = 1
  runs3 = gcd_time(num3_1, num3_2, total_runs)
  answer3 = gcd_helper(num3_1, num3_2)
  set3 = '('+snum3_1+','+snum3_2+')'
  #run4
  num4_1=int(7244)
  snum4_1=str(num4_1)
  num4_2=int(65727)
  snum4_2=str(num4_2)
  total_runs = 1
  runs4 = gcd_time(num4_1, num4_2, total_runs)
  answer4 = gcd_helper(num4_1, num4_2)
  set4 = '('+snum4_1+','+snum4_2+')'
  #run5
  num5_1=int(673745)
  snum5_1=str(num5_1)
  num5_2=int(1733222)
  snum5_2=str(num5_2)
  total_runs = 1
  runs5 = gcd_time(num5_1, num5_2, total_runs)
  answer5 = gcd_helper(num5_1, num5_2)
  set5 = '('+snum5_1+','+snum5_2+')'
  #run6
  num6_1=int(1743532345)
  snum6_1=str(num6_1)
  num6_2=int(4346436654)
  snum6_2=str(num6_2)
  total_runs = 1
  runs6 = gcd_time(num6_1, num6_2, total_runs)
  answer6 = gcd_helper(num6_1, num6_2)
  set6 = '('+snum6_1+','+snum6_2+')'
  #run7
  num7_1=int(5674574577697)
  snum7_1=str(num7_1)
  num7_2=int(13523547676675)
  snum7_2=str(num7_2)
  total_runs = 1
  runs7 = gcd_time(num7_1, num7_2, total_runs)
  answer7 = gcd_helper(num7_1, num7_2)
  set7 = '('+snum7_1+','+snum7_2+')'

  data = [[set1,runs1],[set2,runs2],[set3,runs3],[set4,runs4],[set5,runs5],[set6,runs6],[set7,runs7]]
  df = pd.DataFrame(data,columns=['Numbers Compared','Comparisons Needed'])
  print(df)

def gcd_time(first, second, total_runs):
    if first>second:
        if first % second == 0:
            return total_runs;
        else: 
            total_runs = total_runs + 1
            return gcd_time(first%second, second, total_runs+1)
    else:
        if second % first == 0:
            return total_runs
        else:
            total_runs = total_runs + 1
            return gcd_time(first, second%first, total_runs+1)


#PART2
#-------------------------------------------------------------------------------------------
def SieveOfEratosthenes(n): 
    
    #initialize condition to true
    prime = [True for values in range(n+1)] 
    #the smallest prime is 2. We start here
    num = 2
    #while the prime squared is less than n
    while (num * num <= n): 
        #numbers that are not marked as multiples  
        if (prime[num] == True): 
              #if they are a multiple of a prime
              for values in range(num * num, n+1, num): 
                #mark them as not prime
                prime[values] = False
        #increment the value of number and do it again
        num += 1
    #go through the list and print any numbers that are prime  
    daPrimes = []
    for num in range(2, n): 
        if prime[num]: 
            print(num)
            daPrimes.append(num) 
    #return daPrimes
    return daPrimes




#PART3
#------------------------------------------------------------------------------------------
#3.1
def PrimalityTestTrialDiv(n):
    prime = True
    max = int(math.sqrt(int(n)))
    divisors = list(range(2, max+1))
    for i in divisors: 
        if n%i == 0: 
            prime = False
            break
    return prime

#3.2
def PrimalityTestSieve(n):
    isPrime = False
    prime = [True for values in range(n+2)] 
    num = 2
    while (num * num <= n+1):  
        if (prime[num] == True): 
              for values in range(num * num, n+2, num): 
                prime[values] = False
        num += 1
    daPrimes = []
    for num in range(2, n+1): 
        if prime[num]: 
            daPrimes.append(num) 
    for i in daPrimes: 
        if i == n :
            isPrime = True
    return isPrime

#3.3
def PrimalityTestFLT(p):
    prime = True
    naturalNums = list(range(1,p+1))
    for a in naturalNums: 
        check = (a**p)-a
        if check%p == 0:
            prime = True
        else:
            prime = False
            break
    return prime

#PART 4
#--------------------------------------------------------------------------------
#4.1
def trial(inp):
  num = inp
  factors = []
  while (num%2 == 0):
    factors.append(2)
    num=num/2
  i=3
  while i*i<=num:
    if (num % i == 0):
      factors.append(int(i))
      num = num/i
    else:
      i = i+2
  if (num!=1):
    factors.append(int(num))
  return factors

#4.3
def iter_trial(inp):
  iterations = 0
  num = inp
  factors = []
  while (num%2 == 0):
    factors.append(2)
    num=num/2
    iterations = iterations + 1
  i=3
  while i*i<=num:
    iterations = iterations + 1
    if (num % i == 0):
      factors.append(int(i))
      num = num/i
    else:
      i = i+2
  if (num!=1):
    factors.append(int(num))
  return iterations

def time_trial(inp):
  start_time = float(time.time())
  num = inp
  factors = []
  while (num%2 == 0):
    factors.append(2)
    num=num/2
  i=3
  while i*i<=num:
    if (num % i == 0):
      factors.append(int(i))
      num = num/i
    else:
      i = i+2
  if (num!=1):
    factors.append(int(num))
  end_time = time.time()
  timey = end_time - start_time
  return timey


def make_table_4():
  #run1
  num1=int(542)
  snum1=str(num1)
  factors1 = trial(num1)
  len1 = len(factors1)
  iter1 = iter_trial(num1)
  time1 = time_trial(num1)
  #run2
  num2=int(789)
  snum2=str(num2)
  factors2 = trial(num2)
  len2 = len(factors2)
  iter2 = iter_trial(num2)
  time2 = time_trial(num2)
  #run3
  num3=int(8262)
  snum3=str(num3)
  factors3 = trial(num3)
  len3 = len(factors3)
  iter3 = iter_trial(num3)
  time3 = time_trial(num3)
  #run4
  num4=int(65727)
  snum4=str(num4)
  factors4 = trial(num4)
  len4 = len(factors4)
  iter4 = iter_trial(num4)
  time4 = time_trial(num4)
  #run5
  num5=int(673745)
  snum5=str(num5)
  factors5 = trial(num5)
  len5 = len(factors5)
  iter5 = iter_trial(num5)
  time5 = time_trial(num5)
  #run6
  num6=int(1743532345)
  snum6=str(num6)
  factors6 = trial(num6)
  len6 = len(factors6)
  iter6 = iter_trial(num6)
  time6 = time_trial(num6)
  #run7
  num7=int(5674574577697)
  snum7=str(num7)
  factors7 = trial(num7)
  len7 = len(factors7)
  iter7 = iter_trial(num7)
  time7 = time_trial(num7)

  data = [[snum1,len1,iter1,time1],[snum2,len2,iter2,time2],[snum3,len3,iter3,time3],[snum4,len4,iter4,time4],[snum5,len5,iter5,time5],[snum6,len6,iter6,time6],[snum7, len7,iter7,time7]]
  df = pd.DataFrame(data,columns=['Number Tested','Number of Factors','Iterations Needed','Time Needed'])
  print(df)

#-----------------------------------------------------------------------------------
#5.1
def create_primes():
  return SieveOfEratosthenes(15485863)

#5.2
def prime_2(primes,val):
  primes_a_1 = []
  i=0
  while i < len(primes):
    mod =(primes[i])%10
    if(mod==val):
      primes_a_1.append(primes[i])
    i=i+1
  return primes_a_1

#5.3a:
def prime_a(primes,val):
  primes_a_1 = []
  i=0
  while i < len(primes)-1:
      mod =(primes[i])%10
      if(mod==1):
        mod_next=(primes[i+1])%10
        if(mod_next==val):
          primes_a_1.append(primes[i])
      i=i+1
  return primes_a_1

#5.3b
def prime_b(primes,val):
  primes_a_1 = []
  i=0
  while i < len(primes)-1:
      mod =(primes[i])%10
      if(mod==3):
        mod_next=(primes[i+1])%10
        if(mod_next==val):
          primes_a_1.append(primes[i])
      i=i+1
  return primes_a_1

#5.3c
def prime_c(primes,val):
  primes_a_1 = []
  i=0
  while i < len(primes)-1:
      mod =(primes[i])%10
      if(mod==7):
        mod_next=(primes[i+1])%10
        if(mod_next==val):
          primes_a_1.append(primes[i])
      i=i+1
  return primes_a_1

#5.3d
def prime_d(primes,val):
  primes_a_1 = []
  i=0
  while i < len(primes)-1:
      mod =(primes[i])%10
      if(mod==9):
        mod_next=(primes[i+1])%10
        if(mod_next==val):
          primes_a_1.append(primes[i])
      i=i+1
  return primes_a_1

#5.4
def twin(primes):
  twins=0
  i=0
  while i < len(primes)-1:
      first =primes[i]
      second=primes[i+1]
      if(second-first==2):
        twins = twins+1
      i=i+1
  return twins

#5.5
def sieve_for_5(inp):
    p_list = []
    start = 2
    #create list of all nums from 2 up to n
    x = 0
    while x < inp+1:
        p_list.append(True)
        x += 1
    #starting w first elem (2), count up 
    cur = 2
    while(cur*cur <= inp):
        #if cur number is prime
        if p_list[cur] == True:
            #get rid of all multiples of cur
            for y in range(cur*cur, inp+1, cur):
                p_list[y]=False
        #increment cur
        cur += 1
    final = []
    z = 2
    while z < inp+1:
        if p_list[z] == True:
            final.append(z)
        z += 1
    return final

def plot_it(max):
  x_coords = []
  y_coords = []
  x = 0
  while x < max:
    #x value
    x_coords.append(x)
    #create y value for # of primes less than x
    prime_count = Sieve(x)
    y_coords.append(len(prime_count)) 
    x=x+1 
  plt.plot([x_coords],[y_coords],'ro')
  plt.axis([0, max, 0, (max/2)])
  plt.show()

#PART6
#------------------------------------------------------------------------------------------

def Sieve(n): 
    
    #initialize condition to true
    prime = [True for values in range(n+1)] 
    #the smallest prime is 2. We start here
    num = 2
    #while the prime squared is less than n
    while (num * num <= n): 
        #numbers that are not marked as multiples  
        if (prime[num] == True): 
              #if they are a multiple of a prime
              for values in range(num * num, n+1, num): 
                #mark them as not prime
                prime[values] = False
        #increment the value of number and do it again
        num += 1
    #go through the list and print any numbers that are prime  
    daPrimes = []
    for num in range(2, n): 
        if prime[num]: 
            daPrimes.append(num) 
    return daPrimes

def makeMatrix(n):
     return [[i + (j*j) for i in range(1,n+1)] for j in range(n)]

def makeColorMatrix(n):
    graph = makeMatrix(n)
    thesePrimes = Sieve(n**2)
    shade = []
    for i in graph:
        section = []       
        for j in i:
            if j in thesePrimes:
                section.append(1)
            else:
                section.append(0)
        shade.append(section)
    
    sns.heatmap(shade, linewidths=n/(n*100000), 
                cbar = False , cmap = "Accent");
    plt.title("Visualizing Primes".format(n,n), fontsize=10);
    plt.savefig("n_{}_by_{}.png".format(n,n))
    plt.show()

if __name__ == '__main__':
  menu()