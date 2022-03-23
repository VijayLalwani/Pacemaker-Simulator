# Pacemaker-Simulator
Project work for CSC8208 - RESEARCH METHODS AND GROUP PROJECT IN SECURITY AND RESILIENCE

<h3>Introduction</h3>
Pacemaker simulator has been designed to simulate the pacemaker functionalities including electrocardiograph sensor, pulse generator and the status of its resources, leads and battery. It aims to provide a tool to analyse various pacing modes based in the heart conditions, security concerns with the device software, and the impact of implementing security controls on the device’s battery. It also helps to analyse the malfunctions in the device including battery and leads failure.  
<h3>Technologies</h3>
<b>Programming Language</b> - Python  
<b>Libraries</b> - Following are the key libraries utilised for the development:  
TKinter - To build the GUI graphical interface  
Matplotlib - To build the ECG and battery consumption graphs  
Numpy - To generate the data required for the ECG.  

<h3>Files</h3>
Following files are used for creating the simulator:  
1. wav.py - Defined for mathematical formula to generate P, Q, R, S waves of the heartbeat  
2. main_wav.py - To generate the ECG graph and battery consumption graph based on various pacing modes, failures and security features.  
3. simulator_edition.py - Executable file to run the simulator. This contains the various conditions and calls main_wav for generating the graphs  
<h3>Output</h3>
Below is the screenshot of the simulator. It has two panels at the top to produce ECG graph and battery consumption level. Bottom four pannels are for configuration of the pacemaker by turning it on/off, change pacing modes, change heart rate, investigate resource failures and the impact of implementing security measures.  


![alt text](https://user-images.githubusercontent.com/91553904/159562459-97cf99cd-bd5b-4f4b-bc25-ebbcd2ca6f64.png)

### Steps

**1**. Click the button "ON". the simulator will work. if you want to pause, please click the OFF button. At this point you need to click the "REBOOT "button, then click the "ON "button to restart the simulator.

**2**. Click AAI, VVI ,DDD and then you will see relevant waveform. Each time the button is selected, the battery consumption will change accordingly. In most cases, the battery is consumed in a stable standby state. click "MODE OFF" button, all of modes will end.

**3**. Click on the heart rate adjustment slider to view ECG images at different heart rates. and then you can click "Reset_heartrate" button back to 60 bpm of heartrate.

**4**. Tick the battery failure option,ECG and battery consumption will stop. if you want start again. please cancel this option, and then click "REBOOT" button, and click "ON button".

**5**. Adjust the battery level slider, you can see different battery status reminders. The fourth situation occurs when the battery level is zero. if you want start again. please recover this option, and then click "REBOOT" button, and click "ON button".

**6**. Tick the Leads failure on SA Node option, you will see relevant status on the ECG. and then you can cancel this option.

**7**. Tick the Leads failure on AV Node option, you will see relevant status on the ECG, and then you can cancel this option.

**8**. Click "encryption on" button, and then you will see the different consumption of battery. because the data will be encrypted. you can click the "encryption off" button to close encryption. and also ,"verification" has same operation.  

