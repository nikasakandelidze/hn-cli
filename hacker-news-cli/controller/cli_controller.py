class CliController:
    def __init__(self) -> None:
        pass
    
    def present(self, text) -> None:
        print(f'> {text}')
    
    def get_input(self, text='') -> str :
        input(f'> {text}')