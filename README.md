## qcloudapi-sdk-python

qcloudapi-sdk-python是为了让Python开发者能够在自己的代码里更快捷方便的使用腾讯云的API而开发的SDK工具包。

#### 资源

- [公共参数](http://wiki.qcloud.com/wiki/%E5%85%AC%E5%85%B1%E5%8F%82%E6%95%B0)
- [API列表](http://wiki.qcloud.com/wiki/API)
- [错误码](http://wiki.qcloud.com/wiki/%E9%94%99%E8%AF%AF%E7%A0%81)

#### 入门

在第一次使用云API之前，用户首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。


#### 例子

```
    from qcloudapi.client import QcloudApi

    # module 设置需要加载的模块, 已有的模块列表参考 qcloudapi.modules 模块
    module = 'sec'

    # action 对应接口的接口名，请参考wiki文档上对应接口的接口名
    action = 'CaptchaQuery'

    # 认证信息
    config = {
        'Region': '区域参数',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }

    # params 请求参数，请参考wiki文档上对应接口的说明
    params = {
        'userIp': '127.0.0.1',
        'businessId': 1,
        'captchaType': 1,
        'script': 0,
        # 'Region': 'gz', # 当Region不是上面配置的DefaultRegion值时，可以重新指定请求的Region
    }

    try:
        service = QcloudApi(module, config)

        # 请求前可以通过下面四个方法重新设置请求的secretId/secretKey/region/method参数
        # 重新设置请求的secretId
        secretId = '你的secretId'
        service.setSecretId(secretId)

        # 重新设置请求的secretKey
        secretKey = '你的secretKey'
        service.setSecretKey(secretKey)

        # 重新设置请求的region
        region = 'sh'
        service.setRegion(region)

        # 重新设置请求的method
        method = 'post'
        service.setRequestMethod(method)

        # 生成请求的URL，不发起请求
        print(service.generateUrl(action, params))

        # 调用接口，发起请求
        print(service.call(action, params))
    except Exception as e:
        print(e)
```
