---
title: "C++ Infinite Terrain"
excerpt: "C++ / OpenGL infinite, procedural, realistic terrain generation"
header:
  teaser: terrainGen/act.png
---

[![Action shot](/images/terrainGen/act.png){: .align-center}](/images/terrainGen/act.png)

### Project Type: Solo | Language: C++ / OpenGL

This project was developed for my dissertation in the final year of my BSc in Computer Science with Games Development. [Full dissertation available here](http://sammurphy.me/docs/fractalFlyover.pdf) and the [source code is available here.](https://github.com/SamMurphy/InfiniteTerrain)

<iframe width="560" height="315" src="https://www.youtube.com/embed/hnawkmUVQQQ" frameborder="0" allowfullscreen></iframe>

The terrain is generated using my implementation of the ***diamond square algorithm*** in C++ and rendered using OpenGL. It is generated infinitely in a uniform grid. In order to improve performance ***tessellation*** was implemented in the shaders so that terrain that was closer to the camera was more detailed than terrain that was further away.

[![Action shot](/images/terrainGen/tess1.png){: .align-center}](/images/terrainGen/tess1.png)

[![Action shot](/images/terrainGen/tess2.png){: .align-center}](/images/terrainGen/tess2.png)

*Tessellation*

[![Action shot](/images/terrainGen/alg.png){: .align-center}](/images/terrainGen/alg.png)

