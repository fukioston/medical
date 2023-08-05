import ssl
# 全局取消证书验证 根据自己环境进行使用
# sl._create_default_https_context = ssl._create_unverified_context

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from django.conf import settings


def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
        # 暂时不发送短信 默认就是成功
        print(response)
        # response = {'result': 0, 'msg': "发送成功"}
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN

    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response
