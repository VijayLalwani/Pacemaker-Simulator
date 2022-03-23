import numpy
from wav import p_wav, q_wav, qrs_wav, s_wav

li=30/72

def xwave():
    x=numpy.arange(0.62,0.96,0.01, dtype=float)
    return x

# print(len(list(xwave())))
# print(xwave()[-1])

def pwave():
    a_pwav=0.25
    d_pwav=0.09
    t_pwav=0.16
    pwav = p_wav(xwave(),a_pwav,d_pwav,t_pwav,li)
    return pwav

def non_pwave():
    normalpwave = pwave()
    non_pwave = numpy.empty(normalpwave.size,dtype=float)
    non_pwave.fill(normalpwave[0])
    return non_pwave

def qwave():
    a_qwav=0.025
    d_qwav=0.066
    t_qwav=0.166
    qwav = q_wav(xwave(),a_qwav,d_qwav,t_qwav,li)
    return qwav

def non_qwave():
    normalqwave = qwave()
    non_qwave = numpy.empty(normalqwave.size,dtype=float)
    non_qwave.fill(normalqwave[0])
    return non_qwave

def qrswave():
    a_qrswav=1.6
    d_qrswav=0.11
    qrswav=qrs_wav(xwave(),a_qrswav,d_qrswav,li)
    return qrswav

def non_qrswave():
    normalqrswave = qrswave()
    non_qrswave = numpy.empty(normalqrswave.size,dtype=float)
    non_qrswave.fill(normalqrswave[0])
    return non_qrswave

# def qrswave_reverse():
#     a_qrswav=-1.6
#     d_qrswav=0.11
#     qrswav_reverse=qrs_wav(xwave(),a_qrswav,d_qrswav,li)
#     return qrswav_reverse

def qrswave_reverse():
    targetqrswave = qrswave()
    basevalue_qrsvalue = targetqrswave[14] * 2
    # reverse_period =  normalqrswave[14:28]
    # for i in reverse_period:
    #     reverse_period.append(basevalue_qrsvalue - i)
    #     reverse_period.pop(0)
    for i in range(15,28):
        t = basevalue_qrsvalue - targetqrswave[i]
        targetqrswave[i] = t
    return targetqrswave
def swave():
    a_swav=0.25
    d_swav=0.066
    t_swav=0.09
    swav=s_wav(xwave(),a_swav,d_swav,t_swav,li)
    return swav

def non_swave():
    normalswave = swave()
    non_swave = numpy.empty(normalswave.size,dtype=float)
    non_swave.fill(normalswave[0])
    return non_swave

def pace():
    a_qrswav=1
    d_qrswav=0.03
    pace=qrs_wav(xwave(),a_qrswav,d_qrswav,li)
    return pace

# P-P interval
def interval_x(selected_bpm=60):
    heartrate_bpm = selected_bpm
    interval_length = (60/heartrate_bpm) - 0.32
    interval_x = numpy.arange(1.13,1.13+interval_length,0.01, dtype=float)
    return interval_x

def display_x(selected_bpm=60):
    display_x = numpy.append(xwave(),interval_x(selected_bpm))
    return display_x

def normalcardiacperiod():
    y = pwave()+qwave()+qrswave()+swave()
    return y
# y-axis value of P-P interval
def ecg_interval(selected_bpm=60):
    ecg_interval = numpy.empty(interval_x(selected_bpm).size)
    ecg_interval.fill(float(normalcardiacperiod()[:1]))
    return ecg_interval
#ecg_interval()

def normalywave(bpm=60):
    y = pwave()+qrswave()+swave()+qwave()
    normalywave = numpy.append(y,ecg_interval(bpm))

    return normalywave

def LeadsSAFail(rate=60):
    y = non_pwave()+qwave()+qrswave()+swave()
    wave = numpy.append(y,ecg_interval(rate))
    return wave

# def LeadsAVFail(rate=60):
#     y = pwave()+non_pwave()+non_qrswave()+non_swave()
#     wave = numpy.append(y,ecg_interval(rate))
#     return wave
#print(len(normalywave()))
def LeadsAVFail(rate=60):
    y = pwave()+non_pwave()+non_qrswave()+non_swave()
    wave = numpy.append(y-0.57134,ecg_interval(rate))
    return wave

def AAIwave(bpm):
    aaicycle1 = non_pwave()+qwave()+qrswave()+swave()
    aaicycle1 = numpy.append(aaicycle1,ecg_interval(bpm))
    pacedpwave = pwave()
    pacedpwave[0] = pacedpwave[0] + 1
    aaicycle2 = numpy.append(pacedpwave + qwave() + qrswave() + swave(),ecg_interval(bpm))
    aaicycle3 = aaicycle2
    aaicycle4 = numpy.append(pwave() + qwave() + qrswave() + swave(),ecg_interval(bpm))
    y = numpy.append(aaicycle1,[aaicycle2,aaicycle3,aaicycle4])
    return y


# def VVIwave(bpm=60):
#     #y = 0
#     vvicycle1 = pwave() + non_qwave() + non_qrswave() + non_swave()
#     vvicycle1 = numpy.append(vvicycle1,ecg_interval(bpm))
#     pacedqwave = qwave()
#     pacedqwave[0] = pacedqwave[0] + 1
#     vvicycle2 = numpy.append(pwave() + pacedqwave + qrswave_reverse() + swave(),ecg_interval(bpm))
#     vvicycle3 = vvicycle2
#     vvicycle4 = numpy.append(pwave() + qwave() + qrswave() + swave(),ecg_interval(bpm))
#     y = numpy.append(vvicycle1,[vvicycle2,vvicycle3,vvicycle4])
#     return y

def VVIwave(bpm=60):
    #y = 0
    vvicycle1 = pwave() + non_qwave() + non_qrswave() + non_swave()
    vvicycle1 = numpy.append(vvicycle1,ecg_interval(bpm))
    pacedqwave = qwave()
    pacedqwave[14] = pacedqwave[14] + 1
    vvicycle2 = numpy.append(pwave() + pacedqwave + qrswave_reverse() + swave(),ecg_interval(bpm))
    vvicycle3 = vvicycle2
    vvicycle4 = numpy.append(pwave() + qwave() + qrswave() + swave(),ecg_interval(bpm))
    y = numpy.append(vvicycle1,[vvicycle2,vvicycle3,vvicycle4])
    return y

def DDDwave(bpm):
    y = 0
    pacedpwave = pwave()
    pacedpwave[0] = pacedpwave[0] + 1
    pacedqwave = qwave()
    pacedqwave[14] = pacedqwave[14] + 1
    AsVs = numpy.append(pwave() + qwave() + qrswave() + swave(),ecg_interval(bpm))
    AsVp = numpy.append(pwave() + pacedqwave + qrswave_reverse() + swave(),ecg_interval(bpm))
    ApVp = numpy.append(pacedpwave + pacedqwave + qrswave_reverse() + swave(),ecg_interval(bpm))
    ApVs = numpy.append(pacedpwave + qwave() + qrswave() + swave(),ecg_interval(bpm))
    y = numpy.append(AsVs,[AsVp,ApVp,ApVs])
    return y

#Testing Area


# print(type(qrswave()))
# print(qrswave())
# print(qrswave().size)

# print(type(qrswave_reverse()))
# print(qrswave_reverse())
# print(qrswave_reverse().size)

# Deprecated Codes

# x = xwave()
# y = ywave()
# line1 = []

# while True:
#     line1 = live_plotter(x,y,line1)
#     y = numpy.append(y[1:],y[:1])