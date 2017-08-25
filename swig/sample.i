%module sample
%{
#include "sample.h"
%}

%extend Point{
    Point(double x, double y){
    Point *p = (Point*) malloc(sizeof(Point));

    }
}