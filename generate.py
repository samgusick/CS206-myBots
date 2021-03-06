import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5




# for gridx in range(5):
#     for gridy in range(5):
#         for a in range(10):
#             scale = pow(.9, a);
#             pyrosim.Send_Cube(name="Box", pos=[gridx,gridy,z+a] , size=[scale * length, scale * width, scale * height])


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[1,1,.5] , size=[1, 1, 1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1, 1, 1])
    

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])

    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5] , size=[1, 1, 1])
    
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5] , size=[1, 1, 1])



    pyrosim.End()
    
Create_World()
Create_Robot()