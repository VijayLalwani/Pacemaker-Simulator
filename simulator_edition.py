from cgitb import text
from multiprocessing import Value
import time
from tkinter import *
import tkinter
import main_wav
from tkinter.tix import COLUMN
from turtle import left, width
from webbrowser import get
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import numpy

# heart
################################################################################################################################

afterHandler_heart = 0
heart_switch = True
i = 0
AAI_heart_switch = False
VVI_heart_switch = False
DDD_heart_switch = False
leads_failure_SA_value = False
leads_failure_AV_value = False
x_heart_Initialize_array_length= []
y_heart_Initialize_array_length =[]
x_heart_Initialize=0
y_heart_Initialize=0
for i in range(306):
    x_heart_Initialize += 0.01
    x_heart_Initialize_array_length.append(x_heart_Initialize)
y_heart_Initialize_array_length = [0]*306
#自定义x306  y306

x_heart = list(main_wav.display_x(60))[:] #初始值102个x
y_heart = list(main_wav.normalywave())[:] #赤石脂102个y

AAI_heart=list(main_wav.AAIwave(60))[:]
VVI_heart=list(main_wav.VVIwave(60))[:]
DDD_heart=list(main_wav.DDDwave(60))[:]
LeadsSAFail_value=list(main_wav.LeadsSAFail(60))[:]
LeadsAVFail_value=list(main_wav.LeadsAVFail(60))[:]

def y_heartrate(temp):
    global y_heart
    y_heart = list(main_wav.normalywave(temp))[:]

def AAI_heartrate(temp):
    global AAI_heart
    AAI_heart = list(main_wav.AAIwave(temp))[:]
def VVI_heartrate(temp):
    global VVI_heart
    VVI_heart=list(main_wav.VVIwave(temp))[:]
def DDD_heartrate(temp):
    global DDD_heart
    DDD_heart=list(main_wav.DDDwave(temp))[:]
def leads_failure_SA_FUN(temp):
    global LeadsSAFail_value
    LeadsSAFail_value = list(main_wav.LeadsSAFail(temp))[:]
def leads_failure_AV_FUN(temp):
    global LeadsAVFail_value
    LeadsAVFail_value = list(main_wav.LeadsAVFail(temp))[:]
x_heart_value_progressive_increase_initial_value = 3.06
def run_heart():
    global y_heart_Initialize_array_length
    global x_heart_Initialize_array_length
    global x_heart
    global y_heart
    global AAI_heart
    global VVI_heart
    global DDD_heart
    global heart_switch
    global afterHandler_heart
    global x_heart_value_progressive_increase_initial_value
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    global leads_failure_SA_value
    global leads_failure_AV_value
    global LeadsSAFail_value
    global LeadsAVFail_value

    if heart_switch:
        heartax.clear()
        heartax.plot(x_heart_Initialize_array_length, y_heart_Initialize_array_length, 'r')
        canvas1.draw()

        if AAI_heart_switch:
            y_temp = AAI_heart.pop(0)
            y_heart_Initialize_array_length.pop(0)
            x_heart_Initialize_array_length.pop(0)
            x_heart_value_progressive_increase_initial_value += 0.01

            x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
            # x_heart.append(x_heart_value_progressive_increase_initial_value)
            AAI_heart.append(y_temp)
            y_heart_Initialize_array_length.append(y_temp)

        elif VVI_heart_switch:
            y_temp = VVI_heart.pop(0)
            y_heart_Initialize_array_length.pop(0)
            x_heart_Initialize_array_length.pop(0)
            x_heart_value_progressive_increase_initial_value += 0.01

            x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
            # x_heart.append(x_heart_value_progressive_increase_initial_value)
            VVI_heart.append(y_temp)
            y_heart_Initialize_array_length.append(y_temp)

        elif DDD_heart_switch:
            y_temp = DDD_heart.pop(0)
            y_heart_Initialize_array_length.pop(0)
            x_heart_Initialize_array_length.pop(0)
            x_heart_value_progressive_increase_initial_value += 0.01

            x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
            # x_heart.append(x_heart_value_progressive_increase_initial_value)
            DDD_heart.append(y_temp)
            y_heart_Initialize_array_length.append(y_temp)
        else:
            if leads_failure_SA_value:

                y_temp = LeadsSAFail_value.pop(0)
                y_heart_Initialize_array_length.pop(0)
                x_heart_Initialize_array_length.pop(0)
                x_heart_value_progressive_increase_initial_value += 0.01

                x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
                # x_heart.append(x_heart_value_progressive_increase_initial_value)
                LeadsSAFail_value.append(y_temp)
                y_heart_Initialize_array_length.append(y_temp)


            elif leads_failure_AV_value:

                y_temp = LeadsAVFail_value.pop(0)
                y_heart_Initialize_array_length.pop(0)
                x_heart_Initialize_array_length.pop(0)
                x_heart_value_progressive_increase_initial_value += 0.01

                x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
                # x_heart.append(x_heart_value_progressive_increase_initial_value)
                LeadsAVFail_value.append(y_temp)
                y_heart_Initialize_array_length.append(y_temp)

            else:
                y_temp = y_heart.pop(0)
                y_heart_Initialize_array_length.pop(0)
                x_heart_Initialize_array_length.pop(0)
                x_heart_value_progressive_increase_initial_value += 0.01

                x_heart_Initialize_array_length.append(x_heart_value_progressive_increase_initial_value)
                # x_heart.append(x_heart_value_progressive_increase_initial_value)
                y_heart.append(y_temp)
                y_heart_Initialize_array_length.append(y_temp)
        afterHandler_heart = simulator.after(50, run_heart)




