import sys
sys.stderr.write('stderr test\n')
sys.stderr.flush()
sys.stdout.write('stdout test\n')

print(sys.argv)
if len(sys.argv) > 1:
  print(sys.argv[1])
  print(float(sys.argv[1])+5)

