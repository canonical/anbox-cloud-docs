(howto-enable-client-side-video-upscaling)=
# How to enable client-side video upscaling

The [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk) offers experimental video upscaling features for client side streaming, leveraging [AMD FidelityFX Super Resolution 1.0](https://gpuopen.com/fidelityfx-superresolution/). This feature allows video to be transmitted at lower resolutions, saving bandwidth without losing too much detail. The SDK sets up a [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL) context and utilizes a fragment shader based on the FSR 1.0 algorithm for post-processing, producing clearer and sharper video frames before they are displayed on the screen.

## Initiate the `AnboxStream` object

To enable client-side video upscaling, initiate the `AnboxStream` object as follows:

```html
<!DOCTYPE html>
    stream = new AnboxStream({
        targetElement: "anbox-stream",
        experimental: {
            upscaling: {
              enabled: true,
            },
        },
        ...
    });
```

### Use target frame rate

The option `experimental.upscaling.useTargetFrameRate` allows canvas to use the refresh frame rate setting in the Anbox container for rendering video frames. This avoids relying on `HTMLVideoElement.requestVideoFrameCallback` function, which can occasionally be fired [one v-sync late](https://wicg.github.io/video-rvfc/#introduction). This option is off by default and requires explicit activation.

```{note}
On a WebView where the `HTMLVideoElement.requestVideoFrameCallback` function is not supported, this option will be enabled by default.
```

(sec-custom-fragment-shader)=
### Use custom fragment shader

The option `options.experimental.upscaling.fragmentShaders` allows the use of custom fragment shader-based upscaling algorithms for video streaming. By providing an array of fragment shader source codes, you can apply multiple shaders sequentially to perform multi-pass upscaling. This replaces the default [AMD FidelityFX Super Resolution 1.0](https://gpuopen.com/fidelityfx-superresolution/) shader.

Each shader in the array is applied in order, with the frame buffer from the output of the previous shader being used as the input texture for the next shader. Therefore, the order of shaders in the list is critical to achieving the desired post-processing effects. This provides greater flexibility for advanced video upscaling workflows by combining multiple shaders in a single rendering pipeline.

When using a custom fragment shader in WebGL, you need to manage the following pre-defined variables to interact with textures and control rendering:

- **uSampler**
  Type: sampler2D
  Description: this uniform represents the texture sampler for your fragment shader. It allows the shader to sample from the texture bound to texture unit 0.

- **vTextureCoord**
  Type: varying vec2
  Description: This varying variable is passed from the vertex shader to the fragment shader and represents the texture coordinates for the current fragment. It is used to sample the texture at specific coordinates.

- **uResolution**
  Type: vec2
  Description: This uniform contains the dimensions of the rendering canvas, typically set to the width and height of the canvas in pixels. It helps in normalizing texture coordinates for effects like scaling and post-processing.

## Related topics

* {ref}`exp-application-streaming`
* {ref}`tut-set-up-stream-client`
* {ref}`sec-streaming-sdk`
