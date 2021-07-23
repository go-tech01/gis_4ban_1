# # def decorator(func):
# #     def decorated(input_text):
# #         print('함수 시작!')
# #         func(input_text)
# #         print('함수 끝!')
# #     return decorated
# #
# # @decorator
# # def hello_world(input_text):
# #     print(input_text)
# #
# # hello_world('Hello World!!')
#
# #삼각형 넓이 계산 함수
# #사각형의 넓이 계산 함수
# # 입력값이 모두 양수인지 확인하고 아닐경우 error 발생시키는 decorator 작성 및 적용
#
#
# def check_integer(func):
#     def dec(b, h):
#         if (b > 0) and (h > 0):
#             return func(b, h)
#         else:
#             raise ValueError('Input must be positive value')
#     return dec
#
# @check_integer
# def cal(b, h):
#     print(f'삼각형 넓이 : {b * h / 2}')
#     print(f'사각형 넓이 : {b * h}')
#
#
# cal(3, 2)
# cal(3, -2)
#
# class User:
#     def __init__(self, auth):
#         self.is_auth = auth
#
# user = User(auth=False)
# ~~~~