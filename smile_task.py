#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import requests
import unittest
import json


class SmileTaskTest(unittest.TestCase):
    def setUp(self):
        self.url='http://127.0.0.1:3000'
        self.header={"content-type":"application/json"}

    def tearDown(self):
        pass

    def getTaskId(self,title,desc):
        url=self.url+'/api/tasks'
        payload=json.dumps({"title":title,"desc":desc})

        r=requests.post(url,data=payload,headers=self.header).json()
        return r['id']

    def test_get_task(self):
        tId=self.getTaskId("hello","world")
        url=self.url+"/api/tasks/"+str(tId)

        r=requests.get(url).json()
        self.assertEqual(r['id'],tId)

    def test_complete_task(self):
        tId=self.getTaskId("hello","world")
        url=self.url+"/api/tasks/"+str(tId)

        r=requests.put(url).json()
        self.assertEqual(r['done'],True)

    def test_delete_task(self):
        tId=self.getTaskId("hello","world")
        url=self.url+"/api/tasks/"+str(tId)

        r=requests.delete(url).json()
        self.assertEqual(r['id'],str(tId))

if __name__=='__main__':
    unittest.main()