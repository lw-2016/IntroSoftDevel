##6. Consider this recursive function:


def mystery(n) :
    if n <= 0 :
        return 0
    else:
        return n + mystery(n - 1)


mystery(4)
##What is mystery(4)?
