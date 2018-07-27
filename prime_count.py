# prime_count
def main():
    pass
    a,b = map(int, input().split())
    flag=0
    for num in range(a,b+1):
        if(num>1):
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                flag+=1
    print(flag)
if __name__ == '__main__':
    main()
