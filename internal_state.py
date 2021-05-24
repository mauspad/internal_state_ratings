#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on May 24, 2021, at 14:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'internal_state_ratings'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='C:\\Users\\mauspad\\Desktop\\new_OEA_stuff\\ratings\\internal_state_ratings\\internal_state.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='AliceBlue', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "internal_state"
internal_stateClock = core.Clock()
IS_slider = visual.Slider(win=win, name='IS_slider',
    size=(1000, 30), pos=(0,0), units=None,
    labels=None, ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
ISlabel1 = visual.TextStim(win=win, name='ISlabel1',
    text='default text',
    font='Arial',
    pos=(-500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISlabel2 = visual.TextStim(win=win, name='ISlabel2',
    text='default text',
    font='Arial',
    pos=(500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
IS_text = visual.TextStim(win=win, name='IS_text',
    text='default text',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
##start trial counter
trialno = 0

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='You have completed the ratings :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
IS_pre = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('internal_states.xlsx'),
    seed=None, name='IS_pre')
thisExp.addLoop(IS_pre)  # add the loop to the experiment
thisIS_pre = IS_pre.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIS_pre.rgb)
if thisIS_pre != None:
    for paramName in thisIS_pre:
        exec('{} = thisIS_pre[paramName]'.format(paramName))

for thisIS_pre in IS_pre:
    currentLoop = IS_pre
    # abbreviate parameter names if possible (e.g. rgb = thisIS_pre.rgb)
    if thisIS_pre != None:
        for paramName in thisIS_pre:
            exec('{} = thisIS_pre[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "internal_state"-------
    # update component parameters for each repeat
    IS_slider.reset()
    ISlabel1.setText(LabelL)
    ISlabel2.setText(LabelR)
    IS_text.setText(Question)
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    
    ##marker display options
    IS_slider.marker.size=(.1,2)
    IS_slider.marker.color='Red'
    
    ##set initial mouse and marker positions
    mouse.setPos((-500,0))
    IS_slider.markerPos=0
    # keep track of which components have finished
    internal_stateComponents = [IS_slider, ISlabel1, ISlabel2, IS_text]
    for thisComponent in internal_stateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    internal_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "internal_state"-------
    while continueRoutine:
        # get current time
        t = internal_stateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=internal_stateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IS_slider* updates
        if IS_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_slider.frameNStart = frameN  # exact frame index
            IS_slider.tStart = t  # local t and not account for scr refresh
            IS_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_slider, 'tStartRefresh')  # time at next scr refresh
            IS_slider.setAutoDraw(True)
        
        # *ISlabel1* updates
        if ISlabel1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel1.frameNStart = frameN  # exact frame index
            ISlabel1.tStart = t  # local t and not account for scr refresh
            ISlabel1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel1, 'tStartRefresh')  # time at next scr refresh
            ISlabel1.setAutoDraw(True)
        
        # *ISlabel2* updates
        if ISlabel2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel2.frameNStart = frameN  # exact frame index
            ISlabel2.tStart = t  # local t and not account for scr refresh
            ISlabel2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel2, 'tStartRefresh')  # time at next scr refresh
            ISlabel2.setAutoDraw(True)
        
        # *IS_text* updates
        if IS_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_text.frameNStart = frameN  # exact frame index
            IS_text.tStart = t  # local t and not account for scr refresh
            IS_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_text, 'tStartRefresh')  # time at next scr refresh
            IS_text.setAutoDraw(True)
        ##tie marker to mouse position
        x = mouse.getPos()[0]
        IS_slider.markerPos=500 + (x)
        
        #this is super lazy, it only works because the script runs line by line
        #so if each condition is not filled it passes to the next (easier to
        #fulfill) one
        if mouse.getPressed()[0]:
            if trialno > 9:
                IS_post.addData('ISval_post', (IS_slider.markerPos / 10))
                continueRoutine = False
            elif trialno > 4:
                IS_drink.addData('ISval_drink', (IS_slider.markerPos / 10))
                continueRoutine = False
            elif trialno <= 4:
                IS_pre.addData('ISval_pre', (IS_slider.markerPos / 10))
                continueRoutine = False
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in internal_stateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "internal_state"-------
    for thisComponent in internal_stateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ##take a nap to help prevent accidental double-clicks
    trialno += 1
    print(trialno)
    core.wait(0.5)
    # the Routine "internal_state" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IS_pre'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [done]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    if done.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            done.tStop = t  # not accounting for scr refresh
            done.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done, 'tStopRefresh')  # time at next scr refresh
            done.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
