def isMountain(height):
    # 関数を完成させてください
    if len(height) < 3:return False
    max_height = max(height)
    max_place = height.index(max_height)
    if max_height == height[0] or max_height == height[-1]:return False
    for i in range(max_place):
        if height[i] >= height[i+1]: return False
    for j in range(max_place,len(height)-1):
        if height[j] <= height[j+1]: return False
    return True


print(isMountain([3,4,3]))




