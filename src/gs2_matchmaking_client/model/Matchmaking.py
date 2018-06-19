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
            self.__matchmaking_id = None
            self.__owner_id = None
            self.__name = None
            self.__type = None
            self.__description = None
            self.__service_class = None
            self.__max_player = None
            self.__callback = None
            self.__gathering_pool_name = None
            self.__notification_game_name = None
            self.__create_gathering_trigger_script = None
            self.__create_gathering_done_trigger_script = None
            self.__join_gathering_trigger_script = None
            self.__join_gathering_done_trigger_script = None
            self.__leave_gathering_trigger_script = None
            self.__leave_gathering_done_trigger_script = None
            self.__breakup_gathering_trigger_script = None
            self.__matchmaking_complete_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_matchmaking_id(params['matchmakingId'] if 'matchmakingId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_max_player(params['maxPlayer'] if 'maxPlayer' in params.keys() else None)
            self.set_callback(params['callback'] if 'callback' in params.keys() else None)
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_create_gathering_trigger_script(params['createGatheringTriggerScript'] if 'createGatheringTriggerScript' in params.keys() else None)
            self.set_create_gathering_done_trigger_script(params['createGatheringDoneTriggerScript'] if 'createGatheringDoneTriggerScript' in params.keys() else None)
            self.set_join_gathering_trigger_script(params['joinGatheringTriggerScript'] if 'joinGatheringTriggerScript' in params.keys() else None)
            self.set_join_gathering_done_trigger_script(params['joinGatheringDoneTriggerScript'] if 'joinGatheringDoneTriggerScript' in params.keys() else None)
            self.set_leave_gathering_trigger_script(params['leaveGatheringTriggerScript'] if 'leaveGatheringTriggerScript' in params.keys() else None)
            self.set_leave_gathering_done_trigger_script(params['leaveGatheringDoneTriggerScript'] if 'leaveGatheringDoneTriggerScript' in params.keys() else None)
            self.set_breakup_gathering_trigger_script(params['breakupGatheringTriggerScript'] if 'breakupGatheringTriggerScript' in params.keys() else None)
            self.set_matchmaking_complete_trigger_script(params['matchmakingCompleteTriggerScript'] if 'matchmakingCompleteTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

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

    def get_create_gathering_trigger_script(self):
        """
        ギャザリング作成時 に実行されるGS2-Scriptを取得
        :return: ギャザリング作成時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_gathering_trigger_script

    def set_create_gathering_trigger_script(self, create_gathering_trigger_script):
        """
        ギャザリング作成時 に実行されるGS2-Scriptを設定
        :param create_gathering_trigger_script: ギャザリング作成時 に実行されるGS2-Script
        :type create_gathering_trigger_script: unicode
        """
        self.__create_gathering_trigger_script = create_gathering_trigger_script

    def get_create_gathering_done_trigger_script(self):
        """
        ギャザリング作成完了時 に実行されるGS2-Scriptを取得
        :return: ギャザリング作成完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_gathering_done_trigger_script

    def set_create_gathering_done_trigger_script(self, create_gathering_done_trigger_script):
        """
        ギャザリング作成完了時 に実行されるGS2-Scriptを設定
        :param create_gathering_done_trigger_script: ギャザリング作成完了時 に実行されるGS2-Script
        :type create_gathering_done_trigger_script: unicode
        """
        self.__create_gathering_done_trigger_script = create_gathering_done_trigger_script

    def get_join_gathering_trigger_script(self):
        """
        ギャザリング参加時 に実行されるGS2-Scriptを取得
        :return: ギャザリング参加時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__join_gathering_trigger_script

    def set_join_gathering_trigger_script(self, join_gathering_trigger_script):
        """
        ギャザリング参加時 に実行されるGS2-Scriptを設定
        :param join_gathering_trigger_script: ギャザリング参加時 に実行されるGS2-Script
        :type join_gathering_trigger_script: unicode
        """
        self.__join_gathering_trigger_script = join_gathering_trigger_script

    def get_join_gathering_done_trigger_script(self):
        """
        ギャザリング参加完了時 に実行されるGS2-Scriptを取得
        :return: ギャザリング参加完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__join_gathering_done_trigger_script

    def set_join_gathering_done_trigger_script(self, join_gathering_done_trigger_script):
        """
        ギャザリング参加完了時 に実行されるGS2-Scriptを設定
        :param join_gathering_done_trigger_script: ギャザリング参加完了時 に実行されるGS2-Script
        :type join_gathering_done_trigger_script: unicode
        """
        self.__join_gathering_done_trigger_script = join_gathering_done_trigger_script

    def get_leave_gathering_trigger_script(self):
        """
        ギャザリング離脱時 に実行されるGS2-Scriptを取得
        :return: ギャザリング離脱時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__leave_gathering_trigger_script

    def set_leave_gathering_trigger_script(self, leave_gathering_trigger_script):
        """
        ギャザリング離脱時 に実行されるGS2-Scriptを設定
        :param leave_gathering_trigger_script: ギャザリング離脱時 に実行されるGS2-Script
        :type leave_gathering_trigger_script: unicode
        """
        self.__leave_gathering_trigger_script = leave_gathering_trigger_script

    def get_leave_gathering_done_trigger_script(self):
        """
        ギャザリング離脱完了時 に実行されるGS2-Scriptを取得
        :return: ギャザリング離脱完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__leave_gathering_done_trigger_script

    def set_leave_gathering_done_trigger_script(self, leave_gathering_done_trigger_script):
        """
        ギャザリング離脱完了時 に実行されるGS2-Scriptを設定
        :param leave_gathering_done_trigger_script: ギャザリング離脱完了時 に実行されるGS2-Script
        :type leave_gathering_done_trigger_script: unicode
        """
        self.__leave_gathering_done_trigger_script = leave_gathering_done_trigger_script

    def get_breakup_gathering_trigger_script(self):
        """
        ギャザリング解散時 に実行されるGS2-Scriptを取得
        :return: ギャザリング解散時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__breakup_gathering_trigger_script

    def set_breakup_gathering_trigger_script(self, breakup_gathering_trigger_script):
        """
        ギャザリング解散時 に実行されるGS2-Scriptを設定
        :param breakup_gathering_trigger_script: ギャザリング解散時 に実行されるGS2-Script
        :type breakup_gathering_trigger_script: unicode
        """
        self.__breakup_gathering_trigger_script = breakup_gathering_trigger_script

    def get_matchmaking_complete_trigger_script(self):
        """
        マッチメイキング成立時 に実行されるGS2-Scriptを取得
        :return: マッチメイキング成立時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__matchmaking_complete_trigger_script

    def set_matchmaking_complete_trigger_script(self, matchmaking_complete_trigger_script):
        """
        マッチメイキング成立時 に実行されるGS2-Scriptを設定
        :param matchmaking_complete_trigger_script: マッチメイキング成立時 に実行されるGS2-Script
        :type matchmaking_complete_trigger_script: unicode
        """
        self.__matchmaking_complete_trigger_script = matchmaking_complete_trigger_script

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

    def get_type(self):
        """
        マッチメイキング方式を取得
        :return: マッチメイキング方式
        :rtype: unicode
        """
        return self.__type

    def set_type(self, _type):
        """
        マッチメイキング方式を設定
        :param _type: マッチメイキング方式
        :type _type: unicode
        """
        self.__type = _type

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Matchmaking, self).__getitem__(key)

    def to_dict(self):
        return {
            "matchmakingId": self.__matchmaking_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "type": self.__type,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "maxPlayer": self.__max_player,
            "callback": self.__callback,
            "gatheringPoolName": self.__gathering_pool_name,
            "notificationGameName": self.__notification_game_name,
            "createGatheringTriggerScript": self.__create_gathering_trigger_script,
            "createGatheringDoneTriggerScript": self.__create_gathering_done_trigger_script,
            "joinGatheringTriggerScript": self.__join_gathering_trigger_script,
            "joinGatheringDoneTriggerScript": self.__join_gathering_done_trigger_script,
            "leaveGatheringTriggerScript": self.__leave_gathering_trigger_script,
            "leaveGatheringDoneTriggerScript": self.__leave_gathering_done_trigger_script,
            "breakupGatheringTriggerScript": self.__breakup_gathering_trigger_script,
            "matchmakingCompleteTriggerScript": self.__matchmaking_complete_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
