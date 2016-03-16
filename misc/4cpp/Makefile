
##### Source files and executable ############################################

SRCS 		= images-file.cpp 

OBJECTS 	= images-file.o 

EXECNAME 	= images-file

##### Libraries and paths ####################################################

LIBS            = 
INCDIRS 	= 
LIBDIRS 	= 
 
##### Compiler information ###################################################

CPP		= g++
CPPFLAGS 	= -std=c++11

##### Target compilation #####################################################

all:$(EXECNAME)

$(EXECNAME): 	$(OBJECTS)
	$(CPP) $(CPPFLAGS) $(LIBDIRS) $^ $(LIBS) -o $(EXECNAME) 

.cpp.o:	
	$(CPP) $(CPPFLAGS) $(INCDIRS) -c $<

.cc.o:	
	$(CPP) $(CPPFLAGS) $(INCDIRS) -c $<

clean:
	rm -rf *~ *.o *.a $(EXECNAME) 

##############################################################################

