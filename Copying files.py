# copyfile() = copies contents of a file
# copy() = copyfile + permission mode + destination can be a directory
# copy2 = copy() + copies metadata

import shutil

shutil.copy2('lamb.test','C:\\Users\\User\\Desktop\\copy.test')  #src,dst
