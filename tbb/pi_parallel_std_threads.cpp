#include <iostream>
#include <iomanip>
#include <iostream>
#include <thread>
#include <vector>
#include <algorithm>
#include"tbb/tick_count.h"

int main()
{
  const int num_steps = 100000;

  double pi = 0.0;
  double step = 1.0/(double) num_steps;
  auto numThreads = 4;

  std::vector<std::thread> workers;
  auto start = tbb::tick_count::now();

  std::vector<double> partialSums(numThreads,0.0);
  // vector container stores threads
  for (int id = 0; id < numThreads; id++) {
      workers.push_back(std::thread([=, &partialSums]()
      {
        double x;
        double sum = 0.;
        for (int i=id;i< num_steps; i=i+numThreads) {
          x = (i+0.5)*step;
          sum += 4.0/(1.0+x*x);
        }
        partialSums[id] = sum;
      }));
  }

  std::for_each(workers.begin(), workers.end(), [](std::thread &t)
  {
      t.join();
  });

  for (int id = 0; id < numThreads; id++) {
    pi += partialSums[id] * step;
  }

  auto stop = tbb::tick_count::now();
  std::cout << "result: " <<  std::setprecision (15) << pi << std::endl;
  std::cout << "time: " << (stop-start).seconds() << " seconds" << std::endl;

  return 0;

}
