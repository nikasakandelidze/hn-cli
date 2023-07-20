from domain import NewsDto, JobDto

class HackerNewsApiAdapter:
    def __init__(self) -> None:
        pass

    def fetch_news_list(self) -> list[NewsDto]:
        pass

    def fetch_news_by_id(self, id: str) -> NewsDto:
        pass

    def fetch_jobs_list(self) -> list[NewsDto]:
        pass
