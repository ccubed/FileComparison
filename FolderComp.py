# FolderComp.py
#
# Python script to compare contents of two folders and show the items that are in one folder and not in another.
# 
#
# Author: Cooper AKA Gizmo
import os,sys,os.path,subprocess

if len(sys.argv) < 3:
	print("No Folder specified for Comparison.\nUsage: python FolderComp.py <folder1> <folder2>")
	sys.exit()
elif sys.argv[1] == "" or sys.argv[1] is None or sys.argv[2] == "" or sys.argv[2] is None:
	print("Folder Missing.\nUsage: python FolderComp.py <folder1> <folder2>")
	sys.exit()
elif not os.path.isdir(sys.argv[1]) or not os.path.exists(sys.argv[1]):
	print("Path ",sys.argv[1]," does not exist or is not a directory.")
	sys.exit()
elif not os.path.isdir(sys.argv[2]) or not os.path.exists(sys.argv[2]):
	print("Path ",sys.argv[2]," does not exist or is not a directory.")
	sys.exit()	
else:
	BASE_PATH = sys.argv[1]
	Filelist = os.listdir(BASE_PATH)
	Files = [] #straight files
	Directories = [] #directories
	#First, find part files and separate them. Also separate out directories
	for fname in Filelist:
		if os.path.isdir(os.path.join(BASE_PATH,fname)):
			Directories.append(fname)
		else:
			Files.append(fname)
	#Get files out of directories (and more directories out of these directories)
	for DirName in Directories:
		Filelist = os.listdir(os.path.join(BASE_PATH,DirName))
		Directories.remove(DirName)
		for fname in Filelist:
			if os.path.isdir(os.path.join(BASE_PATH,DirName,fname)):
				Directories.append(os.path.join(BASE_PATH,DirName,fname))
			else:
				Files.append(os.path.join(BASE_PATH,DirName,fname))
	
	#Done with folder 1, move to 2
	BASE_PATH = sys.argv[2]
	Filelist = os.listdir(BASE_PATH)
	Files_Second = [] #second folder files
	Directories = [] #Clear Directories, reuse
	
	for fname in Filelist:
		if os.path.isdir(os.path.join(BASE_PATH,fname)):
			Directories.append(fname)
		else:
			Files_Second.append(fname)
			
	for DirName in Directories:
		Filelist = os.listdir(os.path.join(BASE_PATH,DirName))
		Directories.remove(DirName)
		for fname in Filelist:
			if os.path.isdir(os.path.join(BASE_PATH,DirName,fname)):
				Directories.append(os.path.join(BASE_PATH,DirName,fname))
			else:
				Files_Second.append(os.path.join(BASE_PATH,DirName,fname))
				
	#Done Sorting, Create Sets, Union
	A = set(Files)
	B = set(Files_Second)
	Same = A & B
	ADiff = A - B
	BDiff = B - A
	
	print("Number of Files in both: ",len(Same))
	print("\nNumber of files in ",sys.argv[1]," only: ",len(ADiff))
	print("\nNumber of files in ",sys.argv[2]," only: ",len(BDiff))
	print("\nReport printed to Sort_Results.txt")
	
	Results = open("Sort_Results.txt","w+")
	Results.write("\n\nFiles that are in both folders:\n")
	for item in Same:
		Results.write("\t",item,"\n")
	Results.write("\n\nFiles that are in ",sys.argv[1]," only:\n")
	for item in ADiff:
		Results.write("\t",item,"\n")
	Results.write("\n\nFiles that are in ",sys.argv[2]," only:\n")
	for item in BDiff:
		Results.write("\t",item,"\n")
	Results.write("\n\nResults list for folder comparison between ",sys.argv[1]," and ",sys.argv[2])
	Results.close()