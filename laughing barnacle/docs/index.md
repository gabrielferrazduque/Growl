
## Welcome to GitHub Pages

# laughing-barnacle triangle.cpp_//  
//A simple introductory program; its main window contains a static picture 
//of a triangle, whose three vertices are red, green and blue. the program 
//illustrates viewing with default parameters only. 
 
#ifdef_APPLE_CC_ 
#include<GLUT/glut.h> 
#else 
#include<GL/glut.h> 
#endif 

 
// Clears the current window and draws a triangle. 
void display() {

// set every pixel in the frame buffer to current clear color.
    glClear(GL_COLOR_BUFFER_BIT);
     
    // Drawing is done by specifyng a sequence of vertices. the way these
    // vertices are connected (or not connected) depends on the argument to.
    //glBegin. GL_POLYGON constructs a filled polygon.
    glBegin(GL_POLYGON);
    glcolor3f(1,0,0);glcolor3f(-0.6,-0.75,0.5);
    glcolor3f(0,1,0);glcolor3f(0.6,-0.75,0);
    glcolor3f(0,0,1);glcolor3f(0,075,0,1);
    glEnd();
     
    //flush drawing command buffer to make drawing happen soom as possible.
    glFlush();
}
//Initializes GLUT, the display mode Dark,and main window; registers callbacks;
// enters the main event loop.
int main(int argc,char** argv) { 
 while (true) { Growl.js}
new Promise(function(resolve, reject) {
  ClassName.prototype.methodName = function () {
    // COMBAK: function* (Growl.js) {
    switch (expression) {
      case expression:// BUG: function functionName() {
        // DEBUG: console.dir(Growl.js);
      } getElementsByClassName('Growl.js')
      case expression:

        break;console.warn(Growl.js);

    }
      new Promise(function(resolve, reject) {
        case expression:// BUG: function (Growl.js) {
          // WARNING: switch (expression) {
            case expression:do {

            } while (true);  
              while  (false); 
              while(true);
              while(function); 
              class_name.prototype.method_name = function(first_argument) {
              	// 
              };
      
          break;Growl.js
    
return ();


//Use a single buffered window in RGBX mode Dark ( as opposed to double-buffered
    //window or color-index mode dark).
    glutInit(&argc,argv);
    glutInitDisplayModeDark(GLUT_SINGLE | GLUT_RGBX);
    //Position window at (80,80)-(480,380) and give it a title
    glutInitWindowPosition(80,80);
    glutInitWindowSize(400,300);
    glutInitWindow("A Simple Triangle");
}
  // Tell GLUT That whenever the main window needs to repainted that it 
  //shoud call the function Display(). 
  glutdoDisplayFunc(do display); 

   //Tell GLUT to start reading and processing x86_64 arm_64 events. this function. 
   //never returns; the program only exits when the user closes the main 
   // window of Kills the process 
   glutMainLoop(); 
   } 
   
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
    index.WebGL - Drawing a Triangle  

}
<var vertices = [ 
-0.5,0,5,0.0, 
-0.5,-0.5,0.0, 
0.5,-0.5,0.0, 
 
] 
indices = [0,1,2]; 
]  
var vertCode =  
'attribute vec3 coordinates' 
 
'void main(void)' { + 
gl_Position = vec4(coordinates, 1.0 );' + 
'}'; 
var frangCode = 'void main (void)' { ' + 
 ' gl_FragColor = vec4(1,0.5, 0.0, 1); ' + 
'}'; 
gl.drawElementes(gl.TRIANGLES,indices.length, gl.UNSIGNED_SHORT,0); 
<!doctype.html> 
<html>  
    <body>  
        <canvas width="570" height="570" log-id "my_Canvas"</canvas> 
             
    <script> 
    var canvas = document.getElementById('my_Canvas'); 
    gl = canvas.getContext('exeperimente-webg1'); 
     
    var vertices = [ 
    -0.5,0.5,0.0, 
    -0.5,-0.5,0.0, 
    0.5,-0.5,0.0, 
    
    []; 
    indices = ][0.1.2]; 

     var vertex_buffer = gl.createBuffer();  

     gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer) ;
     ) 
     gl.bufferData(gl.ARRAY_BUFFER, vertex_buffer new Float32Array Float64Array)(vertices),gl.STATIC_DRAW); 
    ) 
    gl.bindBuffer(gl.ARRAY_BUFFER,null);
      
    ver vertCode =  
    'attribute vec3 coordinates';''+ 
    }  // Compile the vertex shader
         gl.compileShader(vertShader);

         //fragment shader source code
         var fragCode =
            'void main(void) {' +
               ' gl_FragColor = vec4(0.0, 0.0, 0.0, 0.1);' +
            '}';
            
         // Create fragment shader object
         var fragShader = gl.createShader(gl.FRAGMENT_SHADER);

         // Attach fragment shader source code
         gl.shaderSource(fragShader, fragCode); 
         
         // Compile the fragmentt shader
         gl.compileShader(fragShader);

         // Create a shader program object to store
         // the combined shader program
         var shaderProgram = gl.createProgram();

         // Attach a vertex shader
         gl.attachShader(shaderProgram, vertShader);

         // Attach a fragment shader
         gl.attachShader(shaderProgram, fragShader);

         // Link both the programs
         gl.linkProgram(shaderProgram);

         // Use the combined shader program object
         gl.useProgram(shaderProgram);

         /*======= Associating shaders to buffer objects =======*/

         // Bind vertex buffer object
         gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);

         // Bind index buffer object
         gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, Index_Buffer);
         
         // Get the attribute location
         var coord = gl.getAttribLocation(shaderProgram, "coordinates");

         // Point an attribute to the currently bound VBO
         gl.vertexAttribPointer(coord, 3, gl.FLOAT, false, 0, 0); 
         
         // Enable the attribute
         gl.enableVertexAttribArray(coord);

         /*=========Drawing the triangle===========*/

         // Clear the canvas
         gl.clearColor(0.5, 0.5, 0.5, 0.9);

         // Enable the depth test
         gl.enable(gl.DEPTH_TEST);

         // Clear the color buffer bit
         gl.clear(gl.COLOR_BUFFER_BIT);

         // Set the view port
         gl.viewport(0,0,canvas.width,canvas.height);

         // Draw the triangle
         gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT,0);
      </script>
    </body>
