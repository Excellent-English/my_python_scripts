# odczytuje informacje o aktualnie zalogowanym użytkowniku Windows/Active Directory
# import win32api
#
# email = win32api.GetUserNameEx(8)
# print(email)


import win32api

for i in range(0, 12):
    try:
        value = win32api.GetUserNameEx(i)
        print(f"{i} -> {value}")
    except Exception as e:
        print(f"{i} -> ERROR: {e}")