fndef PRIMEIROPROGRAMAEMOPENGL_cpp
#define PRIMEIROPROGRAMAEMOPENGL_cpp 

#include <QDeclarativeItem>
#include <QMainWindow>
#include <QObject>
#include <QQuickItem>
#include <QSharedDataPointer>
#include <QWidget>

class PrimeiroProgramaemOpenGLData;

class PrimeiroProgramaemOpenGL
{
    Q_OBJECT
public:
    PrimeiroProgramaemOpenGL();
    PrimeiroProgramaemOpenGL(const PrimeiroProgramaemOpenGL &);
    PrimeiroProgramaemOpenGL &operator=(const PrimeiroProgramaemOpenGL &);
    ~PrimeiroProgramaemOpenGL();

private:
    QSharedDataPointer<PrimeiroProgramaemOpenGLData> data;
};

#endif // PRIMEIROPROGRAMAEMOPENGL_cpp
#pragma  *data
#pragma omp parallel
#pragma omp for ordered
#pragma omp parallel
#pragma omp ordered

