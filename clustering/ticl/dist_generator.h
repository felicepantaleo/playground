#ifndef __DIST_GENERATOR_H_
#define __DIST_GENERATOR_H_
#include <vector>
#include <random>
#include "hgcPoint.h"


std::vector<hgcPoint> generate_cluster(float avgX, float avgY, float peakE, float sigmaXY, unsigned int nPoints)
{
    std::vector<hgcPoint> tmpPoints;
    tmpPoints.reserve(nPoints);
    std::default_random_engine generator;
    std::normal_distribution<float> x_distribution(avgX, sigmaXY);
    std::normal_distribution<float> y_distribution(avgY, sigmaXY);
    for (auto i=0; i<nPoints; ++i) {
      tmpPoints.emplace_back(x_distribution(generator), y_distribution(generator), 1) ;

    }

    return tmpPoints;
}


#endif /* end of include guard: __DIST_GENERATOR_H_ */
