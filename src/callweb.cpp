#include "callweb.h"

string call_python()
{
		// 初始化Python
		//在使用Python系统前，必须使用Py_Initialize对其
		//进行初始化。它会载入Python的内建模块并添加系统路
		//径到模块搜索路径中。这个函数没有返回值，检查系统
		//是否初始化成功需要使用Py_IsInitialized。

	Py_Initialize();

		// 检查初始化是否成功
	if ( !Py_IsInitialized() )
	{
		return "初始化失败";
	}
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	PyObject *pArgs,*pModule,*pFunc,*pRet;

	pModule = PyImport_ImportModule("web");//引入模块
	if ( !pModule )
	{
		return "找不到文件";
	}
	pFunc = PyObject_GetAttrString(pModule, "TestUrlOpen");
	if ( !pFunc || !PyCallable_Check(pFunc) )
	{
		return "找不到函数";
	}
	// 参数进栈
	pArgs = PyTuple_New(0);

	// 调用Python函数
	pRet = PyEval_CallObject(pFunc,pArgs);

	char *aa;
	if(pRet && PyArg_Parse(pRet,"s", &aa));
	string str(aa);
	Py_DECREF(pArgs);
	Py_DECREF(pModule);
	Py_DECREF(pFunc);
	Py_DECREF(pRet);
	
	// 关闭Python
	Py_Finalize();
	return str;
} 

int main(int argc,char* argv[])  
{ 
	if(get_signal()==0x0c)
	{
		string  voice_str=call_python();
		printf("%s\n",voice_str.c_str());
		text_to_voice(voice_str.c_str());
		system("omxplayer /share/Picture/callweb/src/weather.wav");
	}
	if(get_signal()==0x18)
	{
		system("omxplayer /share/Video/Victory.mp3");
	}
	exit(0);
}
//g++ -o weather.cgi voice/voice.c callweb.cpp -I/usr/include/python2.7 
//-L/usr/lib/python2.7 -lpython2.7 -lmsc -lrt -ldl -lpthread
//gcc -c -g -Wall -I../../include tts_sample.c -o tts_sample.o
//gcc -g -Wall -I../../include tts_sample.o -o ../../bin/tts_sample 
//-L../../libs/x64 -lmsc -lrt -ldl -lpthread
//gcc -Wall irm.c -o irm -lbcm2835

//编译过程
//g++ -c voice/voice.c -o voice/voice.o
//g++ -c signal/signal.c -o signal/signal.o
///g++ -o weather.cgi voice/voice.o signal/signal.o callweb.cpp -I/usr/include/python2.7 -L/usr/lib/python2.7 -lpython2.7 -lmsc -lrt -ldl -lpthread -lbcm2835