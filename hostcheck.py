#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  checkhost.py
#  
#  Copyright 2017 Unknown <rafal@cuntslag3> 
#  
import requests, re, sys, os;from time import *; from datetime import *;
red = '\033[38;5;9m';white = '\033[38;5;7m';grey = '\033[38;5;247m';
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1	
def authors():
	s=''
	logo='W̲̲̲̅ ̲̲̲̅R̲̲̲̅ ̲̲̲̅I̲̲̲̅ ̲̲̲̅T̲̲̲̅ ̲̲̲̅T̲̲̲̅ ̲̲̲̅E̲̲̲̅ ̲̲̲̅N̲̲̲̅ ̲̲̲̅ ̲̲̲̅B̲̲̲̅ ̲̲̲̅Y̲̲̲̅ ̲̲̲̅ ̲̲̲̅N̲̲̲̅ ̲̲̲̅Y̲̲̲̅ ̲̲̲̅C̲̲̲̅ ̲̲̲̅T̲̲̲̅ ̲̲̲̅O̲̲̲̅ ̲̲̲̅ ̲̲̲̅&̲̲̲̅ ̲̲̲̅ ̲̲̲̅R̲̲̲̅ ̲̲̲̅A̲̲̲̅ ̲̲̲̅F̲̲̲̅ '
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		Space(1);sys.stdout.write('['+red + '!~!'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)
	print
	return
def HoneyPot(honey):
	reload(sys)  
	sys.setdefaultencoding('utf8')
	s=''
	logo='H̶ ̶O̶ ̶N̶ ̶E̶ ̶Y̶ ̶ ̶P̶O̶T̶ ̶P̶ ̶R̶ ̶O̶ ̶B̶ ̶A̶ ̶B̶ ̶I̶ ̶L̶ ̶I̶ ̶T̶ ̶Y̶: %s '%(honey) 
	honey.decode('utf8', errors='ignore')
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		sys.stdout.write(white+'['+red + '*'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)
	print
	return()
def NoRobots():
	s=''
	logo='N̶ ̶O̶ ̶ ̶R̶ ̶O̶ ̶B̶ ̶O̶ ̶T̶ ̶S̶.̶T̶X̶T̶ ̶F̶ ̶O̶ ̶U̶ ̶N̶ ̶D̶ '
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		sys.stdout.write(white+'['+red + 'X'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)
	print
	return()
def NoCloudFare():
	s=''
	logo='N̶ ̶O̶ ̶ ̶C̶ ̶L̶ ̶O̶ ̶U̶ ̶D̶ ̶F̶ ̶A̶ ̶R̶ ̶E̶ '
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		sys.stdout.write(white+'['+red + '*'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)
	print
	return()
def CloudFare():
	s=''
	logo='C̶ ̶L̶ ̶O̶ ̶U̶ ̶D̶ ̶ ̶F̶ ̶A̶ ̶R̶ ̶E̶ ̶ ̶D̶ ̶E̶ ̶T̶ ̶E̶ ̶C̶ ̶T̶ ̶E̶ ̶D̶ '
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		sys.stdout.write(white+'['+red + '~'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)	
	print
	return()
def Invalid():
	s=''
	logo='ɪ̲̲̲̅ɴ̲̲̲̅ᴠ̲̲̲̅ᴀ̲̲̲̅ʟ̲̲̲̅ɪ̲̲̲̅ᴅ̲̲̲̅ ̲̲̲̅ᴄ̲̲̲̅ʜ̲̲̲̅ᴏ̲̲̲̅ɪ̲̲̲̅ᴄ̲̲̲̅ᴇ̲̲̲̅ '
	s.decode('UTF8')
	for l in logo:
		sys.stdout.write('\r')
		sys.stdout.write(white+'['+red + 'X'+white + '] '+'%s'%(s.decode('utf8', errors='ignore')))
		s+='%s'%l
		sys.stdout.flush()
		sleep(.01)	
	print
	return()
banner = red + '''
			    A 
	       ╔╦╗┌─┐┬─┐┬─┐┌─┐┬─┐╔═╗┌─┐┌─┐
		║ ├┤ ├┬┘├┬┘│ │├┬┘╚═╗├┤ │  
		╩ └─┘┴└─┴└─└─┘┴└─╚═╝└─┘└─┘
			Production'''
