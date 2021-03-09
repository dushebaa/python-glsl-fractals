int mandelbrot(vec2 c, int iters) {
    vec2 z = vec2(0, 0);
    for (int i=0; i<iters; i++) {
        z = vec2(z.x * z.x - z.y * z.y + c.x, 2 * z.x * z.y + c.y);
        if (z.x * z.x + z.y * z.y > 4) return i;
    }
    return iters;
}

int burningShip(vec2 c, int iters) {
    vec2 z = vec2(0, 0);
    for (int i=0; i<iters; i++) {
        z = vec2(z.x * z.x - z.y * z.y + c.x, 2 * abs(z.x) * abs(z.y) + c.y);
        if (z.x * z.x + z.y * z.y > 16) return i;
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
    int iters = 3500;
    float maxTime = 5;

    vec3 col;
    vec2 scaled;
    
    vec2 uv = fragCoord/iResolution.xy; 
    
    float t = min(iTime, maxTime);
    scaled.x = -1.75 + (uv.x - 0.5) / (t * (t/4)); 
    scaled.y = -0.025- (uv.y - 0.5) / (t * (t/4)); 
    
    //int i = mandelbrot(vec2(3.5 * uv.x - diameter, 1 - 2*uv.y), iters);
    //int i = burningShip(vec2(3.5 * uv.x - diameter, 1 - 2*uv.y), iters);
    int i = burningShip(scaled, iters);
    //int i = mandelbrot(scaled, iters);
    
    if (i == iters) col = vec3(0, 0, 0);
    else {
        float h = float(i) / iters;   
        float smoothH = pow(h, 0.3);
        col = hsv2rgb(vec3(smoothH, 1.0, 1.0));
    }

    fragColor = vec4(col,1.0);
}
