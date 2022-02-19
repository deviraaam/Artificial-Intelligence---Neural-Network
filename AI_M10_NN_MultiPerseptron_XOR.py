# Final STEP

import random
import math           # rumus sigmoid

# XOR Gate
Bias = 1
I2 = [0,0,1,1]
I3 = [0,1,0,1]

Output = [0,1,1,0]

print("Bias = ", Bias)
print("="*50)
print("Input1 = ", I2)
print("="*50)
print("Input2 = ", I3)
print("="*50)
print("Output = ", Output)
print("="*50)

# Creates a list containing 5 lists, each of 8 items, all set to 0
g, h = 4, 3;
w = [[0 for x in range(g)] for y in range(h)]
dw = [[0 for x in range(g)] for y in range(h)]

I = {}
wh = {}
summation = {}
H = {}
Cout = {}

dH = {}
dwH = {}

# Creates weight input layer
w[0][1] = random.random()
w[0][2] = random.random()
w[1][1] = random.random()
w[1][2] = random.random()
w[2][1] = random.random()
w[2][2] = random.random()
print("w01= ", w[0][1])
print("w02= ", w[0][2])
print("w11= ", w[1][1])
print("w12= ", w[1][2])
print("w21= ", w[2][1])
print("w22= ", w[2][2])
print("-"*100)

# Creates weight hidden layer
wh[0] = random.random()
wh[1] = random.random()
wh[2] = random.random()
print("wh1= ", wh[0])
print("wh1= ", wh[1])
print("wh2= ", wh[2])
print("-"*100)

epoch = 15000
miu = 0.1
MSE = 0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Learning
for i in range(1, epoch):    
    for j in range (4):                # 4 = Jumlah dataset (4 input)
        # =================================================================== Forward        
        # =================================================================== Input Layer 
        for k in range (1,3):          # 1,3 = 2 - Jumlah hidden layer
            H[k] = (Bias*w[0][k]) + (I2[j]*w[1][k]) + (I3[j]*w[2][k])
            # =================================================================== Sigmoid Output
            H[k] = 1 / (1 + math.exp(-H[k]))            
        # =================================================================== Hidden Layer 1
        SH = (Bias*wh[0]) + (H[1]*wh[1]) + (H[2]*wh[2])        # SH = Output
        # =================================================================== Sigmoid Output
        C = 1 / (1 + math.exp(-SH))        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Learning Performance Analysis
        MSE = MSE + (Output[j] - C)**2
        
        # =================================================================== Backward
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Differensial
        dC = C*(1 - C)*(Output[j] - C)          # Output = TargetC
        dH[1] = H[1]*(1 - H[1])*wh[1]*dC
        dH[2] = H[2]*(1 - H[2])*wh[2]*dC
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Update Weight Hidden Layer
        H[0] = Bias
        for k in range (3):
            dwH[k] = miu*H[k]*dC
            # Update Weight
            wh[k] = wh[k] + dwH[k]            
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Update Weight Input Layer
        I[0] = Bias          # Bias
        I[1] = I2[j]         # Input 1
        I[2] = I3[j]         # Input 2
        for k in range (3):
            for m in range (1,3):
                dw[k][m] = miu*I[k]*dH[m]
                # Update Weight
                w[k][m] = w[k][m] + dw[k][m]                
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Learning Performance Analysis
    MSE = MSE / 4
    print("=====> Error MSE %d = %.12f" %(i, MSE))
    MSE = 0
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Check Re-Check
print()
print("="*100)
for j in range (4):                # 4 = Jumlah dataset (4 input)
        # =================================================================== Forward        
        # =================================================================== Input Layer 
        for k in range (1,3):          # 1,3 = 2 - Jumlah hidden layer
            H[k] = (Bias*w[0][k]) + (I2[j]*w[1][k]) + (I3[j]*w[2][k])
            # =================================================================== Sigmoid Output
            H[k] = 1 / (1 + math.exp(-H[k]))            
        # =================================================================== Hidden Layer 1
        SH = (Bias*wh[0]) + (H[1]*wh[1]) + (H[2]*wh[2])        # SH = Output
        # =================================================================== Sigmoid Output
        Cout[j] = 1 / (1 + math.exp(-SH))        
# ===================================================================> Final Result
print()
print("==========================================================> Final Result")
for j in range (4):                # 4 = Jumlah dataset (4 input)
        print(" I1 = %d I2 = %d ==> Output = %f" %(I2[j], I3[j], Cout[j]))