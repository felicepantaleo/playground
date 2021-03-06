
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

#include "tbb/tbb.h"

#include "dist_generator.h"
#include "hgcPoint.h"

int main(int argc, char *argv[]) {

  int nPoints = 1000;
  unsigned int numberOfThreads = 1;


  tbb::task_scheduler_init init(numberOfThreads);

  auto avgX = -1.f;
  auto avgY = 2.f;
  auto peakE = 2.f;

  auto sigmaXY = 0.5f;

  std::vector<hgcPoint> points_cloud =  generate_cluster(0, avgX, avgY,  peakE, sigmaXY, 50);
  generate_noise(points_cloud, -10, 10, -10,  10,  10000);

  for (auto& p : points_cloud)
  {
      std::cout << std::setw(12) << p.x << "\t" <<std::setw(12) << p.y << "\t" <<std::setw(12) << p.E << std::endl;
  }



  return 0;
}
