#version 330

uniform sampler2D background;
uniform float iTime;
uniform vec2 iMouse;
uniform vec2 iResolution;
uniform float scaleFactor;
uniform vec2 offsetXY;

in vec2 v_uv;
out vec4 out_color;

float getMu (int i, float abszSquared) {
    return i + 1 - (log(0.5 * log(abszSquared))) / log(2.0);
}

float mandelbrot(vec2 c, int iters) {
    vec2 z = vec2(0.0, 0.0);
    for (int i=0; i < iters; i++) {
        z = vec2(z.x * z.x - z.y * z.y + c.x, 2 * z.x * z.y + c.y);

        float abszSquared = z.x * z.x + z.y * z.y;
        float mu = getMu(i, abszSquared);
        if (abszSquared > 4.0) return mu;
    }
    return iters;
}

float burningShip(vec2 c, int iters) {
    vec2 z = vec2(0, 0);
    for (int i=0; i<iters; i++) {
        z = vec2(z.x * z.x - z.y * z.y + c.x, 2 * abs(z.x) * abs(z.y) + c.y);

        float abszSquared = z.x * z.x + z.y * z.y;
        float mu = getMu(i, abszSquared);

        if (abszSquared > 16.0) return mu;
    }
    return iters;
}

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    int iters = 500;
    float maxTime = 15.0;
    float diameter = 2.5;

    float speed = 8;

    vec3 col;
    vec2 scaled;
    vec2 mousexy;

    vec2 uv = fragCoord/iResolution.xy; 

    vec2 mouseScaled = iMouse/(iResolution.xy * scaleFactor);

    mousexy += mouseScaled;


    float t = iTime + 1; //min(iTime+1, maxTime);
    scaled.x =   offsetXY.x + (3*uv.x - 1.5) / pow(abs(scaleFactor)+1, abs(scaleFactor)+1); //(pow(t, (t/speed)));
    scaled.y =   offsetXY.y - (2*uv.y - 1) / pow(abs(scaleFactor)+1, abs(scaleFactor)+1); //(pow(t, (t/speed)));

    //float i = mandelbrot(vec2(3.5 * uv.x - diameter, 2.5*uv.y-1.25), iters);
    //float i = burningShip(vec2(3.5 * uv.x - diameter, 1 - 2*uv.y), iters);
    //float i = burningShip(scaled, iters);
    float i = mandelbrot(scaled, iters);


    float p = 10;
    float offset = 0;

    float c = sin(p * i/float(iters) + offset)/2 + 1;

    if (i == float(iters)) col = vec3(0, 0, 0);
    else col = hsv2rgb(vec3(c, 1.0, 1.0));
    

    fragColor = vec4(col, 1.0);
}

void main() {
    vec4 color;
    mainImage(color, gl_FragCoord.xy);
    out_color = color;
}
