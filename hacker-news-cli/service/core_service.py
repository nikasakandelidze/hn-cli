from controller.cli_controller import CliController
from utils.constants import WELCOME_MESSAGE, POTENTIAL_COMMANDS

class CoreService:
    def __init__(self, controller: CliController) -> None:
        self.controller = controller
    
    def start(self):
        self.controller.present(WELCOME_MESSAGE+'\n>')
        commands_message = self._get_commands_message()
        while True:
            input_result = self.controller.get_input(commands_message)
            print(input_result)

    def _get_commands_message(self):
        max_num = POTENTIAL_COMMANDS['max_num']
        message = f'Input any number between 0 and {max_num} to execute according command:\n'
        for identifier, command_description in POTENTIAL_COMMANDS['commands'].items():
            message += f'> {identifier}) {command_description}\n'
        message += 'Which command you want to use: '
        return message

