#include "tbb/tbb.h"
#include <atomic>
#include <chrono>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <thread>
#include <unistd.h>

static void show_usage(std::string name) {
  std::cerr << "\nUsage: " << name << " <option(s)>"
            << " Options:\n"
            << "\t-h,--help\t\tShow this help message\n"
            << "\t-n <number of points>\tSpecify the number of points to use "
               "for the kdtree [default 100000]\n"
            << "\t-j <number of threads>\tSpecify the number of tbb parallel "
               "threads to use [default 1]\n"
            << std::endl;
}
int main(int argc, char *argv[]) {
  if (argc < 2) {
    show_usage(argv[0]);
    return 1;
  }

  int nPoints = 100000;
  unsigned int numberOfThreads = 1;
  for (int i = 1; i < argc; ++i) {
    std::string arg = argv[i];
    if ((arg == "-h") || (arg == "--help")) {
      show_usage(argv[0]);
      return 0;
    }

    else if (arg == "-n") {
      if (i + 1 < argc) // Make sure we aren't at the end of argv!
      {
        i++;
        std::istringstream ss(argv[i]);
        {
          if (!(ss >> nPoints))
            std::cerr << "Invalid number " << argv[i] << '\n';
          exit(1);
        }
      }
    }

    else if (arg == "-j") {
      if (i + 1 < argc) // Make sure we aren't at the end of argv!
      {
        i++;
        std::istringstream ss(argv[i]);
        if (!(ss >> numberOfThreads)) {
          std::cerr << "Invalid number of threads " << argv[i] << '\n';

          exit(1);
        }
      }
    }
  }
  tbb::task_scheduler_init init(numberOfThreads);








  return 0;
}
