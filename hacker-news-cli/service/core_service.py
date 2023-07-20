from controller.cli_controller import CliController
from hacker_news_api_adapter import HackerNewsApiAdapter
from utils.constants import WELCOME_MESSAGE, POTENTIAL_COMMANDS, VALIDATION_ERROR_MESSAGE, SEPARATOR, INPUT_PROMPT
from domain import NewsDto, JobDto

class CoreService:
    def __init__(self, controller: CliController, hn_adapter: HackerNewsApiAdapter) -> None:
        self.controller = controller
        self.hn_adapter = hn_adapter
    
    def start(self):
        self.controller.present(WELCOME_MESSAGE)
        self.controller.present(SEPARATOR, periodic=False)
        commands_message = self._get_commands_message()
        self.controller.present(commands_message)
        while True:
            input_result = self.controller.get_input(INPUT_PROMPT)
            self.execute_command(input_result)

    def execute_command(self, identifier: str) -> None:
        if not self._validate_input(identifier):
            message = VALIDATION_ERROR_MESSAGE.format(potential_values=','.join(POTENTIAL_COMMANDS['commands'].keys()))
            self.controller.present(message)
            return
        if identifier == '0':
            news_list: list[NewsDto] = self.hn_adapter.fetch_news_list()
        elif identifier == '1':
            single_new :list[NewsDto] = self.hn_adapter.fetch_news_by_id('DUMMY_ID')
        elif identifier == '2':
            jobs_list : list[JobDto] = self.hn_adapter.fetch_jobs_list()


    def _validate_input(self, identifier: str) -> bool:
        return identifier in POTENTIAL_COMMANDS['commands']

    def _get_commands_message(self):
        max_num = POTENTIAL_COMMANDS['max_num']
        message = f'Input any number between 0 and {max_num} to execute according command:\n'
        for identifier, command_description in POTENTIAL_COMMANDS['commands'].items():
            message += f'> {identifier}) {command_description}\n'
        message += f'> {SEPARATOR}\n'
        message += '>'
        return message

