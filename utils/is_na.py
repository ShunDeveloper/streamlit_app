# textがnaならTrueを返す
def is_na(text):
    flag = False
    if text=='<NA>':
        flag=True
    if type(text)==float:
        flag=True
    return flag