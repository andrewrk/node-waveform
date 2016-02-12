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

At least one of the options `transcode`, `waveformjs` or `png` is required as
output destination.

```js
var waveform = require('waveform');

waveform(audiofile, {
  // options
  'scan': false,                  // whether to do a pass to detect duration

  // transcoding options
  transcode: "outputfile.mp3",    // path to output-file, or - for stdout as a Buffer
  bitrate: 320,                   // audio bitrate in kbps
  format: "name",                 // e.g. mp3, ogg, mp4
  codec: "name",                  // e.g. mp3, vorbis, flac, aac
  mime: "mimetype",               // e.g. audio/vorbis
  'tag-artist': "artistname",     // artist tag
  'tag-title': "title",           // title tag
  'tag-year': 2000,               // year tag
  'tag-comment': "comment",       // comment tag

  // waveform.js options
  waveformjs: "outputfile.json",  // path to output-file, or - for stdout as a Buffer
  'wjs-width': 800,               // width in samples
  'wjs-precision': 4,             // how many digits of precision
  'wjs-plain': false,             // exclude metadata in output JSON (default off)

  // png options
  png: "outputfile.png",          // path to output-file, or - for stdout as a Buffer
  'png-width': 256,               // width of the image
  'png-height': 64,               // height of the image
  'png-color-bg': '00000000',     // bg color, rrggbbaa
  'png-color-center': '000000ff', // gradient center color, rrggbbaa
  'png-color-outer': '000000ff',  // gradient outer color, rrggbbaa

  // node-specific options
  encoding: "utf8",               // different output encoding for callback (default is 'buffer')
  maxBuffer: 1024 * 1000          // max buffer before the process is killed (default is 1024 * 5000)

}, function(err, buf) {
  // done
});
```

## Installation

1. Install [libgroove](https://github.com/andrewrk/libgroove) dev package.
   Only the main library is needed. Packages are available for common
   package managers.

2. Install libpng and zlib dev packages.

3. `npm install waveform`
