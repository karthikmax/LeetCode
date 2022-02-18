#get two input numbers. start - starting number, n - Number of even integers to print from starting number.
#print a list of n even integers starting from 'start' 
def even(start, n):
    # write your code here
    result = list()
    if start % 2 == 1:
        start_num =start + 1
    else:
        start_num = start
        
    for i in range(n):
        result.append(start_num)
        start_num += 2   
    
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    start, n = map(int, input().split())
    res = even(start, n)
    print(res)