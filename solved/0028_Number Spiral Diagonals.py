#<p>Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:</p>
#<p class="monospace center"><span class="red"><b>21</b></span> 22 23 24 <span class="red"><b>25</b></span><br>
#20  <span class="red"><b>7</b></span>  8  <span class="red"><b>9</b></span> 10<br>
#19  6  <span class="red"><b>1</b></span>  2 11<br>
#18  <span class="red"><b>5</b></span>  4  <span class="red"><b>3</b></span> 12<br><span class="red"><b>17</b></span> 16 15 14 <span class="red"><b>13</b></span></p>
#<p>It can be verified that the sum of the numbers on the diagonals is $101$.</p>
#<p>What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?</p>

def getMatrix(GridDim):
    
    matrix = [["" for _ in range(GridDim)] for _ in range(GridDim)]

    center = GridDim//2
    val = 1
    matrix[center][center] = val
    val += 1

    for ring in range(1,center+1):
        for i in range(-ring+1, ring+1):
            matrix[center+i][center+ring] = val
            val += 1
        for i in range(ring-1,-ring-1,-1):
            matrix[center+ring][center+i] = val
            val += 1
        for i in range(-ring+1,ring):
            matrix[center-i][center-ring] = val
            val += 1
        for i in range(-ring,ring+1):
            matrix[center-ring][center+i] = val
            val += 1

    return matrix

def getSum(GridDim):
    matrix = getMatrix(GridDim)
    if GridDim <= 15:
        for line in range(0,len(matrix)):
            print(matrix[line])
    center = GridDim//2
    val = matrix[center][center]

    for i in range(1,GridDim//2+1):
        val += matrix[center+i][center+i]
        val += matrix[center+i][center-i]
        val += matrix[center-i][center+i]
        val += matrix[center-i][center-i]
    return val

GridDim = 1001   # GridDim%2 != 0

if GridDim%2 == 0:
    print(f"The Grid dimensions are equal numbers. GridDim%2 have to be != 0 ")
else:
    print(f"The sum of the diagonals is = {getSum(GridDim)}")
