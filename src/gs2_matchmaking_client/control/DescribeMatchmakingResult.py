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


class DescribeMatchmakingResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__next_page_token = unicode(response['nextPageToken']) if 'nextPageToken' in response.keys() and response['nextPageToken'] is not None else None
        
        self.__items = list(
            map(
                lambda data:
                Matchmaking(data)
                ,
                response['items']
            )
        )

    def get_next_page_token(self):
        """
        次のページを読み込むためのトークンを取得
        :return: 次のページを読み込むためのトークン
        :rtype: unicode
        """
        return self.__next_page_token

    def get_items(self):
        """
        マッチメイキングを取得
        :return: マッチメイキング
        :rtype: list[Matchmaking]
        """
        return self.__items
