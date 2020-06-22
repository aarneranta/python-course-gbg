# examples of variable scope
# file scope_example.py

gv = "gv is global"
print(gv)

def scopes():
    print("entering function")
    gv = "  gv is local now"
    print(gv)
    lv = "  lv is local"
    print(lv)
    print("leaving function")

scopes()

print(gv,"again")
print("Trying to use lv outside function:")
print(lv)

