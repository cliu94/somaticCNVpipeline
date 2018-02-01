#!/usr/bin/python
import os

from count import countfile 
import common










def runAll(args):
  
	print('\n\n\nYou have requested to count unique sam files')
	print('\tWARNING:')
	print('\t\tIF USING ANY REFERENCES OTHER THAN THOSE I PROVIDE I CANNOT GUARANTEE RESULT ACCURACY')
	print('\n')
  


	#set up environment#
	args.SamDirectory = common.fixDirName(args.SamDirectory)
	
	if not args.output:
		countDir = os.path.dirname(args.SamDirectory) + '/' + BinCounts + '/'
	else:
		countDir = common.fixDirName(args.output)
	
	statsDir = args.SamDirectory + 'CountStats/'
	
	for i in [countDir, statsDir]:
		common.makeDir(i)

	samFiles = common.getSampleList(args.SamDirectory, args.samples, 'sam')
		
		
	
	#run multiprocessing of all mapping commands#	
	argList = [(x, countDir, statsDir, args.species) for x in samFiles]
	common.daemon(countfile.runOne, argList, 'count sam files')
	
	
	
	print('\nBin counts complete\n\n\n')

	
	
	
	
