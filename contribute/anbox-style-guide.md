
(style-guide)=
# Anbox Cloud Documentation Style Guide

Anbox Cloud documentation’s navigational structure, style, and content follows the Diátaxis systematic framework for technical documentation authoring. So the information is categorized into tutorials, how-to guides, reference material, and explanatory text. See [Diátaxis](https://diataxis.fr/).

This product-specific style guide lists any extra guidelines or deviations from the [Ubuntu style guide](https://docs.ubuntu.com/styleguide/en).

## Format

Anbox Cloud documentation is written in a combination of MyST and Markdown syntax.

## General

* Use inclusive language and assume a friendly tone rather than an overly formal one.
* Use monospaced font for:
    * Inline code and code blocks
    * File names
    * References to utilities/programs
    * File and directory paths
    * Command options
* Avoid long sentences. If it is a complex statement, try and break it down into multiple sentences. While the Canonical copy style guide has guidance about hyphens when joining words, it does not elaborate much on prefixes.
* Use bold and italics very sparingly. Use italics for user interface fields and bold for UI elements that call for action.
* Use single spaces between sentences.
* Use angle brackets to indicate variables.
* All extra white space should be removed, especially at the end of lines.
* Add a new line at the end of the file.

## Section titles

* Insert a blank line after a section title.
* Do not skip heading levels when creating sections.
* Avoid using multiple section titles sequentially without any text between them.
* Avoid manual HTML anchors, links to section titles can be picked up from the page-level table of contents.

## Cross references

Always use [explicit targets](https://webaim.org/techniques/alttext/) for pages and sections to cross reference content within documentation. For external links or to reference a section on the same page, use markdown link syntax.

The target names must be unique for each page and topic.

Anbox Cloud documentation adheres to the following convention when naming explicit targets:
* Reference: `ref-xxx-yyy`
* Explanation: `exp-xxx-yyy`
* How-to guides: `howto-xxx-yyy`
* Tutorials: `tut-xxx-yyy`
* Section targets in any topic: `sec-xxx-yyy`

This helps in maintaining consistency in target naming and creating unique target names.

## Admonishments

While admonishments can be useful to convey important information, they can be a distraction when used often. So before adding an admonishment, assess if the content really belongs in one.

Keeping the types of admonishments to a minimum could be simplistic and also reduce cognitive overload on the reader. Stick to the following types of admonishments:

* Note
* Important
* Tip
* Caution

## Language

### Oxford/Serial Comma

The Anbox Cloud documentation does not use the oxford comma but exceptions are allowed for the sake of technical accuracy and ease of readability.

### Hyphens for Prefixes

Use hyphens when the starting letter of a word is in capital case or starts with a vowel. In other cases, do not hyphenate and use it as a single word.

    **Note:** You might be required to add such words to the wordlist as spellcheck could flag these words.

**Examples:**
* `Pre-employment`
* `Preconfigure`

## Terminology

* It’s always “Anbox Cloud Appliance” when used in full form and “appliance” when used generically.
* Always use product name in full form with capitalization - "Anbox Cloud".
* Within the context of Anbox Cloud, such as AMS, you can use the term "Anbox images" or "Anbox instances". When documenting about LXD images or containers that contain Anbox specific configuration from a big picture point of view,such as the architecture, use the term as "LXD images" or "LXD containers". When there is scope for ambiguity, elaborate and use as "LXD images with Anbox Cloud configuration".
* Use *charmed deployment* vs *appliance* to differentiate the [variants](https://documentation.ubuntu.com/anbox-cloud/en/latest/explanation/anbox-cloud/#variants) of Anbox Cloud.
* Use *Upgrade* to denote a change that results in a different product version and *Update* for making changes to configuration or deployment but don't change the version of the product.
* Use the term 'page' to describe the different pages of the web dashboard.
Example: You can see all the instances you created on the *Instances* page.

## Images and screenshots

While images and screenshots are very helpful in visual appeal and getting the message across to the readers, they can be hard to maintain and cause overhead if they change too often. So use images or screenshots only when they:

* Do not change often requiring updates for every release.
* Explain the concept better than text or it should strongly reinforce the concept explained in the text.
* Add to the reader’s understanding rather than just providing a step by step visual of the user interface.
* Break the monotony of continuous text information when trying to accomplish a tough procedure.

Simple images can be made using an image editor of your choice or you can use [diagrams.net](https://www.diagrams.net).

### Alternative text for images

Use alternative text (or alt text) for images when visual details cannot be included in the written content. You can leave the alternative text empty if it is more appropriate, for example, an icon that has a label.

When writing alt text for images, consider the content, its context and purpose. It should accurately reflect the content and at the same time be concise.

## Creating custom images

Go to [`draw.io`](https://www.drawio.com/). 

```{note}
The use of `draw.io` is only a suggestion. You can create diagrams using other tools as long as it follows the design conventions listed below and is consistent with the appearance of the other diagrams used in this documentation.
```

Load custom shapes:

1. Go to **File** > **Open Library from** > **Device**.
2. Select the [`anbox-cloud-docs/images/anbox-drawio.xml`](/images/anbox-drawio.xml) file.

Configure custom styles and colors:

1. Go to **Extras** > **Configuration**.
2. Paste the following configuration:

```json
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

Always use font `ubuntu` and  the standard font size is 15pt.

Use only the provided colors. See the [Ubuntu color palette](https://design.ubuntu.com/brand/colour-palette).

Once created, upload images along with their source files to the [images](/images/) folder of the documentation repository.

## Redirects

Set up redirects in [`custom_conf.py`](/custom_conf.py) whenever a file path changes as it affects the URL of the page.
