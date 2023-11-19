import os
import subprocess
from config import default_config
import os, random
from pathlib import Path
import tiktoken
from getpass import getpass
import openai
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from config import default_config
import time


def get_gpt_response(user_prompt, system_prompt=default_config.system_prompt_commands, model=default_config.model_name, n=3, max_tokens=80):
    '''
    INPUT: 
    Argument
    user_prompt
    system_prompt
    model
    '''

    messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        n=n,
        max_tokens=max_tokens
    )
    
    return response

def print_help():
    print("\033[95m {}\033[00m" .format("help || h: print this help message"))
    print("\033[91m {}\033[00m" .format("quit || q: exit the program"))
    print("\033[92m {}\033[00m" .format("n: regenerate with the same prompt"))
    print("\033[92m {}\033[00m" .format("enter: run the first command"))
    print("\033[92m {}\033[00m" .format("1-3: run the command in 1-3"))
    print("\033[94m {}\033[00m" .format("any other input will be used as the prompt for the command"))
    print("")



while True:
    # get user input
    user_input = input(">>> ")

    gpt_response = "ls -ltr"

    # print gpt response
    print(gpt_response)

    # if the user types right arrow > then regenerate the gpt response
    if user_input == "n":
        print("\033[91m {}\033[00m" .format("regenerating command... \n"))
        gpt_response = "echo 'hello world'"
        print(gpt_response)


    if user_input == "":
        print("\033[91m {}\033[00m" .format("running command... \n"))
        
        # os.system(gpt_response)
        subprocess.run(gpt_response, shell=True)
        # result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
        # print(result.stdout)
    


    if user_input.lower() in ["help", "h"]:
        print_help()

    # if user input is "quit" or "exit" or hits escape key, then exit
    if user_input.lower() in ["quit", "exit", "q"]:
        break

