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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2MatchmakingClient(AbstractGs2Client):

    ENDPOINT = "matchmaking"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2MatchmakingClient, self).__init__(credential, region)

    def anybody_describe_joined_user(self, request):
        """
        ギャザリングの参加者一覧を取得します<br>
        <br>
        マッチメイキングが成立すると 404 Not Found 応答が返るようになります。<br>
        404応答を返すようになる直前にコールバックエンドポイントに確定した参加者一覧情報が渡されるため、<br>
        コールバックを受け取ってからは本APIを呼び出さないように実装するべきです。<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.AnybodyDescribeJoinedUserRequest.AnybodyDescribeJoinedUserRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.AnybodyDescribeJoinedUserResult.AnybodyDescribeJoinedUserResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.AnybodyDescribeJoinedUserRequest import AnybodyDescribeJoinedUserRequest

        from gs2_matchmaking_client.control.AnybodyDescribeJoinedUserResult import AnybodyDescribeJoinedUserResult
        return AnybodyDescribeJoinedUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/anybody/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=AnybodyDescribeJoinedUserRequest.Constant.MODULE,
            function=AnybodyDescribeJoinedUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def anybody_do_matchmaking(self, request):
        """
        Anybodyマッチメイキングを開始します<br>
        <br>
        すでに存在するギャザリングに参加するか、新しいギャザリングを新規作成します。<br>
        戻り値で参加したギャザリングIDが返りますので、そのIDを利用して後続のAPIを利用できます。<br>
        <br>
        ギャザリングが成立した場合、マッチメイキングに設定したコールバックエンドポイントにギャザリング<br>
        とそのギャザリングの参加者一覧が返されます。<br>
        コールバック後にギャザリング情報はマッチメイキングサーバから削除され、後続のAPIも利用できなくなります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.AnybodyDoMatchmakingRequest.AnybodyDoMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.AnybodyDoMatchmakingResult.AnybodyDoMatchmakingResult
        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.AnybodyDoMatchmakingRequest import AnybodyDoMatchmakingRequest

        from gs2_matchmaking_client.control.AnybodyDoMatchmakingResult import AnybodyDoMatchmakingResult
        return AnybodyDoMatchmakingResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/anybody",
            service=self.ENDPOINT,
            module=AnybodyDoMatchmakingRequest.Constant.MODULE,
            function=AnybodyDoMatchmakingRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def anybody_leave_gathering(self, request):
        """
        ギャザリングから離脱します<br>
        <br>
        本APIは確実に成功することを保証していません。<br>
        例えば、離脱する直前にギャザリングが成立した場合は 404 Not Found を応答します。<br>
        <br>
        404応答を受け取った場合はすでにギャザリングが成立していないかを確認する必要があります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.AnybodyLeaveGatheringRequest.AnybodyLeaveGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.AnybodyLeaveGatheringRequest import AnybodyLeaveGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/anybody/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=AnybodyLeaveGatheringRequest.Constant.MODULE,
            function=AnybodyLeaveGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )




    def create_matchmaking(self, request):
        """
        マッチメイキングを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.CreateMatchmakingRequest.CreateMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.CreateMatchmakingResult.CreateMatchmakingResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
            "callback": request.get_callback(),
            "maxPlayer": request.get_max_player(),
            "type": request.get_type(),
        }

        if request.get_gathering_pool_name() is not None:
            body["gatheringPoolName"] = request.get_gathering_pool_name()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_matchmaking_client.control.CreateMatchmakingRequest import CreateMatchmakingRequest

        from gs2_matchmaking_client.control.CreateMatchmakingResult import CreateMatchmakingResult
        return CreateMatchmakingResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking",
            service=self.ENDPOINT,
            module=CreateMatchmakingRequest.Constant.MODULE,
            function=CreateMatchmakingRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def custom_auto_describe_joined_user(self, request):
        """
        ギャザリングの参加者一覧を取得します<br>
        <br>
        マッチメイキングが成立すると 404 Not Found 応答が返るようになります。<br>
        404応答を返すようになる直前にコールバックエンドポイントに確定した参加者一覧情報が渡されるため、<br>
        コールバックを受け取ってからは本APIを呼び出さないように実装するべきです。<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.CustomAutoDescribeJoinedUserRequest.CustomAutoDescribeJoinedUserRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.CustomAutoDescribeJoinedUserResult.CustomAutoDescribeJoinedUserResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.CustomAutoDescribeJoinedUserRequest import CustomAutoDescribeJoinedUserRequest

        from gs2_matchmaking_client.control.CustomAutoDescribeJoinedUserResult import CustomAutoDescribeJoinedUserResult
        return CustomAutoDescribeJoinedUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/customauto/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=CustomAutoDescribeJoinedUserRequest.Constant.MODULE,
            function=CustomAutoDescribeJoinedUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def custom_auto_do_matchmaking(self, request):
        """
        カスタムオートマッチメイキングを開始します<br>
        <br>
        カスタムオートマッチメイキングは最大5つの属性値を指定してギャザリングを作成するか、<br>
        すでに存在するギャザリングの最大5つの属性値で、すべての属性値が指定した範囲内に収まっているギャザリングに参加します。<br>
        <br>
        ギャザリングへの参加が成功した場合は done に true が返ります。<br>
        done に true が返った場合は、同時に item に参加したギャザリングの情報が格納されています。<br>
        <br>
        done に false が返った場合は、一定時間内に存在するギャザリングの検索が完了しなかった場合に返ります。<br>
        この場合、searchContext に検索を継続するための情報が返ります。<br>
        引き続き検索を続けるために、再度APIを呼び出す際に引数に指定することで検索を再開することができます。<br>
        <br>
        すべてのギャザリングを検索したが、条件にマッチするものがなかった場合、新しいギャザリングを作成し done に true が返ります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.CustomAutoDoMatchmakingRequest.CustomAutoDoMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.CustomAutoDoMatchmakingResult.CustomAutoDoMatchmakingResult
        """
        body = { 
            "searchAttribute1Min": request.get_search_attribute1_min(),
            "searchAttribute1Max": request.get_search_attribute1_max(),
            "attribute1": request.get_attribute1(),
        }

        if request.get_search_attribute2_max() is not None:
            body["searchAttribute2Max"] = request.get_search_attribute2_max()
        if request.get_search_attribute5_min() is not None:
            body["searchAttribute5Min"] = request.get_search_attribute5_min()
        if request.get_search_attribute4_min() is not None:
            body["searchAttribute4Min"] = request.get_search_attribute4_min()
        if request.get_attribute3() is not None:
            body["attribute3"] = request.get_attribute3()
        if request.get_search_attribute3_max() is not None:
            body["searchAttribute3Max"] = request.get_search_attribute3_max()
        if request.get_search_attribute4_max() is not None:
            body["searchAttribute4Max"] = request.get_search_attribute4_max()
        if request.get_search_context() is not None:
            body["searchContext"] = request.get_search_context()
        if request.get_search_attribute5_max() is not None:
            body["searchAttribute5Max"] = request.get_search_attribute5_max()
        if request.get_search_attribute3_min() is not None:
            body["searchAttribute3Min"] = request.get_search_attribute3_min()
        if request.get_attribute2() is not None:
            body["attribute2"] = request.get_attribute2()
        if request.get_search_attribute2_min() is not None:
            body["searchAttribute2Min"] = request.get_search_attribute2_min()
        if request.get_attribute4() is not None:
            body["attribute4"] = request.get_attribute4()
        if request.get_attribute5() is not None:
            body["attribute5"] = request.get_attribute5()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.CustomAutoDoMatchmakingRequest import CustomAutoDoMatchmakingRequest

        from gs2_matchmaking_client.control.CustomAutoDoMatchmakingResult import CustomAutoDoMatchmakingResult
        return CustomAutoDoMatchmakingResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/customauto",
            service=self.ENDPOINT,
            module=CustomAutoDoMatchmakingRequest.Constant.MODULE,
            function=CustomAutoDoMatchmakingRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def custom_auto_leave_gathering(self, request):
        """
        ギャザリングから離脱します<br>
        <br>
        本APIは確実に成功することを保証していません。<br>
        例えば、離脱する直前にギャザリングが成立した場合は 404 Not Found を応答します。<br>
        <br>
        404応答を受け取った場合はすでにギャザリングが成立していないかを確認する必要があります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.CustomAutoLeaveGatheringRequest.CustomAutoLeaveGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.CustomAutoLeaveGatheringRequest import CustomAutoLeaveGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/customauto/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=CustomAutoLeaveGatheringRequest.Constant.MODULE,
            function=CustomAutoLeaveGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_matchmaking(self, request):
        """
        マッチメイキングを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.DeleteMatchmakingRequest.DeleteMatchmakingRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_matchmaking_client.control.DeleteMatchmakingRequest import DeleteMatchmakingRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "",
            service=self.ENDPOINT,
            module=DeleteMatchmakingRequest.Constant.MODULE,
            function=DeleteMatchmakingRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_matchmaking(self, request):
        """
        マッチメイキングの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.DescribeMatchmakingRequest.DescribeMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.DescribeMatchmakingResult.DescribeMatchmakingResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_matchmaking_client.control.DescribeMatchmakingRequest import DescribeMatchmakingRequest

        from gs2_matchmaking_client.control.DescribeMatchmakingResult import DescribeMatchmakingResult
        return DescribeMatchmakingResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking",
            service=self.ENDPOINT,
            module=DescribeMatchmakingRequest.Constant.MODULE,
            function=DescribeMatchmakingRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_matchmaking_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_matchmaking_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/serviceClass",
            service=self.ENDPOINT,
            module=DescribeServiceClassRequest.Constant.MODULE,
            function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_matchmaking(self, request):
        """
        マッチメイキングを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.GetMatchmakingRequest.GetMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.GetMatchmakingResult.GetMatchmakingResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_matchmaking_client.control.GetMatchmakingRequest import GetMatchmakingRequest

        from gs2_matchmaking_client.control.GetMatchmakingResult import GetMatchmakingResult
        return GetMatchmakingResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "",
            service=self.ENDPOINT,
            module=GetMatchmakingRequest.Constant.MODULE,
            function=GetMatchmakingRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_matchmaking_status(self, request):
        """
        マッチメイキングのステータスを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.GetMatchmakingStatusRequest.GetMatchmakingStatusRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.GetMatchmakingStatusResult.GetMatchmakingStatusResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_matchmaking_client.control.GetMatchmakingStatusRequest import GetMatchmakingStatusRequest

        from gs2_matchmaking_client.control.GetMatchmakingStatusResult import GetMatchmakingStatusResult
        return GetMatchmakingStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/status",
            service=self.ENDPOINT,
            module=GetMatchmakingStatusRequest.Constant.MODULE,
            function=GetMatchmakingStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def passcode_breakup_gathering(self, request):
        """
        ギャザリングを解散します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeBreakupGatheringRequest.PasscodeBreakupGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeBreakupGatheringRequest import PasscodeBreakupGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "",
            service=self.ENDPOINT,
            module=PasscodeBreakupGatheringRequest.Constant.MODULE,
            function=PasscodeBreakupGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )




    def passcode_create_gathering(self, request):
        """
        パスコード付きギャザリングを新規作成します<br>
        <br>
        パスコードは8桁の数字で構成されたものが自動的に発行されます。<br>
        パスコードの解像度的に秒間100を超える勢いでギャザリングを作成する必要がある場合は<br>
        オートマッチメイキングと組み合わせる必要があります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeCreateGatheringRequest.PasscodeCreateGatheringRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.PasscodeCreateGatheringResult.PasscodeCreateGatheringResult
        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeCreateGatheringRequest import PasscodeCreateGatheringRequest

        from gs2_matchmaking_client.control.PasscodeCreateGatheringResult import PasscodeCreateGatheringResult
        return PasscodeCreateGatheringResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode",
            service=self.ENDPOINT,
            module=PasscodeCreateGatheringRequest.Constant.MODULE,
            function=PasscodeCreateGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def passcode_describe_joined_user(self, request):
        """
        ギャザリングの参加者一覧を取得します<br>
        <br>
        マッチメイキングが成立すると 404 Not Found 応答が返るようになります。<br>
        404応答を返すようになる直前にコールバックエンドポイントに確定した参加者一覧情報が渡されるため、<br>
        コールバックを受け取ってからは本APIを呼び出さないように実装するべきです。<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeDescribeJoinedUserRequest.PasscodeDescribeJoinedUserRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.PasscodeDescribeJoinedUserResult.PasscodeDescribeJoinedUserResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeDescribeJoinedUserRequest import PasscodeDescribeJoinedUserRequest

        from gs2_matchmaking_client.control.PasscodeDescribeJoinedUserResult import PasscodeDescribeJoinedUserResult
        return PasscodeDescribeJoinedUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=PasscodeDescribeJoinedUserRequest.Constant.MODULE,
            function=PasscodeDescribeJoinedUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def passcode_early_complete_gathering(self, request):
        """
        マッチメイキングを早期終了します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeEarlyCompleteGatheringRequest.PasscodeEarlyCompleteGatheringRequest

        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeEarlyCompleteGatheringRequest import PasscodeEarlyCompleteGatheringRequest

        self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/complete",
            service=self.ENDPOINT,
            module=PasscodeEarlyCompleteGatheringRequest.Constant.MODULE,
            function=PasscodeEarlyCompleteGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        )




    def passcode_join_gathering(self, request):
        """
        パスコード付きギャザリングに参加します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeJoinGatheringRequest.PasscodeJoinGatheringRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.PasscodeJoinGatheringResult.PasscodeJoinGatheringResult
        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeJoinGatheringRequest import PasscodeJoinGatheringRequest

        from gs2_matchmaking_client.control.PasscodeJoinGatheringResult import PasscodeJoinGatheringResult
        return PasscodeJoinGatheringResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode/join/" + str(("null" if request.get_passcode() is None else request.get_passcode())) + "",
            service=self.ENDPOINT,
            module=PasscodeJoinGatheringRequest.Constant.MODULE,
            function=PasscodeJoinGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def passcode_leave_gathering(self, request):
        """
        ギャザリングから離脱します<br>
        <br>
        本APIは確実に成功することを保証していません。<br>
        例えば、離脱する直前にギャザリングが成立した場合は 404 Not Found を応答します。<br>
        <br>
        404応答を受け取った場合はすでにギャザリングが成立していないかを確認する必要があります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.PasscodeLeaveGatheringRequest.PasscodeLeaveGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.PasscodeLeaveGatheringRequest import PasscodeLeaveGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/passcode/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=PasscodeLeaveGatheringRequest.Constant.MODULE,
            function=PasscodeLeaveGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def room_breakup_gathering(self, request):
        """
        ギャザリングを解散します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomBreakupGatheringRequest.RoomBreakupGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomBreakupGatheringRequest import RoomBreakupGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "",
            service=self.ENDPOINT,
            module=RoomBreakupGatheringRequest.Constant.MODULE,
            function=RoomBreakupGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )




    def room_create_gathering(self, request):
        """
        ギャザリングを新規作成します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomCreateGatheringRequest.RoomCreateGatheringRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.RoomCreateGatheringResult.RoomCreateGatheringResult
        """
        body = { 
            "meta": request.get_meta(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomCreateGatheringRequest import RoomCreateGatheringRequest

        from gs2_matchmaking_client.control.RoomCreateGatheringResult import RoomCreateGatheringResult
        return RoomCreateGatheringResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room",
            service=self.ENDPOINT,
            module=RoomCreateGatheringRequest.Constant.MODULE,
            function=RoomCreateGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def room_describe_gathering(self, request):
        """
        ギャザリング一覧を取得します<br>
        <br>
        - 消費クオータ: 20件あたり3クオータ<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomDescribeGatheringRequest.RoomDescribeGatheringRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.RoomDescribeGatheringResult.RoomDescribeGatheringResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomDescribeGatheringRequest import RoomDescribeGatheringRequest

        from gs2_matchmaking_client.control.RoomDescribeGatheringResult import RoomDescribeGatheringResult
        return RoomDescribeGatheringResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room",
            service=self.ENDPOINT,
            module=RoomDescribeGatheringRequest.Constant.MODULE,
            function=RoomDescribeGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def room_describe_joined_user(self, request):
        """
        ギャザリングの参加者一覧を取得します<br>
        <br>
        マッチメイキングが成立すると 404 Not Found 応答が返るようになります。<br>
        404応答を返すようになる直前にコールバックエンドポイントに確定した参加者一覧情報が渡されるため、<br>
        コールバックを受け取ってからは本APIを呼び出さないように実装するべきです。<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomDescribeJoinedUserRequest.RoomDescribeJoinedUserRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.RoomDescribeJoinedUserResult.RoomDescribeJoinedUserResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomDescribeJoinedUserRequest import RoomDescribeJoinedUserRequest

        from gs2_matchmaking_client.control.RoomDescribeJoinedUserResult import RoomDescribeJoinedUserResult
        return RoomDescribeJoinedUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=RoomDescribeJoinedUserRequest.Constant.MODULE,
            function=RoomDescribeJoinedUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def room_early_complete_gathering(self, request):
        """
        マッチメイキングを早期終了します<br>
        <br>
            - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomEarlyCompleteGatheringRequest.RoomEarlyCompleteGatheringRequest

        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomEarlyCompleteGatheringRequest import RoomEarlyCompleteGatheringRequest

        self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/complete",
            service=self.ENDPOINT,
            module=RoomEarlyCompleteGatheringRequest.Constant.MODULE,
            function=RoomEarlyCompleteGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        )




    def room_join_gathering(self, request):
        """
        ギャザリングに参加します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomJoinGatheringRequest.RoomJoinGatheringRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.RoomJoinGatheringResult.RoomJoinGatheringResult
        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomJoinGatheringRequest import RoomJoinGatheringRequest

        from gs2_matchmaking_client.control.RoomJoinGatheringResult import RoomJoinGatheringResult
        return RoomJoinGatheringResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "",
            service=self.ENDPOINT,
            module=RoomJoinGatheringRequest.Constant.MODULE,
            function=RoomJoinGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def room_leave_gathering(self, request):
        """
        ギャザリングから離脱します<br>
        <br>
        本APIは確実に成功することを保証していません。<br>
        例えば、離脱する直前にギャザリングが成立した場合は 404 Not Found を応答します。<br>
        <br>
        404応答を受け取った場合はすでにギャザリングが成立していないかを確認する必要があります。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.RoomLeaveGatheringRequest.RoomLeaveGatheringRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_matchmaking_client.control.RoomLeaveGatheringRequest import RoomLeaveGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "/room/" + str(("null" if request.get_gathering_id() is None else request.get_gathering_id())) + "/player",
            service=self.ENDPOINT,
            module=RoomLeaveGatheringRequest.Constant.MODULE,
            function=RoomLeaveGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def update_matchmaking(self, request):
        """
        マッチメイキングを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_matchmaking_client.control.UpdateMatchmakingRequest.UpdateMatchmakingRequest
        :return: 結果
        :rtype: gs2_matchmaking_client.control.UpdateMatchmakingResult.UpdateMatchmakingResult
        """
        body = { 
            "callback": request.get_callback(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        if request.get_gathering_pool_name() is not None:
            body["gatheringPoolName"] = request.get_gathering_pool_name()
        headers = { 
        }
        from gs2_matchmaking_client.control.UpdateMatchmakingRequest import UpdateMatchmakingRequest

        from gs2_matchmaking_client.control.UpdateMatchmakingResult import UpdateMatchmakingResult
        return UpdateMatchmakingResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/matchmaking/" + str(("null" if request.get_matchmaking_name() is None else request.get_matchmaking_name())) + "",
            service=self.ENDPOINT,
            module=UpdateMatchmakingRequest.Constant.MODULE,
            function=UpdateMatchmakingRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


