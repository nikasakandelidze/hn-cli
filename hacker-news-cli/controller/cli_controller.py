import time
import sys

class CliController:
    def __init__(self) -> None:
        pass
    
    def present(self, text, periodic=True, end_delay=True) -> None:
        if periodic:
            print('>', end='', flush=True)
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.01)
            if end_delay:
                time.sleep(0.2)
            print('')
        else:
            print(f'> {text}')
    
    def get_input(self, text='') -> str :
        return input(f'> {text}')