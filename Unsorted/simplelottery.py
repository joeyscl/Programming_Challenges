import random

def gen_num(n):
    return random.randint(0,n)

def sim(n):
    nums = []
    count = 0
    while len(nums) < n:
        newnum = gen_num(n)
        if newnum not in nums:
            nums.append(newnum)
        count = count + 1
    return count

def main():
    trials = int(input(["number of trials"]))
    lotterysize = int(input(["lottery size"]))
    total = 0
    for i in range(trials):
        total = total + sim(lotterysize)
        if (i%(trials/10) == 0) and i > 0:
            print(total/i)
    print()
    print(total/trials)
                      
                      

if __name__ == "__main__":
    main()
