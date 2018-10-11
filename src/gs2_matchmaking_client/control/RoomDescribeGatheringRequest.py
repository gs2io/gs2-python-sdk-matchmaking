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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_matchmaking_client.Gs2Matchmaking import Gs2Matchmaking


class RoomDescribeGatheringRequest(Gs2UserRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "DescribeGathering"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(RoomDescribeGatheringRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__page_token = None
            self.__limit = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

    def get_matchmaking_name(self):
        """
        マッチメイキングの名前を指定します。を取得
        :return: マッチメイキングの名前を指定します。
        :rtype: unicode
        """
        return self.__matchmaking_name

    def set_matchmaking_name(self, matchmaking_name):
        """
        マッチメイキングの名前を指定します。を設定
        :param matchmaking_name: マッチメイキングの名前を指定します。
        :type matchmaking_name: unicode
        """
        if matchmaking_name is not None and not (isinstance(matchmaking_name, str) or isinstance(matchmaking_name, unicode)):
            raise TypeError(type(matchmaking_name))
        self.__matchmaking_name = matchmaking_name

    def with_matchmaking_name(self, matchmaking_name):
        """
        マッチメイキングの名前を指定します。を設定
        :param matchmaking_name: マッチメイキングの名前を指定します。
        :type matchmaking_name: unicode
        :return: this
        :rtype: RoomDescribeGatheringRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if page_token is not None and not (isinstance(page_token, str) or isinstance(page_token, unicode)):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: RoomDescribeGatheringRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if limit is not None and not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: RoomDescribeGatheringRequest
        """
        self.set_limit(limit)
        return self
