def convert_to_numeric(a):
    '''转换浮点数'''
    num1=float(a)
    return num1
def sum_of_middle_three(a,b,c,d,e):
    '''5个数字相加减去最大最小值'''
    sum5=a+b+c+d+e-max(a,b,c,d,e)-min(a,b,c,d,e)
    return sum5
def score_to_rating_string(a):
    if 0<=a<1:
        return 'Terrible'
    elif 1<=a<2:
        return 'Bad'
    elif 2<=a<3:
        return 'OK'
    elif 3<=a<4:
        return 'Good'
    else:
        return 'Excellent'
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
a='3'
b=5
c=8
d=9.0
e=10
print(scores_to_rating(a,b,c,d,e))
