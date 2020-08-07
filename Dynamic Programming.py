import numpy as np

def dataset():
    examples=1000
    A=[]
    B=[]
    for i in range(examples):
        A.append(np.random.randint(10**5 , size=10))
        B.append(np.random.randint(10**5 , size=10))
        
    A.append(np.ones((10), dtype=int))
    B.append(np.ones((10), dtype=int))
    
    A.append(np.zeros((10), dtype=int))
    B.append(np.zeros((10), dtype=int))
    
    A=np.asarray(A)
    B=np.asarray(B)
    
    #np.savetxt('A', A, fmt='%d') to write data to text files
    #np.savetxt('B', B, fmt='%d')
    
    return A,B
    
'''def data_load():
    
    A = np.loadtxt('A', dtype=int)
    B = np.loadtxt('B', dtype=int)
    
    return (A,B)'''


def sort_sol(a,b):
    res=[]
    
    for i in range(len(a)):
        res.append(a[i]-b[i])
    out = sorted(range(len(res)), key=lambda x: res[x])
    A = out[-int(len(res)/2):]
    return A


def best_dp(a,b):
    cols = int(len(a)/2)+2
    rows = len(a)

    hap  = [[-1e7 for col in range(cols)] for row in range(rows)]
    choices = [['' for col in range(cols)] for row in range(rows)] 

    hap[0][1] = b[0]
    hap[0][2] = a[0]

    
    choices[0][1] = 'B'
    choices[0][2] = 'A'
    
    for i in range(1,rows):
        for j in range(1,cols):
            
            if (hap[i-1][j-1]+a[i]>=hap[i-1][j]+b[i]):
                hap[i][j] = hap[i-1][j-1]+a[i]
                choices[i][j] = choices[i-1][j-1]+'A'
            else :
                hap[i][j] = hap[i-1][j]+b[i]
                choices[i][j] = choices[i-1][j]+'B'
            
           
    res_list = [i for i, value in enumerate(list(choices[-1][-1])) if value == 'A']
    
    return(res_list)
        

def test(A,B):
    
    result=[]
    
    for i in range(A.shape[0]):
        a = A[i]
        b = B[i]
        result.append((sorted(sort_sol(a,b)) == sorted(best_dp(a,b))))
    wrong_values = np.where(np.asarray(result)==False)[0]
    if len(wrong_values)==0:
        print('All Test cases passed!')

    else:
        print('Errors detected!')
        
        
        

A=np.asarray([[20494, 58105 ,47999, 51669, 40228, 98582, 53078, 41855, 77402, 34918] ,
[14988, 74330, 24390, 76473,  1785,  9345, 61897, 22888, 85535, 59365] ,
[55333,   334, 36321, 16405,   877, 72716, 29685, 39364, 14691, 65701] ,
[72094, 69582, 50041, 74936, 49982, 64327, 76362, 80230, 87898, 94006] ,
[20064, 81580, 61220, 13704, 63440, 14411, 75038, 55399, 47175,  6334] ,
[95585, 62773, 21343, 71172, 77188, 52173, 39386, 20652, 82635, 28124] ,
[10442, 55132, 32993, 44516, 92237, 18519, 72136, 77459, 60231,  8031] ,
[91605, 97808, 80825,22091 ,64318,  7454, 42632, 90270, 98579, 29596] ,
[29861, 72240, 28067, 59058, 72834, 30038, 48916, 34250, 11388, 58363] ,
[ 8608, 77878, 67644, 31046, 39783, 93972, 87859, 87514, 13571, 53484]])

B=np.asarray([[69577,  8885, 64017, 65089, 81155, 62165,  3603,  8955, 62424, 80770] ,
[85156, 92273, 80327, 65487, 42083,  4492, 88154, 37321,   992, 95949] ,
[16126, 33495 ,64161, 16283, 55033 ,11516, 25066, 24578, 27137, 66235] ,
[96606, 15299, 36340, 25279, 50927, 97916, 54616, 93770, 23401, 10139] ,
[62573,80480, 32533 , 7279 ,41264, 30397, 62915,  5770, 62585, 30301] ,
[55333,   334, 36321, 16405,   877, 72716, 29685, 39364, 14691, 65701],
[20064, 81580, 61220, 13704, 63440, 14411, 75038, 55399, 47175,  6334] ,
[10442, 55132, 32993, 44516, 92237, 18519, 72136, 77459, 60231,  8031] ,
[14988, 74330, 24390, 76473,  1785,  9345, 61897, 22888, 85535, 59365] ,
[30866 ,60823 ,37810 ,4088 ,38969 ,13885 ,57271 ,99031 ,94061 ,66708]]) 
        
#A,B = dataset() Exhaustive test data generator.

test(A,B)


## Sorting Solution:
### Time Complexity : O(nlogn)
### Memory Complexity : n

## Dynamic Programming Solution:
### Time Complexity : O(n^2)
### Memory Complexity : O(n^2)