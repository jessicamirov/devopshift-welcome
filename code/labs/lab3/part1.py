import httpx

try:
    URL = "https://jsonplaceholder.typicode.com/users/1"
    response = httpx.get(URL)
    code = response.status_code

    if code == 200:
        data = response.json()
        print("name: ", data.get("name"))
        print("email: ", data.get("email"))
        print(f"Address: {data['address']['street']}, {data['address']['city']}")
    elif code == 404: 
        print(f"Code {code}. User not found")
    elif code >= 500:
        print(f"Code {code}. Server error. Please try again later")
    else:
        print ("error", f"Unexpected error. Status code: {code}")
except httpx.HTTPStatusError:
    print("I don't know what to do")
