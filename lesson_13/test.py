# import logging
#
# #логирование - посмотреть временные рамки
#
#
# logging.basicConfig(level=logging.INFO,filename='my_log.log', filemode='w',
#                     format='%(asctime)s %(levelname)s %(message)s')
# # logging.debug('Debug')
# # logging.info('Info') #для информации
# # logging.warning('Warning')
# # logging.error('Error')
# # logging.critical('Critical')
#
# x=3
# y=4
#
# logging.info(f'We get value {x} {y}')
# try:
#     result=x/y
#     logging.info(f'x/y succesfull with result {result}')
# except ZeroDivisionError as err:
#     logging.warning('ZeroDivisionError', exc_info=True)
import logging
logging.basicConfig(level=logging.INFO,filename='my_log.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')

import logging

x_value=[1, 2, 3, 0, 43, 1]
y_value=[11, 0, 13, 234, 0,23]

for x_value, y_value in zip(x_value, y_value):
    x,y=x_value, y_value
    try:
        result=x/y
        logging.info(f'x/y succesfull with result{result}')
    except ZeroDivisionError as err:
        logging.warning('ZeroDivisionError', exc_info=True)