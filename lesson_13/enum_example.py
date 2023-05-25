import enum
from http import HTTPStatus
import requests
class StatusCode(int, enum.Enum):
    OK=200
    NOT_FOUND=404
    SUCCESSFUL=201

# r=requests.get('htttps//:www.google.com')
#
# if r.status_code==StatusCode.OK.value:
#     print('Status code is OK')


class Api(str, enum.Enum):
    POST='/posts'
    COMMENTS='/comments'
    TODOS='/todos'


print(StatusCode.OK.value)
print(StatusCode.OK.name)

r=requests.get('htttps//:www.google.com')
if r.status_code==HTTPStatus.OK:
    print('Status is ok')
    print(HTTPStatus.OK.description)