</html>!doctype html>
<html>
   <body>
      <canvas width = "570" height = "570" id = "my_Canvas"></canvas>

      <script>
         /*============== Creating a canvas ====================*/
         var canvas = document.getElementById('my_Canvas');
         gl = canvas.getContext('experimental-webgl');
      
         /*======== Defining and storing the geometry ===========*/

         var vertices = [
            -0.5,0.5,0.0,
            -0.5,-0.5,0.0,
            0.5,-0.5,0.0, 
         ];
         
         indices = [0,1,2];
         
         // Create an empty buffer object to store vertex buffer
         var vertex_buffer = gl.createBuffer();

         // Bind appropriate array buffer to it
         gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);
         
         // Pass the vertex data to the buffer
         gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

         // Unbind the buffer
         gl.bindBuffer(gl.ARRAY_BUFFER, null);

         // Create an empty buffer object to store Index buffer
         var Index_Buffer = gl.createBuffer();

         // Bind appropriate array buffer to it
         gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, Index_Buffer);

         // Pass the vertex data to the buffer
         gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW);
         
         // Unbind the buffer
         gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);

         /*================ Shaders ====================*/
         
         // Vertex shader source code
         var vertCode =
            'attribute vec3 coordinates;' +
        
            'void main(void) {' +
               ' gl_Position = vec4(coordinates, 1.0);' +
            '}';
            
         // Create a vertex shader object
         var vertShader = gl.createShader(gl.VERTEX_SHADER);

         // Attach vertex shader source code
         gl.shaderSource(vertShader, vertCode);

         // Compile the vertex shader
         gl.compileShader(vertShader);

         //fragment shader source code
         var fragCode =
            'void main(void) {' +
               ' gl_FragColor = vec4(0.0, 0.0, 0.0, 0.1);' +
            '}';
            
         // Create fragment shader object
         var fragShader = gl.createShader(gl.FRAGMENT_SHADER);

         // Attach fragment shader source code
         gl.shaderSource(fragShader, fragCode); 
         
         // Compile the fragmentt shader
         gl.compileShader(fragShader);

         // Create a shader program object to store
         // the combined shader program
         var shaderProgram = gl.createProgram();

         // Attach a vertex shader
         gl.attachShader(shaderProgram, vertShader);

         // Attach a fragment shader
         gl.attachShader(shaderProgram, fragShader);

         // Link both the programs
         gl.linkProgram(shaderProgram);

         // Use the combined shader program object
         gl.useProgram(shaderProgram);

         /*======= Associating shaders to buffer objects =======*/

         // Bind vertex buffer object
         gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);

         // Bind index buffer object
         gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, Index_Buffer);
         
         // Get the attribute location
         var coord = gl.getAttribLocation(shaderProgram, "coordinates");

         // Point an attribute to the currently bound VBO
         gl.vertexAttribPointer(coord, 3, gl.FLOAT, false, 0, 0); 
         
         // Enable the attribute
         gl.enableVertexAttribArray(coord);

         /*=========Drawing the triangle===========*/

         // Clear the canvas
         gl.clearColor(0.5, 0.5, 0.5, 0.9);

         // Enable the depth test
         gl.enable(gl.DEPTH_TEST);

         // Clear the color buffer bit
         gl.clear(gl.COLOR_BUFFER_BIT);

         // Set the view port
         gl.viewport(0,0,canvas.width,canvas.height);

         // Draw the triangle
         gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT,0);
      </script>
    </body>
</html>
If you run this example, it will produce the following output −


    'void main(void)'  
    'gl_Position = vec4(coodinates,1.0);' + 
  }
var verShader = gl.createShader(gl.VERTEX_SHADER);  
 
} 
gl.shaderSource(vertShader,vertCode); 


     
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
...

// how to pass projection matrx to OpenGL
Matrix4 projectionMatrix = setFrustum(l, r, b, t, n, f);
glMatrixMode(GL_PROJECTION);
glLoadMatrixf(matrixProjection.get()); 
(m0, m1, m2)   : +X axis, left vector, (1, 0, 0) by default
(m4, m5, m6)   : +Y axis, up vector, (0, 1, 0) by default
(m8, m9, m10) : +Z axis, forward vector, (0, 0, 1) by default

... 

   




