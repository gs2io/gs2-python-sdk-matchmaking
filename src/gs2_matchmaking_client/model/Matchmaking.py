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

class Matchmaking(object):

    def __init__(self, params=None):
        if params is None:
            self.__name = None
            self.__type = None
            self.__matchmaking_id = None
            self.__service_class = None
            self.__gathering_pool_name = None
            self.__callback = None
            self.__create_at = None
            self.__max_player = None
            self.__notification_game_name = None
            self.__owner_id = None
            self.__update_at = None
            self.__description = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_matchmaking_id(params['matchmakingId'] if 'matchmakingId' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
            self.set_callback(params['callback'] if 'callback' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_max_player(params['maxPlayer'] if 'maxPlayer' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)


    def get_name(self):
        """
        マッチメイキング名を取得
        :return: マッチメイキング名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        マッチメイキング名を設定
        :param name: マッチメイキング名
        :type name: unicode
        """
        self.__name = name

    def get_type(self):
        """
        マッチメイキング方式を取得
        :return: マッチメイキング方式
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type):
        """
        マッチメイキング方式を設定
        :param type: マッチメイキング方式
        :type type: unicode
        """
        self.__type = type

    def get_matchmaking_id(self):
        """
        マッチメイキングGRNを取得
        :return: マッチメイキングGRN
        :rtype: unicode
        """
        return self.__matchmaking_id

    def set_matchmaking_id(self, matchmaking_id):
        """
        マッチメイキングGRNを設定
        :param matchmaking_id: マッチメイキングGRN
        :type matchmaking_id: unicode
        """
        self.__matchmaking_id = matchmaking_id

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_gathering_pool_name(self):
        """
        マッチメイキング完了時に GS2-Realtime と自動的に連携する場合に指定するギャザリングプール名を取得
        :return: マッチメイキング完了時に GS2-Realtime と自動的に連携する場合に指定するギャザリングプール名
        :rtype: unicode
        """
        return self.__gathering_pool_name

    def set_gathering_pool_name(self, gathering_pool_name):
        """
        マッチメイキング完了時に GS2-Realtime と自動的に連携する場合に指定するギャザリングプール名を設定
        :param gathering_pool_name: マッチメイキング完了時に GS2-Realtime と自動的に連携する場合に指定するギャザリングプール名
        :type gathering_pool_name: unicode
        """
        self.__gathering_pool_name = gathering_pool_name

    def get_callback(self):
        """
        マッチメイキング完了時の通知先URLを取得
        :return: マッチメイキング完了時の通知先URL
        :rtype: unicode
        """
        return self.__callback

    def set_callback(self, callback):
        """
        マッチメイキング完了時の通知先URLを設定
        :param callback: マッチメイキング完了時の通知先URL
        :type callback: unicode
        """
        self.__callback = callback

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

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
        self.__max_player = max_player

    def get_notification_game_name(self):
        """
        マッチメイキングの状態変化や完了通知を GS2-InGamePushNotification を使用して通知する場合に指定するゲーム名を取得
        :return: マッチメイキングの状態変化や完了通知を GS2-InGamePushNotification を使用して通知する場合に指定するゲーム名
        :rtype: unicode
        """
        return self.__notification_game_name

    def set_notification_game_name(self, notification_game_name):
        """
        マッチメイキングの状態変化や完了通知を GS2-InGamePushNotification を使用して通知する場合に指定するゲーム名を設定
        :param notification_game_name: マッチメイキングの状態変化や完了通知を GS2-InGamePushNotification を使用して通知する場合に指定するゲーム名
        :type notification_game_name: unicode
        """
        self.__notification_game_name = notification_game_name

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def to_dict(self):
        return { 
            "name": self.__name,
            "type": self.__type,
            "matchmakingId": self.__matchmaking_id,
            "serviceClass": self.__service_class,
            "gatheringPoolName": self.__gathering_pool_name,
            "callback": self.__callback,
            "createAt": self.__create_at,
            "maxPlayer": self.__max_player,
            "notificationGameName": self.__notification_game_name,
            "ownerId": self.__owner_id,
            "updateAt": self.__update_at,
            "description": self.__description,
        }