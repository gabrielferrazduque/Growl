ModelGL.cpp of your modelview matrix project 
matModel.rotateZ(modelAngle[2]);
matModel.rotateY(modelAngle[1]);
matModel.rotateX(modelAngle[0]);
matModel.translate(modelPosition[0], modelPosition[1], modelPosition[2]);
matModelView = matView * matModel;
glLoadMatrixf(matModelView.get());
if i change it to
matModel.rotateZ(modelAngle[2]);
matModel.rotateY(modelAngle[1]);
matModel.rotateX(modelAngle[0]);
matModelView = matView * matModel;
matModelView.translate(modelPosition[0], modelPosition[1], modelPosition[2]);
glLoadMatrixf(matModelView.get());
nothing happens, but if i make opengl do the translation part like this
matModel.rotateZ(modelAngle[2]);
matModel.rotateY(modelAngle[1]);
matModel.rotateX(modelAngle[0]);
matModelView = matView * matModel;
glLoadMatrixf(matModelView.get());
glTranslatef(modelPosition[0], modelPosition[1], modelPosition[2])/* v' = Mt · Mr · v */
glTranslatef(...);
glRotatef(...);
glVertex3f(...);  
matModelView (); 
/ This creates a symmetric frustum.
// It converts to 6 params (l, r, b, t, n, f) for glFrustum()
// from given 4 params (fovy, aspect, near, far)
void makeFrustum(double fovY, double aspectRatio, double front, double back)
{
    const double DEG2RAD = 3.14159265 / 180;

    double tangent = tan(fovY/2 * DEG2RAD);   // tangent of half fovY
    double height = front * tangent;          // half height of near plane
    double width = height * aspectRatio;      // half width of near plane

    // params: left, right, bottom, top, near, far
    glFrustum(-width, width, -height, height, front, back);
}// Note that the object will be translated first then rotated
glRotatef(angle, 1, 0, 0);   // rotate object angle degree around X-axis
glTranslatef(x, y, z);       // move object to (x, y, z)
drawObject();
gluLookAt()glTranslatef()
/ This creates a symmetric frustum.
// It converts to 6 params (l, r, b, t, n, f) for glFrustum()
// from given 4 params (fovy, aspect, near, far)
void makeFrustum(double fovY, double aspectRatio, double front, double back)
{
    const double DEG2RAD = 3.14159265 / 180;

    double tangent = tan(fovY/2 * DEG2RAD);   // tangent of half fovY
    double height = front * tangent;          // half height of near plane
    double width = height * aspectRatio;      // half width of near plane

    // params: left, right, bottom, top, near, far
    glFrustum(-width, width, -height, height, front, back);
}
// rotate texture around X-axis
glMatrixMode(GL_TEXTURE);
glRotatef(angle, 1, 0, 0);
...glRotatef(), glTranslatef(), glScalef().

glPushMatrix();glRotatef(), glTranslatef(), glScalef().

// set view matrix for camera transform
glLoadMatrixf(matrixView.get());

// draw the grid at origin before model transform
drawGrid();

// set modelview matrix for both model and view transform
// It transforms from object space to eye space.
glLoadMatrixf(matrixModelView.get());

// draw a teapot after both view and model transforms
drawTeapot();

glPopMatrix();
... glPushMatrix  

...height()
glPushMatrix();

// initialze ModelView matrix
glLoadIdentity();

// First, transform the camera (viewing matrix) from world space to eye space
// Notice translation and heading values are negated,
// because we move the whole scene with the inverse of camera transform
// ORDER: translation -> roll -> heading -> pitch
glRotatef(cameraAngle[2], 0, 0, 1);  // roll
glRotatef(-cameraAngle[1], 0, 1, 0); // heading
glRotatef(cameraAngle[0], 1, 0, 0);  // pitch
glTranslatef(-cameraPosition[0], -cameraPosition[1], -cameraPosition[2]);

// draw the grid at origin before model transform
drawGrid();

// transform the object (model matrix)
// The result of GL_MODELVIEW matrix will be:
// ModelView_M = View_M * Model_M
// ORDER: rotZ -> rotY -> rotX -> translation
glTranslatef(modelPosition[0], modelPosition[1], modelPosition[2]);
glRotatef(modelAngle[0], 1, 0, 0);
glRotatef(modelAngle[1], 0, 1, 0);
glRotatef(modelAngle[2], 0, 0, 1);

// draw a teapot with model and view transform together
drawTeapot();

glPopMatrix();
... 

///////////////////////////////////////////////////////////////////////////////
// return a perspective frustum with 6 params similar to glFrustum()
// (left, right, bottom, top, near, far)
///////////////////////////////////////////////////////////////////////////////
Matrix4 ModelGL::setFrustum(float l, float r, float b, float t, float n, float f)
{
    Matrix4 matrix;
    matrix[0]  =  2 * n / (r - l);
    matrix[5]  =  2 * n / (t - b);
    matrix[8]  =  (r + l) / (r - l);
    matrix[9]  =  (t + b) / (t - b);
    matrix[10] = -(f + n) / (f - n);
    matrix[11] = -1;
    matrix[14] = -(2 * f * n) / (f - n);
    matrix[15] =  0;
    return matrix;
}

///////////////////////////////////////////////////////////////////////////////
// return a symmetric perspective frustum with 4 params similar to
// gluPerspective() (vertical field of view, aspect ratio, near, far)
///////////////////////////////////////////////////////////////////////////////
Matrix4 ModelGL::setFrustum(float fovY, float aspectRatio, float front, float back)
{
    float tangent = tanf(fovY/2 * DEG2RAD);   // tangent of half fovY
    float height = front * tangent;           // half height of near plane
    float width = height * aspectRatio;       // half width of near plane

    // params: left, right, bottom, top, near, far
    return setFrustum(-width, width, -height, height, front, back);
}glRotatef() 
glTranslatef() glScalef()
///////////////////////////////////////////////////////////////////////////////
// set a orthographic frustum with 6 params similar to glOrtho()
// (left, right, bottom, top, near, far)
///////////////////////////////////////////////////////////////////////////////
Matrix4 ModelGL::setOrthoFrustum(float l, float r, float b, float t, float n, float f)
{ (m0, m1, m2), (m4, m5, m6) and (m8, m9, m10)(m12, m13, m14)
    Matrix4 matrix;
    matrix[0]  =  2 / (r - l);
    matrix[5]  =  2 / (t - b);
    matrix[10] = -2 / (f - n);
    matrix[12] = -(r + l) / (r - l);
    matrix[13] = -(t + b) / (t - b);
    matrix[14] = -(f + n) / (f - n);
    return matrix;
}
... P1=(3,4) à P2=(20,18) 
Xmin = 5, Xmax = 10, Ymin = 7, Ymax = 13,  
  Xmin = 2, Xmax = 10, Ymin = 10, Ymax = 17,
 Xmin = 2, Xmax = 10, Ymin = 10, YmaxP1=(3,4) à P2=(20,18) = 17, 
 P1=(3,4) à P2=(20,18) P1=(15,11) à P2=(1,3)
// how to pass projection matrx to OpenGL
Matrix4 projectionMatrix = setFrustum(l, r, b, t, n, f);
glMatrixMode(GL_PROJECTION);
glLoadMatrixf(matrixProjection.get()); 
(m0, m1, m2)   : +X axis, left vector, (1, 0, 0) by default
(m4, m5, m6)   : +Y axis, up vector, (0, 1, 0) by default
(m8, m9, m10) : +Z axis, forward vector, (0, 0, 1) by default

... 
