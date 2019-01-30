# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_story_single_response(self):
        """测试单个答案是否存储"""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('Chinese')
        self.assertIn('Chinese', my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案是否存储"""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['Chinese', 'English', 'Japanese']
        for response in responses:
            my_survey.store_responses(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
