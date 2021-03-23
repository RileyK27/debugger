from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
  def __init__(self):
    pass
  
  def load(self, path_to_exe):
    #sturucture changes to instuns
    creation_flags = DEBUG_PROCESS
    process_information = PROCESS_INFORMATION()
    
    #It shows independent
    #Shows how effect to debugger process
    startupinfo.dwFlags = 0x1
    startupinfo.wShowWindow = 0x0
    
    startupinfo.cb = sizeof(startupinfo)
    
    if kernel32.CreateProcessA(Path_to_exe,
                               None,
                               None,
                               None,
                               None,
                               creation_flags,
                               None,
                               None,
                               byref(startupinfo),
                               byref(process_information)):
      print("[*] we have successfully launched the process!")
      print("[*] PID: %d" % process_information.dwProcessId)
    else:
      print("[*] Error: 0x%08x." % kernel32.GetLastError())
                              
