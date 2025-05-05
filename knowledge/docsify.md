# Docsify

Docsify is a documentation site generator.

[Docsify](https://docsify.js.org/#/) | [Github](https://github.com/docsifyjs/docsify-cli)


# Commonly used commands

```bash
docsify init ./                         # Initialize a docsify project in current directory
docsify serve ./                        # Serve the docsify project in current directory
docsify generate ./ -s _sidebar.md      # Generate a sidebar file from current directory
```

List of plugins: https://docsify.js.org/#/awesome?id=plugins

Better themes:

- [Docsify Darkly Theme](https://github.com/sushantrahate/docsify-darkly-theme)
- [Docsify Github Theme](https://github.com/w3teal/docsify-theme-github)


# Development Notes

## Set the page width

```html
<!-- index.html -->
<link rel="stylesheet"
      href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">

<style>
  /* Center the text column and cap its width */
  .markdown-section{
    max-width: 720px;   /* pick any size—700–800 px feels book‑like */
    margin: 0 auto;    /* keeps it centred */
    padding: 0 1.2rem; /* optional: add side‑padding on phones */
  }
</style>
```

