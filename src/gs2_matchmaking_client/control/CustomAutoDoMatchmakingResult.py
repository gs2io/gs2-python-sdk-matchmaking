# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_matchmaking_client.model import *


class CustomAutoDoMatchmakingResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        self.__done = bool(response['done']) if 'done' in response.keys() and response['done'] is not None else None
        self.__item = CustomAutoGathering(response['item']) if 'item' in response.keys() and response['item'] is not None else None
        self.__search_context = unicode(response['searchContext']) if 'searchContext' in response.keys() and response['searchContext'] is not None else None
    def get_done(self):
        """
        マッチメイキングが完了したかを取得
        :return: マッチメイキングが完了したか
        :rtype: bool
        """
        return self.__done
    def get_item(self):
        """
        CustomAutoマッチメイキング ギャザリングを取得
        :return: CustomAutoマッチメイキング ギャザリング
        :rtype: CustomAutoGathering
        """
        return self.__item
    def get_search_context(self):
        """
        検索を再開するためのコンテキストを取得
        :return: 検索を再開するためのコンテキスト
        :rtype: unicode
        """
        return self.__search_context

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(CustomAutoDoMatchmakingResult, self).__getitem__(key)

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return {
            'done': self.__done,
            'item': self.__item.to_dict(),
            'searchContext': self.__search_context,
        }
