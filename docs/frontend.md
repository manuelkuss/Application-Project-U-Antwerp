# Angular Frontend

The most relevant design choices are presented below.

## Frontend toolkit

Bootstrap (https://getbootstrap.com/docs/5.3/getting-started/introduction/) is used as feature-rich frontend toolkit. Stylings and frontend components (such as forms) can easily be created by utilizing Bootstrap.

Copyright (c) 2011-2025 The Bootstrap Authors.

## Interactive Graphics

Using Vega (https://vega.github.io/vega/) as visualization tool.
- Objects are specified in JSON.
- Embeeded, interactive web components via vega-embed (https://github.com/vega/vega-embed).
- The JSON graphics are genrated in the backend and provided to the frontend in a shared media folder. The frontend fetches this JSON and generates the graphics.

Copyright (c) 2015, University of Washington Interactive Data Lab
