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
    last_proof_string = f'{json.dumps(last_proof, sort_keys=True)}'.encode()
    last_hash = hashlib.sha256(last_proof_string).hexdigest()

    p_prime = 0
    while valid_proof(last_hash, p_prime, difficulty) is False:
        p_prime += 1
    print("Proof found: " + str(p_prime) + " in " + str(timer() - start))
    return p_prime


def valid_proof(last_hash, proof, difficulty):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?

    IE:  last_hash: ...AE9123456, new hash 123456888...
    """
    guess = f'{proof}'.encode()

    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == last_hash[-difficulty:]


def last_proof():

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers)
    
    print(f'{response.text}')
    return response.json()

def mine_coin(proof):

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
    print("MINING")
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
