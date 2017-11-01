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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_matchmaking_client.Gs2Matchmaking import Gs2Matchmaking


class UpdateMatchmakingRequest(Gs2BasicRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "UpdateMatchmaking"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateMatchmakingRequest, self).__init__(params)
        if params is None:
            self.__matchmaking_name = None
            self.__callback = None
            self.__service_class = None
            self.__description = None
            self.__notification_game_name = None
            self.__gathering_pool_name = None
        else:
            self.set_matchmaking_name(params['matchmakingName'] if 'matchmakingName' in params.keys() else None)
            self.set_callback(params['callback'] if 'callback' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)

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
        :rtype: UpdateMatchmakingRequest
        """
        self.set_matchmaking_name(matchmaking_name)
        return self

    def get_callback(self):
        """
        マッチメイキング完了コールバックURLを取得
        :return: マッチメイキング完了コールバックURL
        :rtype: unicode
        """
        return self.__callback

    def set_callback(self, callback):
        """
        マッチメイキング完了コールバックURLを設定
        :param callback: マッチメイキング完了コールバックURL
        :type callback: unicode
        """
        if not isinstance(callback, unicode):
            raise TypeError(type(callback))
        self.__callback = callback

    def with_callback(self, callback):
        """
        マッチメイキング完了コールバックURLを設定
        :param callback: マッチメイキング完了コールバックURL
        :type callback: unicode
        :return: this
        :rtype: UpdateMatchmakingRequest
        """
        self.set_callback(callback)
        return self

    def get_service_class(self):
        """
        マッチメイキングのサービスクラスを取得
        :return: マッチメイキングのサービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        マッチメイキングのサービスクラスを設定
        :param service_class: マッチメイキングのサービスクラス
        :type service_class: unicode
        """
        if not isinstance(service_class, unicode):
            raise TypeError(type(service_class))
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        マッチメイキングのサービスクラスを設定
        :param service_class: マッチメイキングのサービスクラス
        :type service_class: unicode
        :return: this
        :rtype: UpdateMatchmakingRequest
        """
        self.set_service_class(service_class)
        return self

    def get_description(self):
        """
        マッチメイキングの説明を取得
        :return: マッチメイキングの説明
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        マッチメイキングの説明を設定
        :param description: マッチメイキングの説明
        :type description: unicode
        """
        if not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        マッチメイキングの説明を設定
        :param description: マッチメイキングの説明
        :type description: unicode
        :return: this
        :rtype: UpdateMatchmakingRequest
        """
        self.set_description(description)
        return self

    def get_notification_game_name(self):
        """
        GS2-InGamePushNotification のゲーム名を取得
        :return: GS2-InGamePushNotification のゲーム名
        :rtype: unicode
        """
        return self.__notification_game_name

    def set_notification_game_name(self, notification_game_name):
        """
        GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        """
        if not isinstance(notification_game_name, unicode):
            raise TypeError(type(notification_game_name))
        self.__notification_game_name = notification_game_name

    def with_notification_game_name(self, notification_game_name):
        """
        GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        :return: this
        :rtype: UpdateMatchmakingRequest
        """
        self.set_notification_game_name(notification_game_name)
        return self

    def get_gathering_pool_name(self):
        """
        GS2-Realtime のギャザリングプール名を取得
        :return: GS2-Realtime のギャザリングプール名
        :rtype: unicode
        """
        return self.__gathering_pool_name

    def set_gathering_pool_name(self, gathering_pool_name):
        """
        GS2-Realtime のギャザリングプール名を設定
        :param gathering_pool_name: GS2-Realtime のギャザリングプール名
        :type gathering_pool_name: unicode
        """
        if not isinstance(gathering_pool_name, unicode):
            raise TypeError(type(gathering_pool_name))
        self.__gathering_pool_name = gathering_pool_name

    def with_gathering_pool_name(self, gathering_pool_name):
        """
        GS2-Realtime のギャザリングプール名を設定
        :param gathering_pool_name: GS2-Realtime のギャザリングプール名
        :type gathering_pool_name: unicode
        :return: this
        :rtype: UpdateMatchmakingRequest
        """
        self.set_gathering_pool_name(gathering_pool_name)
        return self
