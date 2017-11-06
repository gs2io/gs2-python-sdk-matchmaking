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


class RoomDescribeJoinedUserRequest(Gs2UserRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "DescribeJoinedUser"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(RoomDescribeJoinedUserRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__gathering_id = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_gathering_id(params['gatheringId'] if 'gatheringId' in params.keys() else None)

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
        if not isinstance(matchmaking_name, unicode):
            raise TypeError(type(matchmaking_name))
        self.__matchmaking_name = matchmaking_name

    def with_matchmaking_name(self, matchmaking_name):
        """
        マッチメイキングの名前を指定します。を設定
        :param matchmaking_name: マッチメイキングの名前を指定します。
        :type matchmaking_name: unicode
        :return: this
        :rtype: RoomDescribeJoinedUserRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_gathering_id(self):
        """
        ギャザリングのIDを指定します。を取得
        :return: ギャザリングのIDを指定します。
        :rtype: unicode
        """
        return self.__gathering_id

    def set_gathering_id(self, gathering_id):
        """
        ギャザリングのIDを指定します。を設定
        :param gathering_id: ギャザリングのIDを指定します。
        :type gathering_id: unicode
        """
        if not isinstance(gathering_id, unicode):
            raise TypeError(type(gathering_id))
        self.__gathering_id = gathering_id

    def with_gathering_id(self, gathering_id):
        """
        ギャザリングのIDを指定します。を設定
        :param gathering_id: ギャザリングのIDを指定します。
        :type gathering_id: unicode
        :return: this
        :rtype: RoomDescribeJoinedUserRequest
        """
        self.set_gathering_id(gathering_id)
        return self
