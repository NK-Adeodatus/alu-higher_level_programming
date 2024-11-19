#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        json_response = response.json()

        if json_response:
            if "id" in json_response and "name" in json_response:
                print(f"[{json_response['id']}] {json_response['name']}")
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
