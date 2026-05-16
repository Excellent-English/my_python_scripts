
import ctypes

def get_upn():
    NameUserPrincipal = 8  # EXTENDED_NAME_FORMAT: NameUserPrincipal
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameUserPrincipal, None, size)

    buf = ctypes.create_unicode_buffer(size.contents.value)
    if not GetUserNameEx(NameUserPrincipal, buf, size):
        return None
    return buf.value

print(get_upn())

