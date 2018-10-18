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
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__type = None
        else:
            self.set_type(params['type'] if 'type' in params.keys() else None)
        if params is None:
            self.__max_player = None
        else:
            self.set_max_player(params['maxPlayer'] if 'maxPlayer' in params.keys() else None)
        if params is None:
            self.__gathering_pool_name = None
        else:
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
        if params is None:
            self.__callback = None
        else:
            self.set_callback(params['callback'] if 'callback' in params.keys() else None)
        if params is None:
            self.__notification_game_name = None
        else:
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
        if params is None:
            self.__create_gathering_trigger_script = None
        else:
            self.set_create_gathering_trigger_script(params['createGatheringTriggerScript'] if 'createGatheringTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_gathering_done_trigger_script = None
        else:
            self.set_create_gathering_done_trigger_script(params['createGatheringDoneTriggerScript'] if 'createGatheringDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__join_gathering_trigger_script = None
        else:
            self.set_join_gathering_trigger_script(params['joinGatheringTriggerScript'] if 'joinGatheringTriggerScript' in params.keys() else None)
        if params is None:
            self.__join_gathering_done_trigger_script = None
        else:
            self.set_join_gathering_done_trigger_script(params['joinGatheringDoneTriggerScript'] if 'joinGatheringDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__leave_gathering_trigger_script = None
        else:
            self.set_leave_gathering_trigger_script(params['leaveGatheringTriggerScript'] if 'leaveGatheringTriggerScript' in params.keys() else None)
        if params is None:
            self.__leave_gathering_done_trigger_script = None
        else:
            self.set_leave_gathering_done_trigger_script(params['leaveGatheringDoneTriggerScript'] if 'leaveGatheringDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__breakup_gathering_trigger_script = None
        else:
            self.set_breakup_gathering_trigger_script(params['breakupGatheringTriggerScript'] if 'breakupGatheringTriggerScript' in params.keys() else None)
        if params is None:
            self.__matchmaking_complete_trigger_script = None
        else:
            self.set_matchmaking_complete_trigger_script(params['matchmakingCompleteTriggerScript'] if 'matchmakingCompleteTriggerScript' in params.keys() else None)

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
        if name is not None and not (isinstance(name, str) or isinstance(name, unicode)):
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
        if description is not None and not (isinstance(description, str) or isinstance(description, unicode)):
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
        if service_class is not None and not (isinstance(service_class, str) or isinstance(service_class, unicode)):
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
        if max_player is not None and not isinstance(max_player, int):
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
        if gathering_pool_name is not None and not (isinstance(gathering_pool_name, str) or isinstance(gathering_pool_name, unicode)):
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
        if callback is not None and not (isinstance(callback, str) or isinstance(callback, unicode)):
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
        if notification_game_name is not None and not (isinstance(notification_game_name, str) or isinstance(notification_game_name, unicode)):
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
        if create_gathering_trigger_script is not None and not (isinstance(create_gathering_trigger_script, str) or isinstance(create_gathering_trigger_script, unicode)):
            raise TypeError(type(create_gathering_trigger_script))
        self.__create_gathering_trigger_script = create_gathering_trigger_script

    def with_create_gathering_trigger_script(self, create_gathering_trigger_script):
        """
        ギャザリング作成時 に実行されるGS2-Scriptを設定
        :param create_gathering_trigger_script: ギャザリング作成時 に実行されるGS2-Script
        :type create_gathering_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_create_gathering_trigger_script(create_gathering_trigger_script)
        return self

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
        if create_gathering_done_trigger_script is not None and not (isinstance(create_gathering_done_trigger_script, str) or isinstance(create_gathering_done_trigger_script, unicode)):
            raise TypeError(type(create_gathering_done_trigger_script))
        self.__create_gathering_done_trigger_script = create_gathering_done_trigger_script

    def with_create_gathering_done_trigger_script(self, create_gathering_done_trigger_script):
        """
        ギャザリング作成完了時 に実行されるGS2-Scriptを設定
        :param create_gathering_done_trigger_script: ギャザリング作成完了時 に実行されるGS2-Script
        :type create_gathering_done_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_create_gathering_done_trigger_script(create_gathering_done_trigger_script)
        return self

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
        if join_gathering_trigger_script is not None and not (isinstance(join_gathering_trigger_script, str) or isinstance(join_gathering_trigger_script, unicode)):
            raise TypeError(type(join_gathering_trigger_script))
        self.__join_gathering_trigger_script = join_gathering_trigger_script

    def with_join_gathering_trigger_script(self, join_gathering_trigger_script):
        """
        ギャザリング参加時 に実行されるGS2-Scriptを設定
        :param join_gathering_trigger_script: ギャザリング参加時 に実行されるGS2-Script
        :type join_gathering_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_join_gathering_trigger_script(join_gathering_trigger_script)
        return self

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
        if join_gathering_done_trigger_script is not None and not (isinstance(join_gathering_done_trigger_script, str) or isinstance(join_gathering_done_trigger_script, unicode)):
            raise TypeError(type(join_gathering_done_trigger_script))
        self.__join_gathering_done_trigger_script = join_gathering_done_trigger_script

    def with_join_gathering_done_trigger_script(self, join_gathering_done_trigger_script):
        """
        ギャザリング参加完了時 に実行されるGS2-Scriptを設定
        :param join_gathering_done_trigger_script: ギャザリング参加完了時 に実行されるGS2-Script
        :type join_gathering_done_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_join_gathering_done_trigger_script(join_gathering_done_trigger_script)
        return self

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
        if leave_gathering_trigger_script is not None and not (isinstance(leave_gathering_trigger_script, str) or isinstance(leave_gathering_trigger_script, unicode)):
            raise TypeError(type(leave_gathering_trigger_script))
        self.__leave_gathering_trigger_script = leave_gathering_trigger_script

    def with_leave_gathering_trigger_script(self, leave_gathering_trigger_script):
        """
        ギャザリング離脱時 に実行されるGS2-Scriptを設定
        :param leave_gathering_trigger_script: ギャザリング離脱時 に実行されるGS2-Script
        :type leave_gathering_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_leave_gathering_trigger_script(leave_gathering_trigger_script)
        return self

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
        if leave_gathering_done_trigger_script is not None and not (isinstance(leave_gathering_done_trigger_script, str) or isinstance(leave_gathering_done_trigger_script, unicode)):
            raise TypeError(type(leave_gathering_done_trigger_script))
        self.__leave_gathering_done_trigger_script = leave_gathering_done_trigger_script

    def with_leave_gathering_done_trigger_script(self, leave_gathering_done_trigger_script):
        """
        ギャザリング離脱完了時 に実行されるGS2-Scriptを設定
        :param leave_gathering_done_trigger_script: ギャザリング離脱完了時 に実行されるGS2-Script
        :type leave_gathering_done_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_leave_gathering_done_trigger_script(leave_gathering_done_trigger_script)
        return self

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
        if breakup_gathering_trigger_script is not None and not (isinstance(breakup_gathering_trigger_script, str) or isinstance(breakup_gathering_trigger_script, unicode)):
            raise TypeError(type(breakup_gathering_trigger_script))
        self.__breakup_gathering_trigger_script = breakup_gathering_trigger_script

    def with_breakup_gathering_trigger_script(self, breakup_gathering_trigger_script):
        """
        ギャザリング解散時 に実行されるGS2-Scriptを設定
        :param breakup_gathering_trigger_script: ギャザリング解散時 に実行されるGS2-Script
        :type breakup_gathering_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_breakup_gathering_trigger_script(breakup_gathering_trigger_script)
        return self

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
        if matchmaking_complete_trigger_script is not None and not (isinstance(matchmaking_complete_trigger_script, str) or isinstance(matchmaking_complete_trigger_script, unicode)):
            raise TypeError(type(matchmaking_complete_trigger_script))
        self.__matchmaking_complete_trigger_script = matchmaking_complete_trigger_script

    def with_matchmaking_complete_trigger_script(self, matchmaking_complete_trigger_script):
        """
        マッチメイキング成立時 に実行されるGS2-Scriptを設定
        :param matchmaking_complete_trigger_script: マッチメイキング成立時 に実行されるGS2-Script
        :type matchmaking_complete_trigger_script: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_matchmaking_complete_trigger_script(matchmaking_complete_trigger_script)
        return self

    def get_type(self):
        """
        マッチメイキングの種類を取得
        :return: マッチメイキングの種類
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type_):
        """
        マッチメイキングの種類を設定
        :param type_: マッチメイキングの種類
        :type type_: unicode
        """
        if type_ is not None and not (isinstance(type_, str) or isinstance(type_, unicode)):
            raise TypeError(type(type_))
        self.__type = type_

    def with_type(self, type_):
        """
        マッチメイキングの種類を設定
        :param type_: マッチメイキングの種類
        :type type_: unicode
        :return: this
        :rtype: CreateMatchmakingRequest
        """
        self.set_type(type_)
        return self
