# -*- coding:utf-8 -*-
class AnonymousSurvey(object):
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for responses in self.responses:
            print('- ' + responses)
