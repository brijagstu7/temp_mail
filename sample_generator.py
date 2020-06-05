from cyaron import *

build_path = "/Users/yang_sijie/Library/Developer/Xcode/DerivedData/test01-eswlmwfqueexisgsfwmplbcfxrio/Build" \
             "/Products/Debug/test01"

# 样例集
io = {}
for i in range(0, 1):
    io[i] = IO(file_prefix="test")

    io[i].output_gen(build_path)
