
# 공유 주차장 
def isInCircle(centerX, centerY, radius, locX, locY) :
    dx=locX-centerX
    dy=locY-centerY
    distance = dx*dx + dy*dy
    if (distance < radius) :
        return 1
    else :
        return 0


