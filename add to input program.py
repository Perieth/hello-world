


faceList = [1,2,3,4,0,2,2,2,3,3,1,2,3,4]
i = 0

while i < lenfaceList:
    if faceList[i] == 0:
        newFaceList.append[[1,0,0,0,0]+ "\n"]
    elif faceList[i] == 1:
        newFaceList.append[[0,1,0,0,0]+ "\n"]
    elif faceList[i] == 2:
        newFaceList.append[[0,0,1,0,0]+ "\n"]
    elif faceList[i] == 3:
        newFaceList.append[[0,0,0,1,0]+ "\n"]
    elif faceList[i] == 4:
        newFaceList.append[[0,0,0,0,1]+ "\n"]
