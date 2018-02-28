#ifndef __DIST_GENERATOR_H_
#define __DIST_GENERATOR_H_
#include <vector>
#include <random>
#include "hgcPoint.h"


std::vector<hgcPoint> generate_cluster(int clusterId, float avgX, float avgY, float peakE, float sigmaXY, unsigned int nPoints)
{
    std::vector<hgcPoint> tmpPoints;
    tmpPoints.reserve(nPoints);
    std::default_random_engine generator;
    std::normal_distribution<float> x_distribution(avgX, sigmaXY);
    std::normal_distribution<float> y_distribution(avgY, sigmaXY);
    for (auto i=0; i<nPoints; ++i) {
        auto x = x_distribution(generator);
        auto y = y_distribution(generator);
        auto dist = std::sqrt((x- avgX)*(x- avgX) + (y - avgY) * (y - avgY));
      tmpPoints.emplace_back(x, y, peakE*std::exp(-2.f*dist), clusterId) ;
    }
    return tmpPoints;
}


void generate_cluster(std::vector<hgcPoint>& points, int clusterId, float avgX, float avgY, float peakE, float sigmaXY, unsigned int nPoints)
{
    points.reserve(points.size() + nPoints);
    std::default_random_engine generator;
    std::normal_distribution<float> x_distribution(avgX, sigmaXY);
    std::normal_distribution<float> y_distribution(avgY, sigmaXY);
    for (auto i=0; i<nPoints; ++i) {
        auto x = x_distribution(generator);
        auto y = y_distribution(generator);
        auto dist = std::sqrt((x- avgX)*(x- avgX) + (y - avgY) * (y - avgY));
      points.emplace_back(x, y, peakE*std::exp(-2.f*dist), clusterId) ;
    }

}



std::vector<hgcPoint> generate_noise( float minX, float maxX, float minY, float maxY, unsigned int nPoints)
{
    std::default_random_engine generator;
    std::uniform_real_distribution<float> x_distribution(minX,maxX);
    std::uniform_real_distribution<float> y_distribution(minY,maxY);
    std::normal_distribution<float> E_distribution(0.5f, 0.3f);
    std::vector<hgcPoint> tmpPoints;
    tmpPoints.reserve(nPoints);
    float tmpE = 0.f;
    for (auto i=0; i<nPoints; ++i) {
        do
        {
            tmpE = E_distribution(generator);

        } while(tmpE<0.f);



      tmpPoints.emplace_back(x_distribution(generator), y_distribution(generator), 1, -1) ;
    }

    return tmpPoints;
}


void generate_noise(std::vector<hgcPoint>& points, float minX, float maxX, float minY, float maxY, unsigned int nPoints)
{
    std::default_random_engine generator;
    std::uniform_real_distribution<float> x_distribution(minX,maxX);
    std::uniform_real_distribution<float> y_distribution(minY,maxY);
    std::normal_distribution<float> E_distribution(0.5f, 0.3f);
    points.reserve(points.size() + nPoints);
    float tmpE = 0.f;
    for (auto i=0; i<nPoints; ++i) {
        do
        {
            tmpE = E_distribution(generator);

        } while(tmpE<0.f);



      points.emplace_back(x_distribution(generator), y_distribution(generator), 1, -1) ;
    }

}


#endif /* end of include guard: __DIST_GENERATOR_H_ */
