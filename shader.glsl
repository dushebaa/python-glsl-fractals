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

vec3 rgb2hsv(vec3 c)
{
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    float diameter = 2.5;
    int iters = 30;
    vec3 col;

    vec2 uv = fragCoord/iResolution.xy;

    int i = mandelbrot(vec2(3.5 * uv.x - diameter, 2*uv.y - 1), iters);
    //int i = burningShip(vec2(3.5 * uv.x - diameter, 2*uv.y - 1), iters);
    
    if (i == iters) col = vec3(0,0,0);
    else {
        col = rgb2hsv(vec3(i, 1, 1));
        col.x += iMouse.x / iResolution.x;
    }
    
    fragColor = vec4(col,1.0);
}