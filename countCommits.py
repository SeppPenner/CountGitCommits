import os

#Script to show the number of git commits in a repository
#Works with Python Version 3.5.2
def countCommits():
	"countCommits"
	os.system('git rev-list --all --count')
	return

#Programm
countCommits()