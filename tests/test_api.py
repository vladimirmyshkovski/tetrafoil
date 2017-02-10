# coding: utf-8
from .suite import BaseSuite


class TestApi(BaseSuite):
    def test_action(self):
        rv = self.client.get('/api/action')
        assert rv.status_code == 200