def heart_AAI_mode_on():
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = True
    VVI_heart_switch = False
    DDD_heart_switch = False
def heart_VVI_mode_on():
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = True
    DDD_heart_switch = False
def heart_DDD_mode_on():
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = True

def all_heart_mode_off():
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = False

def stop_heart():
    global heart_switch
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = False
    heart_switch = False
    heartRate_scale.set(60)
def reboot_set_run_heart_value():
    global heart_switch
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = False
    heart_switch = True
    heartRate_scale.set(60)


def battery_failure_heart():
    global heart_switch
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = False
    heart_switch = False
    heartRate_scale.set(60)

def battery_level_0_heart():
    global heart_switch
    global AAI_heart_switch
    global VVI_heart_switch
    global DDD_heart_switch
    AAI_heart_switch = False
    VVI_heart_switch = False
    DDD_heart_switch = False
    heart_switch = False
    heartRate_scale.set(60)

##################################################################################################################################
# battery
# define battery button function of mode and switch
# AAI mode switch


def AAI_mode_on():
    global AAI
    global DDD
    global VDD
    AAI = True
    VDD = False
    DDD = False


def AAI_mode_off():
    global AAI
    AAI = False


# VDD mode switch
def VDD_mode_on():
    global AAI
    global DDD
    global VDD
    AAI = False
    VDD = True
    DDD = False


def VDD_mode_off():
    global VDD
    VDD = False


# DDD mode switch
def DDD_mode_on():
    global AAI
    global DDD
    global VDD
    AAI = False
    VDD = False
    DDD = True


def DDD_mode_off():
    global DDD
    DDD = False


def all_mode_off():
    global AAI
    global DDD
    global VDD
    AAI = False
    VDD = False
    DDD = False


# to set battery_bool, when you switch off battery, You have to reset the bool of the battery first which
# you need to click battery on button
# And then you click pacemaker button
def battery_on():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    y = [3] * 10  # y_value consume mA
    x = [i for i in range(10)]  # x_value time
    t = 6  # time
    ax.clear()
    battery_switch = True


def reboot_battery():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    y = [3] * 10  # y_value consume mA
    x = [i for i in range(10)]  # x_value time
    t = 6  # time
    ax.clear()
    battery_switch = True
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False

def battery_off():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    #y = [3] * 10  # y_value consume mA
    #x = [i for i in range(10)]  # x_value time
    #t = 6  # time
    ax.clear()
    battery_switch = False


def battery_failure():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    #y = [3] * 10  # y_value consume mA
    #x = [i for i in range(10)]  # x_value time
    #t = 6  # time
    ax.clear()
    battery_switch = False
    label_power.configure(text='batteryFailure ', fg='green')

def battery_level_0():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    #y = [3] * 10  # y_value consume mA
    #x = [i for i in range(10)]  # x_value time
    #t = 6  # time
    ax.clear()
    battery_switch = False


def stop_pacemaker():
    global battery_switch
    global x
    global y
    global t
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    #y = [3] * 10  # y_value consume mA
    #x = [i for i in range(10)]  # x_value time
    #t = 6  # time
    ax.clear()
    battery_switch = False


# encryption mode switch on and off
def encryption_on():
    global encryption_switch
    encryption_switch = True


def encryption_off():
    global encryption_switch
    encryption_switch = False


# verification mode switch on and off
def verification_on():
    global verification_switch
    verification_switch = True


def verification_off():
    global verification_switch
    verification_switch = False


# keep all AAI DDD VDD encryption_switch verification_switch to switch off
def reset_battery():
    global AAI
    global DDD
    global VDD
    global verification_switch
    global encryption_switch
    global battery_switch
    global x
    global y
    global t
    AAI = False
    VDD = False
    DDD = False
    encryption_switch = False
    verification_switch = False
    battery_switch = True
    # battery_switch = False
    y = [3] * 10  # y_value consume mA
    x = [i for i in range(10)]  # x_value time
    t = 6  # time
    ax.clear()
    label_power.configure(text='normal battery ', fg='green')


#############################################################################################
y = [3] * 10  # y_value consume mA
x = [i for i in range(10)]  # x_value time
t = 6  # time
# battery_switch = True  # battery bool #没用了
AAI = False  # pacing mode
VDD = False  # pacing mode
DDD = False  # pacing mode
encryption_switch = False
verification_switch = False
battery_switch = True
afterHandler = 0
afterHandler1 = 0
t_standby_mode = 5
t_encryption = 3
t_verification = 2
mA_standby = 3
mA_encryption = mA_standby + 3
mA_verification = mA_standby + 5
mA_AAI = 5
mA_VDD = 10
mA_DDD = 12
standby_switch = True


