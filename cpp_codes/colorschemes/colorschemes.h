#ifndef COLOR_SCHEMES_H_
#define COLOR_SCHEMES_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct RGB
{
	uint8_t r, g, b;
	RGB(uint8_t r_, uint8_t g_, uint8_t b_) {
		r = r_;
		g = g_;
		b = b_;
	}
} RGB; // __attribute__((aligned (1)))

#define M_CLASSIC		0
#define M_FIRE			1
#define M_OMG			2
#define M_PBJ			3
#define M_PGAITCH		4

extern const char* modes[];
extern const RGB schemes[5][256];

#ifdef __cplusplus
}
#endif

#endif//COLOR_SCHEMES_H_
