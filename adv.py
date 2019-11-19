import requests
from json import dumps, loads
from keys import api_key

def post_move(direction):
    if direction is None:
        return "YOU MUST PASS A DIRECTION"
    elif direction != 'n' and direction != 'e' and direction != 's' and direction != 'w':
        return "NOT A VALID DIRECTION"
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }
    if direction == 'n':
        data = '{"direction":"n"}'
    elif direction == 's':
        data = '{"direction":"s"}'
    elif direction == 'e':
        data = '{"direction":"e"}'
    else:
        data = '{"direction":"w"}'

    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data)
    # print(response.text)
    return loads(response.text)

# Uncomment here to test
json_response = post_move('n')
print(json_response["title"])
