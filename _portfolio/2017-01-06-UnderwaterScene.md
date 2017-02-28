---
title: "Under Water Scene"
excerpt: "C++ / DirectX scene to demonstrate graphical techniques"
header:
  teaser: undewater/whale.png
---

[![Action shot](/images/undewater/overall.png){: .align-center}](/images/undewater/overall.png)

### Project Type: Solo | Language: C++ / DirectX

An underwater scene created in C++ and DirectX to demonstrate graphical techniques. The scene is loaded through config files, allowing complete customisation of the scene while the application is still open. A very simple ***scene graph*** was implemented to allow for easy animation of the submarines in the scene. Some animation was also implemented in the shaders, using sine waves, to provide realistic animation for the fish.

<iframe width="560" height="315" src="https://www.youtube.com/embed/1rMlGKm3JjQ" frameborder="0" allowfullscreen></iframe>

***Spot, point, and directional lights*** were implemented to adequately light the scene, this includes moving spot lights attached to some of the submarines. ***Pathing*** was implemented for the objects, so that they moved around the scene, along with ***multiple user controlled cameras*** some of which follow objects.

***Separating Axis Theorem*** was implemented for collision detection between the objects. Sphere colliders were also used for broad-phase detection.

AntTweakBar was used to allow the user to change various settings on the fly, as well as speed up and slow down time, and review statistics on the performance of the scene.

[![Action shot](/images/undewater/overall2.png){: .align-center}](/images/undewater/overall2.png)

[![Action shot](/images/undewater/newsub.png){: .align-center}](/images/undewater/newsub.png)

[![Action shot](/images/undewater/oldsub.png){: .align-center}](/images/undewater/oldsub.png)

[![Action shot](/images/undewater/whale.png){: .align-center}](/images/undewater/whale.png)

[![Action shot](/images/undewater/fish.png){: .align-center}](/images/undewater/fish.png)



