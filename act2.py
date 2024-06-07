import requests, json, os

def isPrime(n):
    if not n > 0:
        return False

numposts =  input('Indique la cantidad de Posts que desea obtener (que sea un numero entre  1 y  100): ')

if not numposts.isdigit():
    print("No es un NUMERO")
    
if int(numposts) < 1:
    print("Es menor a 1")

if int(numposts) > 100:
    print("Es mayor a 100")

str  = input('Indique la palabra clave  a buscar: ')

if str.isdigit():
    print('Se ingreso un NUMERO')
    
count = 0 
numposts = int(numposts)
json_string = ""

for i in range(1, numposts + 1):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    response.raise_for_status()
    if response.status_code == 200:
            data = response.json()
            json_string = json_string + json.dumps(data)
            
            for i in range (1, numposts+1):
                title = data["title"]
                body = data["body"]
                if title.__contains__(str) or body.__contains__(str):
                    print(data)
                    count = count + 1
            
    if isPrime(i) == True:
        for i in range(1, 100):        
            if(os.path.exists(f'dl{i}Primes.json')):
                with open(f'dl{i+1}Primes.json', 'w') as file:
                    file.write(json_string)
                    break
            else:
                with open('dl1Primes.json', 'w') as file:
                    file.write(json_string)
                    break

    else: 
        for i in range(1, 100):        
            if(os.path.exists(f'dl{i}NotPrimes.json')):
                with open(f'dl{i+1}NotPrimes.json', 'w') as file:
                    file.write(json_string)
                    break
            else:
                with open('dl1NotPrimes.json', 'w') as file:
                    file.write(json_string)
                    break

print(f'Cantidad de Posts con {str}: {count}')