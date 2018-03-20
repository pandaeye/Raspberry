#common makefile header
OBJ_DIR=../obj/
TARGET	=../bin/weather.cgi
LIBFLAGS =-L/usr/lib/python2.7 -lpython2.7 -lmsc -lrt -ldl -lpthread -lbcm2835
INCFLAGS =-I/usr/include/python2.7

SRCS_DIRS=$(shell find . -maxdepth 1 -type d)
SRCS = $(foreach dir,$(SRCS_DIRS),$(wildcard $(dir)/*.c))
OBJS = $(SRCS:%.c=%.o)

$(TARGET) :$(OBJS)
	g++ -o $@ $(patsubst %.o,$(OBJ_DIR)%.o,$(notdir $^)) callweb.cpp $(INCFLAGS) $(LIBFLAGS)

$(OBJS):$(SRCS)
	g++ -c $(patsubst %.o,%.c,$@) -o $(patsubst %.o,$(OBJ_DIR)%.o,$(notdir $@))

clean:
	@rm -f $(OBJ_DIR)*.o 
	@rm -f $(TARGET)

#g++ -c voice/voice.c -o voice/voice.o
#g++ -c signal/signal.c -o signal/signal.o
#g++ -o weather.cgi voice/voice.o signal/signal.o callweb.cpp
#-I/usr/include/python2.7
#-L/usr/lib/python2.7 -lpython2.7 -lmsc -lrt -ldl -lpthread -lbcm2835