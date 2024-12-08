from tqdm import tqdm
from rich.traceback import install
from string import punctuation
from time import sleep
install()
from icecream import ic
# Initialize global variables
ic.configureOutput(prefix='Debug | ')
li: list[str] = []
dictn: dict[int, str] = {}
ic(punctuation)
def sentence(word: str) -> str:
    """
    Reverses the order of non-punctuation characters in a string while keeping punctuation marks in their original positions.
    
    Args:
        word (str): Input string to be processed
        
    Returns:
        str: Modified string with reversed non-punctuation characters and original punctuation positions
    """
    for i in tqdm(range(len(word)), desc="Finding punctuation"):
        sleep(0.1)
        if word[i] in punctuation:
            dictn[i] = word[i]
            
    for i in tqdm(word, desc="Finding non-punctuation"):
        sleep(0.1)
        if i not in punctuation:
            li.append(i)
            
    li.reverse()
    result: list[str] = list(li)
    
    for i, j in tqdm(dictn.items(), desc="Inserting punctuation"):
        sleep(0.1)
        result.insert(i, j)
        
    return ''.join(result)

user_input: str = input("Enter a sentence: ")
ic(user_input)
output=sentence(user_input)
ic(output)
