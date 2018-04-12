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


class RoomCreateGatheringRequest(Gs2UserRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "CreateGathering"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(RoomCreateGatheringRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__meta = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)

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
        if matchmaking_name and not isinstance(matchmaking_name, unicode):
            raise TypeError(type(matchmaking_name))
        self.__matchmaking_name = matchmaking_name

    def with_matchmaking_name(self, matchmaking_name):
        """
        マッチメイキングの名前を指定します。を設定
        :param matchmaking_name: マッチメイキングの名前を指定します。
        :type matchmaking_name: unicode
        :return: this
        :rtype: RoomCreateGatheringRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_meta(self):
        """
        ギャザリングのメタ情報を取得
        :return: ギャザリングのメタ情報
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        ギャザリングのメタ情報を設定
        :param meta: ギャザリングのメタ情報
        :type meta: unicode
        """
        if meta and not isinstance(meta, unicode):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        ギャザリングのメタ情報を設定
        :param meta: ギャザリングのメタ情報
        :type meta: unicode
        :return: this
        :rtype: RoomCreateGatheringRequest
        """
        self.set_meta(meta)
        return self
