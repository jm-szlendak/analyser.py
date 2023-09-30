import unittest
import os
import io
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyse import analyse

class TestAnalyse(unittest.TestCase):
    def setUp(self) -> None:
        self.postsXmlPath = os.path.join(os.path.dirname(__file__), 'data/posts.xml')


    def test_analyse(self):
        expected = {
            'avg_response_score': 8.666666666666666,
            'oldest_post_create_date': '2016-01-12T19:24:29Z',
            'newest_post_create_date': '2016-01-12T20:09:21Z',
            'total_answered_posts_count': 1,
            'total_posts_count': 3
        }

        with open(self.postsXmlPath, 'r') as xmlFile:
            results = analyse(xmlFile)
            self.assertEqual(results, expected)






if __name__ == '__main__':
    unittest.main()