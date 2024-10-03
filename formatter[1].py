import time
import textwrap
import random

def type_text_top_formatted(text, delay):    
    print("\n**********************************************************************************************\n")
    lines = text.split('\n')
    for line in lines:
        indented_text = "          | " + line
        # print each character with a delay
        for c in indented_text:
            print(c, end='', flush=True)
            time.sleep(delay / 1000.0) #delay is in milliseconds
        print()
    
    print()

def type_text_bottom_formatted(text, delay):    
    lines = text.split('\n')
    
    for line in lines:
        indented_text = "          | " + line
        for c in indented_text:
            print(c, end="", flush=True)
            time.sleep(delay / 1000.0)
        print()
        
    print("\n**********************************************************************************************\n")

def type_text_formatted(text, delay):
    print("\n**********************************************************************************************\n")
    
    lines = text.split('\n')
    
    for line in lines:
        indented_text = "          | " +  line
        for c in indented_text:
            print(c, end="", flush=True)
            time.sleep(delay / 1000.0)
        print()
    print("\n**********************************************************************************************\n")

def type_text_no_format(text, delay):    
    lines = text.split('\n')
    
    for line in lines:
        indented_text = "          | " +  line
        for c in indented_text:
            print(c, end="", flush=True)
            time.sleep(delay / 1000.0)
        print()
    print()
    
def shuffle_text(text):
    char_list = list(text.replace("\n", " "))
    random.shuffle(char_list)
    shuffled = ''.join(char_list)
    
    wrapped_shuffled_text = textwrap.fill(shuffled, width=80)
    return wrapped_shuffled_text

def to_lower_string(text):
    return text.lower()

def type_text_blank_format(text, delay):    
    lines = text.split('\n')
    
    for line in lines:
        indented_text = "| " +  line
        for c in indented_text:
            print(c, end="", flush=True)
            time.sleep(delay / 1000.0)
        print()
