#!/usr/bin/env python

import subprocess
import rospy
import urllib2
import os
import time
from rapp_fake_robot.srv import Say, Record, RecognizeWord
from os.path import expanduser
#import sounddevice as sd

home = expanduser("~")
sd.default.samplerate = 44100
sd.default.device = 'digital output'
file_name=home+"/rapp/communication/data/sound.ogg"
path_to_script_say=home+"/rapp/communication/src/rapp_fake_robot/scripts/say.sh"
path_to_script_record=home+"/rapp/communication/src/rapp_fake_robot/scripts/record.sh"

def handle_say(req):
	print "NAO says in %s: %s" % (req.language, req.request)
	subprocess.check_call([path_to_script_say, req.request])
	return 1

def handle_record(req):
	print "NAO records for %s seconds" % req.recordingTime

	duration = 10  # seconds
	myrecording = sd.rec(duration * fs, samplerate=fs, channels=2)
	return file_name

def fake_nao_comm():
#	sd.default.samplerate = 44100
#	sd.default.device = 'digital output'
	rospy.init_node('fake_nao_comm')
	s = rospy.Service('rapp_say', Say, handle_say)
	s = rospy.Service('rapp_record', Record, handle_record)
	#s = rospy.Service('rapp_get_recognized_word', RecognizeWord, handle_recognize_word)
	print "Ready to synthesize words and record sound"
	rospy.spin()

if __name__ == "__main__":
	fake_nao_comm()
