#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 06, 2023, at 19:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'ETproject_Chi_2023.1.1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='C:\\Users\\LangCog\\Desktop\\Erxiao Wang & Wanjun Xiong\\2023Fall_psychopy\\et-project_chi\\ETproject_Chi_2023.1.1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.gazepoint.gp3.EyeTracker'] = {
    'name': 'tracker',
    'network_settings': {
        'ip_address': '192.168.56.1',
        'port': 4242.0
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='ETproject_Chi_2023.1.1', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Intro1" ---
intro_1 = visual.TextStim(win=win, name='intro_1',
    text='Tasks',
    font='NanumGothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "intro2" ---
intro_2 = visual.TextStim(win=win, name='intro_2',
    text='感谢您参与实验。\n本实验旨在探究时间用语与空间概念之间的联系。\n当您准备好开始时，请按空格键。\n\nHello!\nThank you for participating in the experiment.\nThis experiment is to find out the temporal representation of time.\nIf you want to continue, press the spacebar.\n',
    font='NanumGothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro2_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intro3" ---
Intro_3 = visual.TextStim(win=win, name='Intro_3',
    text='接下来您将会看到一些时间词语\n您需要根据提示选出更早或更晚的时间。\n请根据正确答案在屏幕上的位置的位置，按下对应的按键\n（如：“上”，“下”，“左”，“右”）\n如果您已了解规则，请按空格键。\n\nNext, you will see some time words.\nYou will select the earlier or later time based on the prompts.\nPlease press the corresponding arrow key according to the correct answer\'s position on the screen\n(for example: "Up", "Down", "Left", "Right").\nIf you understand the rules, please press the spacebar.',
    font='NanumGothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro3_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Prac_intro" ---
pracintro = visual.TextStim(win=win, name='pracintro',
    text='',
    font='NanumGothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
pracintro_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Practice" ---
# Run 'Begin Experiment' code from code
prac_count = 0
msg_intro = "在参与实验之前，我们先进行练习。 \n\n 为了通过练习，您必须在练习中答对 90%。 \n\n 如果您已理解，请按空格键以开始。 \n\nBefore participating in the experiment, we will pratice first.  \n\n In order to start the experiment, you must get at least 90% correct in the practice round. \n\n If you understand the explanation, please press the space bar. "

net_pos_x = 0
net_pos_y = 0
clicked_net = []
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "solution" ---
early = visual.TextStim(win=win, name='early',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RESP = keyboard.Keyboard()
late = visual.TextStim(win=win, name='late',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from code_2
msg = ''
loop_o = 0
number_correct = 0
pracfeedback = visual.TextStim(win=win, name='pracfeedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Prac_check" ---

# --- Initialize components for Routine "intro5" ---
intro_5 = visual.TextStim(win=win, name='intro_5',
    text="现在，让我们开始实验。\n准备就绪后，按空格键以开始实验。\n\nNow, let's start the experiment.\nWhen you're ready, press the spacebar to start the experiment.",
    font='NanumGothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro5_resp = keyboard.Keyboard()

# --- Initialize components for Routine "baseline" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='现在请您注视屏幕上即将出现的符号，我们将进行校准',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
baselinerecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "BLOCK" ---
main_image_2 = visual.ImageStim(
    win=win,
    name='main_image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
main_early = visual.TextStim(win=win, name='main_early',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ct_resp = keyboard.Keyboard()
main_late = visual.TextStim(win=win, name='main_late',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "BREAK" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fengjing = visual.ImageStim(
    win=win,
    name='fengjing', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,1.5],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='是',
    font='Open Sans',
    pos=(-0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='否',
    font='Open Sans',
    pos=(0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for validation
validationTarget = visual.TargetStim(win, 
    name='validationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for validation
validation = iohub.ValidationProcedure(win,
    target=validationTarget,
    gaze_cursor='green', 
    positions='NINE_POINTS', randomize_positions=True,
    expand_scale=1.5, target_duration=1.5,
    enable_position_animation=True, target_delay=1.0,
    progress_on_key=None, text_color='auto',
    show_results_screen=True, save_results_screen=True,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Intro1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Intro1Components = [intro_1]
for thisComponent in Intro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Intro1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_1* updates
    
    # if intro_1 is starting this frame...
    if intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1.frameNStart = frameN  # exact frame index
        intro_1.tStart = t  # local t and not account for scr refresh
        intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_1.started')
        # update status
        intro_1.status = STARTED
        intro_1.setAutoDraw(True)
    
    # if intro_1 is active this frame...
    if intro_1.status == STARTED:
        # update params
        pass
    
    # if intro_1 is stopping this frame...
    if intro_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > intro_1.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            intro_1.tStop = t  # not accounting for scr refresh
            intro_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_1.stopped')
            # update status
            intro_1.status = FINISHED
            intro_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Intro1" ---
for thisComponent in Intro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "intro2" ---
continueRoutine = True
# update component parameters for each repeat
intro2_resp.keys = []
intro2_resp.rt = []
_intro2_resp_allKeys = []
# keep track of which components have finished
intro2Components = [intro_2, intro2_resp]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_2* updates
    
    # if intro_2 is starting this frame...
    if intro_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_2.frameNStart = frameN  # exact frame index
        intro_2.tStart = t  # local t and not account for scr refresh
        intro_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_2.started')
        # update status
        intro_2.status = STARTED
        intro_2.setAutoDraw(True)
    
    # if intro_2 is active this frame...
    if intro_2.status == STARTED:
        # update params
        pass
    
    # *intro2_resp* updates
    waitOnFlip = False
    
    # if intro2_resp is starting this frame...
    if intro2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro2_resp.frameNStart = frameN  # exact frame index
        intro2_resp.tStart = t  # local t and not account for scr refresh
        intro2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro2_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro2_resp.started')
        # update status
        intro2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro2_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro2_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro2_resp_allKeys.extend(theseKeys)
        if len(_intro2_resp_allKeys):
            intro2_resp.keys = _intro2_resp_allKeys[-1].name  # just the last key pressed
            intro2_resp.rt = _intro2_resp_allKeys[-1].rt
            intro2_resp.duration = _intro2_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro2" ---
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro2_resp.keys in ['', [], None]:  # No response was made
    intro2_resp.keys = None
thisExp.addData('intro2_resp.keys',intro2_resp.keys)
if intro2_resp.keys != None:  # we had a response
    thisExp.addData('intro2_resp.rt', intro2_resp.rt)
    thisExp.addData('intro2_resp.duration', intro2_resp.duration)
thisExp.nextEntry()
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro3" ---
continueRoutine = True
# update component parameters for each repeat
intro3_resp.keys = []
intro3_resp.rt = []
_intro3_resp_allKeys = []
# keep track of which components have finished
intro3Components = [Intro_3, intro3_resp]
for thisComponent in intro3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_3* updates
    
    # if Intro_3 is starting this frame...
    if Intro_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_3.frameNStart = frameN  # exact frame index
        Intro_3.tStart = t  # local t and not account for scr refresh
        Intro_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Intro_3.started')
        # update status
        Intro_3.status = STARTED
        Intro_3.setAutoDraw(True)
    
    # if Intro_3 is active this frame...
    if Intro_3.status == STARTED:
        # update params
        pass
    
    # *intro3_resp* updates
    waitOnFlip = False
    
    # if intro3_resp is starting this frame...
    if intro3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro3_resp.frameNStart = frameN  # exact frame index
        intro3_resp.tStart = t  # local t and not account for scr refresh
        intro3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro3_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro3_resp.started')
        # update status
        intro3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro3_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro3_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro3_resp_allKeys.extend(theseKeys)
        if len(_intro3_resp_allKeys):
            intro3_resp.keys = _intro3_resp_allKeys[-1].name  # just the last key pressed
            intro3_resp.rt = _intro3_resp_allKeys[-1].rt
            intro3_resp.duration = _intro3_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro3" ---
for thisComponent in intro3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro3_resp.keys in ['', [], None]:  # No response was made
    intro3_resp.keys = None
thisExp.addData('intro3_resp.keys',intro3_resp.keys)
if intro3_resp.keys != None:  # we had a response
    thisExp.addData('intro3_resp.rt', intro3_resp.rt)
    thisExp.addData('intro3_resp.duration', intro3_resp.duration)
thisExp.nextEntry()
# the Routine "intro3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_block = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='prac_block')
thisExp.addLoop(prac_block)  # add the loop to the experiment
thisPrac_block = prac_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
if thisPrac_block != None:
    for paramName in thisPrac_block:
        exec('{} = thisPrac_block[paramName]'.format(paramName))

for thisPrac_block in prac_block:
    currentLoop = prac_block
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
    if thisPrac_block != None:
        for paramName in thisPrac_block:
            exec('{} = thisPrac_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Prac_intro" ---
    continueRoutine = True
    # update component parameters for each repeat
    pracintro.setText(msg_intro)
    pracintro_resp.keys = []
    pracintro_resp.rt = []
    _pracintro_resp_allKeys = []
    # keep track of which components have finished
    Prac_introComponents = [pracintro, pracintro_resp]
    for thisComponent in Prac_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prac_intro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracintro* updates
        
        # if pracintro is starting this frame...
        if pracintro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracintro.frameNStart = frameN  # exact frame index
            pracintro.tStart = t  # local t and not account for scr refresh
            pracintro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracintro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracintro.started')
            # update status
            pracintro.status = STARTED
            pracintro.setAutoDraw(True)
        
        # if pracintro is active this frame...
        if pracintro.status == STARTED:
            # update params
            pass
        
        # *pracintro_resp* updates
        waitOnFlip = False
        
        # if pracintro_resp is starting this frame...
        if pracintro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracintro_resp.frameNStart = frameN  # exact frame index
            pracintro_resp.tStart = t  # local t and not account for scr refresh
            pracintro_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracintro_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracintro_resp.started')
            # update status
            pracintro_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracintro_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracintro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracintro_resp.status == STARTED and not waitOnFlip:
            theseKeys = pracintro_resp.getKeys(keyList=['space'], waitRelease=False)
            _pracintro_resp_allKeys.extend(theseKeys)
            if len(_pracintro_resp_allKeys):
                pracintro_resp.keys = _pracintro_resp_allKeys[-1].name  # just the last key pressed
                pracintro_resp.rt = _pracintro_resp_allKeys[-1].rt
                pracintro_resp.duration = _pracintro_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prac_intro" ---
    for thisComponent in Prac_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracintro_resp.keys in ['', [], None]:  # No response was made
        pracintro_resp.keys = None
    prac_block.addData('pracintro_resp.keys',pracintro_resp.keys)
    if pracintro_resp.keys != None:  # we had a response
        prac_block.addData('pracintro_resp.rt', pracintro_resp.rt)
        prac_block.addData('pracintro_resp.duration', pracintro_resp.duration)
    # the Routine "Prac_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Practice_Chi.xlsx'),
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
        
        # --- Prepare to start Routine "Practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(Instruction_stim)
        # keep track of which components have finished
        PracticeComponents = [image]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Practice" ---
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "solution" ---
        continueRoutine = True
        # update component parameters for each repeat
        early.setPos(early_position)
        early.setText(earlier_stim)
        RESP.keys = []
        RESP.rt = []
        _RESP_allKeys = []
        late.setPos(late_position)
        late.setText(later_stim)
        # keep track of which components have finished
        solutionComponents = [early, RESP, late]
        for thisComponent in solutionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "solution" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *early* updates
            
            # if early is starting this frame...
            if early.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                early.frameNStart = frameN  # exact frame index
                early.tStart = t  # local t and not account for scr refresh
                early.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(early, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'early.started')
                # update status
                early.status = STARTED
                early.setAutoDraw(True)
            
            # if early is active this frame...
            if early.status == STARTED:
                # update params
                pass
            
            # if early is stopping this frame...
            if early.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > early.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    early.tStop = t  # not accounting for scr refresh
                    early.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'early.stopped')
                    # update status
                    early.status = FINISHED
                    early.setAutoDraw(False)
            
            # *RESP* updates
            waitOnFlip = False
            
            # if RESP is starting this frame...
            if RESP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RESP.frameNStart = frameN  # exact frame index
                RESP.tStart = t  # local t and not account for scr refresh
                RESP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RESP, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RESP.started')
                # update status
                RESP.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RESP.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RESP.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if RESP is stopping this frame...
            if RESP.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RESP.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RESP.tStop = t  # not accounting for scr refresh
                    RESP.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RESP.stopped')
                    # update status
                    RESP.status = FINISHED
                    RESP.status = FINISHED
            if RESP.status == STARTED and not waitOnFlip:
                theseKeys = RESP.getKeys(keyList=['left','right','up','down'], waitRelease=False)
                _RESP_allKeys.extend(theseKeys)
                if len(_RESP_allKeys):
                    RESP.keys = _RESP_allKeys[-1].name  # just the last key pressed
                    RESP.rt = _RESP_allKeys[-1].rt
                    RESP.duration = _RESP_allKeys[-1].duration
                    # was this correct?
                    if (RESP.keys == str(corr_resp)) or (RESP.keys == corr_resp):
                        RESP.corr = 1
                    else:
                        RESP.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *late* updates
            
            # if late is starting this frame...
            if late.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                late.frameNStart = frameN  # exact frame index
                late.tStart = t  # local t and not account for scr refresh
                late.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(late, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'late.started')
                # update status
                late.status = STARTED
                late.setAutoDraw(True)
            
            # if late is active this frame...
            if late.status == STARTED:
                # update params
                pass
            
            # if late is stopping this frame...
            if late.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > late.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    late.tStop = t  # not accounting for scr refresh
                    late.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'late.stopped')
                    # update status
                    late.status = FINISHED
                    late.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in solutionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "solution" ---
        for thisComponent in solutionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        loop_o += 1
        
        
        if RESP.corr == 1:
            number_correct = number_correct + 1
            msg ='Correct! \nScore = %.1f%%' %(number_correct*100/loop_o)
            msgColor = 'green'
                
        else:
            msg ='Oops! That was wrong \nScore = %.1f%%' %(number_correct*100/loop_o)
            msgColor = 'red'
        
        
        pracfeedback.setColor(msgColor, colorSpace='rgb')
        pracfeedback.setText(msg)
        # keep track of which components have finished
        feedbackComponents = [pracfeedback]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pracfeedback* updates
            
            # if pracfeedback is starting this frame...
            if pracfeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pracfeedback.frameNStart = frameN  # exact frame index
                pracfeedback.tStart = t  # local t and not account for scr refresh
                pracfeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pracfeedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracfeedback.started')
                # update status
                pracfeedback.status = STARTED
                pracfeedback.setAutoDraw(True)
            
            # if pracfeedback is active this frame...
            if pracfeedback.status == STARTED:
                # update params
                pass
            
            # if pracfeedback is stopping this frame...
            if pracfeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pracfeedback.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    pracfeedback.tStop = t  # not accounting for scr refresh
                    pracfeedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pracfeedback.stopped')
                    # update status
                    pracfeedback.status = FINISHED
                    pracfeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "Prac_check" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    if number_correct*100/loop_o >= 0.8: 
        prac_block.finished = True
    else:
            prac_block.finished = False
            msg_intro = "我们再练习一次！\n\n Let's do it again! \nTo continue, please press space bar. "
    # keep track of which components have finished
    Prac_checkComponents = []
    for thisComponent in Prac_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prac_check" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prac_check" ---
    for thisComponent in Prac_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Prac_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'prac_block'


# --- Prepare to start Routine "intro5" ---
continueRoutine = True
# update component parameters for each repeat
intro5_resp.keys = []
intro5_resp.rt = []
_intro5_resp_allKeys = []
# keep track of which components have finished
intro5Components = [intro_5, intro5_resp]
for thisComponent in intro5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro5" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_5* updates
    
    # if intro_5 is starting this frame...
    if intro_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_5.frameNStart = frameN  # exact frame index
        intro_5.tStart = t  # local t and not account for scr refresh
        intro_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_5.started')
        # update status
        intro_5.status = STARTED
        intro_5.setAutoDraw(True)
    
    # if intro_5 is active this frame...
    if intro_5.status == STARTED:
        # update params
        pass
    
    # *intro5_resp* updates
    waitOnFlip = False
    
    # if intro5_resp is starting this frame...
    if intro5_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro5_resp.frameNStart = frameN  # exact frame index
        intro5_resp.tStart = t  # local t and not account for scr refresh
        intro5_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro5_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro5_resp.started')
        # update status
        intro5_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro5_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro5_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro5_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro5_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro5_resp_allKeys.extend(theseKeys)
        if len(_intro5_resp_allKeys):
            intro5_resp.keys = _intro5_resp_allKeys[-1].name  # just the last key pressed
            intro5_resp.rt = _intro5_resp_allKeys[-1].rt
            intro5_resp.duration = _intro5_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro5" ---
for thisComponent in intro5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro5_resp.keys in ['', [], None]:  # No response was made
    intro5_resp.keys = None
thisExp.addData('intro5_resp.keys',intro5_resp.keys)
if intro5_resp.keys != None:  # we had a response
    thisExp.addData('intro5_resp.rt', intro5_resp.rt)
    thisExp.addData('intro5_resp.duration', intro5_resp.duration)
thisExp.nextEntry()
# the Routine "intro5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "baseline" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = [text_4, text_5, baselinerecord]
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "baseline" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # *text_5* updates
    
    # if text_5 is starting this frame...
    if text_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        # update status
        text_5.status = STARTED
        text_5.setAutoDraw(True)
    
    # if text_5 is active this frame...
    if text_5.status == STARTED:
        # update params
        pass
    
    # if text_5 is stopping this frame...
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.stopped')
            # update status
            text_5.status = FINISHED
            text_5.setAutoDraw(False)
    # *baselinerecord* updates
    
    # if baselinerecord is starting this frame...
    if baselinerecord.status == NOT_STARTED and t >= 2-frameTolerance:
        # keep track of start time/frame for later
        baselinerecord.frameNStart = frameN  # exact frame index
        baselinerecord.tStart = t  # local t and not account for scr refresh
        baselinerecord.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(baselinerecord, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('baselinerecord.started', t)
        # update status
        baselinerecord.status = STARTED
    
    # if baselinerecord is stopping this frame...
    if baselinerecord.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > baselinerecord.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            baselinerecord.tStop = t  # not accounting for scr refresh
            baselinerecord.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('baselinerecord.stopped', t)
            # update status
            baselinerecord.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "baseline" ---
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if baselinerecord.status != FINISHED:
    baselinerecord.status = FINISHED
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks/Block 1.csv'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in block1:
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "BLOCK" ---
    continueRoutine = True
    # update component parameters for each repeat
    main_image_2.setImage(Instruction_stim)
    main_early.setPos(early_position)
    main_early.setText(earlier_stim)
    ct_resp.keys = []
    ct_resp.rt = []
    _ct_resp_allKeys = []
    main_late.setPos(late_position)
    main_late.setText(later_stim)
    # keep track of which components have finished
    BLOCKComponents = [main_image_2, main_early, ct_resp, main_late, fix, etRecord]
    for thisComponent in BLOCKComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLOCK" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_image_2* updates
        
        # if main_image_2 is starting this frame...
        if main_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_image_2.frameNStart = frameN  # exact frame index
            main_image_2.tStart = t  # local t and not account for scr refresh
            main_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_image_2.started')
            # update status
            main_image_2.status = STARTED
            main_image_2.setAutoDraw(True)
        
        # if main_image_2 is active this frame...
        if main_image_2.status == STARTED:
            # update params
            pass
        
        # if main_image_2 is stopping this frame...
        if main_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > main_image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                main_image_2.tStop = t  # not accounting for scr refresh
                main_image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_image_2.stopped')
                # update status
                main_image_2.status = FINISHED
                main_image_2.setAutoDraw(False)
        
        # *main_early* updates
        
        # if main_early is starting this frame...
        if main_early.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            main_early.frameNStart = frameN  # exact frame index
            main_early.tStart = t  # local t and not account for scr refresh
            main_early.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_early, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_early.started')
            # update status
            main_early.status = STARTED
            main_early.setAutoDraw(True)
        
        # if main_early is active this frame...
        if main_early.status == STARTED:
            # update params
            pass
        
        # if main_early is stopping this frame...
        if main_early.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > main_early.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                main_early.tStop = t  # not accounting for scr refresh
                main_early.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_early.stopped')
                # update status
                main_early.status = FINISHED
                main_early.setAutoDraw(False)
        
        # *ct_resp* updates
        waitOnFlip = False
        
        # if ct_resp is starting this frame...
        if ct_resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ct_resp.frameNStart = frameN  # exact frame index
            ct_resp.tStart = t  # local t and not account for scr refresh
            ct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct_resp.started')
            # update status
            ct_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ct_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if ct_resp is stopping this frame...
        if ct_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ct_resp.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                ct_resp.tStop = t  # not accounting for scr refresh
                ct_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct_resp.stopped')
                # update status
                ct_resp.status = FINISHED
                ct_resp.status = FINISHED
        if ct_resp.status == STARTED and not waitOnFlip:
            theseKeys = ct_resp.getKeys(keyList=['left','right','up','down'], waitRelease=False)
            _ct_resp_allKeys.extend(theseKeys)
            if len(_ct_resp_allKeys):
                ct_resp.keys = _ct_resp_allKeys[-1].name  # just the last key pressed
                ct_resp.rt = _ct_resp_allKeys[-1].rt
                ct_resp.duration = _ct_resp_allKeys[-1].duration
                # was this correct?
                if (ct_resp.keys == str(corr_resp)) or (ct_resp.keys == corr_resp):
                    ct_resp.corr = 1
                else:
                    ct_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *main_late* updates
        
        # if main_late is starting this frame...
        if main_late.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            main_late.frameNStart = frameN  # exact frame index
            main_late.tStart = t  # local t and not account for scr refresh
            main_late.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_late, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_late.started')
            # update status
            main_late.status = STARTED
            main_late.setAutoDraw(True)
        
        # if main_late is active this frame...
        if main_late.status == STARTED:
            # update params
            pass
        
        # if main_late is stopping this frame...
        if main_late.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > main_late.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                main_late.tStop = t  # not accounting for scr refresh
                main_late.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_late.stopped')
                # update status
                main_late.status = FINISHED
                main_late.setAutoDraw(False)
        
        # *fix* updates
        
        # if fix is starting this frame...
        if fix.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix.started')
            # update status
            fix.status = STARTED
            fix.setAutoDraw(True)
        
        # if fix is active this frame...
        if fix.status == STARTED:
            # update params
            pass
        
        # if fix is stopping this frame...
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.stopped')
                # update status
                fix.status = FINISHED
                fix.setAutoDraw(False)
        # *etRecord* updates
        
        # if etRecord is starting this frame...
        if etRecord.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord.started', t)
            # update status
            etRecord.status = STARTED
        
        # if etRecord is stopping this frame...
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord.stopped', t)
                # update status
                etRecord.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLOCKComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLOCK" ---
    for thisComponent in BLOCKComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ct_resp.keys in ['', [], None]:  # No response was made
        ct_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           ct_resp.corr = 1;  # correct non-response
        else:
           ct_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block1 (TrialHandler)
    block1.addData('ct_resp.keys',ct_resp.keys)
    block1.addData('ct_resp.corr', ct_resp.corr)
    if ct_resp.keys != None:  # we had a response
        block1.addData('ct_resp.rt', ct_resp.rt)
        block1.addData('ct_resp.duration', ct_resp.duration)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block1'


# set up handler to look after randomisation of conditions etc
break1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Break_material/Break_chi.xlsx', selection='0:7'),
    seed=None, name='break1')
thisExp.addLoop(break1)  # add the loop to the experiment
thisBreak1 = break1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBreak1.rgb)
if thisBreak1 != None:
    for paramName in thisBreak1:
        exec('{} = thisBreak1[paramName]'.format(paramName))

for thisBreak1 in break1:
    currentLoop = break1
    # abbreviate parameter names if possible (e.g. rgb = thisBreak1.rgb)
    if thisBreak1 != None:
        for paramName in thisBreak1:
            exec('{} = thisBreak1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "BREAK" ---
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(Qustion)
    fengjing.setImage(Path)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    BREAKComponents = [text, fengjing, key_resp, text_2, text_3]
    for thisComponent in BREAKComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BREAK" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 11.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # *fengjing* updates
        
        # if fengjing is starting this frame...
        if fengjing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fengjing.frameNStart = frameN  # exact frame index
            fengjing.tStart = t  # local t and not account for scr refresh
            fengjing.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fengjing, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fengjing.started')
            # update status
            fengjing.status = STARTED
            fengjing.setAutoDraw(True)
        
        # if fengjing is active this frame...
        if fengjing.status == STARTED:
            # update params
            pass
        
        # if fengjing is stopping this frame...
        if fengjing.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fengjing.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fengjing.tStop = t  # not accounting for scr refresh
                fengjing.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fengjing.stopped')
                # update status
                fengjing.status = FINISHED
                fengjing.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp is stopping this frame...
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                # update status
                key_resp.status = FINISHED
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # was this correct?
                if (key_resp.keys == str('CorrAns')) or (key_resp.keys == 'CorrAns'):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BREAKComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BREAK" ---
    for thisComponent in BREAKComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str('CorrAns').lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for break1 (TrialHandler)
    break1.addData('key_resp.keys',key_resp.keys)
    break1.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        break1.addData('key_resp.rt', key_resp.rt)
        break1.addData('key_resp.duration', key_resp.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-11.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'break1'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
