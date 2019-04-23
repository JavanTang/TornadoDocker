import json
import tornado.ioloop
import tornado.web

from algorithm import f


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        '''触发Get的操作
        '''

        x = self.get_argument('x')  # 获取请求的值
        y = f(x)    # f是算法的接口
        y = json.dumps(y, ensure_ascii=False)
        self.write(y)

    def post(self):
        '''触发Get的操作
        '''

        x = self.get_argument('x')  # 获取请求的值
        y = f(x)    # f是算法的接口
        y = json.dumps(y, ensure_ascii=False)
        self.write(y)

    def set_default_headers(self):
        '''支持跨域请求
        '''

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST,GET,OPTIONS")


def make_app():
    return tornado.web.Application([
        (r"/pow", MainHandler),    # 路由匹配
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()
