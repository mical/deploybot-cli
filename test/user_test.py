# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.user import User


class TestUser(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        self.user = User()

    # test users list
    def test_list_must_be_return_json(self):
        self.assertNotEquals("", self.user.list())