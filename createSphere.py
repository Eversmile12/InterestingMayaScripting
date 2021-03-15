import maya.cmds as cmds

#Create a polysphere
cmds.polySphere()

#Create a polysphere setting the radius to 10
cmds.polySphere(radius = 10)

#Print polysphere help docs
cmds.help("polySphere")

#Query polysphere radius
cmds.polySphere(query=True, radius=True)

#Edit polysphere radius
cmds.polySphere(edit=True, radius=2)

#List specified items -> cameras
cmds.ls(cameras=True)

#List ls related cmds
cmds.help("ls")

#List items in selection
cmds.ls(selection=True)

cmds.select("pSphere4")

#Add item to selection
cmds.select("pPlane1", add=True)

cmds.ls(selection = True)