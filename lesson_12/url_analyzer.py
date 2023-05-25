import argparse
class UrlAnalyzer:

    def __new__(cls, *args, **kwargs):
        analyser=super().__new__(cls)
        if not args and not kwargs:
            analyser.url=cls.user_input()
            analyser.count=8
        return analyser
    def __init__(self, url):
        if url:
            self.url=url

    @staticmethod
    def user_uinput():
        parse = argparse.ArgumentParser()
        parse.add_argument("-url", help='Please sse url for parser')
        args = parse.parse_args()
        #запит користувача
        if args.url:
            return args.url
        else:
            url=input('Please sse url for parser')
            return url

if __name__=='__main__':
    url = UrlAnalyzer('www.google.com')



