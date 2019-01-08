#ifndef HEAT_MAP_H_
#define HEAT_MAP_H_

#ifdef __cplusplus
extern "C" {
#endif

struct info
{
	float minX;
	float minY;
	float maxX;
	float maxY;

	int width;
	int height;
	int dotsize;
};

struct point {
    float x;
    float y;
};

unsigned char *tx(float *points, 
                  int cPoints, 
                  int w, int h, 
                  int dotsize, 
                  int scheme_mode, 
                  unsigned char *pix_color, 
                  int opacity, 
                  int boundsOverride, 
                  float minX, float minY, float maxX, float maxY);


#ifdef __cplusplus
}
#endif

#endif //HEAT_MAP_H_