##################################################################################################################################
# new battery function, please use this to demonstrate.
# below the new section where is the old plan that I have commented out, You can comment out the new section to run
# old plan. its just two different plan to demonstrate  encryption and verification. the others are the same.
def battery_switch_standby():
    global t_standby_mode
    global t_encryption
    global t_verification
    global t
    global x
    global y
    global AAI
    global VDD
    global DDD
    global ax
    global afterHandler
    global battery_switch
    global encryption_switch
    global verification_switch
    # Regenerate the image every 30 seconds
    # if t % 30 == 0:
    #     del x[:]
    #     del y[:]
    ax.clear()
    # Drawing the standby mode image
    if battery_switch:
        if standby_switch and not encryption_switch and not verification_switch:
            x.append(t - 1)
            if AAI:
                y.append(mA_AAI + mA_standby)
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI', fg='green')
            elif VDD:
                y.append(mA_VDD + mA_standby)
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI', fg='green')
            elif DDD:
                y.append(mA_DDD + mA_standby)
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD', fg='green')
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='standby',fg='green')
                y.append(mA_standby)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            x.append(t)
            if AAI:
                y.append(mA_AAI + mA_standby)
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI', fg='green')
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI', fg='green')
                y.append(mA_VDD + mA_standby)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD', fg='green')
                y.append(mA_DDD + mA_standby)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='standby', fg='green')
                y.append(mA_standby)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            t = t + 1

            afterHandler = simulator.after(1000, battery_switch_standby)
            # print(t_standby_mode)
            # to judge mode

        elif encryption_switch and verification_switch and standby_switch:
            x.append(t - 1)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI encrytion verticfiction', fg='green')
                y.append(mA_AAI + mA_encryption + mA_verification-mA_standby)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI encrytion verticfiction', fg='green')
                y.append(mA_VDD + mA_encryption + mA_verification-mA_standby)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD encrytion verticfiction', fg='green')
                y.append(mA_DDD + mA_encryption + mA_verification-mA_standby)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text=' encrytion verticfiction', fg='green')
                y.append(mA_encryption + mA_verification-mA_standby)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            x.append(t)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(
                    text='AAI encrytion verticfiction', fg='green')
                y.append(mA_AAI + mA_encryption + mA_verification-mA_standby)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(
                    text='VVI encrytion verticfiction', fg='green')
                y.append(mA_VDD + mA_encryption + mA_verification-mA_standby)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(
                    text='DDD encrytion verticfiction', fg='green')
                y.append(mA_DDD + mA_encryption + mA_verification-mA_standby)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(
                    text='encrytion verticfiction', fg='green')
                y.append(mA_encryption + mA_verification-mA_standby)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            t = t + 1

            afterHandler = simulator.after(1000, battery_switch_standby)
        elif encryption_switch  and standby_switch:
            x.append(t - 1)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI encrytion',fg='green')
                y.append(mA_AAI + mA_encryption)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI encrytion',fg='green')
                y.append(mA_VDD + mA_encryption)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD encrytion',fg='green')
                y.append(mA_DDD + mA_encryption)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='encrytion',fg='green')
                y.append(mA_encryption)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            x.append(t)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI encrytion',fg='green')
                y.append(mA_AAI + mA_encryption)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI encrytion',fg='green')
                y.append(mA_VDD + mA_encryption)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD encrytion',fg='green')
                y.append(mA_DDD + mA_encryption)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='encrytion',fg='green')
                y.append(mA_encryption)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)
            t = t + 1
            afterHandler = simulator.after(1000, battery_switch_standby)
        elif verification_switch and standby_switch:
            x.append(t - 1)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI verification',fg='green')
                y.append(mA_AAI + mA_verification)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI verification',fg='green')
                y.append(mA_VDD + mA_verification)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD verification',fg='green')
                y.append(mA_DDD + mA_verification)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='verification',fg='green')
                y.append(mA_verification)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)

            x.append(t)
            if AAI:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='AAI verification',fg='green')
                y.append(mA_AAI + mA_verification)
            elif VDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='VVI verification',fg='green')
                y.append(mA_VDD + mA_verification)
            elif DDD:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='DDD verification',fg='green')
                y.append(mA_DDD + mA_verification)
            else:
                label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.configure(text='verification',fg='green')
                y.append(mA_verification)
            ax.plot(x, y, 'g')
            canvas.draw()
            x.pop(0)
            y.pop(0)
            t = t + 1
            afterHandler = simulator.after(1000, battery_switch_standby)
##################################################################################################################################


