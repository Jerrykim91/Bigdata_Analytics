import os 

# print(os.getcwd())
# print(os.listdir('data'))

tmp = ['data/dataset/2' ,'data/dataset/2/OK', 'data/dataset/2/FAIL' ] 

for file_name in tmp : 
#     print(file_name)
    func_dir(file_name)
    print(file_name, '== 완료')



def func_dir(adr):
    base = os.getcwd()
    full = base + adr
    tmp = adr.split('\\')

    for idx in range(len(tmp)):
        ck = base +'\\'+'\\'.join(tmp[:idx+1])
        if os.path.exists(ck) is False:
            os.mkdir(ck)
            print('데이터 확인 :', ck , os.path.isdir(ck))
        else:
            print('이미 데이터 존재 ->PASS')

    return 'DONE'



def func_dir(adr):
    base = os.getcwd()
    full = base + adr
    tmp = adr.split('\\')

    for idx in range(len(tmp)):
        ck = base +'\\'+'\\'.join(tmp[:idx+1])
        if os.path.exists(ck) is False:
            os.mkdir(ck)
            print('데이터 확인 :', ck , os.path.isdir(ck))

    return 'DONE'
print(func_dir('Tmp\\a\\b\\c\\d'))




def func_dir(adr):
    base = os.getcwd()
    full = base + adr
    tmp = adr.split('\\')
    # print(len(tmp[1:])) # 5
    # print(tmp[1:])
    # for idx, val in enumerate(tmp[1:]):
    # for idx in range(len(tmp)-1, 0, -1):
    for idx in range(len(tmp)):
        # print(idx)
        # print(tmp[0:])
        # print(tmp[idx])
        # print('\\'.join(tmp[idx]))
        ck = base +'\\'+'\\'.join(tmp[:idx+1])
        if os.path.exists(ck) is False:
            os.mkdir(ck)
            # print(os.listdir(tmp[idx]))
            print('데이터 확인 :', ck , os.path.isdir(ck))
        # print(os.listdir())
        # print(ck)

    # return os.listdir()
    return 'DONE'
    # return print('done')

print(func_dir('Tmp\\a\\b\\c\\d'))





# def func_dir_tmp(adr):
#     base = os.getcwd()
#     full = base + adr
#     tmp = adr.split('\\')
#     # print(len(tmp[1:])) # 5
#     # print(tmp[1:])
#     # for idx, val in enumerate(tmp[1:]):
#     for idx in range(len(tmp), 0, -1):
#         print(idx)
#         print(tmp[idx:])
#         print('\\'.join(tmp[:idx]))
#         # ck = base +'\\'.join(tmp[idx])
#         # print(ck)
#     # return os.listdir()
#     pass

# print(func_dir_tmp('Tmp\\a\\b\\c\\d'))