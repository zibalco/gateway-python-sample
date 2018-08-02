import requests

class zibal:
    merchant = "zibal"
    callback_url = "http://yourapiurl.com/callbackurl"


    def request(self, amount, order_id, mobile, description, multiplexingInfos = None):
        data = {}
        data['merchant'] = self.merchant
        data['callbackUrl'] = self.callback_url
        data['amount'] = amount

        data['orderId'] = order_id
        data['mobile'] = mobile
        data['description'] = description
        data['multiplexingInfos'] = multiplexingInfos

        response = self.postTo('request', data)
        return response

    def verify(self, trackId):
        data = {}
        data['merchant'] = self.merchant
        data['trackId'] = trackId
        return self.postTo('verify', data)

    def postTo(self, path, parameters):

        url = "https://gateway.zibal.ir/" + path

        response = requests.post(url = url, json= parameters)

        return response.json()
