import cProfile
import euler_funcs

#https://jiffyclub.github.io/snakeviz/
#https://docs.python.org/3/library/profile.html

main_str = "euler_funcs."
for func in euler_funcs.__dict__:
     if "euler" in func:
         cProfile.run(main_str + str(func) + "()", "Euler/Profiles/" + str(func) + ".prof")