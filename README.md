# node-waveform

![](http://i.imgur.com/oNy41Cr.png)

Input: any format audio or video file

Output: any or all of these:

 * transcoded audio file
 * waveform.js-compatible JSON representation of the audio file
 * PNG rendering of the waveform

This is a [Node.js](http://nodejs.org) module that wraps the [waveform command
line interface](https://github.com/andrewrk/waveform). The C code is bundled
from that repository, so if you want to file an issue with or fork the C code,
go to the waveform repository.

## Usage

```js
var waveform = require('waveform');

waveform(audiofile, {
  // options
  'scan': false,             // whether to do a pass to detect duration
  // transcoding options
  transcode: "outputfile.mp3", // required
  bitrate: 320,
  format: "name",
  codec: "name",
  mime: "mimetype",
  'tag-artist': "artistname",
  'tag-title': "title",
  'tag-year': 2000,
  'tag-comment': "comment",

  // waveform.js options

  // png options
  width: 256,                // width of the image
  height: 64,                // height of the image
  'color-bg': '00000000',    // bg color, rrggbbaa
  'color-center': '000000ff',// gradient center color, rrggbbaa
  'color-outer': '000000ff', // gradient outer color, rrggbbaa
}, function(err) {
  // done
});
```

## Installation

1. Install [libgroove](https://github.com/andrewrk/libgroove) dev package.
   Only the main library is needed. Packages are available for common
   package managers.

2. Install libpng and zlib dev packages.

3. `npm install waveform`
