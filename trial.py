strObj = "160/80/02/04/20211"


start = 3
stop = 17
# Remove charactes from index 5 to 10
if len(strObj) > stop :
    strObj = strObj[0: start:] + strObj[stop + 1::]
print('Modified String : ', strObj)