def rot(num):
    return(str(num).replace('6', '9', 1))

if __name__ == "__main__":
    num = 99669
    print(rot(num))
