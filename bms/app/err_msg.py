# coding=utf-8

class ErrMsg:
    def __init__(self, results=None):
        self.err_msg = dict()
        self.err_msg['000000'] = 'OK'
        self.err_msg['000001'] = '用户名或密码必填项.'
        self.err_msg['000002'] = '用户名未注册.'
        self.err_msg['000003'] = '用户名或密码错误.'

        self.results = results

    def get(self, err_code='000000'):
        res_msg = {
            'code': err_code,
            'msg': self.err_msg.get(err_code)
        }
        if self.results:
            res_msg.update(self.results)
        return res_msg
