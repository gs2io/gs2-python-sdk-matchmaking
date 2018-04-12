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


class RoomGathering(object):

    def __init__(self, params=None):
        if params is None:
            self.__gathering_id = None
            self.__owner_user_id = None
            self.__meta = None
            self.__join_player = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_gathering_id(params['gatheringId'] if 'gatheringId' in params.keys() else None)
            self.set_owner_user_id(params['ownerUserId'] if 'ownerUserId' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_join_player(params['joinPlayer'] if 'joinPlayer' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_gathering_id(self):
        """
        ギャザリングIDを取得
        :return: ギャザリングID
        :rtype: unicode
        """
        return self.__gathering_id

    def set_gathering_id(self, gathering_id):
        """
        ギャザリングIDを設定
        :param gathering_id: ギャザリングID
        :type gathering_id: unicode
        """
        self.__gathering_id = gathering_id

    def get_owner_user_id(self):
        """
        ギャザリングを作成したユーザIDを取得
        :return: ギャザリングを作成したユーザID
        :rtype: unicode
        """
        return self.__owner_user_id

    def set_owner_user_id(self, owner_user_id):
        """
        ギャザリングを作成したユーザIDを設定
        :param owner_user_id: ギャザリングを作成したユーザID
        :type owner_user_id: unicode
        """
        self.__owner_user_id = owner_user_id

    def get_meta(self):
        """
        ギャザリングメタデータを取得
        :return: ギャザリングメタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        ギャザリングメタデータを設定
        :param meta: ギャザリングメタデータ
        :type meta: unicode
        """
        self.__meta = meta

    def get_join_player(self):
        """
        参加プレイヤー数を取得
        :return: 参加プレイヤー数
        :rtype: int
        """
        return self.__join_player

    def set_join_player(self, join_player):
        """
        参加プレイヤー数を設定
        :param join_player: 参加プレイヤー数
        :type join_player: int
        """
        self.__join_player = join_player

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
        更新日時(エポック秒)を取得
        :return: 更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        更新日時(エポック秒)を設定
        :param update_at: 更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return {
            "gatheringId": self.__gathering_id,
            "ownerUserId": self.__owner_user_id,
            "meta": self.__meta,
            "joinPlayer": self.__join_player,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
