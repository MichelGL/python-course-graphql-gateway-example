from datetime import datetime

import pytest

from dataloaders import NewsLoader
from models.news import NewsModel


class TestNewsLoader:
    @pytest.fixture
    def loader(self):
        return NewsLoader()

    def test_load_one_news(self, loader):
        news: list[NewsModel] = loader.load("RU").get()

        assert len(news) == 3
        news_item = news[0]
        assert news_item.author == "Иван Иванов"
        assert news_item.source == "ТАСС"
        assert (
            news_item.title
            == "Путин проведет встречу с лидерами стран ШОС в Москве"
        )
        assert (
                news_item.description == "Президент России Владимир Путин встретится с лидерами стран Шанхайской Организации Сотрудничества (ШОС) в Москве для обсуждения сотрудничества и региональной стабильности."
        )
        assert (
            news_item.url == "https://tass.ru/politika/1357924"
        )


    def test_load_many_news(self, loader):
        news: list[list[NewsModel]] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(news) == 3