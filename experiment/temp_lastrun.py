#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on november 04, 2022, at 15:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'colPal'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\sarak\\OneDrive - Aarhus Universitet\\26102021\\Cog sci\\3_semester\\Perception_action\\Per-Act-EXAM\\temp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=64, interpolate=True, depth=0.0)
val = visual.ImageStim(
    win=win,
    name='val', units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, -250), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
hueSlider = visual.Slider(win=win, name='hueSlider',
    startValue=None, size=(.37, .02), pos=(0, 0.2), units=None,
    labels=None, ticks=(0, 360), granularity=0,
    style=['rating'], styleTweaks=[], opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-3, readOnly=False)
satSlider = visual.Slider(win=win, name='satSlider',
    startValue=None, size=(.02, .37), pos=(0.2, 0), units=None,
    labels=None, ticks=(0, 1), granularity=0,
    style=['rating'], styleTweaks=[], opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=True, depth=-4, readOnly=False)
valSlider = visual.Slider(win=win, name='valSlider',
    startValue=None, size=(.37, .02), pos=(0, -0.25), units=None,
    labels=None, ticks=(0,1), granularity=0,
    style=['rating'], styleTweaks=[], opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-5, readOnly=False)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, 0.35),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
from psychopy import misc

def createPalette(size):
    # Create array 
    hsv = np.ones([size,size,3], dtype=float)
    
    # Set hue
    hsv[:,:,0] = np.linspace(0,360, size, endpoint=False)
    
    # Set saturation
    for i in range(size):
        hsv[:,i, 1] = np.linspace(0,1, size, endpoint=False)
    
    # Convert to RGB
    rgb = misc.hsv2rgb(hsv)

    # Make in range 0:1 for image stim
    rgb[:][:][:] =  (rgb[:][:][:] + 1) / 2
    return rgb
 
def createValue(size):
    # Create array 
    hsv = np.zeros([20,size,3], dtype=float)
    # Set value
    hsv[:,:,2] = np.linspace(0,1, size, endpoint=False)
    # Convert to RGB
    rgb = misc.hsv2rgb(hsv)

    # Make in range 0:1 for image stim
    rgb[:][:][:] =  (rgb[:][:][:] + 1) / 2
    return rgb
    

size = 400
valBar = createValue(size) 
rgb = createPalette(size)

text_2 = visual.TextStim(win=win, name='text_2',
    text='Press space to continue',
    font='Arial',
    pos=(0, -.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "colourSelected"
colourSelectedClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setSize([size,size])
    val.setSize((size, 20))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    hueSlider.reset()
    satSlider.reset()
    valSlider.reset()
    image.setImage(rgb)
    val.setImage(valBar)
    
    
    # keep track of which components have finished
    trialComponents = [image, val, key_resp, hueSlider, satSlider, valSlider, polygon, text_2]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *val* updates
        if val.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val.frameNStart = frameN  # exact frame index
            val.tStart = t  # local t and not account for scr refresh
            val.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val, 'tStartRefresh')  # time at next scr refresh
            val.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *hueSlider* updates
        if hueSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hueSlider.frameNStart = frameN  # exact frame index
            hueSlider.tStart = t  # local t and not account for scr refresh
            hueSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hueSlider, 'tStartRefresh')  # time at next scr refresh
            hueSlider.setAutoDraw(True)
        
        # *satSlider* updates
        if satSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            satSlider.frameNStart = frameN  # exact frame index
            satSlider.tStart = t  # local t and not account for scr refresh
            satSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(satSlider, 'tStartRefresh')  # time at next scr refresh
            satSlider.setAutoDraw(True)
        
        # *valSlider* updates
        if valSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valSlider.frameNStart = frameN  # exact frame index
            valSlider.tStart = t  # local t and not account for scr refresh
            valSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valSlider, 'tStartRefresh')  # time at next scr refresh
            valSlider.setAutoDraw(True)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        h = hueSlider.getRating() or 0
        s = satSlider.getRating() or 0
        v = valSlider.getRating() or 0
        
            
        polygon.fillColor = [h,s,v]
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('val.started', val.tStartRefresh)
    trials.addData('val.stopped', val.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('hueSlider.response', hueSlider.getRating())
    trials.addData('hueSlider.rt', hueSlider.getRT())
    trials.addData('hueSlider.started', hueSlider.tStartRefresh)
    trials.addData('hueSlider.stopped', hueSlider.tStopRefresh)
    trials.addData('satSlider.response', satSlider.getRating())
    trials.addData('satSlider.rt', satSlider.getRT())
    trials.addData('satSlider.started', satSlider.tStartRefresh)
    trials.addData('satSlider.stopped', satSlider.tStopRefresh)
    trials.addData('valSlider.response', valSlider.getRating())
    trials.addData('valSlider.rt', valSlider.getRT())
    trials.addData('valSlider.started', valSlider.tStartRefresh)
    trials.addData('valSlider.stopped', valSlider.tStopRefresh)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "colourSelected"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text.text = f"Hue: {h:.2f}\nSat: {s:.2f}\nVal: {v:.2f}"
    # keep track of which components have finished
    colourSelectedComponents = [text]
    for thisComponent in colourSelectedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    colourSelectedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "colourSelected"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = colourSelectedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=colourSelectedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in colourSelectedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "colourSelected"-------
    for thisComponent in colourSelectedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
