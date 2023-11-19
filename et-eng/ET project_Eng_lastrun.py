#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Tue Nov  7 22:00:57 2023
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'ET eng'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'gender': '',
    'age': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/Tracey/Desktop/Teachers College Columbia/Gordon Lab/Temporal spacial/Psychopy/et_eng/ET project_Eng_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.DEBUG)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1470, 956], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Intro1" ---
    intro_1 = visual.TextStim(win=win, name='intro_1',
        text=' Temporal-Spatial Task',
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Intro2" ---
    intro_2 = visual.TextStim(win=win, name='intro_2',
        text='\nHello!\nThank you for participating in the experiment.\nThis experiment is to find out temporal representation of time.\nIf you want to continue, press the spacebar.\n',
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro2_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Intro3" ---
    Intro_3 = visual.TextStim(win=win, name='Intro_3',
        text='\nIn a moment, you will be presented with a series of  time words. After the question, the two time words will be presented on the screen. \nPlease press the corresponding key (eg, ‘up’, ‘down’, ‘left’, ‘right’) according to the location of the correct answer.\nIf you understand the rules, press the spacebar.',
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro3_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Intro4" ---
    Intro_4 = visual.TextStim(win=win, name='Intro_4',
        text='\nPlease respond as quickly and error-free as possible.\nIf you are ready to experiment, press the space bar.',
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro4_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Prac_intro" ---
    pracintro = visual.TextStim(win=win, name='pracintro',
        text='',
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    pracintro_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practrial" ---
    # Run 'Begin Experiment' code from code
    prac_count = 0
    msg_intro = " \n\nBefore participating in the experiment, we will pratice first.  \n\n In order to start the experiment, you must get at least 90% correct in the practice round. \n\n If you understand the explanation, please press the space bar. "
    
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.7, 0.4),
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
        text="\nNow, let's start the experiment.\nWhen you're ready, press the spacebar to start the experiment.",
        font='NanumGothic',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro5_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "block" ---
    main_image = visual.ImageStim(
        win=win,
        name='main_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    main_early1 = visual.TextStim(win=win, name='main_early1',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp1 = keyboard.Keyboard()
    main_late1 = visual.TextStim(win=win, name='main_late1',
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
    
    # --- Initialize components for Routine "break_2" ---
    question = visual.TextStim(win=win, name='question',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
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
    Yes = visual.TextStim(win=win, name='Yes',
        text='Yes',
        font='Open Sans',
        pos=(-0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    no = visual.TextStim(win=win, name='no',
        text='No',
        font='Open Sans',
        pos=(0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "block" ---
    main_image = visual.ImageStim(
        win=win,
        name='main_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    main_early1 = visual.TextStim(win=win, name='main_early1',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp1 = keyboard.Keyboard()
    main_late1 = visual.TextStim(win=win, name='main_late1',
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
    
    # --- Initialize components for Routine "break_2" ---
    question = visual.TextStim(win=win, name='question',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
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
    Yes = visual.TextStim(win=win, name='Yes',
        text='Yes',
        font='Open Sans',
        pos=(-0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    no = visual.TextStim(win=win, name='no',
        text='No',
        font='Open Sans',
        pos=(0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "block" ---
    main_image = visual.ImageStim(
        win=win,
        name='main_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    main_early1 = visual.TextStim(win=win, name='main_early1',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp1 = keyboard.Keyboard()
    main_late1 = visual.TextStim(win=win, name='main_late1',
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
    
    # --- Initialize components for Routine "break_2" ---
    question = visual.TextStim(win=win, name='question',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
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
    Yes = visual.TextStim(win=win, name='Yes',
        text='Yes',
        font='Open Sans',
        pos=(-0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    no = visual.TextStim(win=win, name='no',
        text='No',
        font='Open Sans',
        pos=(0.3,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "block" ---
    main_image = visual.ImageStim(
        win=win,
        name='main_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    main_early1 = visual.TextStim(win=win, name='main_early1',
        text='',
        font='Open Sans',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp1 = keyboard.Keyboard()
    main_late1 = visual.TextStim(win=win, name='main_late1',
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
    
    # --- Initialize components for Routine "The_end" ---
    theend = visual.TextStim(win=win, name='theend',
        text='非常感谢您的参与。\n\nThanks for participating the experiment. ',
        font='NanumGothic',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Intro1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro1.started', globalClock.getTime())
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
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    thisExp.addData('Intro1.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Intro2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro2.started', globalClock.getTime())
    intro2_resp.keys = []
    intro2_resp.rt = []
    _intro2_resp_allKeys = []
    # keep track of which components have finished
    Intro2Components = [intro_2, intro2_resp]
    for thisComponent in Intro2Components:
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
    
    # --- Run Routine "Intro2" ---
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
            theseKeys = intro2_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro2_resp_allKeys.extend(theseKeys)
            if len(_intro2_resp_allKeys):
                intro2_resp.keys = _intro2_resp_allKeys[-1].name  # just the last key pressed
                intro2_resp.rt = _intro2_resp_allKeys[-1].rt
                intro2_resp.duration = _intro2_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro2" ---
    for thisComponent in Intro2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro2.stopped', globalClock.getTime())
    # check responses
    if intro2_resp.keys in ['', [], None]:  # No response was made
        intro2_resp.keys = None
    thisExp.addData('intro2_resp.keys',intro2_resp.keys)
    if intro2_resp.keys != None:  # we had a response
        thisExp.addData('intro2_resp.rt', intro2_resp.rt)
        thisExp.addData('intro2_resp.duration', intro2_resp.duration)
    thisExp.nextEntry()
    # the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Intro3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro3.started', globalClock.getTime())
    intro3_resp.keys = []
    intro3_resp.rt = []
    _intro3_resp_allKeys = []
    # keep track of which components have finished
    Intro3Components = [Intro_3, intro3_resp]
    for thisComponent in Intro3Components:
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
    
    # --- Run Routine "Intro3" ---
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
            theseKeys = intro3_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro3_resp_allKeys.extend(theseKeys)
            if len(_intro3_resp_allKeys):
                intro3_resp.keys = _intro3_resp_allKeys[-1].name  # just the last key pressed
                intro3_resp.rt = _intro3_resp_allKeys[-1].rt
                intro3_resp.duration = _intro3_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro3" ---
    for thisComponent in Intro3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro3.stopped', globalClock.getTime())
    # check responses
    if intro3_resp.keys in ['', [], None]:  # No response was made
        intro3_resp.keys = None
    thisExp.addData('intro3_resp.keys',intro3_resp.keys)
    if intro3_resp.keys != None:  # we had a response
        thisExp.addData('intro3_resp.rt', intro3_resp.rt)
        thisExp.addData('intro3_resp.duration', intro3_resp.duration)
    thisExp.nextEntry()
    # the Routine "Intro3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Intro4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro4.started', globalClock.getTime())
    intro4_resp.keys = []
    intro4_resp.rt = []
    _intro4_resp_allKeys = []
    # keep track of which components have finished
    Intro4Components = [Intro_4, intro4_resp]
    for thisComponent in Intro4Components:
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
    
    # --- Run Routine "Intro4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intro_4* updates
        
        # if Intro_4 is starting this frame...
        if Intro_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Intro_4.frameNStart = frameN  # exact frame index
            Intro_4.tStart = t  # local t and not account for scr refresh
            Intro_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Intro_4.started')
            # update status
            Intro_4.status = STARTED
            Intro_4.setAutoDraw(True)
        
        # if Intro_4 is active this frame...
        if Intro_4.status == STARTED:
            # update params
            pass
        
        # *intro4_resp* updates
        waitOnFlip = False
        
        # if intro4_resp is starting this frame...
        if intro4_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro4_resp.frameNStart = frameN  # exact frame index
            intro4_resp.tStart = t  # local t and not account for scr refresh
            intro4_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro4_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro4_resp.started')
            # update status
            intro4_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intro4_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intro4_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intro4_resp.status == STARTED and not waitOnFlip:
            theseKeys = intro4_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro4_resp_allKeys.extend(theseKeys)
            if len(_intro4_resp_allKeys):
                intro4_resp.keys = _intro4_resp_allKeys[-1].name  # just the last key pressed
                intro4_resp.rt = _intro4_resp_allKeys[-1].rt
                intro4_resp.duration = _intro4_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro4" ---
    for thisComponent in Intro4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro4.stopped', globalClock.getTime())
    # check responses
    if intro4_resp.keys in ['', [], None]:  # No response was made
        intro4_resp.keys = None
    thisExp.addData('intro4_resp.keys',intro4_resp.keys)
    if intro4_resp.keys != None:  # we had a response
        thisExp.addData('intro4_resp.rt', intro4_resp.rt)
        thisExp.addData('intro4_resp.duration', intro4_resp.duration)
    thisExp.nextEntry()
    # the Routine "Intro4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_block = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='prac_block')
    thisExp.addLoop(prac_block)  # add the loop to the experiment
    thisPrac_block = prac_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
    if thisPrac_block != None:
        for paramName in thisPrac_block:
            globals()[paramName] = thisPrac_block[paramName]
    
    for thisPrac_block in prac_block:
        currentLoop = prac_block
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_block.rgb)
        if thisPrac_block != None:
            for paramName in thisPrac_block:
                globals()[paramName] = thisPrac_block[paramName]
        
        # --- Prepare to start Routine "Prac_intro" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Prac_intro.started', globalClock.getTime())
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
                theseKeys = pracintro_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _pracintro_resp_allKeys.extend(theseKeys)
                if len(_pracintro_resp_allKeys):
                    pracintro_resp.keys = _pracintro_resp_allKeys[-1].name  # just the last key pressed
                    pracintro_resp.rt = _pracintro_resp_allKeys[-1].rt
                    pracintro_resp.duration = _pracintro_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
        thisExp.addData('Prac_intro.stopped', globalClock.getTime())
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
            trialList=data.importConditions('Practice_Eng.xlsx'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "practrial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('practrial.started', globalClock.getTime())
            image.setImage(Instruction_stim)
            # keep track of which components have finished
            practrialComponents = [image]
            for thisComponent in practrialComponents:
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
            
            # --- Run Routine "practrial" ---
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
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practrial" ---
            for thisComponent in practrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('practrial.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "solution" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('solution.started', globalClock.getTime())
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
                    theseKeys = RESP.getKeys(keyList=['left','right','up','down'], ignoreKeys=["escape"], waitRelease=False)
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
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
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
            thisExp.addData('solution.stopped', globalClock.getTime())
            # check responses
            if RESP.keys in ['', [], None]:  # No response was made
                RESP.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   RESP.corr = 1;  # correct non-response
                else:
                   RESP.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('RESP.keys',RESP.keys)
            trials.addData('RESP.corr', RESP.corr)
            if RESP.keys != None:  # we had a response
                trials.addData('RESP.rt', RESP.rt)
                trials.addData('RESP.duration', RESP.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('feedback.started', globalClock.getTime())
            # Run 'Begin Routine' code from code_2
            if RESP.corr == 1:
                msg = "Correct"
                msgColor = 'MediumBlue'
                prac_count +=1
                
                
            else:
                msg = "Incorrect"
                msgColor = 'DarkRed'
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
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
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
            thisExp.addData('feedback.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials'
        
        
        # --- Prepare to start Routine "Prac_check" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Prac_check.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_3
        if prac_count >= trials.nTotal*0.9: #연습 끝나는 규칙
            prac_block.finished = True
        else:
                prac_block.finished = False
                msg_intro = "\n\n Let's do it again! \nTo continue, please press space bar. "
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
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
        thisExp.addData('Prac_check.stopped', globalClock.getTime())
        # the Routine "Prac_check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'prac_block'
    
    
    # --- Prepare to start Routine "intro5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('intro5.started', globalClock.getTime())
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
            theseKeys = intro5_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro5_resp_allKeys.extend(theseKeys)
            if len(_intro5_resp_allKeys):
                intro5_resp.keys = _intro5_resp_allKeys[-1].name  # just the last key pressed
                intro5_resp.rt = _intro5_resp_allKeys[-1].rt
                intro5_resp.duration = _intro5_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    thisExp.addData('intro5.stopped', globalClock.getTime())
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
            globals()[paramName] = thisBlock1[paramName]
    
    for thisBlock1 in block1:
        currentLoop = block1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
        if thisBlock1 != None:
            for paramName in thisBlock1:
                globals()[paramName] = thisBlock1[paramName]
        
        # --- Prepare to start Routine "block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block.started', globalClock.getTime())
        main_image.setImage(Instruction_stim)
        main_early1.setPos(early_position)
        main_early1.setText(earlier_stim)
        key_resp1.keys = []
        key_resp1.rt = []
        _key_resp1_allKeys = []
        main_late1.setPos(late_position)
        main_late1.setText(later_stim)
        # keep track of which components have finished
        blockComponents = [main_image, main_early1, key_resp1, main_late1, fix]
        for thisComponent in blockComponents:
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
        
        # --- Run Routine "block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *main_image* updates
            
            # if main_image is starting this frame...
            if main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_image.frameNStart = frameN  # exact frame index
                main_image.tStart = t  # local t and not account for scr refresh
                main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_image.started')
                # update status
                main_image.status = STARTED
                main_image.setAutoDraw(True)
            
            # if main_image is active this frame...
            if main_image.status == STARTED:
                # update params
                pass
            
            # if main_image is stopping this frame...
            if main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    main_image.tStop = t  # not accounting for scr refresh
                    main_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_image.stopped')
                    # update status
                    main_image.status = FINISHED
                    main_image.setAutoDraw(False)
            
            # *main_early1* updates
            
            # if main_early1 is starting this frame...
            if main_early1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_early1.frameNStart = frameN  # exact frame index
                main_early1.tStart = t  # local t and not account for scr refresh
                main_early1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_early1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_early1.started')
                # update status
                main_early1.status = STARTED
                main_early1.setAutoDraw(True)
            
            # if main_early1 is active this frame...
            if main_early1.status == STARTED:
                # update params
                pass
            
            # if main_early1 is stopping this frame...
            if main_early1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_early1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_early1.tStop = t  # not accounting for scr refresh
                    main_early1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_early1.stopped')
                    # update status
                    main_early1.status = FINISHED
                    main_early1.setAutoDraw(False)
            
            # *key_resp1* updates
            waitOnFlip = False
            
            # if key_resp1 is starting this frame...
            if key_resp1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp1.frameNStart = frameN  # exact frame index
                key_resp1.tStart = t  # local t and not account for scr refresh
                key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp1.started')
                # update status
                key_resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp1 is stopping this frame...
            if key_resp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp1.tStop = t  # not accounting for scr refresh
                    key_resp1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp1.stopped')
                    # update status
                    key_resp1.status = FINISHED
                    key_resp1.status = FINISHED
            if key_resp1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp1.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp1_allKeys.extend(theseKeys)
                if len(_key_resp1_allKeys):
                    key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                    key_resp1.rt = _key_resp1_allKeys[-1].rt
                    key_resp1.duration = _key_resp1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp1.keys == str(corr_resp)) or (key_resp1.keys == corr_resp):
                        key_resp1.corr = 1
                    else:
                        key_resp1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *main_late1* updates
            
            # if main_late1 is starting this frame...
            if main_late1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_late1.frameNStart = frameN  # exact frame index
                main_late1.tStart = t  # local t and not account for scr refresh
                main_late1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_late1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_late1.started')
                # update status
                main_late1.status = STARTED
                main_late1.setAutoDraw(True)
            
            # if main_late1 is active this frame...
            if main_late1.status == STARTED:
                # update params
                pass
            
            # if main_late1 is stopping this frame...
            if main_late1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_late1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_late1.tStop = t  # not accounting for scr refresh
                    main_late1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_late1.stopped')
                    # update status
                    main_late1.status = FINISHED
                    main_late1.setAutoDraw(False)
            
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
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block.stopped', globalClock.getTime())
        # check responses
        if key_resp1.keys in ['', [], None]:  # No response was made
            key_resp1.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp1.corr = 1;  # correct non-response
            else:
               key_resp1.corr = 0;  # failed to respond (incorrectly)
        # store data for block1 (TrialHandler)
        block1.addData('key_resp1.keys',key_resp1.keys)
        block1.addData('key_resp1.corr', key_resp1.corr)
        if key_resp1.keys != None:  # we had a response
            block1.addData('key_resp1.rt', key_resp1.rt)
            block1.addData('key_resp1.duration', key_resp1.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'block1'
    
    
    # set up handler to look after randomisation of conditions etc
    break1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Break_material/Break_eng.xlsx', selection='0:8'),
        seed=None, name='break1')
    thisExp.addLoop(break1)  # add the loop to the experiment
    thisBreak1 = break1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBreak1.rgb)
    if thisBreak1 != None:
        for paramName in thisBreak1:
            globals()[paramName] = thisBreak1[paramName]
    
    for thisBreak1 in break1:
        currentLoop = break1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBreak1.rgb)
        if thisBreak1 != None:
            for paramName in thisBreak1:
                globals()[paramName] = thisBreak1[paramName]
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        question.setText(Qustion)
        fengjing.setImage(Path)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        break_2Components = [question, fengjing, key_resp, Yes, no]
        for thisComponent in break_2Components:
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
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 11.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            
            # if question is starting this frame...
            if question.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question.started')
                # update status
                question.status = STARTED
                question.setAutoDraw(True)
            
            # if question is active this frame...
            if question.status == STARTED:
                # update params
                pass
            
            # if question is stopping this frame...
            if question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question.tStop = t  # not accounting for scr refresh
                    question.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question.stopped')
                    # update status
                    question.status = FINISHED
                    question.setAutoDraw(False)
            
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
                theseKeys = key_resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Yes* updates
            
            # if Yes is starting this frame...
            if Yes.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                Yes.frameNStart = frameN  # exact frame index
                Yes.tStart = t  # local t and not account for scr refresh
                Yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Yes.started')
                # update status
                Yes.status = STARTED
                Yes.setAutoDraw(True)
            
            # if Yes is active this frame...
            if Yes.status == STARTED:
                # update params
                pass
            
            # if Yes is stopping this frame...
            if Yes.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Yes.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    Yes.tStop = t  # not accounting for scr refresh
                    Yes.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Yes.stopped')
                    # update status
                    Yes.status = FINISHED
                    Yes.setAutoDraw(False)
            
            # *no* updates
            
            # if no is starting this frame...
            if no.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                # update status
                no.status = STARTED
                no.setAutoDraw(True)
            
            # if no is active this frame...
            if no.status == STARTED:
                # update params
                pass
            
            # if no is stopping this frame...
            if no.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > no.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    no.tStop = t  # not accounting for scr refresh
                    no.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no.stopped')
                    # update status
                    no.status = FINISHED
                    no.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
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
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'break1'
    
    
    # set up handler to look after randomisation of conditions etc
    block2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('blocks/Block 2.csv'),
        seed=None, name='block2')
    thisExp.addLoop(block2)  # add the loop to the experiment
    thisBlock2 = block2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2:
            globals()[paramName] = thisBlock2[paramName]
    
    for thisBlock2 in block2:
        currentLoop = block2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
        if thisBlock2 != None:
            for paramName in thisBlock2:
                globals()[paramName] = thisBlock2[paramName]
        
        # --- Prepare to start Routine "block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block.started', globalClock.getTime())
        main_image.setImage(Instruction_stim)
        main_early1.setPos(early_position)
        main_early1.setText(earlier_stim)
        key_resp1.keys = []
        key_resp1.rt = []
        _key_resp1_allKeys = []
        main_late1.setPos(late_position)
        main_late1.setText(later_stim)
        # keep track of which components have finished
        blockComponents = [main_image, main_early1, key_resp1, main_late1, fix]
        for thisComponent in blockComponents:
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
        
        # --- Run Routine "block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *main_image* updates
            
            # if main_image is starting this frame...
            if main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_image.frameNStart = frameN  # exact frame index
                main_image.tStart = t  # local t and not account for scr refresh
                main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_image.started')
                # update status
                main_image.status = STARTED
                main_image.setAutoDraw(True)
            
            # if main_image is active this frame...
            if main_image.status == STARTED:
                # update params
                pass
            
            # if main_image is stopping this frame...
            if main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    main_image.tStop = t  # not accounting for scr refresh
                    main_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_image.stopped')
                    # update status
                    main_image.status = FINISHED
                    main_image.setAutoDraw(False)
            
            # *main_early1* updates
            
            # if main_early1 is starting this frame...
            if main_early1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_early1.frameNStart = frameN  # exact frame index
                main_early1.tStart = t  # local t and not account for scr refresh
                main_early1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_early1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_early1.started')
                # update status
                main_early1.status = STARTED
                main_early1.setAutoDraw(True)
            
            # if main_early1 is active this frame...
            if main_early1.status == STARTED:
                # update params
                pass
            
            # if main_early1 is stopping this frame...
            if main_early1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_early1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_early1.tStop = t  # not accounting for scr refresh
                    main_early1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_early1.stopped')
                    # update status
                    main_early1.status = FINISHED
                    main_early1.setAutoDraw(False)
            
            # *key_resp1* updates
            waitOnFlip = False
            
            # if key_resp1 is starting this frame...
            if key_resp1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp1.frameNStart = frameN  # exact frame index
                key_resp1.tStart = t  # local t and not account for scr refresh
                key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp1.started')
                # update status
                key_resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp1 is stopping this frame...
            if key_resp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp1.tStop = t  # not accounting for scr refresh
                    key_resp1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp1.stopped')
                    # update status
                    key_resp1.status = FINISHED
                    key_resp1.status = FINISHED
            if key_resp1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp1.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp1_allKeys.extend(theseKeys)
                if len(_key_resp1_allKeys):
                    key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                    key_resp1.rt = _key_resp1_allKeys[-1].rt
                    key_resp1.duration = _key_resp1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp1.keys == str(corr_resp)) or (key_resp1.keys == corr_resp):
                        key_resp1.corr = 1
                    else:
                        key_resp1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *main_late1* updates
            
            # if main_late1 is starting this frame...
            if main_late1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_late1.frameNStart = frameN  # exact frame index
                main_late1.tStart = t  # local t and not account for scr refresh
                main_late1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_late1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_late1.started')
                # update status
                main_late1.status = STARTED
                main_late1.setAutoDraw(True)
            
            # if main_late1 is active this frame...
            if main_late1.status == STARTED:
                # update params
                pass
            
            # if main_late1 is stopping this frame...
            if main_late1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_late1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_late1.tStop = t  # not accounting for scr refresh
                    main_late1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_late1.stopped')
                    # update status
                    main_late1.status = FINISHED
                    main_late1.setAutoDraw(False)
            
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
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block.stopped', globalClock.getTime())
        # check responses
        if key_resp1.keys in ['', [], None]:  # No response was made
            key_resp1.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp1.corr = 1;  # correct non-response
            else:
               key_resp1.corr = 0;  # failed to respond (incorrectly)
        # store data for block2 (TrialHandler)
        block2.addData('key_resp1.keys',key_resp1.keys)
        block2.addData('key_resp1.corr', key_resp1.corr)
        if key_resp1.keys != None:  # we had a response
            block2.addData('key_resp1.rt', key_resp1.rt)
            block2.addData('key_resp1.duration', key_resp1.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'block2'
    
    
    # set up handler to look after randomisation of conditions etc
    break2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Break_material/Break_eng.xlsx', selection='0:8'),
        seed=None, name='break2')
    thisExp.addLoop(break2)  # add the loop to the experiment
    thisBreak2 = break2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBreak2.rgb)
    if thisBreak2 != None:
        for paramName in thisBreak2:
            globals()[paramName] = thisBreak2[paramName]
    
    for thisBreak2 in break2:
        currentLoop = break2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBreak2.rgb)
        if thisBreak2 != None:
            for paramName in thisBreak2:
                globals()[paramName] = thisBreak2[paramName]
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        question.setText(Qustion)
        fengjing.setImage(Path)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        break_2Components = [question, fengjing, key_resp, Yes, no]
        for thisComponent in break_2Components:
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
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 11.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            
            # if question is starting this frame...
            if question.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question.started')
                # update status
                question.status = STARTED
                question.setAutoDraw(True)
            
            # if question is active this frame...
            if question.status == STARTED:
                # update params
                pass
            
            # if question is stopping this frame...
            if question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question.tStop = t  # not accounting for scr refresh
                    question.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question.stopped')
                    # update status
                    question.status = FINISHED
                    question.setAutoDraw(False)
            
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
                theseKeys = key_resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Yes* updates
            
            # if Yes is starting this frame...
            if Yes.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                Yes.frameNStart = frameN  # exact frame index
                Yes.tStart = t  # local t and not account for scr refresh
                Yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Yes.started')
                # update status
                Yes.status = STARTED
                Yes.setAutoDraw(True)
            
            # if Yes is active this frame...
            if Yes.status == STARTED:
                # update params
                pass
            
            # if Yes is stopping this frame...
            if Yes.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Yes.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    Yes.tStop = t  # not accounting for scr refresh
                    Yes.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Yes.stopped')
                    # update status
                    Yes.status = FINISHED
                    Yes.setAutoDraw(False)
            
            # *no* updates
            
            # if no is starting this frame...
            if no.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                # update status
                no.status = STARTED
                no.setAutoDraw(True)
            
            # if no is active this frame...
            if no.status == STARTED:
                # update params
                pass
            
            # if no is stopping this frame...
            if no.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > no.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    no.tStop = t  # not accounting for scr refresh
                    no.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no.stopped')
                    # update status
                    no.status = FINISHED
                    no.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str('CorrAns').lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for break2 (TrialHandler)
        break2.addData('key_resp.keys',key_resp.keys)
        break2.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            break2.addData('key_resp.rt', key_resp.rt)
            break2.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-11.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'break2'
    
    
    # set up handler to look after randomisation of conditions etc
    block3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('blocks/Block 3.csv'),
        seed=None, name='block3')
    thisExp.addLoop(block3)  # add the loop to the experiment
    thisBlock3 = block3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3.rgb)
    if thisBlock3 != None:
        for paramName in thisBlock3:
            globals()[paramName] = thisBlock3[paramName]
    
    for thisBlock3 in block3:
        currentLoop = block3
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock3.rgb)
        if thisBlock3 != None:
            for paramName in thisBlock3:
                globals()[paramName] = thisBlock3[paramName]
        
        # --- Prepare to start Routine "block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block.started', globalClock.getTime())
        main_image.setImage(Instruction_stim)
        main_early1.setPos(early_position)
        main_early1.setText(earlier_stim)
        key_resp1.keys = []
        key_resp1.rt = []
        _key_resp1_allKeys = []
        main_late1.setPos(late_position)
        main_late1.setText(later_stim)
        # keep track of which components have finished
        blockComponents = [main_image, main_early1, key_resp1, main_late1, fix]
        for thisComponent in blockComponents:
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
        
        # --- Run Routine "block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *main_image* updates
            
            # if main_image is starting this frame...
            if main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_image.frameNStart = frameN  # exact frame index
                main_image.tStart = t  # local t and not account for scr refresh
                main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_image.started')
                # update status
                main_image.status = STARTED
                main_image.setAutoDraw(True)
            
            # if main_image is active this frame...
            if main_image.status == STARTED:
                # update params
                pass
            
            # if main_image is stopping this frame...
            if main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    main_image.tStop = t  # not accounting for scr refresh
                    main_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_image.stopped')
                    # update status
                    main_image.status = FINISHED
                    main_image.setAutoDraw(False)
            
            # *main_early1* updates
            
            # if main_early1 is starting this frame...
            if main_early1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_early1.frameNStart = frameN  # exact frame index
                main_early1.tStart = t  # local t and not account for scr refresh
                main_early1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_early1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_early1.started')
                # update status
                main_early1.status = STARTED
                main_early1.setAutoDraw(True)
            
            # if main_early1 is active this frame...
            if main_early1.status == STARTED:
                # update params
                pass
            
            # if main_early1 is stopping this frame...
            if main_early1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_early1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_early1.tStop = t  # not accounting for scr refresh
                    main_early1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_early1.stopped')
                    # update status
                    main_early1.status = FINISHED
                    main_early1.setAutoDraw(False)
            
            # *key_resp1* updates
            waitOnFlip = False
            
            # if key_resp1 is starting this frame...
            if key_resp1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp1.frameNStart = frameN  # exact frame index
                key_resp1.tStart = t  # local t and not account for scr refresh
                key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp1.started')
                # update status
                key_resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp1 is stopping this frame...
            if key_resp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp1.tStop = t  # not accounting for scr refresh
                    key_resp1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp1.stopped')
                    # update status
                    key_resp1.status = FINISHED
                    key_resp1.status = FINISHED
            if key_resp1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp1.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp1_allKeys.extend(theseKeys)
                if len(_key_resp1_allKeys):
                    key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                    key_resp1.rt = _key_resp1_allKeys[-1].rt
                    key_resp1.duration = _key_resp1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp1.keys == str(corr_resp)) or (key_resp1.keys == corr_resp):
                        key_resp1.corr = 1
                    else:
                        key_resp1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *main_late1* updates
            
            # if main_late1 is starting this frame...
            if main_late1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_late1.frameNStart = frameN  # exact frame index
                main_late1.tStart = t  # local t and not account for scr refresh
                main_late1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_late1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_late1.started')
                # update status
                main_late1.status = STARTED
                main_late1.setAutoDraw(True)
            
            # if main_late1 is active this frame...
            if main_late1.status == STARTED:
                # update params
                pass
            
            # if main_late1 is stopping this frame...
            if main_late1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_late1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_late1.tStop = t  # not accounting for scr refresh
                    main_late1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_late1.stopped')
                    # update status
                    main_late1.status = FINISHED
                    main_late1.setAutoDraw(False)
            
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
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block.stopped', globalClock.getTime())
        # check responses
        if key_resp1.keys in ['', [], None]:  # No response was made
            key_resp1.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp1.corr = 1;  # correct non-response
            else:
               key_resp1.corr = 0;  # failed to respond (incorrectly)
        # store data for block3 (TrialHandler)
        block3.addData('key_resp1.keys',key_resp1.keys)
        block3.addData('key_resp1.corr', key_resp1.corr)
        if key_resp1.keys != None:  # we had a response
            block3.addData('key_resp1.rt', key_resp1.rt)
            block3.addData('key_resp1.duration', key_resp1.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'block3'
    
    
    # set up handler to look after randomisation of conditions etc
    break3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Break_material/Break_eng.xlsx', selection='0:8'),
        seed=None, name='break3')
    thisExp.addLoop(break3)  # add the loop to the experiment
    thisBreak3 = break3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBreak3.rgb)
    if thisBreak3 != None:
        for paramName in thisBreak3:
            globals()[paramName] = thisBreak3[paramName]
    
    for thisBreak3 in break3:
        currentLoop = break3
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBreak3.rgb)
        if thisBreak3 != None:
            for paramName in thisBreak3:
                globals()[paramName] = thisBreak3[paramName]
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        question.setText(Qustion)
        fengjing.setImage(Path)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        break_2Components = [question, fengjing, key_resp, Yes, no]
        for thisComponent in break_2Components:
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
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 11.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            
            # if question is starting this frame...
            if question.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question.started')
                # update status
                question.status = STARTED
                question.setAutoDraw(True)
            
            # if question is active this frame...
            if question.status == STARTED:
                # update params
                pass
            
            # if question is stopping this frame...
            if question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question.tStop = t  # not accounting for scr refresh
                    question.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question.stopped')
                    # update status
                    question.status = FINISHED
                    question.setAutoDraw(False)
            
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
                theseKeys = key_resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Yes* updates
            
            # if Yes is starting this frame...
            if Yes.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                Yes.frameNStart = frameN  # exact frame index
                Yes.tStart = t  # local t and not account for scr refresh
                Yes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Yes, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Yes.started')
                # update status
                Yes.status = STARTED
                Yes.setAutoDraw(True)
            
            # if Yes is active this frame...
            if Yes.status == STARTED:
                # update params
                pass
            
            # if Yes is stopping this frame...
            if Yes.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Yes.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    Yes.tStop = t  # not accounting for scr refresh
                    Yes.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Yes.stopped')
                    # update status
                    Yes.status = FINISHED
                    Yes.setAutoDraw(False)
            
            # *no* updates
            
            # if no is starting this frame...
            if no.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                no.frameNStart = frameN  # exact frame index
                no.tStart = t  # local t and not account for scr refresh
                no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no.started')
                # update status
                no.status = STARTED
                no.setAutoDraw(True)
            
            # if no is active this frame...
            if no.status == STARTED:
                # update params
                pass
            
            # if no is stopping this frame...
            if no.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > no.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    no.tStop = t  # not accounting for scr refresh
                    no.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no.stopped')
                    # update status
                    no.status = FINISHED
                    no.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str('CorrAns').lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for break3 (TrialHandler)
        break3.addData('key_resp.keys',key_resp.keys)
        break3.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            break3.addData('key_resp.rt', key_resp.rt)
            break3.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-11.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'break3'
    
    
    # set up handler to look after randomisation of conditions etc
    block4 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('blocks/Block 4.csv'),
        seed=None, name='block4')
    thisExp.addLoop(block4)  # add the loop to the experiment
    thisBlock4 = block4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4.rgb)
    if thisBlock4 != None:
        for paramName in thisBlock4:
            globals()[paramName] = thisBlock4[paramName]
    
    for thisBlock4 in block4:
        currentLoop = block4
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock4.rgb)
        if thisBlock4 != None:
            for paramName in thisBlock4:
                globals()[paramName] = thisBlock4[paramName]
        
        # --- Prepare to start Routine "block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block.started', globalClock.getTime())
        main_image.setImage(Instruction_stim)
        main_early1.setPos(early_position)
        main_early1.setText(earlier_stim)
        key_resp1.keys = []
        key_resp1.rt = []
        _key_resp1_allKeys = []
        main_late1.setPos(late_position)
        main_late1.setText(later_stim)
        # keep track of which components have finished
        blockComponents = [main_image, main_early1, key_resp1, main_late1, fix]
        for thisComponent in blockComponents:
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
        
        # --- Run Routine "block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *main_image* updates
            
            # if main_image is starting this frame...
            if main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_image.frameNStart = frameN  # exact frame index
                main_image.tStart = t  # local t and not account for scr refresh
                main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_image.started')
                # update status
                main_image.status = STARTED
                main_image.setAutoDraw(True)
            
            # if main_image is active this frame...
            if main_image.status == STARTED:
                # update params
                pass
            
            # if main_image is stopping this frame...
            if main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    main_image.tStop = t  # not accounting for scr refresh
                    main_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_image.stopped')
                    # update status
                    main_image.status = FINISHED
                    main_image.setAutoDraw(False)
            
            # *main_early1* updates
            
            # if main_early1 is starting this frame...
            if main_early1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_early1.frameNStart = frameN  # exact frame index
                main_early1.tStart = t  # local t and not account for scr refresh
                main_early1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_early1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_early1.started')
                # update status
                main_early1.status = STARTED
                main_early1.setAutoDraw(True)
            
            # if main_early1 is active this frame...
            if main_early1.status == STARTED:
                # update params
                pass
            
            # if main_early1 is stopping this frame...
            if main_early1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_early1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_early1.tStop = t  # not accounting for scr refresh
                    main_early1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_early1.stopped')
                    # update status
                    main_early1.status = FINISHED
                    main_early1.setAutoDraw(False)
            
            # *key_resp1* updates
            waitOnFlip = False
            
            # if key_resp1 is starting this frame...
            if key_resp1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp1.frameNStart = frameN  # exact frame index
                key_resp1.tStart = t  # local t and not account for scr refresh
                key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp1.started')
                # update status
                key_resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp1 is stopping this frame...
            if key_resp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp1.tStop = t  # not accounting for scr refresh
                    key_resp1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp1.stopped')
                    # update status
                    key_resp1.status = FINISHED
                    key_resp1.status = FINISHED
            if key_resp1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp1.getKeys(keyList=['up','down','left','right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp1_allKeys.extend(theseKeys)
                if len(_key_resp1_allKeys):
                    key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                    key_resp1.rt = _key_resp1_allKeys[-1].rt
                    key_resp1.duration = _key_resp1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp1.keys == str(corr_resp)) or (key_resp1.keys == corr_resp):
                        key_resp1.corr = 1
                    else:
                        key_resp1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *main_late1* updates
            
            # if main_late1 is starting this frame...
            if main_late1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                main_late1.frameNStart = frameN  # exact frame index
                main_late1.tStart = t  # local t and not account for scr refresh
                main_late1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_late1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'main_late1.started')
                # update status
                main_late1.status = STARTED
                main_late1.setAutoDraw(True)
            
            # if main_late1 is active this frame...
            if main_late1.status == STARTED:
                # update params
                pass
            
            # if main_late1 is stopping this frame...
            if main_late1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_late1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    main_late1.tStop = t  # not accounting for scr refresh
                    main_late1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'main_late1.stopped')
                    # update status
                    main_late1.status = FINISHED
                    main_late1.setAutoDraw(False)
            
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
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block.stopped', globalClock.getTime())
        # check responses
        if key_resp1.keys in ['', [], None]:  # No response was made
            key_resp1.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp1.corr = 1;  # correct non-response
            else:
               key_resp1.corr = 0;  # failed to respond (incorrectly)
        # store data for block4 (TrialHandler)
        block4.addData('key_resp1.keys',key_resp1.keys)
        block4.addData('key_resp1.corr', key_resp1.corr)
        if key_resp1.keys != None:  # we had a response
            block4.addData('key_resp1.rt', key_resp1.rt)
            block4.addData('key_resp1.duration', key_resp1.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'block4'
    
    
    # --- Prepare to start Routine "The_end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('The_end.started', globalClock.getTime())
    # keep track of which components have finished
    The_endComponents = [theend]
    for thisComponent in The_endComponents:
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
    
    # --- Run Routine "The_end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *theend* updates
        
        # if theend is starting this frame...
        if theend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            theend.frameNStart = frameN  # exact frame index
            theend.tStart = t  # local t and not account for scr refresh
            theend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(theend, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'theend.started')
            # update status
            theend.status = STARTED
            theend.setAutoDraw(True)
        
        # if theend is active this frame...
        if theend.status == STARTED:
            # update params
            pass
        
        # if theend is stopping this frame...
        if theend.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > theend.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                theend.tStop = t  # not accounting for scr refresh
                theend.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'theend.stopped')
                # update status
                theend.status = FINISHED
                theend.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in The_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "The_end" ---
    for thisComponent in The_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('The_end.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
