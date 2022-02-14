import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

programRunTime = 100

backLegSensorValues = numpy.zeros(programRunTime)
frontLegSensorValues = numpy.zeros(programRunTime)

for x in range(programRunTime):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)

print(backLegSensorValues)
numpy.save('data\\backLegSensorValues.npy', backLegSensorValues)
numpy.save('data\\frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
