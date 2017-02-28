---
title: "Creating A Heightmap With Particle Deposition"
layout: single
author_profile: true
read_time: true
comments: true
share: true
related: true
categories:
  - Technology
  - Tutorial
  - Procedural
tags:
  - Procedural
  - Technology
  - Tutorial
  - Javascript
  - js
  - heightmap
  - particle deposition
  - three.js
---

After completing a third year project on procedural terrain generation, I decided to look in to some of the other algorithms for generating height maps. One of the more interesting methods I came across was called __Particle Deposition__, I found out about it in the book _Game Programming Gems_ (which I highly recommend). The book briefly describes the technique, but provides no code and I've been unable to find much information on it any where else; so I've put together this post to provide others who might be researching the topic.

The general purpose of the algorithm is to create height map by dropping particles onto a plane, the clever part is that once the particle lands it is tested for stability and moved slightly into a position where it settles. The overall effect of this is creating volcanic style islands.

## The Algorithm

To start with you need to define a number of droppers, and a number of particles for each dropper. A dropper in this instance is just a starting point somewhere on the grid, that we'll drop the particles onto. Once you have these defined, you just loop through the number of particles for each dropper moving the dropper every time you place a particle.

```
foreach dropper
{
	x = random(0, Width);
	y = random(0, Height);
	
	foreach particle
	{
		Check stability at x,y
		Place particle
		Increment x or y to move dropping point		
	}
}
```



