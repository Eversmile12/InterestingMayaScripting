import maya.cmds as cmds

jointlist = cmds.ls(type="joint")

for joint in jointlist:
    cmds.setAttr(joint+".rotateOrder", 0)