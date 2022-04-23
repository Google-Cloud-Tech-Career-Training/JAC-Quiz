# Copyright 2017, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from google.cloud import datastore

project_id = os.getenv('GCLOUD_PROJECT')


"""
Persists initial questions into datastore
"""
def main():

    """
    Create an array of dicts defining questions
    """
    questions = [
        {
            'quiz': u'pets',
            'author': u'Cherie',
            'title': u'Whh has a pet?',
            'answer1': u'Justice',
            'answer2': u'Cherie',
            'answer3': u'Aliyah',
            'answer4': u'none',
            'correctAnswer': 1,
            'imageUrl': u''
        },
        {
            'quiz': u'state',
            'author': u'Cherie',
            'title': u'Which one lives in California?',
            'answer1': u'Cherie',
            'answer2': u'Justicee',
            'answer3': u'Aliyah',
            'answer4': u'none',
            'correctAnswer': 1,
            'imageUrl': u''
        },
        {
            'quiz': u'vowel',
            'author': u'Cherie',
            'title': u'Which one name starts with a vowel?',
            'answer1': u'Justice',
            'answer2': u'Aliyah',
            'answer3': u'Cherie',
            'answer4': u'All of the above',
            'correctAnswer': 2,
            'imageUrl': u''
        },
        {
            'quiz': u'gcp fellow',
            'author': u'Cherie',
            'title': u'Which one is a Google Cloud Fellow',
            'answer1': u'Cherie',
            'answer2': u'Aliyah',
            'answer3': u'Justice',
            'answer4': u'All of them',
            'correctAnswer': 4,
            'imageUrl': u''
        },
    ]

    client = datastore.Client(project_id)

    """
    Create and persist and entity for each question
    """
    for q_info in questions:
        key = client.key('Question')
        q_entity = datastore.Entity(key=key)
        for q_prop, q_val in q_info.iteritems():
            q_entity[q_prop] = q_val
        client.put(q_entity)

if __name__ == '__main__':
    main()
