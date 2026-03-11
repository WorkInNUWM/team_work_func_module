# working_with_group("CT-21",4)
# print(f"Out value count students: {count_student_in_ct2}")
# ==============name function as params function===
def expression_calc(a,b,func):
    if func==add:
        print(func(a,b)**2)
    elif func==div:
        print(func(a,b)**3)
    else:
        print(func(a,b))

def add(a,b):
    return a+b

def div(a,b):
    if b==0:
        b=1
    return a/b

def kw_minues(a,b):
    return (a+b)*(a-b)

if __name__=="__main__":
    pass