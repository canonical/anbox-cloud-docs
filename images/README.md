---
orphan: true
---

# Customise drawio/diagrams.net

Load custom shapes:

1. Go to **File** > **Open Library**.
2. Select the `anbox-cloud-docs/images/anbox-drawio.xml` file.

Configure custom styles and colours:

1. Go to **Extras** > **Configuration**.
2. Paste the following configuration:

```
{
  "defaultFonts": [
    {
      "fontFamily": "ubuntu",
      "fontUrl": "https://fonts.googleapis.com/css2?family=Ubuntu"
    }
  ],
  "defaultVertexStyle": {
    "fontFamily": "ubuntu",
    "fontSize": "15"
  },
  "defaultEdgeStyle": {
    "fontFamily": "ubuntu"
  },
  "presetColors": [
    "E95420",
    "FFFFFF",
    "000000",
    "77216F",
    "772953",
    "5E2750",
    "2C001E",
    "AEA79F",
    "333333",
    "111111"
  ],
  "defaultColorSchemes": [
    [
      null,
      {
        "fill": "#E95420",
        "stroke": "none",
        "font": "#FFFFFF"
      },
      {
        "fill": "#DEDBD8",
        "stroke": "none",
        "font": "#111111"
      },
      {
        "fill": "#77216F",
        "stroke": "none",
        "font": "#FFFFFF"
      },
      {
        "fill": "#772953",
        "stroke": "none",
        "font": "#FFFFFF"
      },
      {
        "fill": "#5E2750",
        "stroke": "none",
        "font": "#FFFFFF"
      },
      {
        "fill": "#2C001E",
        "stroke": "none",
        "font": "#FFFFFF"
      },
      {
        "fill": "#AEA79F",
        "stroke": "none",
        "font": "#111111"
      }
    ]
  ],
  "defaultColors": [
    "none",
    "E95420",
    "EB6536",
    "ED764D",
    "F08763",
    "F29879",
    "F4AA90",
    "F5B29B",
    "F6BBA6",
    "F7C3B1",
    "F8CCBC",
    "FAD4C7",
    "FBDDD2",
    "FCE5DE",
    "FDEEE9",
    "772953",
    "843E64",
    "925375",
    "9F6986",
    "AD7E97",
    "BB94A9",
    "C19EB1",
    "C8A9BA",
    "CFB4C2",
    "D6BECB",
    "DDC9D4",
    "E3D4DC",
    "EADEE5",
    "F1E9ED",
    "77216F",
    "84377D",
    "924D8B",
    "9F639A",
    "AD79A8",
    "BB90B7",
    "C19BBE",
    "C8A6C5",
    "CFB1CC",
    "D6BCD3",
    "DDC7DB",
    "E3D2E2",
    "EADDE9",
    "F1E8F0",
    "5E2750",
    "6E3C61",
    "7E5273",
    "8E6784",
    "9E7D96",
    "AE93A7",
    "B69DB0",
    "BEA8B9",
    "C6B3C1",
    "CEBECA",
    "D6C9D3",
    "DED3DC",
    "E6DEE4",
    "EEE9ED",
    "2C001E",
    "411934",
    "56334B",
    "6B4C61",
    "806678",
    "957F8E",
    "A08C99",
    "AA99A5",
    "B5A5B0",
    "BFB2BB",
    "CABFC6",
    "D4CCD2",
    "DFD8DD",
    "E9E5E8",
    "AEA79F",
    "B6AFA8",
    "BEB8B2",
    "C6C1BB",
    "CECAC5",
    "D6D3CF",
    "DAD7D3",
    "DEDBD8",
    "E2E0DD",
    "E6E4E2",
    "EAE9E7",
    "EEEDEB",
    "F2F1F0",
    "F6F6F5"
  ]
}
```

# Conventions

- Use font `ubuntu`.
- Standard font size: 15pt
- Use only the provided colours. See the colour palette at [`https://design.ubuntu.com/brand/colour-palette/`](https://design.ubuntu.com/brand/colour-palette/) .

# Upload images to the asset manager

Images should be uploaded to [Ubuntu assets](https://assets.ubuntu.com/manager) .

To do this from the command line, get an API token and install [`https://github.com/canonical/canonicalwebteam.upload-assets`](https://github.com/canonical/canonicalwebteam.upload-assets)

Export the required environment variables:

    export UPLOAD_ASSETS_API_TOKEN=<api_token>
    export UPLOAD_ASSETS_API_DOMAIN=assets.ubuntu.com

Then upload with the following command:

    upload-assets -t "Anbox Cloud" images/<file_name(s)>

Add more tags if it makes sense (as a comma-separated list).
