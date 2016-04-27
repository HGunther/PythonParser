import time
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import random
import cmath



def fftMult(P,Q):
    pad(P,Q)
    O = getOmega(len(P))
    Pt = FFT(P, len(P), 1, O)
    Qt = FFT(Q, len(Q), 1, O)
    PQt = mult(Pt, Qt)
    O = getOmega(len(PQt), False)
    PQ = FFT(PQt, len(PQt), 1, O)
    return makeRealandDivide(PQ)

def pad(P,Q):
    n = len(P) + len(Q)
    size = 1
    while size < n:
        size = size * 2
    while len(P) < size:
        P.append(0)
    while len(Q) < size:
        Q.append(0)

def getOmega(n, forward = True):
    O = []
    if forward:
        for i in range(0,n):
            O.append(complex(cmath.cos(2*i*cmath.pi/n),cmath.sin(2*i*cmath.pi/n)))
    else:
        for i in range(0,n):
            O.append(complex(cmath.cos(2*i*cmath.pi/n),-1*cmath.sin(2*i*cmath.pi/n)))
    return O

def FFT(Pin, n, exp, O):
    Pe = []
    Po = []
    S = []
    So = []
    Se = []
    if (n == 1):
        S.append(Pin[0])
        return S
    for i in range(0,len(Pin)/2):
        Pe.append(Pin[2*i])
        Po.append(Pin[2*i+1])
    Se = FFT(Pe, n/2, 2*exp, O)
    So = FFT(Po, n/2, 2*exp, O)
    S = [0 for i in range(n)]
    for i in range(0, len(Pin)/2):
        S[i] = Se[i] + O[i*exp]*So[i]
        S[i+n/2] = Se[i] - O[i*exp]*So[i]
    return S

def mult(P,Q):
    PQ = [0 for i in range(len(P))]
    for i in range(len(PQ)):
        PQ[i] = P[i] * Q[i]
    return PQ

def makeRealandDivide(PQ):
    answer = [0 for i in PQ]
    n = len(PQ)
    for i in range(len(answer)):
        answer[i] = float(PQ[i].real) / float(n)
    return answer

#
# Returns a randomly generated polynomial with values between -1.0 and 1.0
#
def getTestPoly(length, maxValue = 1, canBeNegative = True):
    poly = []
    for i in range(length):
        if canBeNegative:
            if random.randint(0,1):
                poly.append(random.random())
            else:
                poly.append( - random.random())
        else: 
            poly.append(random.randint(0,abs(maxValue)))
    return poly
    

#
# Multiplies polynomials using the simple method.
#
def simpleMult(P,Q):
    if len(P) == 0 and len(Q) == 0:
        return []
    answer = [0 for i in range(len(P) + len(Q) -1)]
    for i in range(len(P)):
        for j in range(len(Q)):
            answer[i + j] += P[i] * Q[j]
    while answer[len(answer)-1] == 0 and len(answer) > 1:
        answer.pop()
    return answer
    
#
# Multiplies polynomial using the Divide and Conquer method.
#
def DCMult(P,Q):
    length = max(len(P), len(Q))
    for i in range(len(P), length):
        P.append(0)
    for i in range(len(Q), length):
        Q.append(0)
    answer = recMult(P, Q)
    while answer[len(answer)-1] == 0 and len(answer) > 1:
        answer.pop()
    return answer
    
def recMult(P,Q):
    if len(P) == 0 or len(Q) == 0:
        return []
    if len(P) == 1 or len(Q) == 1:
        return simpleMult(P,Q)
    PL = P[:len(P)/2]
    PH = P[len(P)/2:]
    QL = Q[:len(Q)/2]
    QH = Q[len(Q)/2:]
    
    low = recMult(PL, QL)
    high = recMult(PH, QH)
    mid = recMult( addArray(PL, PH), addArray(QL, QH))
    mid2 = addArray(low, high)
    mid = subtractArray(mid, mid2)
    
    return(addArray(low, addArray(mid, high, 0, len(P)/2), 0, len(P)/2))#len(P)/2-1?

