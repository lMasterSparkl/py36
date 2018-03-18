def whitch_price(a):
    #根据输入积分数a返回是否中奖
    if 0<=a<=50:
        return '恭喜！ 你赢得了 wooden rabbit'
    elif 51<=a<=150:
        return '哦，亲爱的，这次没有奖品'
    elif 151<=a<=180:
        return '恭喜！ 你赢得了 wafer-thin mint'
    elif 181<=a<=200:
        return '恭喜！ 你赢得了 penguin'
a=int(input())
print (whitch_price(a))
'''def which_prize(a):
    #根据输入积分数b返回是否中奖
    prize=None
    if a<=50:
        prize= 'wooden rabbit'
    elif 151<=a<=180:
        prize= 'wafer-thin mint'
    elif 181<=a<=200:
        prize= 'penguin'
    if prize:
        return "恭喜！ 你赢得了 "+ prize+"!"
    else:
        return "哦，亲爱的，这次没有奖品"
a=int(input())
print(which_prize(a))'''
