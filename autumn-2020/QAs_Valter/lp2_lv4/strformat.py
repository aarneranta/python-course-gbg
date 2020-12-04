# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 : 123.46, 1.00e+04, 1.23e+04'

def format_func(t):
    s = "file_{:03} : {:.2f}, {:.2e}, {:.2e}"
    return s.format(t[0], t[1], t[2], t[3])s
