#lightIntensity.py
#Sergio Torres

import maya.cmds as cmds

selectionList = cmds.ls(type = "light")

for light in selectionList:
    #print "Selected Items: %s" % (selectionList)
    #print "Intensity: %s" % (objectName) 
    cmds.cutKey(objectName, time=(StartTime, EndTime), attribute = targetName)
    currentIntensity = cmds.getAttr('{0}.intensity'.format(objectName))
    cmds.setKeyframe(objectName, time = StartTime, attribute = targetName)
    newIntensity = currentIntensity * 2
    cmds.setAttr('{0}.intensity'.format(light), newIntensity)
    cmds.setKeyframe(objectName, time = EndTime, attribute = targetName)
         
         
else:
        print "Please select a light"