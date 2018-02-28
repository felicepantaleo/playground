#ifndef __HGCPOINT_H__
#define __HGCPOINT_H__
struct hgcPoint
{
    hgcPoint(float ox, float oy, float oE, int oc):
    x(ox), y(oy), E(oE), clid(oc)
    {

    }
    float x,y,E;
    int clid;

};


#endif /* end of include guard: __HGCPOINT_H__ */