##################################################################################################################################
##################################################################################################################################
# old function for battery, please don't delete this code, it just different plan for battery
# old function for battery, please don't delete this code, it just different plan for battery
# old function for battery, please don't delete this code, it just different plan for battery
###############################################################################################
###############################################################################################
###############################################################################################
# standby mode and this is the entrance of this program
# def battery_switch_standby():
#     global t_standby_mode
#     global t_encryption
#     global t_verification
#     global t
#     global x
#     global y
#     global AAI
#     global VDD
#     global DDD
#     global ax
#     global afterHandler
#     global battery_switch
#     # Regenerate the image every 30 seconds
#     # if t % 30 == 0:
#     #     del x[:]
#     #     del y[:]
#     ax.clear()
#     # Drawing the standby mode image
#     if battery_switch:
#         if t_standby_mode:
#             x.append(t - 1)
#             if AAI:
#                 y.append(mA_AAI + mA_standby)
#             elif VDD:
#                 y.append(mA_VDD + mA_standby)
#             elif DDD:
#                 y.append(mA_DDD + mA_standby)
#             else:
#                 y.append(mA_standby)
#             ax.plot(x, y, 'g')
#             canvas.draw()
#             x.pop(0)
#             y.pop(0)
#
#             x.append(t)
#             if AAI:
#                 y.append(mA_AAI + mA_standby)
#             elif VDD:
#                 y.append(mA_VDD + mA_standby)
#             elif DDD:
#                 y.append(mA_DDD + mA_standby)
#             else:
#                 y.append(mA_standby)
#             ax.plot(x, y, 'g')
#             canvas.draw()
#             x.pop(0)
#             y.pop(0)
#
#             t = t + 1
#             t_standby_mode -= 1
#             afterHandler = simulator.after(1000, battery_switch_standby)
#             # print(t_standby_mode)
#             # to judge mode
#             if t_standby_mode == 0:
#                 if encryption_switch and verification_switch:
#                     x.append(t - 1)
#                     if AAI:
#                         y.append(mA_AAI + mA_encryption)
#                     elif VDD:
#                         y.append(mA_VDD + mA_encryption)
#                     elif DDD:
#                         y.append(mA_DDD + mA_encryption)
#                     else:
#                         y.append(mA_encryption)
#                     ax.plot(x, y, 'g')
#                     canvas.draw()
#                     x.pop(0)
#                     y.pop(0)
#
#                     t_encryption = 3
#                     afterHandler = simulator.after(1000, encryption)
#                 elif encryption_switch:
#                     x.append(t - 1)
#                     if AAI:
#                         y.append(mA_AAI + mA_encryption)
#                     elif VDD:
#                         y.append(mA_VDD + mA_encryption)
#                     elif DDD:
#                         y.append(mA_DDD + mA_encryption)
#                     else:
#                         y.append(mA_encryption)
#                     ax.plot(x, y, 'g')
#                     canvas.draw()
#                     x.pop(0)
#                     y.pop(0)
#
#                     t_encryption = 3
#                     afterHandler = simulator.after(1000, encryption)
#                 elif verification_switch:
#                     x.append(t - 1)
#                     if AAI:
#                         y.append(mA_AAI + mA_verification)
#                     elif VDD:
#                         y.append(mA_VDD + mA_verification)
#                     elif DDD:
#                         y.append(mA_DDD + mA_verification)
#                     else:
#                         y.append(mA_verification)
#                     ax.plot(x, y, 'g')
#                     canvas.draw()
#                     x.pop(0)
#                     y.pop(0)
#                     t_verification = 2
#                     afterHandler = simulator.after(1000, verification)
#                 else:
#                     t_standby_mode = 5
#                     # afterHandler = simulator.after(1000, standby)

# old function for battery, please don't delete this code, it just different plan for battery
# def encryption():
#     global mA_DDD
#     global mA_VDD
#     global mA_AAI
#     global mA_standby
#     global mA_encryption
#     global mA_verification
#     global t_standby_mode
#     global t_encryption
#     global t_verification
#     global t
#     global x
#     global y
#     global AAI
#     global VDD
#     global DDD
#     # global battery_switch
#     global ax
#     global afterHandler
#     ax.clear()
#     # Regenerate the image every 30 seconds
#     # if t % 30 == 0:
#     #     del x[:]
#     #     del y[:]
#
#     if t_encryption:
#         x.append(t - 1)
#         if AAI:
#             y.append(mA_AAI + mA_encryption)
#         elif VDD:
#             y.append(mA_VDD + mA_encryption)
#         elif DDD:
#             y.append(mA_DDD + mA_encryption)
#         else:
#             y.append(mA_encryption)
#         ax.plot(x, y, 'g')
#         canvas.draw()
#         x.pop(0)
#         y.pop(0)
#
#         x.append(t)
#         if AAI:
#             y.append(mA_AAI + mA_encryption)
#         elif VDD:
#             y.append(mA_VDD + mA_encryption)
#         elif DDD:
#             y.append(mA_DDD + mA_encryption)
#         else:
#             y.append(mA_encryption)
#         ax.plot(x, y, 'g')
#         canvas.draw()
#         x.pop(0)
#         y.pop(0)
#
#         t_encryption = t_encryption - 1
#         # print(t_encryption)
#         t = t + 1
#         afterHandler = simulator.after(1000, encryption)
#         # to judge mode
#         if t_encryption == 0:
#             if encryption_switch and verification_switch:
#                 x.append(t - 1)
#                 if AAI:
#                     y.append(mA_AAI + mA_verification)
#                 elif VDD:
#                     y.append(mA_VDD + mA_verification)
#                 elif DDD:
#                     y.append(mA_DDD + mA_verification)
#                 else:
#                     y.append(mA_verification)
#                 ax.plot(x, y, 'g')
#                 canvas.draw()
#                 x.pop(0)
#                 y.pop(0)
#                 t_verification = 2
#                 afterHandler = simulator.after(1000, verification)
#             else:  # encryption_switch:
#                 x.append(t - 1)
#                 if AAI:
#                     y.append(mA_AAI + mA_encryption)
#                 elif VDD:
#                     y.append(mA_VDD + mA_encryption)
#                 elif DDD:
#                     y.append(mA_DDD + mA_encryption)
#                 else:
#                     y.append(mA_encryption)
#                 ax.plot(x, y, 'g')
#                 canvas.draw()
#                 x.pop(0)
#                 y.pop(0)
#                 t_standby_mode = 5
#                 afterHandler = simulator.after(1000, battery_switch_standby)

