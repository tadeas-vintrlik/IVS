# Makefile for IVS calculator
# Author: Vojtěch Bůbela <xbubel08>
#
# Makefile has all the required targets 
# make all wont do anything because our project
# is written python which is not compiled but interpreted


# variables

SRC_FILES = ./src/*.py
APP = ./gui.py
TEST = ./math_library_tests.py
INTERPRET = python3
TRASH = /dev/null
MSSG = Since this is a python project, this wont compile anything

# targets:

.PHONY: all clean 

all: 
	echo $(MSSG)

pack:
	#zip that bitch

clean:
	@rm -rf ./__pycache__ 

test:
	$(INTERPRET) $(TEST)

doc:
	@doxygen

run:
	$(INTERPRET) $(APP) 2>$(TRASH)

profile:
	# TODO
