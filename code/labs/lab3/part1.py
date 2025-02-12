import httpx

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/users/1')
    code = response.status_code
    if code == 200:
        data = response.json()
        print({"name": data.get("name")})
        print({"email": data.get("email")})
        print(f"Address: {data['address']['street']}, {data['address']['city']}")
    elif code == 404: 
        print("User not found")
    elif code == 500: 
        print("Server error. Please try again later")
    else:
        print ({"error": f"Unexpected error. Status code: {response.status_code}"})
except TypeError:
    print("I don't know what to do")
