{
  "targets": [
    {
      "target_name": "waveform",
      "type": "executable",
      "cflags": [
        "-O3",
        "--std=c99"
      ],
      "libraries": [
        "-lgroove",
        "-pthread",
        "-lz",
        "-lpng"
      ],
      "sources": [
        "waveform.c"
      ],
      "conditions": [
        ['OS=="mac"', {
          "include_dirs": ["/usr/X11/include"],
          "libraries": ["-L/usr/X11/lib"]
         }]
      ]
    }
  ]
}
