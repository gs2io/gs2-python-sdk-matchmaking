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


class CreateMatchmakingRequest(Gs2BasicRequest):

    class Constant(Gs2Matchmaking):
        FUNCTION = "CreateMatchmaking"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateMatchmakingRequest, self).__init__(params)
        if params is None:
            self.__name = None
            self.__service_class = None
            self.__gathering_pool_name = None
            self.__callback = None
            self.__max_player = None
            self.__notification_game_name = None
            self.__type = None
            self.__description = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
            self.set_callback(params['callback'] if 'callback' in params.keys() else None)
            self.set_max_player(params['maxPlayer'] if 'maxPlayer' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_name(self):
        """
        マッチメイキングの名前を取得
        :return: マッチメイキングの名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        マッチメイキングの名前を設定
        :param name: マッチメイキングの名前
        :type name: unicode
        """
        if not isinstance(name, unicode):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        マッチメイキングの名前を設定
        :param name: マッチメイキングの名前
        :type name: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_name(name)
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
        :rtype: CreateMatchmakingRequest
        """
        self.set_service_class(service_class)
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
        :rtype: CreateMatchmakingRequest
        """
        self.set_gathering_pool_name(gathering_pool_name)
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
        :rtype: CreateMatchmakingRequest
        """
        self.set_callback(callback)
        return self

    def get_max_player(self):
        """
        最大プレイヤー数を取得
        :return: 最大プレイヤー数
        :rtype: int
        """
        return self.__max_player

    def set_max_player(self, max_player):
        """
        最大プレイヤー数を設定
        :param max_player: 最大プレイヤー数
        :type max_player: int
        """
        if not isinstance(max_player, int):
            raise TypeError(type(max_player))
        self.__max_player = max_player

    def with_max_player(self, max_player):
        """
        最大プレイヤー数を設定
        :param max_player: 最大プレイヤー数
        :type max_player: int
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_max_player(max_player)
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
        :rtype: CreateMatchmakingRequest
        """
        self.set_notification_game_name(notification_game_name)
        return self

    def get_type(self):
        """
        マッチメイキングの種類を取得
        :return: マッチメイキングの種類
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type):
        """
        マッチメイキングの種類を設定
        :param type: マッチメイキングの種類
        :type type: unicode
        """
        if not isinstance(type, unicode):
            raise TypeError(type(type))
        self.__type = type

    def with_type(self, type):
        """
        マッチメイキングの種類を設定
        :param type: マッチメイキングの種類
        :type type: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_type(type)
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
        :rtype: CreateMatchmakingRequest
        """
        self.set_description(description)
        return self
