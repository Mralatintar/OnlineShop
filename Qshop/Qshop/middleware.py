from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

from Qshop.settings import ERROR_PATH
import time
class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        request_ip=request.META["REMOTE_ADDR"]
        if request_ip=="10.10.14.250":
            return HttpResponse("冯浩,快乐是怎么消失的呢")

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print("我是process_view")
        print(callback)
    # def process_exception(self,request,exception):
    #     if exception:
    #         with open(ERROR_PATH,"a")as f:
    #             now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    #             content="[%s]:%s\n"%(now,exception)
    #             f.write(content)
    #             sendDing(content)
    #         return HttpResponse("代码错了，错误在下方:<br> %s"%exception)
    def process_template_response(self,request,response):
        """
        必须返回一个render才可以触发
        :param response:
        :return:
        """
        print("我是process_template_response")
        return HttpResponse("123")

    def process_response(self,request,response):
        """
        process_response 和 process_template_response必须有返回值
        :param request:
        :param response:
        :return:
        """
        print("我是process_response")
        return response
