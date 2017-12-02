#include <iostream>
#include <iomanip>
#include"tbb/task_scheduler_init.h"
#include"tbb/parallel_for.h"
#include"tbb/blocked_range.h"
#include"tbb/spin_mutex.h"
#include"tbb/tick_count.h"

int main()
{
  const int num_steps = 1000000000;

  double pi = 0.0;
  double step = 1.0/(double) num_steps;

  tbb::spin_mutex myMutex;
  tbb::task_scheduler_init tbb_init;



  auto start = tbb::tick_count::now();

  tbb::parallel_for (tbb::blocked_range<int> (0, num_steps),
  [&](const tbb::blocked_range<int>& range)
  {

    double x, sum = 0.0;
    for (int i = range.begin(); i< range.end(); ++i) {
      x = (i+0.5)*step;
      sum = sum + 4.0/(1.0 + x*x);
    }
    tbb::spin_mutex::scoped_lock lock(myMutex);
    pi += step * sum;

  }
  , tbb::auto_partitioner());



  auto stop = tbb::tick_count::now();
  std::cout << "result: " <<  std::setprecision (15) << pi << std::endl;
  std::cout << "time: " << (stop-start).seconds() << " seconds" << std::endl;

  return 0;

}