def addArray(X,Y, xoffset = 0, yoffset = 0):
    if type(X) == np.ndarray:
        A = X.tolist()
    elif type(X) == list:
        A = X[:]
    else:
        print "Error: addArray(A,B) was passed a combination of types it does not know how to use."
        print "A: " + repr(type(X)) + ", B: " + repr(type(Y))
        return False
    
    if type(Y) == np.ndarray:
        B = Y.tolist
    elif type(Y) == list:
        B = Y[:]
    else:
        print "Error: addArray(A,B) was passed a combination of types it does not know how to use."
        print "A: " + repr(type(X)) + ", B: " + repr(type(Y))
        return False
        
    if xoffset - yoffset > 0:
        for i in range(xoffset - yoffset):
            A.insert(0,0)
    if yoffset - xoffset > 0:
        for i in range(yoffset - xoffset):
            B.insert(0,0)
            
    answer = []    
    smaller = min(len(A), len(B))
    for i in range(0, smaller):
        answer.append(A[i] + B[i])
    for i in range(smaller, len(A)):
        answer.append(A[i])
    for i in range(smaller, len(B)):
        answer.append(B[i])
    return answer

def subtractArray(X,Y, xoffset = 0, yoffset = 0):
    if type(X) == np.ndarray:
        A = X.tolist()
    elif type(X) == list:
        A = X[:]
    else:
        print "Error: subtractArray(A,B) was passed a combination of types it does not know how to use."
        print "A: " + repr(type(X)) + ", B: " + repr(type(Y))
        return False
    
    if type(Y) == np.ndarray:
        B = Y.tolist
    elif type(Y) == list:
        B = Y[:]
    else:
        print "Error: subtractArray(A,B) was passed a combination of types it does not know how to use."
        print "A: " + repr(type(X)) + ", B: " + repr(type(Y))
        return False
        
    if xoffset - yoffset > 0:
        for i in range(xoffset - yoffset):
            A.insert(0,0)
    if yoffset - xoffset > 0:
        for i in range(yoffset - xoffset):
            B.insert(0,0)
            
    answer = []    
    smaller = min(len(A), len(B))
    for i in range(0, smaller):
        answer.append(A[i] - B[i])
    for i in range(smaller, len(A)):
        answer.append(A[i])
    for i in range(smaller, len(B)):
        answer.append( - B[i])
    return answer
  
    
#Function I used to confirm that the two polynomial multiplication methods
#were returning the same results (and ignoring rounding errors).  
def test(number_of_tests):
    for i in range(number_of_tests):
        P = getTestPoly(random.randint(1,20))
        Q = getTestPoly(random.randint(1,20))
        simp = simpleMult(P,Q)
        dc = DCMult(P,Q)
        fft = fftMult(P,Q)
        for j in range(len(simp)):
            if abs(simp[j] - dc[j]) > 0.00000000000001:
                return(P,Q)
        for j in range(len(simp)):
            if abs(simp[j] - fft[j]) > 0.00000000000001:
                return(P,Q, simp, fft)
    return True

        
def timeSimple(finalTime, samplesPerPoint = 1):
    times = []
    i = 1
    runTime = 0
    while sum(times) + 2 * samplesPerPoint * runTime < finalTime:
    #while runTime < penultimateRunTime:
        i = i * 2
        sample = []
        for j in range(samplesPerPoint):
            start = time.clock()
            simpleMult(getTestPoly(i), getTestPoly(i))
            stop = time.clock()
            runTime = stop-start
            sample.append(runTime)
        times.append(sum(sample)/len(sample))
    return times
    
