#function main passes value 5 (mystery (4+1)) to function mystery

def main() :
    a = 4
    print(mystery(a + 1))
# function mystery takes value 5 from main()performs operation y=5*5 
def mystery(x):
    y = x * x 
    return y #returns 25    

main()

