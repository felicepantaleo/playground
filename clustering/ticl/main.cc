#include "tbb/tbb.h"
#include <atomic>
#include <chrono>
#include <iostream>
#include <iomanip>

#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <thread>
#include <unistd.h>



#include "dist_generator.h"
#include "hgcPoint.h"

int main(int argc, char *argv[]) {

  int nPoints = 1000;
  unsigned int numberOfThreads = 1;


  tbb::task_scheduler_init init(numberOfThreads);

  auto avgX = -10.f;
  auto avgY = 2.f;
  auto peakE = 2.f;

  auto sigmaXY = 2.f;

  std::vector<hgcPoint> points_cloud =  generate_cluster(avgX, avgY,  peakE, sigmaXY, nPoints);

  for (auto& p : points_cloud)
  {
      std::cout << std::setw(12) << p.x << "\t" <<std::setw(12) << p.y << std::endl;
  }





  return 0;
}