def timeDC(finalTime, samplesPerPoint = 1):
    times = []
    i = 1
    runTime = 0
    while sum(times) + 2 * samplesPerPoint * runTime < finalTime:
    #while runTime < penultimateRunTime:
        i = i * 2
        sample = []
        for j in range(samplesPerPoint):
            start = time.clock()
            DCMult(getTestPoly(i), getTestPoly(i))
            stop = time.clock()
            runTime = stop-start
            sample.append(runTime)
        times.append(sum(sample)/len(sample))
    return times
    
def timefft(finalTime, samplesPerPoint = 1):
    times = []
    i = 1
    runTime = 0
    while sum(times) + 2 * samplesPerPoint * runTime < finalTime:
    #while runTime < penultimateRunTime:
        i = i * 2
        sample = []
        for j in range(samplesPerPoint):
            start = time.clock()
            fftMult(getTestPoly(i), getTestPoly(i))
            stop = time.clock()
            runTime = stop-start
            sample.append(runTime)
        times.append(sum(sample)/len(sample))
    return times
    
#
# Creates a log-log graph of problem size vs time to solve for both polynomial
# multiplication methods.
# 
def graph(time, samplesPerPoint = 1):
    simp = timeSimple(time/2, samplesPerPoint)
    dc = timeDC(time/2, samplesPerPoint)
    fft = timefft(time/2, samplesPerPoint)
    n = []
    for i in range(max(len(simp), len(dc), len(fft))):
        n.append(2**(i+1))
    
    #Regression
    simpIP = 3 #Number of influential points to discard
    logSimp = np.log2(simp[simpIP:])    
    simpSlope, simpIntercept, simpR_value, simpP_value, simpStd_err = stats.linregress(np.log2(n[simpIP:len(simp)]), logSimp)
    simpFit = []
    for i in range(simpIP, len(simp)):
        simpFit.append(n[i]**simpSlope * 2**simpIntercept)
    
    dcIP = 1 #Number of influential points to discard
    logDC = np.log2(dc[dcIP:])    
    dcSlope, dcIntercept, dcR_value, dcP_value, dcStd_err = stats.linregress(np.log2(n[dcIP:len(dc)]), logDC)
    dcFit = []
    for i in range(dcIP, len(dc)):
        dcFit.append(n[i]**dcSlope * 2**dcIntercept)
        
    fftIP = 1 #Number of influential points to discard
    logFFT = np.log2(fft[fftIP:])    
    fftSlope, fftIntercept, fftR_value, fftP_value, fftStd_err = stats.linregress(np.log2(n[fftIP:len(fft)]), logFFT)
    fftFit = []
    for i in range(fftIP, len(fft)):
        fftFit.append(n[i]**fftSlope * 2**fftIntercept)
    
    plt.close()
    plt.yscale('log')
    plt.ylabel('Time To Solve (seconds)')
    plt.xscale('log')
    plt.xlabel('Problem Size (n)')
    plt.plot(n[:len(simp)], simp, 'ro', label="School Book Algorithm Timeing Data")
    plt.plot(n[simpIP:len(simp)], simpFit, 'r', label="School Book Linear Fit")
    plt.plot(n[:len(dc)], dc, 'bo', label="Divide and Conquer Algorithm Timeing Data")
    plt.plot(n[dcIP:len(dc)], dcFit, 'b', label="Divide and Conquer Linear Fit")
    plt.plot(n[:len(fft)], fft, 'go', label="Fast Fourier Transform Timeing Data")
    plt.plot(n[fftIP:len(fft)], fftFit, 'g', label="Fast Fourier Transform Linear Fit")
    #plt.legend()
    plt.show()
    
    simpData = (simpSlope, simpIntercept, simpR_value, simpP_value, simpStd_err)
    dcData = (dcSlope, dcIntercept, dcR_value, dcP_value, dcStd_err)
    fftData = (fftSlope, fftIntercept, fftR_value, fftP_value, fftStd_err)
    return(simpData, dcData, fftData)
	
    for i in range(10):
        print "Hello"
