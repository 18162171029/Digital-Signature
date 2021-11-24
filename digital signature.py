import random
def check_prime(num):
    if num > 1: 
       for i in range(2, num): 
           if (num % i) == 0: 
               return 0
               break
       else: 
           return 1
      
    else: 
       return 0

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
        
hash_value=1234
p=int(input('Enter the prime number: '))
for i in range(1, p):
    if (p-1)%i==0:
        if check_prime(i)==1:
            q=i
            break
        else:
            continue

a=(p-1)//q
for i in range(2, p):
    if (i**a)%p >1:
        h=i
        g=(i*(p-1))/q
        g=g%p
        
x=random.randint(1, q-1)
y=g**x
y=y%p
k=random.randint(1, q-1)

r=((g**k)%p)%q
k_in=modInverse(k, q)
s=((k_in*hash_value)+(x*r))%q


w=modInverse(s, q)
u1=(hash_value*w)%q
u2=(r*w)%q
v=(((g**u1)*(y**u2))%p)%q
print(f'p = {p}\nq = {q}\ng = {g}\nselected value for h = {h}\nUsers Private key = {x}\nUsers Public Key = {y}')
print(f'Users per message secret number = k')
print(f'Hashing algorithm value = {hash_value}')
print(f'r = {r}\ns = {s}')
print(f'Signature = ({r}, {s})')
print(f'\nVerifying')
print(f'w = {w}\nU1 = {u1}\nU2 = {u2}\nV = {v}')
