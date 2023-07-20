from controller.cli_controller import CliController
from service.core_service import CoreService

def main():
    cli_presenter = CliController()
    service = CoreService(cli_presenter)
    service.start()

main()