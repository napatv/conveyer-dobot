# example of point series

from zmqRemoteApi import RemoteAPIClient
import numpy as np
import matplotlib.pyplot as plt
import suffering as suf
from Forlorn import plot_graphs, mk8CSV

print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')

executedMovId = 'notReady'

targetArm = '/Dobot'

stringSignalName = targetArm + '_executedMovId'

cuboidHandle = sim.getObject('/Cuboid[1]')
cuboid = []
time = []

def waitForMovementExecuted(id_):
    global executedMovId, stringSignalName
    while executedMovId != id_:
        s = sim.getStringSignal(stringSignalName)
        executedMovId = s
        pos = sim.getObjectPose(cuboidHandle,-1)
        cuboid.append(pos)
        # print(pos)
        tsim = sim.getSimulationTime()
        time.append(tsim)

# Set-up some movement variables:
# Start editing the profile -----------------------------------
times = []
t = 0.0
for i in range(0, 600, 1):
	times.append(t)
	t = t + 0.050

# Target 0, -1.25, 0.0174
# crd = suf.globaltoFrame(0, -1.25, 0.2)
crd = suf.globaltoFrame(0, -1.25, -0.01)
inv = suf.invkinec(crd.item(0), crd.item(1), crd.item(2))

crd = suf.globaltoFrame(0, -1.25, 0.2)
inv1 = suf.invkinec(crd.item(0), crd.item(1), crd.item(2))

crd = suf.globaltoFrame(0, -1.25, 0.035)
inv2 = suf.invkinec(crd.item(0), crd.item(1), crd.item(2))



sec1 = 60
sec2 = 40
sec3 = 500



j1 = []
theta = 0
rad = np.radians(theta)
j1_move = inv.item(0)/ sec1 
for i in range(0,sec1, 1):
    j1.append(rad)
    theta = theta + j1_move
    rad = np.radians(theta)

theta = 0
rad = np.radians(theta)
j1_move = inv1.item(0)/ sec2 
for i in range(0, sec2, 1):
    j1.append(rad)
    theta = theta + j1_move
    rad = np.radians(theta )

theta = 0
rad = np.radians(theta)
j1_move = inv2.item(0)/ sec3
for i in range(0, sec3, 1):
    j1.append(rad)
    theta = theta + j1_move
    rad = np.radians(theta )



j2 = []
theta = 0
rad = np.radians(theta)
j2_move = inv.item(1)/ sec1 
for i in range(0,sec1, 1):
    j2.append(rad)
    theta = theta + j2_move
    rad = np.radians(theta)
theta = 0
rad = np.radians(theta)
j2_move = inv1.item(1)/ sec2 
for i in range(0, sec2, 1):
    j2.append(rad)
    theta = theta + j2_move
    rad = np.radians(theta)
theta = 0
rad = np.radians(theta)
j2_move = inv2.item(1)/ sec3
for i in range(0, sec3, 1):
    j2.append(rad)
    theta = theta + j2_move
    rad = np.radians(theta)
rad = 0.0


j3 = []
theta = 0
rad = np.radians(theta)
j3_move = inv.item(2)/ sec1
for i in range(0,sec1, 1):
    j3.append(rad)
    theta = theta + j3_move
    rad = np.radians(theta)

theta = 0
rad = np.radians(theta)
j3_move = inv1.item(2)/ sec2
for i in range(0, sec2, 1):
    j3.append(rad)
    theta = theta + j3_move
    rad = np.radians(theta)

theta = 0
rad = np.radians(theta)
j3_move = inv2.item(2)/ sec3
for i in range(0, sec3, 1):
    j3.append(rad)
    theta = theta + j3_move
    rad = np.radians(theta)
rad = 0.0


j4 = []
theta = 0.0
for i in range(0, 300, 1):
    j4.append(theta)
    theta = theta + 0.00

theta = 0.0  
for i in range(0, 300, 1):
    j4.append(theta)
    theta = theta + 0.00


suction = []
status = 0
for i in range(0,55, 1):
    suction.append(status)
status = 1
for i in range(0,545, 1):
    suction.append(status)

# status = 0
# for i in range(0,300, 1):
# 	suction.append(status)

# End editing -----------------------------------

# Start simulation:
sim.startSimulation()

# Wait until ready:
waitForMovementExecuted('ready')

# Send the movement sequence:
movementData = {
    'id': 'movSeq1',
    'type': 'pts',
    'times': times,
    'j1': j1, 'j2': j2, 'j3': j3, 'j4': j4, 'suction': suction
}
sim.callScriptFunction(
    'remoteApi_movementDataFunction' + '@' + targetArm,
    sim.scripttype_childscript,
    movementData)

# Execute movement sequence:
sim.callScriptFunction(
    'remoteApi_executeMovement' + '@' + targetArm,
    sim.scripttype_childscript,
    'movSeq1')

# Wait until above movement sequence finished executing:
waitForMovementExecuted('movSeq1')

sim.stopSimulation()

print('Program ended')

# red dashes, blue squares and green triangles
plt.figure(1)
plt.plot(times, j1, 'r--', times, j2, 'b--', times, j3, 'g--') # plot j1, j2, j3
#plt.plot(times, suction, 'b') # suction ON/OFF

# coboid position vs time
plt.figure(2)
coboid_x = [row[0] for row in cuboid]
coboid_z = [row[1] for row in cuboid]
coboid_y = [row[2] for row in cuboid]
plt.plot(time, coboid_x, 'r--', time, coboid_y, 'b--', time, coboid_z, 'g--') # plot j1, j2, j3
plt.title('cubiod pos')
# plt.plot(time, coboid_x, 'b') # plot 2D
# mk8CSV(time, coboid_x, coboid_y, coboid_z)



# figure = plt.figure()
# ax_3d_pos = figure.add_subplot(projection='3d')
# ax_3d_pos.plot(coboid_x, coboid_y, coboid_z, lw=2, label='random')
# ax_3d_pos.set_aspect('equal', 'box')  
# plt.xlabel("z")
# plt.ylabel("y")

# coboid position(x, y, z) in 3D

#ax = plt.figure().add_subplot(projection='3d')
#ax.plot(coboid_x, coboid_y, coboid_z, 'r', zdir='z', label='coboid position(x, y, z) in 3D')
#ax.legend()
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')

# plt.show()


