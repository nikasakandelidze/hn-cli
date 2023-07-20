from controller.cli_controller import CliController
from service.core_service import CoreService
from service.hacker_news_api_adapter import HackerNewsApiAdapter

def main():
    cli_presenter = CliController()
    hn_adapter = HackerNewsApiAdapter()
    service = CoreService(cli_presenter, hn_adapter)
    service.start()

main()