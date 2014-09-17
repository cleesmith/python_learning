import datetime
import multiprocessing

def worker(num):
  print('(%s). worker at %s' % (num, datetime.datetime.now()))
  return

if __name__ == '__main__':
  jobs = []
  for i in range(5):
    print('before: multiprocessing.Process')
    p = multiprocessing.Process(target=worker, args=(i,))
    print('before: jobs.append')
    jobs.append(p)
    print('before: p.start')
    p.start()
    print('after: p.start')
