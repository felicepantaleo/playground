#ifndef __HGCPOINT_H__
#define __HGCPOINT_H__
struct hgcPoint
{
    hgcPoint(float a, float b, float c):
    x(a), y(b), E(c)
    {

    }
    float x,y,E;

};


#endif /* end of include guard: __HGCPOINT_H__ */
