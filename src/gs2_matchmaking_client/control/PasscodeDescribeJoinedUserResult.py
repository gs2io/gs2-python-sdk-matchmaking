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


class PasscodeDescribeJoinedUserResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__items = list(
            map(
                lambda data:
                unicode(data)
                ,
                response['items']
            )
        )

    def get_items(self):
        """
        ギャザリングに参加しているユーザIDリストを取得
        :return: ギャザリングに参加しているユーザIDリスト
        :rtype: list[unicode]
        """
        return self.__items
