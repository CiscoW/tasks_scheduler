from django.utils.deprecation import MiddlewareMixin


# restful 输出标准化
class NormalizeResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        if response.get("Content-Type") == "application/json":
            response = self.normalize_data(response)

        return response

    @staticmethod
    def normalize_data(response):
        response_template = dict()

        response_template["status"] = response.status_code
        if 200 <= response.status_code <= 299:
            response_template["message"] = "成功"
            response_template["data"] = response.data
            response_template["ok"] = True

        else:
            response_template["message"] = response.data
            response_template["data"] = []
            response_template["ok"] = False

        response.data = response_template
        # 因返回时已经render过response，要想让这里的修改有效，需要手动在render一次
        response._is_rendered = False
        response.render()

        return response