# old function for battery, please don't delete this code, it just different plan for battery
# def verification():
#     global mA_DDD
#     global mA_VDD
#     global mA_AAI
#     global mA_standby
#     global mA_encryption
#     global mA_verification
#     global t_standby_mode
#     global t_encryption
#     global t_verification
#     global t
#     global x
#     global y
#     global AAI
#     global VDD
#     global DDD
#     # global battery_switch
#     global ax
#     global afterHandler
#     ax.clear()
#     # Regenerate the image every 30 seconds
#     # if t % 30 == 0:
#     #     del x[:]
#     #     del y[:]
#
#     if t_verification:
#         x.append(t - 1)
#         if AAI:
#             y.append(mA_AAI + mA_verification)
#         elif VDD:
#             y.append(mA_VDD + mA_verification)
#         elif DDD:
#             y.append(mA_DDD + mA_verification)
#         else:
#             y.append(mA_verification)
#         ax.plot(x, y, 'g')
#         canvas.draw()
#         x.pop(0)
#         y.pop(0)
#
#         x.append(t)
#         if AAI:
#             y.append(mA_AAI + mA_verification)
#         elif VDD:
#             y.append(mA_VDD + mA_verification)
#         elif DDD:
#             y.append(mA_DDD + mA_verification)
#         else:
#             y.append(mA_verification)
#         ax.plot(x, y, 'g')
#         canvas.draw()
#         x.pop(0)
#         y.pop(0)
#
#         t_verification = t_verification - 1
#         # print(t_verification)
#         t = t + 1
#         # to judge mode
#         if t_verification == 0:
#             if encryption_switch and verification_switch:
#                 x.append(t - 1)
#                 if AAI:
#                     y.append(mA_AAI + mA_standby)
#                 elif VDD:
#                     y.append(mA_VDD + mA_standby)
#                 elif DDD:
#                     y.append(mA_DDD + mA_standby)
#                 else:
#                     y.append(mA_standby)
#                 ax.plot(x, y, 'g')
#                 canvas.draw()
#                 x.pop(0)
#                 y.pop(0)
#                 t_standby_mode = 5
#                 afterHandler = simulator.after(1000, battery_switch_standby)
#             else:  # verification_switch:
#                 x.append(t - 1)
#                 if AAI:
#                     y.append(mA_AAI + mA_verification)
#                 elif VDD:
#                     y.append(mA_VDD + mA_verification)
#                 elif DDD:
#                     y.append(mA_DDD + mA_verification)
#                 else:
#                     y.append(mA_verification)
#                 ax.plot(x, y, 'g')
#                 canvas.draw()
#                 x.pop(0)
#                 y.pop(0)
#                 t_standby_mode = 5
#                 afterHandler = simulator.after(1000, battery_switch_standby)
#
#         afterHandler = simulator.after(1000, verification)

###################################################################################################################################
###################################################################################################################################

# Buttons functions

def controlButton():
    # if start_button['text']=='on':
    # start_button.configure(text='off')
    battery_switch_standby()
    pacemaker_state.configure(text='State: on')
    run_heart()
    label_power.configure(text='normal battery ', fg='green')
    # else:
    #     start_button.configure(text='on')
    #     pacemaker_state.configure(text='State: off')
    #     label3.configure(text='Mode:N/A')
    # battery_off()


def stop_controlButton():
    stop_pacemaker()
    pacemaker_state.configure(text='State: off')
    label3.configure(text='Mode:N/A')
    stop_heart()
    label_power.configure(text='normal battery ', fg='green')

def rebootButton():
    reboot_battery()
    reboot_set_run_heart_value()
    label_power.configure(text='normal battery ', fg='green')


#     battery_off()
# start_button.configure(text='on')
# pacemaker_state.configure(text='State: off')
# label3.configure(text='Mode:N/A')
# if start_button['text']=='off':


# mode button
def AAIButton():
    # if start_button['text']=='off':
    if pacemaker_state['text'] == 'State: on':
        label3.configure(text='Mode: AAI')
        AAI_mode_on()
        heart_AAI_mode_on()

def VVIButton():
    # if start_button['text']=='off':
    if pacemaker_state['text'] == 'State: on':
        label3.configure(text='Mode: VVI')
        VDD_mode_on()
        heart_VVI_mode_on()

def DDDButton():
    # if start_button['text']=='off':
    if pacemaker_state['text'] == 'State: on':
        label3.configure(text='Mode: DDD')
        DDD_mode_on()
        heart_DDD_mode_on()

def All_Mode_Off():
    label3.configure(text='Mode:N/A')
    all_mode_off()
    all_heart_mode_off()

def reSetButton():
    heartRate_label.config(text='Heart Rate: 30 bpm')
    heartRate_scale.config(var_hr=heartRate_scale.set(60))
    # prInterval_label.config(text='PRInterval: 0 ms')
    # prInterval_scale.config(var_hr=prInterval_scale.set(0))




batteryFailureButton_value = True

