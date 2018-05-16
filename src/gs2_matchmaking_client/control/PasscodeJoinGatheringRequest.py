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


class PasscodeJoinGatheringRequest(Gs2UserRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "JoinGathering"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(PasscodeJoinGatheringRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__passcode = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_passcode(params['passcode'] if 'passcode' in params.keys() else None)

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
        if matchmaking_name and not (isinstance(matchmaking_name, str) or isinstance(matchmaking_name, unicode)):
            raise TypeError(type(matchmaking_name))
        self.__matchmaking_name = matchmaking_name

    def with_matchmaking_name(self, matchmaking_name):
        """
        マッチメイキングの名前を指定します。を設定
        :param matchmaking_name: マッチメイキングの名前を指定します。
        :type matchmaking_name: unicode
        :return: this
        :rtype: PasscodeJoinGatheringRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_passcode(self):
        """
        ギャザリングのパスコードを指定します。を取得
        :return: ギャザリングのパスコードを指定します。
        :rtype: unicode
        """
        return self.__passcode

    def set_passcode(self, passcode):
        """
        ギャザリングのパスコードを指定します。を設定
        :param passcode: ギャザリングのパスコードを指定します。
        :type passcode: unicode
        """
        if passcode and not (isinstance(passcode, str) or isinstance(passcode, unicode)):
            raise TypeError(type(passcode))
        self.__passcode = passcode

    def with_passcode(self, passcode):
        """
        ギャザリングのパスコードを指定します。を設定
        :param passcode: ギャザリングのパスコードを指定します。
        :type passcode: unicode
        :return: this
        :rtype: PasscodeJoinGatheringRequest
        """
        self.set_passcode(passcode)
        return self
