# coding: utf-8
from .suite import BaseSuite


class TestAdmin(BaseSuite):
    def test_action(self):
        rv = self.client.get('/admin/action')
        assert rv.status_code == 200