def batteryFailureButton():
    global batteryFailureButton_value
    if batteryFailureButton_value:
        batteryFailureButton_value = False
        battery_failure()
        battery_failure_heart()

        label_power.configure(text='batteryFailure', fg='red')
    else:
        batteryFailureButton_value = True
        label_power.configure(text='normal battery ', fg='green')


leadsFailure_SA_bool = True
def leadsFailure_SA_Button():
    global leadsFailure_SA_bool
    global leads_failure_SA_value

    if leadsFailure_SA_bool:
        leadsFailure_SA_bool = False
        leads_failure_SA_value = True
        #leads_failure_SA_FUN()
        label_leads.configure(text='leadsFailure_SA',fg='red')
    else:
        leadsFailure_SA_bool = True
        leads_failure_SA_value = False
        label_leads.configure(text='normal leads',fg='green')
    return 0

leadsFailure_AV_bool = True
def leadsFailure_AV_Button():
    global leadsFailure_AV_bool
    global leads_failure_AV_value
    if leadsFailure_AV_bool:
        leadsFailure_AV_bool = False
        leads_failure_AV_value = True
        #leads_failure_AV_FUN()
        label_leads.configure(text='leadsFailure_AV',fg='red')
    else:
        leadsFailure_AV_bool = True
        leads_failure_AV_value = False
        label_leads.configure(text='normal leads',fg='green')
    return 0


# Set window
simulator = Tk()
simulator.title("Pacemaker Simulator")
width = 1500
height = 800
simulator.config(bg='#EDEDED')
screenwidth = simulator.winfo_screenwidth()
screenheight = simulator.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
simulator.geometry(alignstr)
# simulator.resizable(width=False, height=False)

# Information above the canvas: ECG and Pace mode
topframe = tkinter.Frame(simulator, width=2000, height=500)
topframe.pack(side=TOP, anchor=N)
# Heartbeat figure
#####################################################################################
heart = tkinter.Canvas(topframe, bg='#ffffff', width=1000, height=500)
heart.pack(side=LEFT)
fig1 = plt.figure(figsize=(10, 5), edgecolor='green')
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['figure.figsize'] = (3.5, 2.5)1500
plt.rcParams['font.size'] = 5
heartax = fig1.add_subplot(111)  # 心电图子图
#heartax.set_xlabel("X axis")
#heartax.set_ylabel("Y axis")
heartax.grid()
plt.xticks([])
plt.yticks([])
canvas1 = FigureCanvasTkAgg(fig1, master=heart)
canvas1.draw()
canvas1.get_tk_widget().place(x=0, y=0)
heart.pack()

#####################################################################################################
# label3 = tkinter.Label(topframe, text='Mode:N/A', font=("Times", 16), fg='green', bg='black', justify=CENTER)
# label3.place(relx=0.05, rely=0.05)
# label4 = tkinter.Label(heart, text='ECG', font=("Times", 16), fg='green', justify=LEFT)
# label4.place(relx=0.3, rely=0.02)
# label5 = tkinter.Label(heart, text='mA', font=("Times", 8), fg='green', justify=LEFT)
# label5.place(relx=0.005, rely=0.03)
# label6 = tkinter.Label(heart, text='Time/s', font=("Times", 8), fg='green', justify=LEFT)
# label6.place(relx=0.85, rely=0.93)

label1=tkinter.Label(topframe,text='ECG',font=("Times",16),fg='green',bg='white',justify=CENTER)
label1.place(relx=0.1,rely=0.05)
#  Temporarily empty
label2=tkinter.Label(heart,text='',font=("Times",16),fg='green',bg='white',justify=LEFT)
label2.place(relx=0.15,rely=0.9)

label3=tkinter.Label(heart,text='Mode:N/A',font=("Times",16),fg='green',bg='white',justify=LEFT)
label3.place(relx=0.1,rely=0.9)
label4=tkinter.Label(heart,text='Time/50ms',font=("Times",16),fg='green',bg='white',justify=LEFT)
label4.place(relx=0.9,rely=0.85)

# Battery status
label_power = tkinter.Label(heart, text='normal battery', font=("Times", 16), fg='green', bg='white', justify=CENTER)
label_power.place(relx=0.8, rely=0.9)
# leads
label_leads = tkinter.Label(heart, text='normal leads', font=("Times", 16), fg='green', bg='white', justify=CENTER)
label_leads.place(relx=0.6, rely=0.9)
# battery canvas in ecg frame
battery = tkinter.Canvas(topframe, bg='#ffffff', width=500, height=500)
fig = plt.figure(figsize=(5, 5), edgecolor='blue')
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['figure.figsize'] = (3.5, 2.5)
plt.rcParams['font.size'] = 10
ax = fig.add_subplot(111)
# plt.axis('off')
plt.xticks([])
plt.yticks([])
# ax.set_xlabel("Time/s")
# ax.set_ylabel("mA")
canvas = FigureCanvasTkAgg(fig, master=battery)
canvas.draw()
canvas.get_tk_widget().place(x=0, y=0)
battery.pack()

# label4 = tkinter.Label(battery, text='Battery Consumotion', font=("Times", 16), fg='green', justify=LEFT)
# label4.place(relx=0.3, rely=0.02)
# label5 = tkinter.Label(battery, text='mA', font=("Times", 8), fg='green', justify=LEFT)
# label5.place(relx=0.005, rely=0.03)
# label6 = tkinter.Label(battery, text='Time/s', font=("Times", 8), fg='green', justify=LEFT)
# label6.place(relx=0.85, rely=0.93)

