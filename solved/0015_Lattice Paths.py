#<p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
#<div class="center">
#<img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
#<p>How many such routes are there through a $20 \times 20$ grid?</p>

GridDim = [20,20]

def binomialcoefficient(n,k):
    #binomialcoefficient = (n k) = n! // ( k! * (n-k)! )
    return faculty(n) // ( faculty(k) * faculty(n-k))

def faculty(n):
    result = 1

    if n == 1 or n == 0:
        return result
    for i in range(1,n+1):
        result *= i
    return result

print(f"In einem Grid von {GridDim[0]}:{GridDim[1]} gibt es {binomialcoefficient(GridDim[0]+GridDim[1],GridDim[0])} mögliche Lösungen!")
