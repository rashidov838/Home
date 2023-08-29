# def get_user_info(name,clan='Trident',*args,**kwargs):
#     if args:
#         args=''.join([f'\n- {arg}' for arg in args])
#         return f'Name : {name} and clan: {clan}. Other information {args}'
#     elif kwargs:
#         kwargs=''.join([f'\n-{kwarg}' for kwarg in kwargs])
#         return f'Name : {name} and clan: {clan}. Other information {args}. Key skils: {kwargs}'
#     else:
#         return f'Name {name} and clan {clan}'
# print(get_user_info('Bekzod'))
# print(get_user_info('Bekzod','Bratva'))
# print(get_user_info('Bekzod','Bratva','sonic speed','lighting','programming'))
# print(get_user_info('Bekzod','Bratva','sonic speed','lighting','programming',jump=100,play=10))