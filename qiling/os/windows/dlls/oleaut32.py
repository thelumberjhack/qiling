#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

import struct
from qiling.os.windows.fncc import *
from qiling.os.fncc import *
from qiling.os.windows.utils import *


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
        ret = strlen = len(_str)    # TODO: /sizeof(WCHAR)

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
        ret = strlen = len(_str)

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