label4=tkinter.Label(battery,text='Battery Consumption',font=("Times",16),fg='green',bg='white',justify=LEFT)
label4.place(relx=0.35,rely=0.05)

label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction=tkinter.Label(battery,text='',font=("Times",16),fg='green',bg='white',justify=LEFT)
label_battery_comsumption_AAI_VVI_DDD_encrytion_verticfiction.place(relx=0.2,rely=0.93)

label5=tkinter.Label(battery,text='mA',font=("Times",13),fg='green',bg='white',justify=LEFT)
label5.place(relx=0.08,rely=0.07)
label6=tkinter.Label(battery,text='Time/s',font=("Times",16),fg='green',bg='white',justify=LEFT)
label6.place(relx=0.85,rely=0.89)

# Defining variables
var_hr = IntVar()
var_pr = IntVar()

# set Pacemaker Frame
pacemaker = tkinter.LabelFrame(simulator, text="Pacemaker", labelanchor="n", relief=RIDGE, borderwidth=3, bg='white',
                               width=300, height=250)
pacemaker.pack(fill="both", expand="yes", side=LEFT, anchor=W)
# Pacemaker Frame--Button and Label
pacemaker_state = tkinter.Label(pacemaker, text="State:", font=("Times", 10), bg='white', justify=LEFT)
pacemaker_state.pack()
start_button = tkinter.Button(pacemaker, text="ON", command=controlButton, width=10, height=1, bg='lightcyan')
start_button.pack()

stop_button = tkinter.Button(pacemaker, text="OFF", command=stop_controlButton, width=10, height=1, bg='lightcyan')
stop_button.pack()
reboot_button = tkinter.Button(pacemaker, text="REBOOT", command=rebootButton, width=10, height=1,
                               bg='lightcyan')
reboot_button.pack()

empty1 = tkinter.Label(pacemaker, text="", font=("Times", 10), bg='white', justify=LEFT)
empty1.pack()
modes = tkinter.Label(pacemaker, text="Modes", font=("Times", 10), bg='white', justify=LEFT)
modes.pack()
aai_on = tkinter.Button(pacemaker, text="AAI", command=AAIButton, width=10, height=1, bg='lightcyan')
aai_on.pack()
vdd_on = tkinter.Button(pacemaker, text="VVI", command=VVIButton, width=10, height=1, bg='lightcyan')
vdd_on.pack()
ddd_on = tkinter.Button(pacemaker, text="DDD", command=DDDButton, width=10, height=1, bg='lightcyan')
ddd_on.pack()
ddd_off = tkinter.Button(pacemaker, text="MODE OFF", command=All_Mode_Off, width=10, height=1, bg='lightcyan')
ddd_off.pack()

empty2 = tkinter.Label(pacemaker, text="", font=("Times", 10), bg='white', justify=LEFT)
empty2.pack()
# encryption_button=tkinter.Button(pacemaker,text="Encryption",command=encryptionButton,width=10,height=1,bg='lightcyan')
# encryption_button.pack()
# validation_button=tkinter.Button(pacemaker,text="Validation",command=validationButton,width=10,height=1,bg='lightcyan')
# validation_button.pack()


# Set Heart Frame
heart = tkinter.LabelFrame(simulator, text="Heart", labelanchor="n", relief=RIDGE, borderwidth=3, bg='white', width=300,
                           height=250)
heart.pack(fill="both", expand="yes", side=LEFT)
# Heart Frame--HeartRate's button and label
heartRate_label = tkinter.Label(heart, bg='white', text='Heart Rate:')
heartRate_label.pack()


def print_heartRate(hr):
    heartRate_label.config(text='Heart Rate: ' + hr + ' bpm')

    if heartRate_scale.get() == 30:
        y_heartrate(30)
        AAI_heartrate(30)
        VVI_heartrate(30)
        DDD_heartrate(30)
        leads_failure_SA_FUN(30)
        leads_failure_AV_FUN(30)
    elif heartRate_scale.get() == 60:
        y_heartrate(60)
        AAI_heartrate(60)
        VVI_heartrate(60)
        DDD_heartrate(60)
        leads_failure_SA_FUN(60)
        leads_failure_AV_FUN(60)
    elif heartRate_scale.get() == 90:
        y_heartrate(90)
        AAI_heartrate(90)
        VVI_heartrate(90)
        DDD_heartrate(90)
        leads_failure_SA_FUN(90)
        leads_failure_AV_FUN(90)
    elif heartRate_scale.get() == 120:
        y_heartrate(120)
        AAI_heartrate(120)
        VVI_heartrate(120)
        DDD_heartrate(120)
        leads_failure_SA_FUN(120)
        leads_failure_AV_FUN(120)
    elif heartRate_scale.get() == 150:
        y_heartrate(150)
        AAI_heartrate(150)
        VVI_heartrate(150)
        DDD_heartrate(150)
        leads_failure_SA_FUN(150)
        leads_failure_AV_FUN(150)
    elif heartRate_scale.get() == 180:
        y_heartrate(180)
        AAI_heartrate(180)
        VVI_heartrate(180)
        DDD_heartrate(180)
        leads_failure_SA_FUN(180)
        leads_failure_AV_FUN(180)
