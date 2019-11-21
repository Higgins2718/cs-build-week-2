import hashlib
import requests
import json
import sys
from keys import api_key
from uuid import uuid4
from time import sleep
from timeit import default_timer as timer
from json import loads

import random

def proof_of_work(last_proof, difficulty):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    #  TODO: Your code here

    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start) + "\n")
    return proof

def valid_proof(last_hash, proof, difficulty):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?

    IE:  last_hash: ...AE9123456, new hash 123456888...
    """

    # TODO: Your code here!

    previous_proof = f'{last_hash}'.encode()
    previous_proof = hashlib.sha256(previous_proof).hexdigest()
    
    guess = f"{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    first = guess_hash[:difficulty]
    last = previous_proof[-difficulty:]
    return  last == first

def last_proof():
    # curl -X GET -H 'Authorization: Token 15d04b7d7f437a151894f4e9eea4029eff396d4d' https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers)
    
    print(f'{response.text}')
    return response.json()

def mine_coin(proof):
    # curl -X POST -H 'Authorization: Token 15d04b7d7f437a151894f4e9eea4029eff396d4d' -H "Content-Type: application/json" -d '{"proof": 5978240}' https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    data = '{"proof": my_proof}'.replace("my_proof", str(proof))
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=headers, data=data)

    print(f'{response.status_code}\n{response.text}\n\n')
    return response.json()

if __name__ == "__main__":
    i = 1
    while True:
        print(f"{i}. ", end=" ")
        #get last proof
        last_proof_json = last_proof()
        last_proof_cooldown = last_proof_json.get('cooldown')
        proof = last_proof_json.get('proof')
        last_proof_difficulty = last_proof_json.get('difficulty')
        sleep(last_proof_cooldown)

        # look for proof
        work = proof_of_work(proof,last_proof_difficulty)
        
        # check proof
        mine_coin_json = mine_coin(work)
        mine_coin_cooldown = mine_coin_json.get('cooldown')
        sleep(mine_coin_cooldown)
        i += 1
