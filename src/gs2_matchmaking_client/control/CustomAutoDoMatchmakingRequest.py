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


class CustomAutoDoMatchmakingRequest(Gs2UserRequest):

    FUNCTION = "DoMatchmaking"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CustomAutoDoMatchmakingRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__search_attribute2_max = None
            self.__search_attribute1_min = None
            self.__search_attribute5_min = None
            self.__search_attribute4_min = None
            self.__attribute3 = None
            self.__search_attribute3_max = None
            self.__search_attribute4_max = None
            self.__search_attribute1_max = None
            self.__search_context = None
            self.__search_attribute5_max = None
            self.__search_attribute3_min = None
            self.__attribute2 = None
            self.__search_attribute2_min = None
            self.__attribute1 = None
            self.__attribute4 = None
            self.__attribute5 = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_search_attribute2_max(params['searchAttribute2Max'] if 'searchAttribute2Max' in params.keys() else None)
            self.set_search_attribute1_min(params['searchAttribute1Min'] if 'searchAttribute1Min' in params.keys() else None)
            self.set_search_attribute5_min(params['searchAttribute5Min'] if 'searchAttribute5Min' in params.keys() else None)
            self.set_search_attribute4_min(params['searchAttribute4Min'] if 'searchAttribute4Min' in params.keys() else None)
            self.set_attribute3(params['attribute3'] if 'attribute3' in params.keys() else None)
            self.set_search_attribute3_max(params['searchAttribute3Max'] if 'searchAttribute3Max' in params.keys() else None)
            self.set_search_attribute4_max(params['searchAttribute4Max'] if 'searchAttribute4Max' in params.keys() else None)
            self.set_search_attribute1_max(params['searchAttribute1Max'] if 'searchAttribute1Max' in params.keys() else None)
            self.set_search_context(params['searchContext'] if 'searchContext' in params.keys() else None)
            self.set_search_attribute5_max(params['searchAttribute5Max'] if 'searchAttribute5Max' in params.keys() else None)
            self.set_search_attribute3_min(params['searchAttribute3Min'] if 'searchAttribute3Min' in params.keys() else None)
            self.set_attribute2(params['attribute2'] if 'attribute2' in params.keys() else None)
            self.set_search_attribute2_min(params['searchAttribute2Min'] if 'searchAttribute2Min' in params.keys() else None)
            self.set_attribute1(params['attribute1'] if 'attribute1' in params.keys() else None)
            self.set_attribute4(params['attribute4'] if 'attribute4' in params.keys() else None)
            self.set_attribute5(params['attribute5'] if 'attribute5' in params.keys() else None)

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
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_search_attribute2_max(self):
        """
        既存のギャザリングに参加する対象とする属性値2の最大値を取得
        :return: 既存のギャザリングに参加する対象とする属性値2の最大値
        :rtype: int
        """
        return self.__search_attribute2_max

    def set_search_attribute2_max(self, search_attribute2_max):
        """
        既存のギャザリングに参加する対象とする属性値2の最大値を設定
        :param search_attribute2_max: 既存のギャザリングに参加する対象とする属性値2の最大値
        :type search_attribute2_max: int
        """
        if not isinstance(search_attribute2_max, int):
            raise TypeError(type(search_attribute2_max))
        self.__search_attribute2_max = search_attribute2_max

    def with_search_attribute2_max(self, search_attribute2_max):
        """
        既存のギャザリングに参加する対象とする属性値2の最大値を設定
        :param search_attribute2_max: 既存のギャザリングに参加する対象とする属性値2の最大値
        :type search_attribute2_max: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute2_max(search_attribute2_max)
        return self

    def get_search_attribute1_min(self):
        """
        既存のギャザリングに参加する対象とする属性値1の最小値を取得
        :return: 既存のギャザリングに参加する対象とする属性値1の最小値
        :rtype: int
        """
        return self.__search_attribute1_min

    def set_search_attribute1_min(self, search_attribute1_min):
        """
        既存のギャザリングに参加する対象とする属性値1の最小値を設定
        :param search_attribute1_min: 既存のギャザリングに参加する対象とする属性値1の最小値
        :type search_attribute1_min: int
        """
        if not isinstance(search_attribute1_min, int):
            raise TypeError(type(search_attribute1_min))
        self.__search_attribute1_min = search_attribute1_min

    def with_search_attribute1_min(self, search_attribute1_min):
        """
        既存のギャザリングに参加する対象とする属性値1の最小値を設定
        :param search_attribute1_min: 既存のギャザリングに参加する対象とする属性値1の最小値
        :type search_attribute1_min: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute1_min(search_attribute1_min)
        return self

    def get_search_attribute5_min(self):
        """
        既存のギャザリングに参加する対象とする属性値5の最小値を取得
        :return: 既存のギャザリングに参加する対象とする属性値5の最小値
        :rtype: int
        """
        return self.__search_attribute5_min

    def set_search_attribute5_min(self, search_attribute5_min):
        """
        既存のギャザリングに参加する対象とする属性値5の最小値を設定
        :param search_attribute5_min: 既存のギャザリングに参加する対象とする属性値5の最小値
        :type search_attribute5_min: int
        """
        if not isinstance(search_attribute5_min, int):
            raise TypeError(type(search_attribute5_min))
        self.__search_attribute5_min = search_attribute5_min

    def with_search_attribute5_min(self, search_attribute5_min):
        """
        既存のギャザリングに参加する対象とする属性値5の最小値を設定
        :param search_attribute5_min: 既存のギャザリングに参加する対象とする属性値5の最小値
        :type search_attribute5_min: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute5_min(search_attribute5_min)
        return self

    def get_search_attribute4_min(self):
        """
        既存のギャザリングに参加する対象とする属性値4の最小値を取得
        :return: 既存のギャザリングに参加する対象とする属性値4の最小値
        :rtype: int
        """
        return self.__search_attribute4_min

    def set_search_attribute4_min(self, search_attribute4_min):
        """
        既存のギャザリングに参加する対象とする属性値4の最小値を設定
        :param search_attribute4_min: 既存のギャザリングに参加する対象とする属性値4の最小値
        :type search_attribute4_min: int
        """
        if not isinstance(search_attribute4_min, int):
            raise TypeError(type(search_attribute4_min))
        self.__search_attribute4_min = search_attribute4_min

    def with_search_attribute4_min(self, search_attribute4_min):
        """
        既存のギャザリングに参加する対象とする属性値4の最小値を設定
        :param search_attribute4_min: 既存のギャザリングに参加する対象とする属性値4の最小値
        :type search_attribute4_min: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute4_min(search_attribute4_min)
        return self

    def get_attribute3(self):
        """
        ギャザリングを新規作成する場合の属性値3を取得
        :return: ギャザリングを新規作成する場合の属性値3
        :rtype: int
        """
        return self.__attribute3

    def set_attribute3(self, attribute3):
        """
        ギャザリングを新規作成する場合の属性値3を設定
        :param attribute3: ギャザリングを新規作成する場合の属性値3
        :type attribute3: int
        """
        if not isinstance(attribute3, int):
            raise TypeError(type(attribute3))
        self.__attribute3 = attribute3

    def with_attribute3(self, attribute3):
        """
        ギャザリングを新規作成する場合の属性値3を設定
        :param attribute3: ギャザリングを新規作成する場合の属性値3
        :type attribute3: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_attribute3(attribute3)
        return self

    def get_search_attribute3_max(self):
        """
        既存のギャザリングに参加する対象とする属性値3の最大値を取得
        :return: 既存のギャザリングに参加する対象とする属性値3の最大値
        :rtype: int
        """
        return self.__search_attribute3_max

    def set_search_attribute3_max(self, search_attribute3_max):
        """
        既存のギャザリングに参加する対象とする属性値3の最大値を設定
        :param search_attribute3_max: 既存のギャザリングに参加する対象とする属性値3の最大値
        :type search_attribute3_max: int
        """
        if not isinstance(search_attribute3_max, int):
            raise TypeError(type(search_attribute3_max))
        self.__search_attribute3_max = search_attribute3_max

    def with_search_attribute3_max(self, search_attribute3_max):
        """
        既存のギャザリングに参加する対象とする属性値3の最大値を設定
        :param search_attribute3_max: 既存のギャザリングに参加する対象とする属性値3の最大値
        :type search_attribute3_max: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute3_max(search_attribute3_max)
        return self

    def get_search_attribute4_max(self):
        """
        既存のギャザリングに参加する対象とする属性値4の最大値を取得
        :return: 既存のギャザリングに参加する対象とする属性値4の最大値
        :rtype: int
        """
        return self.__search_attribute4_max

    def set_search_attribute4_max(self, search_attribute4_max):
        """
        既存のギャザリングに参加する対象とする属性値4の最大値を設定
        :param search_attribute4_max: 既存のギャザリングに参加する対象とする属性値4の最大値
        :type search_attribute4_max: int
        """
        if not isinstance(search_attribute4_max, int):
            raise TypeError(type(search_attribute4_max))
        self.__search_attribute4_max = search_attribute4_max

    def with_search_attribute4_max(self, search_attribute4_max):
        """
        既存のギャザリングに参加する対象とする属性値4の最大値を設定
        :param search_attribute4_max: 既存のギャザリングに参加する対象とする属性値4の最大値
        :type search_attribute4_max: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute4_max(search_attribute4_max)
        return self

    def get_search_attribute1_max(self):
        """
        既存のギャザリングに参加する対象とする属性値1の最大値を取得
        :return: 既存のギャザリングに参加する対象とする属性値1の最大値
        :rtype: int
        """
        return self.__search_attribute1_max

    def set_search_attribute1_max(self, search_attribute1_max):
        """
        既存のギャザリングに参加する対象とする属性値1の最大値を設定
        :param search_attribute1_max: 既存のギャザリングに参加する対象とする属性値1の最大値
        :type search_attribute1_max: int
        """
        if not isinstance(search_attribute1_max, int):
            raise TypeError(type(search_attribute1_max))
        self.__search_attribute1_max = search_attribute1_max

    def with_search_attribute1_max(self, search_attribute1_max):
        """
        既存のギャザリングに参加する対象とする属性値1の最大値を設定
        :param search_attribute1_max: 既存のギャザリングに参加する対象とする属性値1の最大値
        :type search_attribute1_max: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute1_max(search_attribute1_max)
        return self

    def get_search_context(self):
        """
        中断された検索を再開するためのコンテキストを取得
        :return: 中断された検索を再開するためのコンテキスト
        :rtype: unicode
        """
        return self.__search_context

    def set_search_context(self, search_context):
        """
        中断された検索を再開するためのコンテキストを設定
        :param search_context: 中断された検索を再開するためのコンテキスト
        :type search_context: unicode
        """
        if not isinstance(search_context, unicode):
            raise TypeError(type(search_context))
        self.__search_context = search_context

    def with_search_context(self, search_context):
        """
        中断された検索を再開するためのコンテキストを設定
        :param search_context: 中断された検索を再開するためのコンテキスト
        :type search_context: unicode
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_context(search_context)
        return self

    def get_search_attribute5_max(self):
        """
        既存のギャザリングに参加する対象とする属性値5の最大値を取得
        :return: 既存のギャザリングに参加する対象とする属性値5の最大値
        :rtype: int
        """
        return self.__search_attribute5_max

    def set_search_attribute5_max(self, search_attribute5_max):
        """
        既存のギャザリングに参加する対象とする属性値5の最大値を設定
        :param search_attribute5_max: 既存のギャザリングに参加する対象とする属性値5の最大値
        :type search_attribute5_max: int
        """
        if not isinstance(search_attribute5_max, int):
            raise TypeError(type(search_attribute5_max))
        self.__search_attribute5_max = search_attribute5_max

    def with_search_attribute5_max(self, search_attribute5_max):
        """
        既存のギャザリングに参加する対象とする属性値5の最大値を設定
        :param search_attribute5_max: 既存のギャザリングに参加する対象とする属性値5の最大値
        :type search_attribute5_max: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute5_max(search_attribute5_max)
        return self

    def get_search_attribute3_min(self):
        """
        既存のギャザリングに参加する対象とする属性値3の最小値を取得
        :return: 既存のギャザリングに参加する対象とする属性値3の最小値
        :rtype: int
        """
        return self.__search_attribute3_min

    def set_search_attribute3_min(self, search_attribute3_min):
        """
        既存のギャザリングに参加する対象とする属性値3の最小値を設定
        :param search_attribute3_min: 既存のギャザリングに参加する対象とする属性値3の最小値
        :type search_attribute3_min: int
        """
        if not isinstance(search_attribute3_min, int):
            raise TypeError(type(search_attribute3_min))
        self.__search_attribute3_min = search_attribute3_min

    def with_search_attribute3_min(self, search_attribute3_min):
        """
        既存のギャザリングに参加する対象とする属性値3の最小値を設定
        :param search_attribute3_min: 既存のギャザリングに参加する対象とする属性値3の最小値
        :type search_attribute3_min: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute3_min(search_attribute3_min)
        return self

    def get_attribute2(self):
        """
        ギャザリングを新規作成する場合の属性値2を取得
        :return: ギャザリングを新規作成する場合の属性値2
        :rtype: int
        """
        return self.__attribute2

    def set_attribute2(self, attribute2):
        """
        ギャザリングを新規作成する場合の属性値2を設定
        :param attribute2: ギャザリングを新規作成する場合の属性値2
        :type attribute2: int
        """
        if not isinstance(attribute2, int):
            raise TypeError(type(attribute2))
        self.__attribute2 = attribute2

    def with_attribute2(self, attribute2):
        """
        ギャザリングを新規作成する場合の属性値2を設定
        :param attribute2: ギャザリングを新規作成する場合の属性値2
        :type attribute2: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_attribute2(attribute2)
        return self

    def get_search_attribute2_min(self):
        """
        既存のギャザリングに参加する対象とする属性値2の最小値を取得
        :return: 既存のギャザリングに参加する対象とする属性値2の最小値
        :rtype: int
        """
        return self.__search_attribute2_min

    def set_search_attribute2_min(self, search_attribute2_min):
        """
        既存のギャザリングに参加する対象とする属性値2の最小値を設定
        :param search_attribute2_min: 既存のギャザリングに参加する対象とする属性値2の最小値
        :type search_attribute2_min: int
        """
        if not isinstance(search_attribute2_min, int):
            raise TypeError(type(search_attribute2_min))
        self.__search_attribute2_min = search_attribute2_min

    def with_search_attribute2_min(self, search_attribute2_min):
        """
        既存のギャザリングに参加する対象とする属性値2の最小値を設定
        :param search_attribute2_min: 既存のギャザリングに参加する対象とする属性値2の最小値
        :type search_attribute2_min: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_search_attribute2_min(search_attribute2_min)
        return self

    def get_attribute1(self):
        """
        ギャザリングを新規作成する場合の属性値1を取得
        :return: ギャザリングを新規作成する場合の属性値1
        :rtype: int
        """
        return self.__attribute1

    def set_attribute1(self, attribute1):
        """
        ギャザリングを新規作成する場合の属性値1を設定
        :param attribute1: ギャザリングを新規作成する場合の属性値1
        :type attribute1: int
        """
        if not isinstance(attribute1, int):
            raise TypeError(type(attribute1))
        self.__attribute1 = attribute1

    def with_attribute1(self, attribute1):
        """
        ギャザリングを新規作成する場合の属性値1を設定
        :param attribute1: ギャザリングを新規作成する場合の属性値1
        :type attribute1: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_attribute1(attribute1)
        return self

    def get_attribute4(self):
        """
        ギャザリングを新規作成する場合の属性値4を取得
        :return: ギャザリングを新規作成する場合の属性値4
        :rtype: int
        """
        return self.__attribute4

    def set_attribute4(self, attribute4):
        """
        ギャザリングを新規作成する場合の属性値4を設定
        :param attribute4: ギャザリングを新規作成する場合の属性値4
        :type attribute4: int
        """
        if not isinstance(attribute4, int):
            raise TypeError(type(attribute4))
        self.__attribute4 = attribute4

    def with_attribute4(self, attribute4):
        """
        ギャザリングを新規作成する場合の属性値4を設定
        :param attribute4: ギャザリングを新規作成する場合の属性値4
        :type attribute4: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_attribute4(attribute4)
        return self

    def get_attribute5(self):
        """
        ギャザリングを新規作成する場合の属性値5を取得
        :return: ギャザリングを新規作成する場合の属性値5
        :rtype: int
        """
        return self.__attribute5

    def set_attribute5(self, attribute5):
        """
        ギャザリングを新規作成する場合の属性値5を設定
        :param attribute5: ギャザリングを新規作成する場合の属性値5
        :type attribute5: int
        """
        if not isinstance(attribute5, int):
            raise TypeError(type(attribute5))
        self.__attribute5 = attribute5

    def with_attribute5(self, attribute5):
        """
        ギャザリングを新規作成する場合の属性値5を設定
        :param attribute5: ギャザリングを新規作成する場合の属性値5
        :type attribute5: int
        :return: this
        :rtype: CustomAutoDoMatchmakingRequest
        """
        self.set_attribute5(attribute5)
        return self
