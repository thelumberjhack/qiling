#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

import struct
from qiling.os.windows.fncc import *
from qiling.os.fncc import *
from qiling.os.windows.utils import *

LPCOLESTR = WSTRING


class BSTR:
    """
    typedef struct {
        #ifdef _WIN64
            DWORD pad;
        #endif
            DWORD size;
            union {
                char ptr[1];
                WCHAR str[1];
                DWORD dwptr[1];
            } u;
        } bstr_t;
    """
    def __init__(self, ql, base=0, size=0, data=b""):
        self.ql = ql
        self.base = base

        self.pad = None
        self.data = data
        self.size = len(self.data)
        self.terminator = 0x0000


    def bytes(self):
        s = b""
        
        s += self.ql.pack(self.size)        # 0x00
        s += self.ql.pack(self.data)        # 0x04
        s += self.ql.pack(self.terminator)  # 0x04 + len(self.data)

        return s


# UINT WINAPI SysStringLen(
#     BSTR str
# );
@winapi(cc=STDCALL, params={
    "str": BSTR
})
def hook_SysStringLen(ql, address, params):
    ret = 0

    _str = params["str"]

    if _str:
        ret = _str.size

    return ret

# UINT WINAPI SysStringByteLen(
#     BSTR str
# );
@winapi(cc=STDCALL, params={
    "str": BSTR
})
def hook_SysStringByteLen(ql, address, params):
    ret = 0

    _str = params["str"]

    if _str:
        ret = len(_str.data)

    return ret


# BSTR WINAPI SysAllocString(
#     LPCOLESTR str
# );
@winapi(cc=STDCALL, params={
    "str": LPCOLESTR
})
def hook_SysAllocString(ql, address, params):
    _str = params["str"]

    if not _str:
        return 0

    raise NotImplementedError


# void WINAPI DECLSPEC_HOTPATCH SysFreeString(
#     BSTR str
# );
@winapi(cc=STDCALL, params={
    "str": BSTR
})
def hook_SysFreeString(ql, address, params):
    _str = params["str"]

    raise NotImplementedError


# BSTR WINAPI SysAllocStringLen(
#     const OLECHAR *str,
#     unsigned int len
# );
@winapi(cc=STDCALL, params={
    "str": POINTER,
    "len": UINT,
})
def hook_SysAllocStringLen(ql, address, params):
    _str = params["str"]
    lgth = params["len"]

    raise NotImplementedError


# int WINAPI SysReAllocStringLen(
#     BSTR* old,
#     const OLECHAR* str,
#     unsigned int len
# );
@winapi(cc=STDCALL, params={
    "old": POINTER,
    "str": POINTER,
    "len": UINT,
})
def hook_SysReAllocStringLen(ql, address, params):
    old = params["old"]
    _str = params["str"]
    lgth = params["len"]

    raise NotImplementedError