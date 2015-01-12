import bge

#frequently Used Variables
cont = bge.logic.getCurrentScene()
objPlayer = cont.objects["Player"]
objSun = cont.objects["Sun"]

def main():
    
    movement()
    

def movement():
    
    #frequently Used Variables Inside movement()
    keyboard = bge.logic.keyboard
    forwardSpeed = 0.08
    backwardSpeed = 0.04
    leftwardSpeed = 0.04
    rightwardSpeed = 0.04
    jumpHeight = 1
    
    #sensors
    onGround = objPlayer.sensors["onGround"]
    playerRefresh = objPlayer.sensors["playerRefresh"]
    
    #actuators
    
    #property
    
    #keyboard Key Actions
    wKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]
    wKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.WKEY]
    aKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]
    aKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.AKEY]
    sKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]
    sKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.SKEY]
    dKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]
    dKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.DKEY]
    shiftKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTSHIFTKEY]
    spaceKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]
    spaceKeyJustDown = bge.logic.KX_INPUT_JUST_ACTIVATED == keyboard.events[bge.events.SPACEKEY]
    
    #jumping
    if spaceKeyJustDown and onGround.positive:
        objPlayer.applyForce((0,0,jumpHeight*250*objPlayer.mass),True)
            
    #movement
    if wKeyDown and shiftKeyDown:
        objPlayer.applyMovement((forwardSpeed*2,0,0),True)
    elif wKeyDown:
        objPlayer.applyMovement((forwardSpeed,0,0),True)
        
    if sKeyDown and shiftKeyDown:
        objPlayer.applyMovement((-backwardSpeed*2,0,0),True)
    elif sKeyDown:
        objPlayer.applyMovement((-backwardSpeed,0,0),True)
    
    if aKeyDown and shiftKeyDown:
        objPlayer.applyMovement((0,leftwardSpeed*2,0),True)
    elif aKeyDown:
        objPlayer.applyMovement((0,leftwardSpeed,0),True)
    
    if dKeyDown and shiftKeyDown:
        objPlayer.applyMovement((0,-rightwardSpeed*2,0),True)
    elif dKeyDown:
        objPlayer.applyMovement((0,-rightwardSpeed,0),True)
    
    
    