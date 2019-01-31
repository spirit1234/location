# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinese', 'English', 'Japanese']

    def test_story_single_response(self):
        """测试单个答案是否存储"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案是否存储"""
        for response in self.responses:
            self.my_survey.store_responses(response)
            self.assertIn(response, self.my_survey.responses)


unittest.main()