heartRate_scale = tkinter.Scale(heart, from_=30, to=180, orient=tkinter.HORIZONTAL, length=400, showvalue=0.01,
                                resolution=30, tickinterval=30, command=print_heartRate, variable=var_hr,
                                bg='lightcyan')
heartRate_scale.set(60)
#heartRate_scale.place(x=0,y=100)
heartRate_scale.pack()
# Heart Frame--PRInterval's button and label

# prInterval_label = tkinter.Label(heart, bg='white', text='PRInterval')
# prInterval_label.pack()
#
#
# def print_prInterval(pr):
#     prInterval_label.config(text='PRInterval: ' + pr + ' ms')
#
# prInterval_scale = tkinter.Scale(heart, from_=0, to=1000, orient=tkinter.HORIZONTAL, length=400, showvalue=0.01,
#                                  resolution=1, tickinterval=100, command=print_prInterval, variable=var_pr,
#                                  bg='lightcyan')
# prInterval_scale.set(0)
# prInterval_scale.pack()
# Heart Frame--Reset button
empty3 = tkinter.Label(heart, text="", font=("Times", 10), bg='white', justify=LEFT)
empty3.pack()
reset = tkinter.Button(heart, text="ReSet_heartrate", command=reSetButton, width=13, height=1, bg='lightcyan')
reset.pack()

# Set Battery Frame
batteryOptions = tkinter.LabelFrame(simulator, text="Security Features", labelanchor="n", relief=RIDGE, borderwidth=3, bg='white',
                                    width=300, height=250)
batteryOptions.pack(fill="both", expand="yes", side=RIGHT, anchor=E)
# Battery Frame--Click the button to bring up a new window to view the battery consumption graph

# Battery Frame--Battery consumption in encrypted
encryption_on_button = tkinter.Button(batteryOptions, text="Encryption On", command=encryption_on, width=13, height=1,
                                      bg='lightcyan', pady=3)
encryption_on_button.pack()

encryption_off_button = tkinter.Button(batteryOptions, text="Encryption Off", command=encryption_off, width=13,
                                       height=1, bg='lightcyan', pady=3)
encryption_off_button.pack()

# Battery Frame--Battery consumption in verification
validation_on_button = tkinter.Button(batteryOptions, text="Validation On", command=verification_on, width=13, height=1,
                                      bg='lightcyan', pady=3)
validation_on_button.pack()

validation_off_button = tkinter.Button(batteryOptions, text="Validation Off", command=verification_off, width=13,
                                       height=1, bg='lightcyan', pady=3)
validation_off_button.pack()

# Set Battery Frame
battery_leadsFailure = tkinter.LabelFrame(simulator, text="Battery & Leads Failure", labelanchor="n", relief=RIDGE,
                                          borderwidth=3, bg='white', width=300, height=200)
battery_leadsFailure.pack(fill="both", expand="yes", side=RIGHT, anchor=E)
# Set Battery Frame--BatteryFailure button


batteryFailure = tkinter.Checkbutton(battery_leadsFailure, text="Battery Failure", command=batteryFailureButton,
                                     width=15, height=1, bg='white')
batteryFailure.pack(fill=Y, expand=0)  #

empty4 = tkinter.Label(battery_leadsFailure, text="", font=("Times", 10), bg='white', justify=LEFT)
empty4.pack()
# Set Battery Frame--BatteryLevel button and label
batteryLevel_label = tkinter.Label(battery_leadsFailure, bg='white', text='Battery Level')
batteryLevel_label.pack()


def print_batterylevel(bl):
    batteryLevel_label.config(text='Battery Level: ' + bl + '%'),
    # define function when battery_level is 0, it will stop
    if batteryLevel_scale.get() == 0:
        battery_level_0()
        battery_level_0_heart()
        label_power.configure(text='no power', fg='red')
    elif 0 < batteryLevel_scale.get() <= 20:
        label_power.configure(text='low power', fg='red')
    else:
        label_power.configure(text='normal battery ', fg='green')


batteryLevel_scale = tkinter.Scale(battery_leadsFailure, from_=0, to=100, orient=tkinter.HORIZONTAL, length=300,
                                   showvalue=0.01, resolution=1, tickinterval=10, command=print_batterylevel,
                                   bg='lightcyan')
batteryLevel_scale.pack()
batteryLevel_scale.set(100)  # Set initial slider position

empty5 = tkinter.Label(battery_leadsFailure, text="", font=("Times", 10), bg='white', justify=LEFT)
empty5.pack()
# Set Battery Frame--leadsFailure_SA button and label
leadsFailure_SA = tkinter.Checkbutton(battery_leadsFailure, text="Leads Failure on SA Node",
                                      command=leadsFailure_SA_Button, width=22, height=1, bg='white')
leadsFailure_SA.pack()
empty6 = tkinter.Label(battery_leadsFailure, text="", font=("Times", 10), bg='white', justify=LEFT)
empty6.pack()
# Set Battery Frame--leadsFailure_AV button and label
leadsFailure_AV = tkinter.Checkbutton(battery_leadsFailure, text="Leads Failure on AV Node",
                                      command=leadsFailure_AV_Button, width=22, height=1, bg='white')
leadsFailure_AV.pack()

simulator.mainloop()
