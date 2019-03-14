from libtbx import easy_run
for i in range(73):
  command="cat ./ase/%d/%d_capping/energy"%(i,i)
  print command
  easy_run.call(command)
