# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

	pwd - Print working directory
	
	mkdir - Make Directory (mkdir -p)
	
	pushd, popd - Moving Around
	
	cp - Copy a File (rbcopy for Windows)

	cat - Stream a File

	find - Finding Files

	grep - Search inside files

	env - Show Environment Variables

	export - Add Environment Variable

	man - Displays User Manual for Command

	touch - Creates a File

	top - Displays Top Processes in System by CPU Usage

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

	ls
	List information about files in the current directory.

	ls -a
	Do not hide directory entries starting with (.).

	ls -l
	Use a long listing format.

	ls -lh
	Use long listing format and print file sizes in human readable format.
	
	ls -lah
	Use long listing and human readable formats while not hiding files starting with (.).
	
	ls -t
	Sort by modification time.
	
	ls -Glp
	Enable colorized output on mac (inhibit display of group information on linux), use long listing format, and append file type indicator to entries (ex - appends directories with a slash).

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

	ls -1
	Displays each entry on a line.

	ls -c
	Displays files by timestamp.

	ls -d
	Displays only directories.
	
	ls -m
	Displays the names as a comma-separated list.
	
	ls -R
	Displays subdirectories as well.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

	xargs is a command that can execute another command (such as cp or rm) over a list or standard input that is passed to it.
	
	The example below will tell you how many lines each ".txt" document has in a directory.
	ls -1  *.txt | xargs wc -l
 

