
import numpy

PI = numpy.pi
SIN = numpy.sin
COS = numpy.cos

def p_wav(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav
    x=x+t_pwav
    b=(2*l)/d_pwav
    n=100
    p1=1/l
    p2=0

    for i in range(1,n+1):
        harm1=(((SIN((PI/(2*b))*(b-(2*i))))/(b-(2*i))+(SIN((PI/(2*b))*(b+(2*i))))/(b+(2*i)))*(2/PI))*COS((i*PI*x)/l)             
        p2=p2+harm1

    pwav1=p1+p2
    pwav=a*pwav1
    return pwav

def q_wav(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    x=x+t_qwav
    a=a_qwav
    b=(2*l)/d_qwav
    n=100
    q1=(a/(2*b))*(2-b)
    q2=0
    for i in range(1,n+1):
        harm5=(((2*b*a)/(i*i*PI*PI))*(1-COS((i*PI)/b)))*COS((i*PI*x)/l)
        q2=q2+harm5
    qwav=-1*(q1+q2)
    return qwav

def qrs_wav(x,a_qrswav,d_qrswav,li):
    l=li
    a=a_qrswav
    b=(2*l)/d_qrswav
    n=100
    qrs1=(a/(2*b))*(2-b)
    qrs2=0
    for i in range(1,n+1):
        harm=(((2*b*a)/(i*i*PI*PI))*(1-COS((i*PI)/b)))*COS((i*PI*x)/l)
        qrs2=qrs2+harm
        
    qrswav=qrs1+qrs2
    return qrswav

def s_wav(x,a_swav,d_swav,t_swav,li):
    l=li
    x=x-t_swav
    a=a_swav
    b=(2*l)/d_swav
    n=100
    s1=(a/(2*b))*(2-b)
    s2=0
    for i in range(1,n+1):
        harm3=(((2*b*a)/(i*i*PI*PI))*(1-COS((i*PI)/b)))*COS((i*PI*x)/l)
        s2=s2+harm3
    swav=-1*(s1+s2)
    return swav