class checkhost:
	""" Class checkhost """	
	def __init__ (self):
		self.session = requests.Session()
		self.session.headers.update({'User-Agent':'User-Agent Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
		print banner
		authors()
		self.menu()
	def menu(self):
		print red + '╔═' + '═' * 50 + '╗'
		print red + '║ ' + white + 'whois search'+red+': ' + grey + '1' + red + ' '  *34 +' ║'
		print red + '║ ' + white + 'DNS Lookup + Cloudflare Detector'+red+': ' + grey + '2' + red + ' '  *14 +' ║'
		print red + '║ ' + white + 'Zone Transfer(dig)'+red+': ' + grey + '3' + red + ' '  *28 +' ║'
		print red + '║ ' + white + 'Port scan'+red+': ' + grey + '4' + red + ' '  *37 +' ║'
		print red + '║ ' + white + 'HTTP Header Grabber'+red+': ' + grey + '5' + red + ' '  *27 +' ║'
		print red + '║ ' + white + 'Honeypot Detector'+red+': ' + grey + '6' + red + ' '  *29 +' ║'
		print red + '║ ' + white + 'Robots.txt Scanner'+red+': ' + grey + '7' + red + ' '  *28 +' ║'
		print red + '║ ' + white + 'Link Grabber'+red+': ' + grey + '8' + red + ' '  *34 +' ║'
		print red + '║ ' + white + 'IP Location Finder'+red+': ' + grey + '9' + red + ' '  *28 +' ║'
		print red + '║ ' + white + 'Traceroute'+red+': ' + grey + '10' + red + ' '  *35 +' ║'
		print red + '║ ' + white + 'Exit'+red+': ' + grey + '11' + red + ' '  *41 +' ║'
		choice = raw_input(red + '║ ' + white + 'Choice' + red + ': $ '+grey)
		if choice == '1' or choice == 'whois':
			target = raw_input(red + '║ ' + white + 'Enter the domain'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			whois = self.session.get('http://api.hackertarget.com/whois/?q=%s'%(target)).text
			print whois
			self.menu()
		elif choice == '2':
			target = raw_input(red + '║ ' + white + 'Enter the domain'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			dns = self.session.get('http://api.hackertarget.com/dnslookup/?q=%s'%(target)).text
			cloudfare = self.session.get('http://www.doesitusecloudflare.com/?url=%s'%(target)).text
			check = re.findall('<h2>([A-Za-z .,]+)',cloudfare)[0]
			print dns
			if 'Wow' in check:
				CloudFare()
				self.menu()
			elif 'Phew' in check:
				NoCloudFare()
				self.menu()
		elif choice == '3':
			target = raw_input(red + '║ ' + white + 'Enter the domain/IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			os.system('dig %s'%target)		
			self.menu()	
		elif choice == '4':
			target = raw_input(red + '║ ' + white + 'Enter the domain/IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			ports = self.session.get('http://api.hackertarget.com/nmap/?q=%s'%(target)).text 
			print ports
			self.menu()
		elif choice == '5':
			target = raw_input(red + '║ ' + white + 'Enter the domain/IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			headers = self.session.get('http://api.hackertarget.com/httpheaders/?q=%s'%(target)).text
			print headers 
			self.menu()
		elif choice == '6':
			target = raw_input(red + '║ ' + white + 'Enter the target IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			honey = self.session.get('https://api.shodan.io/labs/honeyscore/%s?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by'%(target)).text 
			#print honey
			HoneyPot(honey)
			self.menu()
		elif choice == '7':
			target = raw_input(red + '║ ' + white + 'Enter the domain(use"http://")'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			try:
				robots = self.session.get('%s/robots.txt'%(target)).text
				print robots
			except:
				NoRobots()
			self.menu()
		elif choice == '8':
			target = raw_input(red + '║ ' + white + 'Enter the domain'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			links = self.session.get('https://api.hackertarget.com/pagelinks/?q=%s'%(target)).text 
			print links
			self.menu()
		elif choice == '9':
			target = raw_input(red + '║ ' + white + 'Enter the IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			ipinfo = self.session.get('http://ipinfo.io/%s/geo'%(target)).text 
			print ipinfo 
			self.menu()
		elif choice == '10':
			target = raw_input(red + '║ ' + white + 'Enter the domain/IP'+red + ': $ '+grey)
			print red + '╚═' +  '═' * 50 +'╝'
			trace = self.session.get('https://api.hackertarget.com/mtr/?q=%s'%(target)).text 
			print trace 
			self.menu()
		elif choice == '11':
			print red + '╚═' +  '═' * 50 +'╝'
			exit(0)
		else:
			Space(8);print red + '╚═' +  '═' * 50 +'╝'
			Invalid()
			self.menu()
checkhost()
